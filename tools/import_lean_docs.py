"""Replay documentation from a pinned Lean source archive without evaluating Lean."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import statistics
import tarfile
import tempfile
from urllib.parse import quote

import yaml

from check_informalization_pr import note_key, read_note

# Skip ordinary comments, line comments, quoted literals and escaped identifiers.
MARK = re.compile(r'/-|--|"(?:\\.|[^"\\])*"|«[^»]*»|\'(?:\\.|[^\'\\\n])\'', re.S)
NEST = re.compile(r"/-|-/")
IDENT = r"(?:«[^»]+»|[^\W\d][\w'₀-₉.]*)(?:\.«[^»]+»)*"
CMD = re.compile(
    r"(?:(?:private|protected|local|noncomputable|partial|unsafe|public|nonrec|scoped)\s+)*"
    r"(?:theorem|lemma|def|abbrev|instance|structure|class|inductive|axiom|opaque|alias)\s+("
    + IDENT
    + r")"
)
NOTATION = re.compile(
    r"(?:local\s+|scoped\s+)?(?:notation|syntax|macro)\s*\(name\s*:=\s*(" + IDENT + r")\)"
)
STRUCT = re.compile(
    r"^([ \t]*)(?:@\[[^]\n]+\][ \t]*)*(?:(?:private|protected)\s+)?(?:structure|class|inductive)\s+(" + IDENT + r")",
    re.M,
)
FIELD = re.compile(r"(?:protected\s+)?(?:[({\[]\s*)?(" + IDENT + r")\s*(?=:(?!=)|[({\[⦃])")


BOUND_FIELDS = re.compile(r"[({]\s*(" + IDENT + r"(?:\s+" + IDENT + r")+?)\s*:")


def source_surface(source):
    comments = []
    surface = list(source)
    i = 0
    while match := MARK.search(source, i):
        start = match.start()
        if match[0] == "--":
            i = source.find("\n", match.end())
            if i < 0:
                i = len(source)
        elif match[0] == "/-":
            depth = 1
            i = match.end()
            while depth:
                mark = NEST.search(source, i)
                if mark is None:
                    raise ValueError(
                        f"unterminated block comment on line {source.count(chr(10), 0, start) + 1}"
                    )
                depth += 1 if mark[0] == "/-" else -1
                i = mark.end()
            marker = source[start + 2 : start + 3]
            comments.append(
                (
                    start,
                    i,
                    marker,
                    source[start + (3 if marker in {"!", "-"} else 2) : i - 2],
                )
            )
        else:
            i = match.end()
            continue
        surface[start:i] = [c if c in "\r\n" else " " for c in source[start:i]]
    return comments, "".join(surface)


def scan(source):
    comments, code = source_surface(source)
    notes = []
    leading = []
    # A doc comment inside a to_additive attribute describes its generated declaration.
    additive = {}
    for start, _, marker, _ in comments:
        if marker == "-":
            attr = code.rfind("@[", 0, start)
            if attr >= 0 and (match := re.fullmatch(r"@\[to_additive(?:\s+(" + IDENT + r"))?\s*", code[attr:start])):
                additive[start] = match[1] or "to_additive (anonymous instance)"
    doc_starts = [start for start, _, marker, _ in comments if marker in {"!", "-"} and start not in additive]
    doc_index = 0
    for start, end, marker, text in comments:
        if marker not in {"!", "-"}:
            if not code[:start].strip():
                leading.append(text)
            continue
        if start in additive:
            notes.append((additive[start], text))
            continue
        doc_index += 1
        if marker == "!":
            notes.append((None, text))
            continue
        pos = re.compile(r"\S").search(code, end)
        limit = doc_starts[doc_index] if doc_index < len(doc_starts) else len(code)
        if pos and pos.start() < limit:
            offset = pos.start()
            while code.startswith("@[", offset):
                depth = 1
                cursor = offset + 2
                while depth and cursor < limit:
                    depth += (code[cursor] == "[") - (code[cursor] == "]")
                    cursor += 1
                following = re.compile(r"\S").search(code, cursor, limit)
                if depth or following is None:
                    break
                offset = following.start()
            command = CMD.match(code, offset) or NOTATION.match(code, offset)
            if command:
                notes.append((command[1], text))
                continue
            # Anonymous instances have no printed identifier. Use the source signature.
            anon = re.match(r"(?:(?:local|scoped|noncomputable)\s+)*instance\s*(?=[:({\[])", code[offset:limit])
            if anon:
                signature = re.split(r":=|\bwhere\b|\n\s*\|", code[offset:limit], maxsplit=1)
                if len(signature) == 2:
                    notes.append((" ".join(signature[0].split()), text))
                    continue
            macro = re.match(r'(?:local\s+|scoped\s+)?macro\s+"([^"\n]+)"', code[offset:limit])
            if macro:
                notes.append((macro[1].strip(), text))
                continue
            infix = re.match(r'(?:infix[lr]?|prefix|postfix):\d+\s+"([^"\n]+)"\s*=>', code[offset:limit])
            if infix:
                notes.append((infix[1].strip(), text))
                continue
            # Fields and constructors belong to the closest enclosing type.
            constructor = re.match(r"\|\s*(" + IDENT + r")", code[offset:limit])
            field = constructor or BOUND_FIELDS.match(code, offset) or FIELD.match(code, offset)
            indent = offset - code.rfind("\n", 0, offset) - 1
            if field and (indent or constructor):
                owner = None
                for decl in reversed(list(STRUCT.finditer(code, 0, start))):
                    outer = len(decl[1])
                    if outer > indent or (outer == indent and not constructor):
                        continue
                    between = code[decl.end() : start].splitlines()[1:]
                    if not any(
                        line.strip() and len(line) - len(line.lstrip()) <= outer and not (constructor and line.lstrip().startswith("|"))
                        for line in between
                    ):
                        owner = decl[2]
                    break
                if owner:
                    notes.append((", ".join(owner.rstrip(".") + "." + name for name in field[1].split()), text))
                    continue
        raise ValueError(
            f"unattached declaration documentation at line {source.count(chr(10), 0, start) + 1}"
        )
    return leading, notes


def replay(config_path, archive, destination, *, groups=None, blob_list=None):
    cfg = json.loads(config_path.read_text())
    if archive.is_dir():
        from lean_selection import select_archive
        with tempfile.TemporaryDirectory() as tmp:
            subset = Path(tmp) / "selection.tar"
            groups = select_archive(cfg, archive, subset, source_surface)
            return replay(config_path, subset, destination, groups=groups, blob_list=blob_list)
    with archive.open("rb") as stream:
        if hashlib.file_digest(stream, "sha256").hexdigest() != cfg["archiveSha256"]:
            raise ValueError("source archive SHA-256 differs")
    with tarfile.open(archive, "r:*") as tar:
        files = [m for m in tar if m.isfile()]
        roots = {PurePosixPath(m.name).parts[0] for m in files}
        if len(roots) != 1:
            raise ValueError("expected one source revision root")
        prefix = (PurePosixPath(roots.pop()) / cfg["folder"]).as_posix().rstrip(
            "/"
        ) + "/"
        entries = {
            m.name.removeprefix(prefix): m for m in files if m.name.startswith(prefix)
        }

        def blob(name):
            return tar.extractfile(entries[name]).read()

        proof_file = config_path.parents[2] / "proofs" / cfg["package"] / "proof.yml"
        if proof_file.exists():
            record = json.loads(proof_file.read_text())
            if "readmeOpening" in record:
                readme = blob("README.md")
                opening = config_path.with_name("readme-opening.md").read_bytes()
                if (hashlib.sha256(readme).hexdigest() != record["readmeSHA256"]
                        or not readme.startswith(opening)
                        or hashlib.sha256(opening).hexdigest() != record["openingSHA256"]):
                    raise ValueError("vendored README excerpt differs from the pinned source")
        if metadata_name := cfg.get("metadata"):
            metadata = blob(metadata_name)
            if config_path.with_name(Path(metadata_name).name).read_bytes() != metadata:
                raise ValueError("vendored project metadata differs from source")
            project = yaml.safe_load(metadata)
        else:
            metadata = None
            project = {
                "project": {"authors": cfg["authors"], "license": cfg["license"]},
                "automation": {"methods": [{"models": cfg.get("models", [])}]},
            }
        models = {
            name
            for method in project.get("automation", {}).get("methods", [])
            for name in method.get("models", [])
        }
        inventory = sorted(
            (name for name in entries if name.endswith(".lean")), key=str.encode
        )
        blocks = []
        sizes = []
        allnotes = []
        header_counts = Counter()
        lengths = Counter()
        written = {}
        closures = {root: Counter() for root in groups or {}}
        blobs = []
        for path in inventory:
            if ".." in PurePosixPath(path).parts or PurePosixPath(path).is_absolute():
                raise ValueError(f"invalid archive path {path}")
            data = blob(path)
            source = data.decode()
            if blob_list is not None:
                oid = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
                blobs.append(f"{path}\t{oid}\n")
            try:
                header, notes = scan(source)
            except ValueError as exc:
                raise ValueError(f"{path}: {exc}") from exc
            for root, paths in (groups or {}).items():
                if path in paths:
                    closures[root].update(files=1, withNotes=int(bool(notes)), sourceBytes=len(data),
                                          moduleNotes=sum(name is None for name, _ in notes),
                                          declarationNotes=sum(name is not None for name, _ in notes))
            credits = [
                line
                for h in header
                for line in h.splitlines()
                if line.startswith(("Copyright", "Authors:", "Author:"))
            ]
            copyright = next((x for x in credits if x.startswith("Copyright")), None)
            header_counts[copyright] += 1
            if not notes:
                continue
            if project["project"]["license"] in {"Apache-2.0", "MIT"} and not copyright and cfg.get("copyrightStatus") != "absent":
                raise ValueError(f"{path}: missing upstream copyright")
            writers = [
                x.split(":", 1)[1].strip()
                for x in credits
                if x.startswith(("Authors:", "Author:"))
            ]
            port = re.search(r"(?im)^ported from https://github\.com/[^/\s]+/([\w.-]+)", "\n".join(header))
            fallback = [port[1] + " contributors"] if port else project["project"]["authors"]
            writer = ", ".join(writers or fallback)
            address = (
                cfg["repository"]
                + "/blob/"
                + cfg["commit"]
                + "/"
                + quote(prefix.split("/", 1)[1] + path)
            )
            meta = dict(
                module=path,
                declarations=[],
                author=cfg["submitter"],
                writer=writer,
                origin="other-author",
                entry_type="source-documentation",
                license=project["project"]["license"],
                **({"copyright": copyright} if copyright else {"copyright_status": "absent"} if cfg.get("copyrightStatus") == "absent" else {}),
                source=address,
                source_commit=cfg["commit"],
            )
            if not port and writer in models:
                meta["kind"] = "ai"
            # Keep upstream header comments, delimiters and line breaks in the ledger.
            header_text = "\n\n".join("/-" + h + "-/" for h in header)
            fence = "`" * max([3] + [len(m[0]) + 1 for m in re.finditer(r"`+", header_text)])
            body = [
                f"Documentation comments extracted from this file at [{cfg['commit'][:7]}]({address}). "
                "Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.",
                *([f"{fence}text\n{header_text}\n{fence}"] if header_text else []),
                *cfg.get("credits", {}).get(path, []),
            ]
            module_words = 0
            has_module = False
            for name, text in notes:
                if name:
                    body.append(f"### `{name}`")
                    sizes.append(len(text.strip()))
                else:
                    module_words += len(text.split())
                    has_module = True
                body.append(text)
                allnotes.append(text)
            if has_module:
                blocks.append(module_words)
            content = (
                "---\n"
                + json.dumps(meta, ensure_ascii=False, indent=2)
                + "\n---\n\n"
                + "\n\n".join(body)
                + "\n"
            )
            rendered = read_note(content.encode(), maintainer=True, path=path, import_config=cfg).html
            if "<merror" in rendered:
                raise ValueError(f"{path}: MathML conversion failed")
            lengths[path] = len(rendered.encode())
            target = Path(
                cfg["package"],
                "informalizations",
                path,
                note_key(meta["author"], writer) + ".md",
            )
            written[target] = content
        (destination / cfg["package"]).mkdir(parents=True, exist_ok=True)
        for target, content in written.items():
            p = destination / target
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(content.encode())
        (destination / cfg["package"] / "modules.txt").write_text(
            "\n".join(inventory) + "\n"
        )
    if blob_list is not None:
        blob_list.write_text("path\tblob\n" + "".join(blobs))
    return dict(
        **({"closures": closures} if groups else {}),
        files=len(inventory),
        entries=len(written),
        withoutNotes=len(inventory) - len(written),
        filesWithModuleNotes=len(blocks),
        medianModuleWords=statistics.median(blocks) if blocks else None,
        declarationNotes=len(sizes),
        medianDeclarationChars=statistics.median(sizes) if sizes else None,
        noteWords=sum(len(s.split()) for s in allnotes),
        noteDollarSigns=sum(s.count("$") for s in allnotes),
        headerCopyright=dict(header_counts),
        largestRenderedBody=lengths.most_common(1),
        **({"metadataSha256": hashlib.sha256(metadata).hexdigest()} if metadata is not None else {}),
    )


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("config", type=Path)
    cli.add_argument("archive", type=Path)
    cli.add_argument(
        "destination",
        type=Path,
        help="Empty replay directory for the generated package",
    )
    cli.add_argument("--blob-list", type=Path, help="Write a path and verified source blob ID per line")
    args = cli.parse_args()
    if args.destination.exists() and any(args.destination.iterdir()):
        cli.error("choose an empty replay directory")
    print(
        json.dumps(
            replay(args.config, args.archive, args.destination, blob_list=args.blob_list),
            ensure_ascii=False,
            indent=2,
        )
    )

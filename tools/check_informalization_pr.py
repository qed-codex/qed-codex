"""Validate an informalization contribution against the base proof ledger and a trusted database."""
from source_registry import directory_proof

import argparse
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from typing import NamedTuple
from urllib.parse import quote, urlsplit

import yaml

from informalizations import render_informalization


PUBLIC_MAX_BYTES = 256_000
PUBLIC_MAX_DECLARATIONS = 64
MAX_RENDERED_BYTES = 1_000_000


class InvalidInformalization(ValueError):
    pass


class UniqueKeys(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        fields = super().construct_mapping(node, deep)
        if len(fields) != len(node.value):
            raise InvalidInformalization("duplicate front matter key")
        return fields


REQUIRED = {"module", "declarations", "author", "source_commit", "license", "writer", "origin"}
OPTIONAL = {"kind", "source", "agrees_with", "copyright", "copyright_status", "entry_type", "license_source", "notice", "changes"}
IMPORT_LICENSES = {"with-permission", "Apache-2.0", "MIT", "CC0-1.0"}
INFORMALIZATION_PATH = re.compile(r"^(?:proofs|packages)/[^/]+/informalizations(?:/|$)")
HANDLE = re.compile(r"[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*")


def writer_slug(writer):
    # Keep Unicode letters and numbers. JS uses the same NFKC/lowercase rule.
    normalized = unicodedata.normalize("NFKC", writer).lower()
    slug = re.sub("-+", "-", "".join(c if c.isalnum() else "-" for c in normalized)).strip("-")
    if (not slug or writer != writer.strip() or any(not c.isprintable() for c in writer)
            or len(slug.encode("utf-8")) > 210):
        raise InvalidInformalization("invalid writer name or filename length")
    return slug


def note_key(author, writer):
    if not HANDLE.fullmatch(author) or len(author) > 39:
        raise InvalidInformalization("invalid submitter handle")
    return author + "--" + writer_slug(writer)


def git(repo, *args):
    return subprocess.check_output(["git", "--literal-pathspecs", "-C", repo, *args])


def contribution(repo, base, head, author):
    for revision in (base, head):
        if not re.fullmatch("[0-9a-f]{40}|[0-9a-f]{64}", revision):
            raise InvalidInformalization("both revisions must be full Git object IDs")
        if git(repo, "cat-file", "-t", revision) != b"commit\n":
            raise InvalidInformalization("each revision must identify a commit")
    ancestors = git(repo, "merge-base", "--all", base, head).decode().splitlines()
    if len(ancestors) != 1:
        raise InvalidInformalization("expected one common merge base")
    # Disable rename detection so both the old and new names undergo the ownership check.
    raw = git(repo, "diff", "--raw", "--no-abbrev", "--no-renames", "-z", ancestors[0], head, "--")
    records = raw.split(b"\0")[:-1]
    changes = [(entry.decode("ascii").split(), name.decode("utf-8"))
               for entry, name in zip(records[::2], records[1::2], strict=True)]
    if not any(INFORMALIZATION_PATH.match(path) for _, path in changes):
        return None
    if not HANDLE.fullmatch(author) or len(author) > 39:
        raise InvalidInformalization("invalid GitHub pull request author")
    notes = []
    for (oldmode, newmode, _old, oid, status), path in changes:
        parts = PurePosixPath(path).parts
        own_file = parts[-1].startswith(author + "--") and parts[-1].endswith(".md")
        legacy_deletion = status == "D" and parts[:3] == ("proofs", "rh", "informalizations")
        package_file = len(parts) >= 5 and parts[0] == "packages" and parts[2] == "informalizations"
        if not own_file or not (legacy_deletion or package_file):
            raise InvalidInformalization("contribution changes a path outside the PR author's informalization files")
        if oldmode[1:] not in {"000000", "100644"} or newmode not in {"000000", "100644"}:
            raise InvalidInformalization("informalization must be a regular non-executable Markdown file")
        module = "/".join(parts[3:-1])
        if not module.endswith(".lean"):
            raise InvalidInformalization("informalization directory must name a Lean module path")
        if status in {"A", "M"}:
            notes.append((path, module, oid))
        elif status == "D":
            notes.append((path,module,None))
        else:
            raise InvalidInformalization("unsupported change to an informalization")
    return notes


def check_public_size(count):
    if count > PUBLIC_MAX_BYTES:
        raise InvalidInformalization(f"public entries may contain at most {PUBLIC_MAX_BYTES:,} bytes")


def note_parts(content, *, maintainer, import_config=None):
    if not maintainer:
        check_public_size(len(content))
    try:
        lines = content.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").split("\n")
    except UnicodeDecodeError as error:
        raise InvalidInformalization("informalization must be UTF-8") from error
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise InvalidInformalization("expected fenced YAML front matter")
    end = lines.index("---", 1)
    if not any(line.strip() for line in lines[end + 1:]):
        raise InvalidInformalization("informalization body is empty")
    try:
        meta = yaml.load("\n".join(lines[1:end]), Loader=UniqueKeys)
    except InvalidInformalization:
        raise
    except RecursionError as error:
        raise InvalidInformalization("front matter is nested too deeply") from error
    except Exception as error:
        # SafeLoader's scalar constructors can also raise native Python errors.
        raise InvalidInformalization("invalid YAML front matter") from error
    if not isinstance(meta, dict):
        raise InvalidInformalization("front matter must be a mapping")
    if REQUIRED - meta.keys() or meta.keys() - (REQUIRED | OPTIONAL):
        raise InvalidInformalization("front matter has missing or unknown fields")
    for key in (REQUIRED | OPTIONAL) - {"declarations", "agrees_with"}:
        if key in meta and (not isinstance(meta[key], str) or (key != "notice" and not meta[key].strip())):
            raise InvalidInformalization(f"{key} must be a nonempty string")
    names = meta["declarations"]
    if isinstance(names, list) and not maintainer and len(names) > PUBLIC_MAX_DECLARATIONS:
        raise InvalidInformalization(f"public entries may list at most {PUBLIC_MAX_DECLARATIONS} declarations")
    if not isinstance(names, list) or not all(isinstance(n, str) and n.strip() for n in names):
        raise InvalidInformalization("declarations must be a list of nonempty Lean names")
    note_key(meta["author"], meta["writer"])
    origin = meta["origin"]
    if origin not in {"wrote", "generated", "other-author"}:
        raise InvalidInformalization("invalid origin")
    kind = meta.get("kind", {"wrote": "human", "generated": "ai"}.get(origin))
    allowed = {"wrote": {"human"}, "generated": {"ai", "ai-reviewed-by-human"},
               "other-author": {None, "human", "ai", "ai-reviewed-by-human"}}
    if "entry_type" in meta and not (
            maintainer and origin == "other-author" and meta["entry_type"] == "source-documentation"):
        raise InvalidInformalization("source documentation must be imported by a maintainer")
    if kind not in allowed[origin]:
        raise InvalidInformalization("kind disagrees with origin")
    meta["kind"] = kind
    licence = meta["license"]
    if licence not in IMPORT_LICENSES | {"CC-BY-4.0"} or (origin != "other-author" and licence != "CC-BY-4.0"):
        raise InvalidInformalization("own text must be CC-BY-4.0 and published text must use a listed licence")
    if licence == "with-permission" and not maintainer:
        raise InvalidInformalization("with-permission entries require a maintainer")
    published_fields = {"license_source", "notice", "changes"}
    if published_fields & meta.keys() or (not maintainer and origin == "other-author"):
        if origin != "other-author" or licence == "with-permission" or meta.get("entry_type"):
            raise InvalidInformalization("public licensing fields are for another author's published text")
        missing = (published_fields | {"copyright"}) - meta.keys()
        if missing:
            raise InvalidInformalization("published text requires " + ", ".join(sorted(missing)))
    if "copyright_status" in meta:
        cfg = import_config or {}
        if not (maintainer and meta["copyright_status"] == cfg.get("copyrightStatus") == "absent"
                and "copyright" not in meta and meta.get("entry_type") == "source-documentation"
                and meta["license"] == cfg.get("license") and meta["source_commit"] == cfg.get("commit")
                and meta.get("source") == f"{cfg['repository']}/blob/{cfg['commit']}/{cfg['folder']}/{quote(meta['module'])}"):
            raise InvalidInformalization("missing copyright must be confirmed by the pinned source import")
    elif meta["license"] in {"Apache-2.0", "MIT"} and "copyright" not in meta:
        raise InvalidInformalization("this import requires its original copyright line")
    if origin == "other-author" and "source" not in meta:
        raise InvalidInformalization("other-author text requires a source address")
    for field in ("source", "license_source"):
        if field not in meta:
            continue
        try:
            url = urlsplit(meta[field])
        except ValueError as error:
            raise InvalidInformalization("invalid source address") from error
        if (url.scheme not in {"https", "http"} or not url.hostname or url.username is not None
                or any(c.isspace() for c in meta[field])):
            raise InvalidInformalization(f"{field} must be an absolute HTTP(S) URL")
    return meta, "\n".join(lines[end + 1:])


class RenderedNote(NamedTuple):
    meta: dict
    body: str
    html: str


def read_note(content, *, maintainer=False, path="", repository=None, import_config=None):
    location = f"{path}: " if path else ""
    try:
        meta, body = note_parts(content, maintainer=maintainer, import_config=import_config)
    except InvalidInformalization as error:
        raise InvalidInformalization(f"{location}{error}") from error
    source = meta.get("source")
    if not source:
        if repository is None:
            settings = Path(__file__).resolve().parents[1] / "site-settings.json"
            repository = json.loads(settings.read_text())["repository"]
        source = repository + "/blob/main/" + quote(str(path))
    try:
        fragment = render_informalization(body, source)
        size = len(fragment.encode("utf-8"))
    except Exception as error:
        raise InvalidInformalization(f"{location}{str(error) or type(error).__name__}") from error
    if size > MAX_RENDERED_BYTES:
        raise InvalidInformalization(
            f"{location}rendered HTML is {size:,} UTF-8 bytes (limit {MAX_RENDERED_BYTES:,} bytes)"
        )
    return RenderedNote(meta, body, fragment)


def parse_note(content, *, maintainer=False):
    return read_note(content, maintainer=maintainer).meta


def validate(repo, base, head, author, notes, database, *, maintainer=False):
    if not maintainer and len({(PurePosixPath(path).parts[1], module) for path, module, _ in notes}) > 1:
        raise InvalidInformalization("a public pull request must cover one package and one module")
    proof = directory_proof(lambda name: git(repo, "show", base + ":" + name))
    repository = json.loads(git(repo, "show", base + ":site-settings.json"))["repository"]
    with sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True) as db:
        for path, module, oid in notes:
            spec = proof["packages"].get(PurePosixPath(path).parts[1], {})
            cfg = json.loads(git(repo, "show", base + ":" + spec["importConfig"])) if "importConfig" in spec else None
            if not maintainer:
                previous = git(repo, "ls-tree", "-z", base, "--", path)
                if previous.startswith(b"100644 blob "):
                    previous_oid = previous.partition(b"\t")[0].split()[-1].decode("ascii")
                    previous_meta, _ = note_parts(git(repo, "cat-file", "blob", previous_oid), maintainer=True, import_config=cfg)
                    if previous_meta["license"] == "with-permission" or previous_meta.get("entry_type") == "source-documentation":
                        raise InvalidInformalization("a maintainer must edit an imported record")
            if oid is None:
                continue
            if not maintainer:
                # Inspect the object size before bringing the proposed blob into memory.
                check_public_size(int(git(repo, "cat-file", "-s", oid)))
            meta = read_note(git(repo, "cat-file", "blob", oid), maintainer=maintainer,
                             path=path, repository=repository, import_config=cfg).meta
            if meta["module"] != module or meta["author"] != author:
                raise InvalidInformalization("module and author must match the contribution path")
            if PurePosixPath(path).stem != note_key(author, meta["writer"]):
                raise InvalidInformalization("filename must match the handle and writer slug")
            package = PurePosixPath(path).parts[1]
            if package not in proof["packages"] or meta["source_commit"] != proof["packages"][package]["commit"]:
                raise InvalidInformalization("source_commit differs from the trusted proof pin")
            owner = db.execute("SELECT id FROM modules WHERE package=? AND path=?", (package,module)).fetchone()
            if owner is None:
                raise InvalidInformalization("module is absent from the trusted database")
            if meta["declarations"] and not proof["packages"][package]["hasDeclarationIndex"]:
                raise InvalidInformalization(f"{package} has no declaration index; leave declarations empty")
            for name in meta["declarations"]:
                if not db.execute("SELECT 1 FROM declarations WHERE module=? AND name=?", (owner[0], name)).fetchone():
                    raise InvalidInformalization("named declaration is absent from the cited module")
            agreements = meta.get("agrees_with", {})
            if not isinstance(agreements, dict):
                raise InvalidInformalization("agrees_with must map handle--writer-slug keys to informalization digests")
            for peer, digest in agreements.items():
                if not isinstance(peer,str) or "--" not in peer or peer == PurePosixPath(path).stem:
                    raise InvalidInformalization("invalid agreement target")
                handle, slug = peer.split("--",1)
                if not HANDLE.fullmatch(handle) or len(handle)>39 or not slug or writer_slug(slug) != slug:
                    raise InvalidInformalization("invalid agreement target")
                target = str(PurePosixPath(path).with_name(peer + ".md"))
                # Read authored changes as blobs. An unchanged peer on a diverged
                # branch must match the revision now in the target branch.
                ancestor = git(repo, "merge-base", base, head).decode().strip()
                changed = git(repo, "diff", "--name-only", ancestor, head, "--", target)
                revision = head if handle == author and changed else base
                entry = git(repo, "ls-tree", "-z", revision, "--", target)
                if not entry.startswith(b"100644 blob "):
                    raise InvalidInformalization("agreement peer informalization is missing")
                peer_oid = entry.partition(b"\t")[0].split()[-1].decode("ascii")
                if hashlib.sha256(git(repo, "cat-file", "blob", peer_oid)).hexdigest() != digest:
                    raise InvalidInformalization("agreement peer informalization digest differs")


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--repo", type=Path, default=Path("."))
    cli.add_argument("--base", required=True)
    cli.add_argument("--head", required=True)
    cli.add_argument("--author", required=True)
    cli.add_argument("--maintainer", action="store_true", help="Trusted base verified the PR submitter has a maintainer role")
    mode = cli.add_mutually_exclusive_group(required=True)
    mode.add_argument("--scope", action="store_true", help="print informalization or code for CI routing")
    mode.add_argument("--database", type=Path, help="SQLite file compiled from the trusted base")
    args = cli.parse_args()
    try:
        notes = contribution(args.repo, args.base, args.head, args.author)
        if args.scope:
            print("code" if notes is None else "informalization")
        elif notes is None:
            print("No informalization changes.")
        else:
            validate(args.repo, args.base, args.head, args.author, notes, args.database, maintainer=args.maintainer)
            print(f"Informalization contribution accepted. Validated {len(notes)} added or modified files.")
    except (ValueError, yaml.YAMLError, UnicodeError, sqlite3.Error, subprocess.CalledProcessError) as e:
        print("Informalization check failed:", e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

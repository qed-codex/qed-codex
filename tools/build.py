"""Build the original RH directory from its ledger and checked source snapshots."""
from source_registry import directory_proof, populate_proofs

import argparse
import csv
import gzip
import hashlib
import json
import sqlite3
import tempfile
import time
from collections import defaultdict
from pathlib import Path

import yaml
import disputes
from mirror_projection import populate_board
from submission_order import submission_order
from check_informalization_pr import InvalidInformalization, note_key, read_note
from informalizations import agreement_json
from note_headings import index_headings
from search_counts import populate_search_counts
from statement_links import DECLS_SHA, unlinked_cards
from urllib.parse import urlsplit
from seed import PROOF, rows, verify_version

SHORE = {
    "constants.csv.gz": "2964f5236046325ac7884906cb9517b0aa582330dd48a07eef291cb579444820",
    "decls.csv.gz": DECLS_SHA,
}
UP = "upstream/e5ae821a/"
BUILD_SQLITE = "3.46.1"
TABLES = [
    "inventory.tsv.gz",
    "metrics.tsv.gz",
    "imports.json.gz",
    "spine.tsv",
    "rh-trace.tsv.gz",
    UP + "kernel-file-usage.tsv.gz",
    UP + "metrics.tsv.gz",
]


def sha(path):
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def csv_rows(path):
    with gzip.open(path, "rt", newline="") as f:
        yield from csv.DictReader(f)


def link_rows(path_ids, ledger, declarations=()):
    for r in rows(ledger):
        path, url = r["module"], r["url"]
        if path not in path_ids:
            raise ValueError(f"Outside link cites unknown module {path}")
        parsed = urlsplit(url)
        if parsed.scheme not in ("https","http") or not parsed.hostname or not r["author"].strip():
            raise ValueError(f"Outside link requires an author and HTTP(S) address: {url}")
        name = r.get("declaration") or ""
        if name and (path_ids[path],name) not in declarations:
            raise ValueError(f"Unknown declaration {name} for outside link in {path}")
        yield path_ids[path], r["author"], url, r.get("label") or "", name


def build(repo, release, dest, comparison=False, issue_data=None):
    if sqlite3.sqlite_version != BUILD_SQLITE and not comparison:
        raise ValueError(f"Build requires SQLite {BUILD_SQLITE}, found {sqlite3.sqlite_version}. See README.")
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=dest.parent) as tmp:
        working = Path(tmp) / "proof.sqlite3"
        populate(repo, release, working, issue_data)
        working.replace(dest)


def populate(repo, release, working, issue_data):
    verify_version(repo, ["results/" + t for t in TABLES])
    for file, expected in SHORE.items():
        if sha(release / file) != expected:
            raise ValueError(f"Incorrect v0.2.1 release bytes for {file}")
    results = repo / "results"
    inventory = sorted(rows(results / TABLES[0]), key=lambda r: r["path"])
    module_ids = {r["module"]: i for i, r in enumerate(inventory, 1)}
    path_ids = {r["path"]: module_ids[r["module"]] for r in inventory}
    owners = {module_ids[r["module"]]: ("riemann-hypothesis" if r["category"] == "Novel" else "mathlib") for r in inventory}
    metrics = {
        r["module"]: (int(r["import_rank"]), int(r["disconnected_novel"]))
        for r in rows(results / "metrics.tsv.gz")
        if r["import_rank"]
    }
    upstream = {
        r["module"]: int(r["import_rank"]) for r in rows(results / UP / "metrics.tsv.gz") if r["import_rank"]
    }
    usage = {r["original_path"]: r for r in rows(results / UP / "kernel-file-usage.tsv.gz")}
    spine = {r["path"]: int(r["rank"]) for r in rows(results / "spine.tsv")}
    masks = defaultdict(int)
    mathlib_masks = defaultdict(int)
    for r in csv_rows(release / "constants.csv.gz"):
        mask = int(r["thm_mask"] or 0)
        if r["origin"] == "mathlib":
            mathlib_masks[r["module"]] |= mask
        elif r["origin"] == "project" and r["shared_aux"] == "false" and r["decl"] and mask:
            masks[(r["file"], r["decl"])] |= mask

    db = sqlite3.connect(working)
    db.executescript("""PRAGMA page_size=32768; PRAGMA secure_delete=ON; PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF;
                        PRAGMA temp_store=MEMORY; PRAGMA cache_size=-120000; PRAGMA foreign_keys=ON;""")
    db.executescript(Path("tools/schema.sql").read_text())

    def module_rows():
        for r in inventory:
            name, path = r["module"], r["path"]
            project = r["category"] == "Novel"
            u = usage[path] if project else None
            rank, cut = metrics.get(name, (None, None))
            yield (
                module_ids[name],
                path,
                project,
                rank,
                cut,
                int(u["target_mask"]) if u else mathlib_masks[name],
                int(u["trace_reached"]) if u else 0,
                1 - int(u["upstream_retained"]) if u else None,
                upstream.get(name),
                spine.get(path), owners[module_ids[name]],
            )

    db.executemany("INSERT INTO modules VALUES(?,?,?,?,?,?,?,?,?,?,?)", module_rows())
    packages = directory_proof()["packages"]
    package_paths = {(owners[mid], path): mid for path, mid in path_ids.items()}
    extra_names = []
    for package, spec in packages.items():
        if "moduleList" not in spec:
            continue
        paths = Path(spec["moduleList"]).read_text().splitlines()
        if paths != sorted(set(paths)) or any(not p.endswith(".lean") for p in paths):
            raise ValueError(f"Invalid module inventory for {package}")
        for path in paths:
            mid = len(package_paths) + 1
            package_paths[package, path] = mid
            db.execute("INSERT INTO modules(id,path,package,project) VALUES(?,?,?,1)", (mid,path,package))
            name = path.removeprefix(spec["sourceRoot"]).removesuffix(".lean").replace("/",".")
            extra_names.append((name.rsplit(".",1)[-1].lower(), name, "module", mid, package))
    offset = len(package_paths)
    with gzip.open(results / "imports.json.gz", "rt") as f:
        graph = json.load(f)
    db.executemany(
        "INSERT INTO imports VALUES(?,?)",
        (
            (module_ids[s], module_ids[d])
            for s, deps in graph.items()
            if s in module_ids
            for d in deps
            if d in module_ids
        ),
    )
    del graph
    ids = {}
    verified_used = 0

    def declaration_rows():
        nonlocal verified_used
        for i, r in enumerate(csv_rows(release / "decls.csv.gz"), 1):
            mid = path_ids[r["file"]]
            name = r["decl"]
            if r["origin"] != "project" or (mid, name) in ids:
                raise ValueError(f"Ambiguous project declaration {name}")
            ids[mid, name] = i
            mask = masks.get((r["file"], name), 0)
            if bool(mask) != (r["in_cone"] == "true"):
                raise ValueError(f"Original kernel mask mismatch for {name}")
            verified_used += bool(mask)
            yield (
                i,
                mid,
                name,
                int(r["start_line"]) if r["start_line"] else None,
                int(r["end_line"]) if r["end_line"] else None,
                r["kind"],
                mask, owners[mid],
            )

    db.executemany("INSERT INTO declarations VALUES(?,?,?,?,?,?,?,?)", declaration_rows())
    masks.clear()
    seen = {}

    def trace_rows():
        for i, r in enumerate(rows(results / "rh-trace.tsv.gz"), 1):
            mid = module_ids[r["module"]]
            key = (mid, int(r["line"]), r["name"])
            if key in seen:
                raise ValueError(f"Duplicate trace site {key}")
            parent = (module_ids[r["caller_module"]], int(r["caller_decl_line"]), r["caller"])
            root = r["depth"] == "0"
            if root and (key != parent or r["name"] != "riemannHypothesis" or i != 1):
                raise ValueError("Unexpected trace root")
            parent_id = None if root else seen[parent]
            seen[key] = i
            decl = ids.get((mid, r["name"]))
            yield i, mid, key[1], decl, None if decl else r["name"], parent_id, int(r["use_line"])

    db.executemany("INSERT INTO trace VALUES(?,?,?,?,?,?,?)", trace_rows())
    seen.clear()
    db.executemany("INSERT INTO links VALUES(?,?,?,?,?)", link_rows(path_ids, PROOF/"links.tsv", ids))
    old_root = PROOF / "informalizations"
    root = Path("packages")
    notes = sorted(root.glob("*/informalizations/**/*.md"))
    # Allow the reviewed records between the compiler change and their Git moves.
    notes += sorted(old_root.rglob("*.md"))
    order = submission_order(root, previous=(old_root,))
    ledger_hashes = {(note.parent, note.stem): sha(note) for note in notes}
    repository = json.loads(Path("site-settings.json").read_text())["repository"]
    import_configs = {key: json.loads(Path(s["importConfig"]).read_text()) for key, s in packages.items() if "importConfig" in s}
    for note in notes:
        package = "riemann-hypothesis" if note.is_relative_to(old_root) else note.relative_to(root).parts[0]
        meta, body, fragment = read_note(note.read_bytes(), maintainer=True, path=note, repository=repository,
                                         import_config=import_configs.get(package))
        mid = package_paths[package, meta["module"]]
        source_commit = packages[package]["commit"]
        folder = old_root if note.is_relative_to(old_root) else root / package / "informalizations"
        author_path = folder / meta["module"] / (note_key(meta["author"], meta["writer"]) + ".md")
        names = meta["declarations"]
        if (
            note != author_path
            or meta["source_commit"] != source_commit
            or not isinstance(names, list)
            or not all((mid, n) in ids for n in names)
        ):
            raise ValueError(f"Invalid informalization {note}")
        if meta.get("entry_type") == "source-documentation":
            fragment, headings = index_headings(body, fragment, note.stem)
            db.executemany("INSERT INTO note_headings(module,name,lookup,anchor) VALUES(?,?,?,?)",
                           ((mid, *heading) for heading in headings))
        db.execute(
            """INSERT INTO informalizations(module,author,kind,writer,origin,submitted_order,license,source_commit,declarations_json,source_url,body,informalization_html,agrees_with_json,copyright,entry_type,license_source,notice,changes)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                mid,
                meta["author"],
                meta["kind"],
                meta["writer"],
                meta["origin"],
                order[note.as_posix()],
                meta["license"],
                source_commit,
                json.dumps(names, ensure_ascii=False, separators=(",", ":")),
                meta.get("source"),
                body.strip(),
                fragment,
                agreement_json(note, meta.get("agrees_with", {}), ledger_hashes),
                "" if meta.get("copyright_status") == "absent" else meta.get("copyright"),
                meta.get("entry_type", "informalization"),
                meta.get("license_source"), meta.get("notice"), meta.get("changes"),
            ),
        )
    issue_paths = {pkg + ":" + path: mid for (pkg,path), mid in package_paths.items()}
    disputes.store(db, disputes.snapshot(issue_paths) if issue_data is None else issue_data, issue_paths)
    # IDs follow original paths in binary order. Keep missing cuts after measured cuts.
    populate_board(db)
    populate_proofs(db, packages)
    # A covering prefix scan returns the display names and the destination IDs together.
    db.executemany(
        "INSERT INTO shortnames VALUES(?,?,?,?,?)",
        ((name.rsplit(".", 1)[-1].lower(), name, "module", mid, owners[mid]) for name, mid in module_ids.items()),
    )
    db.executemany(
        "INSERT INTO shortnames VALUES(?,?,?,?,?)",
        ((name.rsplit(".", 1)[-1].lower(), name, "declaration", ref, owners[mid]) for (mid, name), ref in ids.items()),
    )
    db.executemany("INSERT INTO shortnames VALUES(?,?,?,?,?)", extra_names)
    ids.clear()
    db.executescript(f"""
        CREATE INDEX decl_by_module ON declarations(module,start);
        CREATE INDEX trace_by_decl ON trace(declaration) WHERE declaration IS NOT NULL;
        CREATE INDEX imports_by_dependency ON imports(dependency);
        CREATE INDEX disputes_by_module ON disputes(module);
        -- Sorting docids puts the project before library imports without collecting every hit.
        INSERT INTO names(rowid,module_path) SELECT (1 << 40)+id,path FROM modules WHERE project;
        INSERT INTO names(rowid,module_path) SELECT (2 << 40)+id,path FROM modules WHERE NOT project;
        INSERT INTO names(rowid,declaration_name) SELECT {offset}+id,name FROM declarations;
        INSERT INTO names(rowid,declaration_name) SELECT (3 << 40)+id,name FROM note_headings;
        INSERT INTO names(names) VALUES('optimize');
    """)
    populate_search_counts(db)
    counts = {
        t: db.execute(f"SELECT count(*) FROM {t}").fetchone()[0]
        for t in (
            "modules",
            "imports",
            "declarations",
            "trace",
            "links",
            "informalizations",
            "disputes",
            "shortnames",
            "most_wanted",
        )
    }
    if [counts[t] for t in ("modules", "imports", "declarations", "trace")] != [
        184039 + len(extra_names),
        925310,
        1063284,
        641100,
    ]:
        raise ValueError(f"Reference counts differ: {counts}")
    counts["source_documentation"] = db.execute("SELECT count(*) FROM informalizations WHERE entry_type='source-documentation'").fetchone()[0]
    counts["informalizations"] -= counts["source_documentation"]
    counts["unmatched_statements"] = len(unlinked_cards(url for (url,) in db.execute("SELECT DISTINCT url FROM links")))
    counts["declarations_in_five_cones"] = verified_used
    counts["fts_declaration_offset"] = offset
    if offset + counts["declarations"] >= 1 << 40:
        raise ValueError("FTS document IDs would overlap the imported-module interval")
    db.executemany("INSERT INTO summary VALUES(?,?)", sorted(counts.items()))
    db.commit()
    db.execute("VACUUM")
    if (
        db.execute("PRAGMA integrity_check").fetchone()[0] != "ok"
        or db.execute("PRAGMA foreign_key_check").fetchone()
    ):
        raise ValueError("SQLite integrity check failed")
    db.close()
    print(json.dumps(counts), flush=True)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("analysis", type=Path)
    cli.add_argument("shore", type=Path)
    cli.add_argument("--out", type=Path, default=Path("build/rh.sqlite3"))
    cli.add_argument(
        "--comparison-build",
        action="store_true",
        help="Allow another SQLite for a logical-content comparison",
    )
    cli.add_argument("--disputes", type=Path, help="Replay a normalized issue snapshot instead of fetching the open disputes")
    args = cli.parse_args()
    start = time.monotonic()
    try:
        build(args.analysis, args.shore, args.out, args.comparison_build,
              json.loads(args.disputes.read_text()) if args.disputes else None)
    except InvalidInformalization as error:
        cli.exit(1, f"Database build failed: {error}\n")
    print(f"Database build: {time.monotonic() - start:.2f} seconds", flush=True)

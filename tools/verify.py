"""Verify the static upload against SQLite, including page addresses and search plans."""

import argparse
import gzip
import hashlib
import json
import sqlite3
from itertools import islice
from trail_pieces import NODES_PER_PIECE
from pathlib import Path

from disputes import manifest_fields
from check_links import directory_urls, verify_receipt
from fixtures import parameters
from tables import ordered_tables, row_digest


def query_plans(db, groups, offset):
    plans = {}
    for kind, queries in groups.items():
        for label, sql in queries.items():
            ops = [
                r[3]
                for r in db.execute(
                    "EXPLAIN QUERY PLAN " + sql,
                    parameters(kind, "RowSrc", offset),
                )
            ]
            # The FTS index and the bounded result/recursive work queues have SCAN labels.
            for op in ops:
                if op.startswith("SCAN ") and not (
                    (
                        kind in ("search", "searchCount")
                        and (
                            op in {"SCAN hits", "SCAN candidates", "SCAN exact"}
                            or (op.startswith("SCAN names VIRTUAL TABLE INDEX") and ":M" in op)
                        )
                    )
                    or (kind == "searchCount" and op == "SCAN CONSTANT ROW")
                    or (kind == "trail" and op in {"SCAN trail", "SCAN c"})
                ):
                    raise ValueError(f"Unexpected full scan for {kind}: {op}")
            if not any("SEARCH " in op or "VIRTUAL TABLE INDEX" in op for op in ops):
                raise ValueError(f"Unindexed lookup for {kind}: {ops}")
            plans[f"{kind}.{label}"] = ops
    return plans


def verify_trail_sample(db, directory, stride=97):
    """Compare packed target-to-root chains with the rows reached in SQLite."""
    targets = db.execute("SELECT id FROM trace WHERE declaration IS NOT NULL ORDER BY id")
    previous_piece = None
    count = 0
    for target, in islice(targets, 0, None, stride):
        piece = directory / str(target // NODES_PER_PIECE)
        if piece != previous_piece:
            with gzip.open(piece, "rt", encoding="utf-8") as stream:
                packed = json.load(stream)
            previous_piece = piece
        expected = db.execute("""
            WITH RECURSIVE chain(id,depth) AS (
                SELECT ?,0 UNION ALL
                SELECT t.parent,c.depth+1 FROM chain c JOIN trace t ON t.id=c.id
                WHERE t.parent IS NOT NULL
            )
            SELECT t.id,t.parent,m.package,m.path,t.line,t.use_line,d.id IS NOT NULL,
                   coalesce(d.name,t.source_name)
            FROM chain c JOIN trace t ON t.id=c.id JOIN modules m ON m.id=t.module
            LEFT JOIN declarations d ON d.id=t.declaration ORDER BY c.depth""", (target,))
        for node, *fields in expected:
            if packed.get(str(node)) != fields:
                raise ValueError(f"Packed trail differs for target {target}, node {node} in {piece}")
        count += 1
    return count


def verify(database, site, receipt=Path("proofs/rh/outside-link-check.json"), *, review=False):
    manifest = json.loads((site / "proof.json").read_text())
    ident = manifest["buildId"]
    folder = site / "db" / ident
    page_size = manifest["pageBytes"]
    with sqlite3.connect(f"{database.resolve().as_uri()}?mode=ro", uri=True) as db:
        pages = db.execute("PRAGMA page_count").fetchone()[0]
        assert pages == manifest["pageCount"] and page_size == 32768
        internal = [
            r[0] for r in db.execute("SELECT pageno FROM dbstat WHERE pagetype='internal' ORDER BY pageno")
        ]
        assert internal == manifest["interior"]
        verify_trail_sample(db, folder / "trails-v1")
        dispute_metadata = manifest_fields(db)
        urls = directory_urls(r[0] for r in db.execute("SELECT DISTINCT url FROM links"))
        outside = verify_receipt(json.loads(receipt.read_text()), urls, review=review)
        counts = dict(db.execute("SELECT metric,value FROM summary ORDER BY metric"))
        content = {
            name: row_digest([c[0] for c in cursor.description], cursor)
            for name, _, cursor in ordered_tables(db)
        }
        plans = query_plans(
            db, json.loads((site / "queries.json").read_text()), counts["fts_declaration_offset"]
        )
    individual = folder / "p"
    per_piece = manifest.get("pagesPerPiece", 1)
    assert per_piece in (1, 2, 4, 8)
    pieces = (pages + per_piece - 1) // per_piece
    assert {int(p.name) for p in individual.iterdir()} == set(range(1, pieces + 1))
    interior_set = set(internal)
    reconstructed = hashlib.sha256()
    with gzip.open(folder / "interior", "rb") as bundle, database.open("rb") as source:
        for piece in range(pieces):
            first = piece * per_piece + 1
            count = min(per_piece, pages - first + 1)
            raw = gzip.decompress((individual / str(piece + 1)).read_bytes())
            if len(raw) != count * page_size or source.read(len(raw)) != raw:
                raise ValueError(f"Incorrect bytes in piece {piece + 1}, starting at page {first}")
            for index in range(count):
                if first + index in interior_set and bundle.read(page_size) != raw[index * page_size:(index + 1) * page_size]:
                    raise ValueError(f"Incorrect interior page {first + index}")
            reconstructed.update(raw)
        assert not source.read(1) and not bundle.read(1)
    database_hash = reconstructed.hexdigest()
    expected_id = "gzip-v1-" + database_hash + (f"-p{per_piece}" if per_piece != 1 else "")
    assert expected_id == ident
    # Early packages used direct vendor paths. Current immutable URLs must match their bytes.
    if not (site / "vendor/index.mjs").exists():
        engine, = (site / "vendor").iterdir()
        expected_files = {"index.mjs", "sqlite3.wasm", "sqlite3-opfs-async-proxy.js", "pako-inflate.mjs"}
        assert {p.name for p in engine.iterdir()} == expected_files
        digest = hashlib.sha256()
        for asset in sorted(engine.iterdir()):
            digest.update(asset.name.encode() + b"\0" + hashlib.sha256(asset.read_bytes()).digest())
        assert engine.name == digest.hexdigest(), "Incorrect content address for the SQLite engine"
        for asset in (site / "assets").glob("*/*"):
            assert asset.parent.name == hashlib.sha256(asset.read_bytes()).hexdigest(), asset
    tree = hashlib.sha256()
    sizes = {}
    for p in sorted(site.rglob("*")):
        if p.is_file():
            name = p.relative_to(site).as_posix()
            sizes[name] = p.stat().st_size
            tree.update(name.encode() + b"\0" + hashlib.sha256(p.read_bytes()).digest())
    assert len(sizes) < 20000
    return {
        "databaseSha256": database_hash,
        "sqliteVersion": sqlite3.sqlite_version,
        "pageBytes": page_size,
        "pages": pages,
        "pagesPerPiece": per_piece,
        "pieceFiles": pieces,
        "databaseBytes": database.stat().st_size,
        "interiorPages": len(internal),
        "interiorBytes": len(internal) * page_size,
        "interiorGzipBytes": (folder / "interior").stat().st_size,
        "deployFiles": len(sizes),
        "deployBytes": sum(sizes.values()),
        "treeSha256": tree.hexdigest(),
        "counts": counts,
        "tableContent": content,
        "plans": plans,
        **dispute_metadata,
        "outsideLinks": {k:v for k,v in outside.items() if k!="destinations"},
    }


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("database", type=Path)
    cli.add_argument("site", type=Path)
    cli.add_argument(
        "--check-content",
        type=Path,
        metavar="REFERENCE_MANIFEST",
        help="Compare ordered logical table contents even if SQLite lays out the file differently",
    )
    cli.add_argument("--link-check", type=Path, default=Path("proofs/rh/outside-link-check.json"),
                     help="Dated URL checks for the complete compiled ledger")
    cli.add_argument("--pr-review",action="store_true",help="List newly proposed URLs as pending a trusted live build")
    a = cli.parse_args()
    report = verify(a.database, a.site, a.link_check, review=a.pr_review)
    if a.check_content:
        reference = json.loads(a.check_content.read_text())["tableContent"]
        mismatch = sorted(
            k
            for k in report["tableContent"].keys() | reference.keys()
            if report["tableContent"].get(k) != reference.get(k)
        )
        if mismatch:
            cli.exit(1, f"Table content differs: {', '.join(mismatch)}\n")
    print(json.dumps(report, indent=2))

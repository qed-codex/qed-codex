"""Replay the native short-name comparison or summarize the browser measurement TSV."""
import argparse
import csv
import json
import sqlite3
import statistics
import sys
from pathlib import Path

from fixtures import parameters


def load(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def native_report(database, sample):
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["short", "fts_rank_within_20", "first_result", "total"])
    queries = json.loads(Path("site/queries.json").read_text())
    terms = [r["input"] for r in load(sample) if r["browser"] == "chromium" and r["category"] == "search"]
    with sqlite3.connect(database.resolve().as_uri()+"?mode=ro", uri=True) as db:
        offset, = db.execute("SELECT value FROM summary WHERE metric='fts_declaration_offset'").fetchone()
        for term in terms:
            args = parameters("search", term, offset)
            first = db.execute(queries["search"]["matches"], args).fetchone()[0]
            total, = db.execute(queries["searchCount"]["totals"], args).fetchone()
            rank = ""
            for index, (ref,) in enumerate(db.execute("SELECT rowid FROM names WHERE names MATCH ? ORDER BY rowid LIMIT 20", args[:1]), 1):
                if ref > 1 << 40:
                    path, = db.execute("SELECT path FROM modules WHERE id=?", (ref % (1 << 40),)).fetchone()
                    short = Path(path).stem
                else:
                    name, = db.execute("SELECT name FROM declarations WHERE id=?", (ref-offset,)).fetchone()
                    short = name.rsplit(".", 1)[-1]
                if short.lower() == term:
                    rank = index
                    break
            out.writerow([term, rank, first, total])


def hosted_report(path, over):
    rows = load(path)
    assert len(rows) == 1659
    with over.open("w", encoding="utf-8", newline="") as stream:
        columns = ["browser","category","input","ms","transfer_bytes","db_transfer_bytes"]
        out = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore", delimiter="\t", lineterminator="\n")
        out.writeheader()
        for engine in ("chromium","firefox","webkit"):
            group = [r for r in rows if r["browser"] == engine]
            searches = [r for r in group if r["category"] in {"search","qualified-search","path-search"}]
            assert len(searches) == 220
            exceeded = [r for r in searches if int(r["ms"]) > 2000 or (r["transfer_bytes"] and int(r["transfer_bytes"]) > 1000000)]
            for row in exceeded:
                out.writerow({key: row[key] if row[key] != "" else "unavailable" for key in columns})
            print(engine, f'{sum(r["status"]=="PASS" for r in group)}/{len(group)} passed;', len(exceeded), "over threshold")
            for col in columns[-3:]:
                measured = [r for r in searches if r[col] != ""]
                worst = max(measured, key=lambda r: int(r[col]))
                med = statistics.median(int(r[col]) for r in measured)
                print(" ",col, "n",len(measured),"median",med,"max",worst[col],worst["input"])


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    modes = cli.add_subparsers(dest="mode", required=True)
    native = modes.add_parser("native")
    native.add_argument("database", type=Path)
    native.add_argument("sample", type=Path)
    hosted = modes.add_parser("hosted")
    hosted.add_argument("results", type=Path)
    hosted.add_argument("over_threshold", type=Path)
    args = cli.parse_args()
    if args.mode == "native":
        native_report(args.database, args.sample)
    else:
        hosted_report(args.results, args.over_threshold)

"""Compute native SQLite result fixtures for the browser measurements."""

import argparse
import json
import re
import sqlite3
from pathlib import Path

ANCHOR = "UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter"


def parameters(kind, value, fts_offset, package="riemann-hypothesis", source_root=None):
    if kind == "wantedSource":
        return package, int(value) if str(value).isdecimal() else 1
    if kind == "wanted":
        return (int(value) if str(value).isdecimal() else 1,)
    if kind == "typeahead":
        return (value.strip().lower(),)
    if kind in ("search", "searchCount"):
        raw = value.strip()
        words = re.findall(r"[^\W_]+", raw)
        expression = " AND ".join(f'"{word}"' for word in words)
        module = raw.removeprefix("src/").removesuffix(".lean").replace("/", ".")
        return (expression, fts_offset, 0, raw, module.rsplit(".", 1)[-1].lower(),
                module, raw.rsplit(".", 1)[-1].lower(), raw.lower())
    full = value.strip()
    if kind == "module" and full.endswith(".lean"):
        prefix = source_root if source_root is not None else ("src/" if package == "riemann-hypothesis" else "")
        full = full.removeprefix(prefix)
        full = full[:-5].replace("/", ".")
    return full.rsplit(".", 1)[-1].lower(), full, package


def fixtures(path):
    statements = json.loads(Path("site/queries.json").read_text())
    with sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True) as db:
        db.row_factory = sqlite3.Row

        offset = db.execute("SELECT value FROM summary WHERE metric='fts_declaration_offset'").fetchone()[0]

        def run(kind, value):
            results = {
                k: [dict(r) for r in db.execute(sql, parameters(kind, value, offset))]
                for k, sql in statements[kind].items()
            }
            if not any(results.values()):
                raise ValueError(f"Empty fixture for {kind}")
            return {"kind": kind, "value": value, "expected": results}

        def spine(rank):
            return db.execute("SELECT path FROM modules WHERE spine_rank=?", (rank,)).fetchone()[0]

        queries = [
            run("module", spine(1)),
            *(run("typeahead", t) for t in ("RowS", "galois", "zero", "siegel", "a", "Α", "_aux")),
            *(run("search", t) for t in ("RowSrc", "zero*", "Formalism siegel", "map*")),
            run("declaration", ANCHOR),
            run("trail", ANCHOR),
        ]
        if queries[-1]["expected"]["sites"][-1]["name"] != "riemannHypothesis":
            raise ValueError("Trail does not reach RH")
        return {"prime": run("module", spine(2)), "queries": queries}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("database", type=Path)
    args = cli.parse_args()
    print(json.dumps(fixtures(args.database), ensure_ascii=False))

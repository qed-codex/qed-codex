"""Repack the same logical database for the two alternate page-size controls."""

import argparse
import json
import sqlite3
import tempfile
from pathlib import Path


def alternatives(database):
    results = {}
    with tempfile.TemporaryDirectory() as temp:
        for size in (16384, 65536):
            copy = Path(temp) / f"{size}.sqlite3"
            with sqlite3.connect(database) as db:
                db.execute(f"PRAGMA page_size={size}")
                db.execute("VACUUM INTO ?", (str(copy),))
            with sqlite3.connect(copy) as db:
                results[size] = {
                    "bytes": copy.stat().st_size,
                    "pages": db.execute("PRAGMA page_count").fetchone()[0],
                    "interior": db.execute(
                        "SELECT count(*) FROM dbstat WHERE pagetype='internal'"
                    ).fetchone()[0],
                }
    return results


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("database", type=Path)
    print(json.dumps(alternatives(cli.parse_args().database), indent=2))

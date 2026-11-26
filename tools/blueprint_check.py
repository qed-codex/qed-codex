"""Check explicit TOML declaration names in a pinned copy of the blueprint."""

import argparse
import json
import sqlite3
import subprocess
import tomllib
from collections import Counter
from pathlib import Path

PIN = "137d97602647e450901981a7decfb86ab3024a48"
STATEMENTS = {"theorem", "lemma", "proposition", "corollary", "definition", "remark"}


def inspect(repo, database):
    paths = subprocess.check_output(
        ["git", "-C", repo, "ls-tree", "-r", "--name-only", PIN, "--", "blueprint/"],
        text=True,
    )
    by_kind = Counter()
    named = Counter()
    statements = {}
    for path in paths.splitlines():
        if not path.endswith(".md"):
            continue
        body = subprocess.check_output(
            ["git", "-C", repo, "show", f"{PIN}:{path}"]
        ).decode()
        if not body.startswith("+++\n"):
            continue
        meta = tomllib.loads(body.split("+++\n", 2)[1])
        kind = meta["kind"]
        if kind in STATEMENTS:
            by_kind[kind] += 1
            names = meta.get("lean", [])
            if not isinstance(names, list) or not all(
                isinstance(n, str) and n for n in names
            ):
                raise ValueError(f"Unrecognized Lean field {path}")
            if names:
                named[kind] += 1
            statements[path] = set(names)
    names = set().union(*statements.values())
    with sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True) as db:
        found = {
            n
            for n in names
            if db.execute(
                "SELECT 1 FROM shortnames WHERE short=? AND full=? AND kind='declaration'",
                (n.rsplit(".", 1)[-1].lower(), n),
            ).fetchone()
        }
    return {
        "blueprintCommit": PIN,
        "statementKinds": dict(sorted(by_kind.items())),
        "withLeanField": dict(sorted(named.items())),
        "statements": len(statements),
        "statementsWithNames": sum(bool(v) for v in statements.values()),
        "distinctNames": len(names),
        "matchedOriginalProjectNames": len(found),
        "statementsWithOriginalProjectName": sum(
            bool(ns & found) for ns in statements.values()
        ),
        "unmatchedNames": sorted(names - found),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("database", type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.blueprint, args.database), indent=2))

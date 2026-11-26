"""Snapshot the public identifiers of open, dispute-labelled module issues."""
from source_registry import directory_proof
import argparse
import csv
import gzip
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

REPO = "qed-codex/qed-codex"
LABEL = "dispute"


REASONS = {"missing module path", "malformed module path", "unknown module path"}


def issue_path(body, paths):
    sections = re.split(r"(?m)^### ", (body or "").replace("\r\n", "\n"))
    values = [s.partition("\n")[2].strip() for s in sections[1:]
              if s.partition("\n")[0].strip() == "Package and module path"]
    if not values or values == [""] or values == ["_No response_"]:
        return None, "missing module path"
    if len(values) != 1:
        return None, "malformed module path"
    path = values[0]
    if path.startswith("`") and path.endswith("`"):
        path = path[1:-1]
    pkg, sep, file = path.partition(":")
    if (not sep or not re.fullmatch(r"[a-z0-9-]+",pkg) or not file.endswith(".lean") or any(c in path for c in "\r\n\t\\`")
            or any(part in {"", ".", ".."} for part in file.split("/"))):
        return None, "malformed module path"
    if path not in paths:
        return None, "unknown module path"
    return path, None


def snapshot(paths):
    issues = {}
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "qed-codex-compiler"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    page = 1
    while True:
        url = f"https://api.github.com/repos/{REPO}/issues?state=open&labels={LABEL}&sort=created&direction=asc&per_page=100&page={page}"
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
            batch = json.load(response)
        for item in batch:
            if "pull_request" in item or item["state"] != "open" or LABEL not in {x["name"] for x in item["labels"]}:
                continue
            number = item["number"]
            path, reason = issue_path(item.get("body"), paths)
            issues[number] = {"number": number, "reason": reason} if reason else {"number": number, "module": path}
        if len(batch) < 100:
            break
        page += 1
    entries = [issues[n] for n in sorted(issues)]
    data = {"repository": REPO, "label": LABEL, "issues": [r for r in entries if "module" in r]}
    skipped = [r for r in entries if "reason" in r]
    if skipped:
        data["skipped"] = skipped
    return data


def rows(data, path_ids):
    if data["repository"] != REPO or data["label"] != LABEL:
        raise ValueError("Incorrect dispute snapshot repository or label")
    used = set()
    for issue in data["issues"]:
        number, path = issue["number"], issue.get("module")
        if type(number) is not int or number <= 0 or number in used or path not in path_ids:
            raise ValueError(f"Invalid or duplicate dispute #{number} for {path}")
        used.add(number)
        yield number, path_ids[path], f"https://github.com/{REPO}/issues/{number}"


def store(db, data, path_ids):
    valid = list(rows(data, path_ids))
    used = {number for number, _, _ in valid}
    skipped = []
    for r in data.get("skipped", []):
        number, reason = r["number"], r["reason"]
        if type(number) is not int or number <= 0 or number in used or reason not in REASONS:
            raise ValueError("Invalid skipped dispute in snapshot")
        used.add(number)
        skipped.append((number, reason))
    db.executemany("INSERT INTO disputes VALUES(?,?,?)", valid)
    if skipped:
        db.execute("CREATE TABLE skipped_disputes(number INTEGER PRIMARY KEY, reason TEXT NOT NULL)")
        db.executemany("INSERT INTO skipped_disputes VALUES(?,?)", sorted(skipped))
        for number, reason in sorted(skipped):
            print(f"Skipped dispute #{number}: {reason}", file=sys.stderr)


def manifest_fields(db):
    if not db.execute("SELECT 1 FROM sqlite_schema WHERE name='skipped_disputes' AND type='table'").fetchone():
        return {}
    return {"skippedDisputes": [{"number": n, "reason": reason} for n, reason in
                                db.execute("SELECT number, reason FROM skipped_disputes ORDER BY number")]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out", type=Path)
    parser.add_argument("--inventory", type=Path, default=Path("inputs/analysis/results/inventory.tsv.gz"))
    args = parser.parse_args()
    with gzip.open(args.inventory, "rt", newline="") as src:
        paths = {("riemann-hypothesis" if r["category"] == "Novel" else "mathlib") + ":" + r["path"] for r in csv.DictReader(src, delimiter="\t")}
    packages = directory_proof()["packages"]
    for package, spec in packages.items():
        if "moduleList" in spec:
            paths.update(package + ":" + path for path in Path(spec["moduleList"]).read_text().splitlines())
    args.out.write_text(json.dumps(snapshot(paths), indent=2, ensure_ascii=False)+"\n")

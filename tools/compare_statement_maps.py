"""Compare page identities with the reviewed address-name ledger and explain missing exact matches."""
import argparse
import csv
import gzip
import hashlib
import io
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

from statement_index import tsv
from statement_links import AUTHOR, SOURCE, current_rows

CONSTANTS_SHA = "2964f5236046325ac7884906cb9517b0aa582330dd48a07eef291cb579444820"


def baseline(revision, path):
    text = subprocess.check_output(["git","show",revision + ":" + path],text=True)
    return list(csv.DictReader(io.StringIO(text),delimiter="\t"))


def compare(shore, out, revision):
    old = baseline(revision, (SOURCE / "cards.tsv").as_posix())
    linked = {r["url"] for r in baseline(revision, "proofs/rh/links.tsv") if r["author"] == AUTHOR}
    named = {(c["card_id"],c["declaration"]) for c in old if c["declaration"]}
    unmatched = {c["card_id"] for c in old if c["url"] not in linked}
    new = current_rows()
    credited = {(r["card_id"],r["declaration"]) for r in new if r["module"]}
    missing = defaultdict(set)
    for r in new:
        if r["declaration"] and not r["module"]:
            missing[r["declaration"]].add(r["card_id"])
    with shore.open("rb") as f:
        if hashlib.file_digest(f,"sha256").hexdigest() != CONSTANTS_SHA:
            raise ValueError("Unrecognized constants table")
    evidence = defaultdict(set)
    with gzip.open(shore,"rt",newline="") as f:
        for r in csv.DictReader(f):
            if r["name"] in missing:
                evidence[r["name"]].add((r["origin"],r["decl"],r["module"]))
    rows = []
    for name in sorted(missing):
        for origin, owner, module in sorted(evidence.get(name, {("","","")})):
            rows.append((name,origin,owner,module,",".join(sorted(missing[name]))))
    out.mkdir(parents=True,exist_ok=True)
    tsv(out / "names-without-project-declaration.tsv",
        ("lean_name","compiled_constant_origin","compiled_owner","compiled_module","page_ids"),rows)
    projected = {r["card_id"] for r in new if r["module"]}
    pages = {r["card_id"]:r for r in new}
    tsv(out / "unmatched-pages.tsv", ("page_id","kind","title","url","tested_names"), (
        (key,pages[key]["kind"],pages[key]["title"],pages[key]["url"],
         ",".join(sorted(n for n,ids in missing.items() if key in ids))) for key in sorted(pages.keys()-projected)))
    categories = Counter(tuple(sorted({t[0] for t in evidence[name]})) for name in missing)
    totals = {"baseline":revision,"previousAddressNames":len(named),"confirmedAddressNames":len(credited & named),
              "previousAddressNamesMissing":sorted(named-credited),"previousUnmatchedPages":len(unmatched),
              "previousUnmatchedNowResolved":len(unmatched & projected),
              "previousUnmatchedStillUnresolved":sorted(unmatched-projected),
              "missingNamesByCompiledConstantOrigin":{",".join(k) or "absent":n for k,n in sorted(categories.items())}}
    (out / "comparison.json").write_text(json.dumps(totals,indent=2)+"\n")
    tables = ("unmatched-pages.tsv", "names-without-project-declaration.tsv", "comparison.json")
    digests = {name:hashlib.sha256((out / name).read_bytes()).hexdigest() for name in tables}
    (out / "comparison-sha256.json").write_text(json.dumps(digests,indent=2)+"\n")


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("constants",type=Path)
    cli.add_argument("out",type=Path)
    cli.add_argument("--baseline", required=True, help="Git revision containing the earlier map")
    args=cli.parse_args()
    compare(args.constants,args.out,args.baseline)

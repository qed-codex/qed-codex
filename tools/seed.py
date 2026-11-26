"""Import the pinned informalization and outside identifiers. Run from the ledger root."""

import argparse
import csv
import gzip
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml
from statement_links import LINK_FIELDS, statement_links

PROOF = Path("proofs/rh")
PIN = yaml.safe_load((PROOF / "proof.yml").read_text())["analysis_commit"]


def rows(file):
    with gzip.open(file, "rt") if file.suffix == ".gz" else file.open() as stream:
        yield from csv.DictReader(stream, delimiter="\t")


def verify_version(repo, files):
    subprocess.run(["git", "-C", str(repo), "diff", "--exit-code", "--quiet", PIN, "--", *files], check=True)


def atlas_titles(model=None):
    path = PROOF / "sources/atlas-titles.tsv"
    if model:
        data = model.read_bytes()
        if hashlib.sha256(data).hexdigest() != "8c85bd83b65afa31e330392acd81124397815d6d072a51dca19633936c4af544":
            raise ValueError("Unexpected pinned atlas model")
        with path.open("w", newline="") as f:
            writer = csv.writer(f, delimiter="\t", lineterminator="\n")
            writer.writerow(["atlas_id","label"])
            writer.writerows(sorted((n["id"],n["title"]) for n in json.loads(data)["nodes"]))
    return {r["atlas_id"]:r["label"] for r in rows(path)}


def seed(repo, model=None):
    tables = [
        "comparison-atlas.tsv",
        "spine.tsv",
        "phase-2/01-row0b.md",
    ]
    verify_version(repo, ["results/" + f for f in tables] + ["LICENSE"])
    results = repo / "results"
    links = statement_links()
    titles = atlas_titles(model)
    for r in rows(results / tables[0]):
        links.add(
            (
                "src/" + r["module"].replace(".", "/") + ".lean",
                "Bartosz Naskręcki",
                "https://nasqret.github.io/riemann-rev/atlas/#n-" + r["atlas_id"],
                "", titles[r["atlas_id"]],
            )
        )
    ledger = PROOF/"links.tsv"
    seeded = {(module,url) for module,_,url,_,_ in links}
    if ledger.exists():
        for r in rows(ledger):
            if (r["module"],r["url"]) not in seeded:
                links.add(tuple(r.get(k, "") for k in LINK_FIELDS))
    with ledger.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(LINK_FIELDS)
        w.writerows(sorted(links))
    spine = next(rows(results / tables[1]))
    assert spine["path"].endswith("/RowSrc.lean") and spine["rank"] == "1"
    note = Path("packages/riemann-hypothesis/informalizations") / spine["path"] / "dial481--codex-gpt-6-2-astra.md"
    note.parent.mkdir(parents=True, exist_ok=True)
    # The archived note cites the repository address used in the pinned source.
    upstream_readme = subprocess.check_output(["git", "-C", repo, "show", f"{PIN}:README.md"], text=True)
    archived_repository, = set(re.findall(r"https://github\.com/[\w.-]+/riemann-hypothesis-rosetta\b", upstream_readme))
    metadata = {
        "module": spine["path"],
        "declarations": [spine["anchor"]],
        "author": "dial481",
        "kind": "ai",
        "writer": "Codex (GPT-6.2 Astra)",
        "origin": "generated",
        "source_commit": yaml.safe_load((PROOF / "proof.yml").read_text())["source_commit"],
        "license": "CC-BY-4.0",
        "source": f"{archived_repository}/blob/{PIN}/results/{tables[2]}",
    }
    body = (results / tables[2]).read_text()
    # Keep the pinned source and links, adjusting the directory's editorial terminology.
    body = (body.replace("# Reading the first spine module:", "# Informalization of the top spine module:")
            .replace("is reading rank 1", "is spine rank 1")
            .replace("AI drafted this reading note", "AI drafted this autoinformalization")
            .replace("when reading the three arguments", "when interpreting the three arguments"))
    note.write_text(
        "---\n"
        + json.dumps(metadata, indent=2, ensure_ascii=False)
        + "\n---\n\n"
        + body
    )
    (PROOF / "seed-license.txt").write_bytes((repo / "LICENSE").read_bytes())


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("analysis", type=Path)
    cli.add_argument("--atlas-model",type=Path,help="Re-extract titles from the pinned atlas model")
    args=cli.parse_args()
    seed(args.analysis,args.atlas_model)

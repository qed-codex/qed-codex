"""Stage verified, commit-stamped mirror files on the local filesystem."""
from source_registry import directory_proof

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import tempfile
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import yaml

from mirror_projection import project
from parquet import TYPES, read_rows
from tables import row_digest


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def git_file(commit, path):
    return subprocess.check_output(["git", "show", f"{commit}:{path}"])


def write_manifest(directory, provenance):
    files = {
        p.relative_to(directory).as_posix(): {"bytes": p.stat().st_size, "sha256": sha(p)}
        for p in sorted(directory.rglob("*")) if p.is_file()
    }
    path = directory / "manifest.json"
    path.write_text(json.dumps({**provenance, "files": files}, indent=2) + "\n")
    return {
        "files": len(files) + 1,
        "totalBytes": sum(f["bytes"] for f in files.values()) + path.stat().st_size,
        "manifestSha256": sha(path),
    }


def credits(proof, commit, reference):
    analysis = f"{proof['analysis_url']}/blob/{proof['analysis_commit']}"
    return f"""The ledger revision is `{commit}`. The compiler manifest records the physical SQLite hash and ordered content hash of every table. [Ledger](https://github.com/qed-codex/qed-codex/tree/{commit}) · [Compiler manifest](https://github.com/qed-codex/qed-codex/blob/{commit}/{reference})

Levent Alpöge supplied the proof. Riemann Hypothesis Rosetta contributors supplied the module metrics and source trace. [Original proof]({proof['source_url']}/tree/{proof['source_commit']}) · [Mathlib]({proof['mathlib_url']}/tree/{proof['mathlib_commit']}) · [Rosetta analysis]({proof['analysis_url']}/tree/{proof['analysis_commit']})

James Shore supplied the CC0 declaration and kernel-mask data. Andrew Sutherland’s [kernel export](https://math.mit.edu/~drew/grh/) supplies the list of used declarations. [Release v0.2.1]({proof['kernel_url']}) · [Target order](https://github.com/james-shore/rh-proof-dependencies/blob/v0.2.1/data/per-theorem.tsv)

The links table credits Andrew O’Desky’s *Statements of the Lean RH project* and Bartosz Naskręcki’s atlas. [Author's Lean map](https://andrewodesky.com/rh/lean-map.tsv) · [Dated map capture](https://github.com/qed-codex/qed-codex/blob/{commit}/proofs/rh/sources/odesky/capture.json) · [Pinned atlas model](https://github.com/nasqret/riemann-rev/blob/d53b3804bd013df4cf9af3b4087728148c90c9bd/data/model.json)

The compiler code uses the MIT license. Each informalization row carries its writer, submitter’s GitHub handle, origin, kind, source and its own license. Each mirrored entry retains its own license and copyright attribution. Permission-only text is excluded from the Parquet files and SQLite release. The imported RowSrc informalization submitted by `dial481` carries its original MIT notice as well. [Code notice](LICENSE) · [Contributed informalization license](https://creativecommons.org/licenses/by/4.0/) · [Seed notice](seed-license.txt) · [Original informalization]({analysis}/results/phase-2/01-row0b.md)
"""


def dataset_card(names, attribution):
    configs = []
    for name in names:
        config = {"config_name": name, "data_files": [{"split": "train", "path": f"data/{name}.parquet"}]}
        if name == "modules":
            config["default"] = True
        configs.append(config)
    header = yaml.safe_dump({"license": "other", "configs": configs}, sort_keys=False)
    template = Path(__file__).with_name("templates") / "hf-dataset-card.md"
    return template.read_text(encoding="utf-8").format(header=header, attribution=attribution)


def stage(database, reference_path, parquet_dir, out, commit):
    if not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError("Pass a full 40-character ledger commit")
    # Bind both formats to a reference from the named revision, even if another
    # revision is checked out or someone has edited the working copy since compilation.
    root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
    rel = reference_path.resolve().relative_to(root).as_posix()
    pinned = git_file(commit, rel)
    if reference_path.read_bytes() != pinned:
        raise ValueError("Local compiler manifest differs from its recorded commit")
    verify = json.loads(pinned)
    tables = verify["tableContent"]
    export = json.loads((parquet_dir / "manifest.json").read_text())
    if export["sourceDatabaseSha256"] != verify["databaseSha256"] or sha(database) != verify["databaseSha256"] or set(export["tables"]) != set(tables):
        raise ValueError("Parquet inventory does not match the committed SQLite build")
    proof = directory_proof(lambda name: git_file(commit, name))
    provenance = {
        "ledgerCommit": commit,
        "proofCommit": proof["source_commit"],
        "packageCommits": {name: data["commit"] for name,data in proof["packages"].items()},
        "analysisCommit": proof["analysis_commit"],
        "compilerManifest": rel,
        "compilerManifestSha256": hashlib.sha256(pinned).hexdigest(),
        "databaseSha256": verify["databaseSha256"],
    }
    if out.exists():
        raise FileExistsError(f"Choose a new output directory: {out}")
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=out.parent) as tmp:
        staging = Path(tmp) / "mirrors"
        dataset, release = staging / "huggingface", staging / "release"
        data = dataset / "data"
        data.mkdir(parents=True)
        release.mkdir()
        asset = release / f"qed-codex-rh-{commit}.sqlite3"
        filtered, tables, excluded = project(database, Path(tmp)/"redistributable.sqlite3", tables)
        shutil.copyfile(filtered, asset)
        provenance["sourceDatabaseSha256"] = verify["databaseSha256"]
        provenance["databaseSha256"] = sha(asset)
        provenance["permissionRowsExcluded"] = excluded
        if provenance["databaseSha256"] != export["databaseSha256"] or excluded != export["permissionRowsExcluded"]:
            raise ValueError("SQLite bytes differ from the committed compiler manifest")
        with sqlite3.connect(asset.resolve().as_uri() + "?mode=ro", uri=True) as db:
            for name, expected in sorted(tables.items()):
                encoded = export["tables"][name]
                if not re.fullmatch(r"[a-zA-Z0-9_]+", name) or encoded["file"] != name + ".parquet":
                    raise ValueError(f"Unexpected table filename: {name}")
                target = data / encoded["file"]
                shutil.copyfile(parquet_dir / target.name, target)
                if target.stat().st_size != encoded["bytes"] or sha(target) != encoded["sha256"]:
                    raise ValueError(f"Parquet file hash or size differs: {name}")
                if name == "names":
                    columns = [("term", "TEXT"), ("doc", "INTEGER")]
                else:
                    columns = db.execute("SELECT name,type FROM pragma_table_info(?) ORDER BY cid", (name,))
                schema = pa.schema([(column, TYPES[kind]) for column, kind in columns])
                if pq.read_schema(target) != schema:
                    raise ValueError(f"Parquet schema differs from SQLite: {name}")
                if encoded["content"] != expected or row_digest(schema.names, read_rows(target)) != expected:
                    raise ValueError(f"Parquet rows differ from committed SQLite content: {name}")
            # Compiler and seed notices are MIT. The declaration and kernel data are CC0.
            licenses = {"MIT", "CC0-1.0"}
            licenses.update(r[0] for r in db.execute("SELECT DISTINCT license FROM informalizations"))
        source_files = subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", commit, "--", "packages/"], text=True
        ).splitlines()
        legal_paths = [f"LICENSES/{identifier}.txt" for identifier in sorted(licenses)]
        legal_paths += [name for name in source_files if len(Path(name).parts) == 3
                        and Path(name).name in {"LICENSE", "NOTICE", "ATTRIBUTION.md"}]
        attribution = credits(proof, commit, rel)
        (dataset / "README.md").write_text(dataset_card(sorted(tables), attribution))
        (dataset / ".gitattributes").write_text("*.parquet filter=lfs diff=lfs merge=lfs -text\n")
        (release / "CREDITS.md").write_text("# QED Codex proof directory\n\n" + attribution)
        for directory in [dataset, release]:
            for name in legal_paths:
                target = directory / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(git_file(commit, name))
            (directory / "LICENSE").write_bytes(git_file(commit, "LICENSE"))
            (directory / "seed-license.txt").write_bytes(git_file(commit, "proofs/rh/seed-license.txt"))
        report = {
            **provenance,
            "parquetConfigurations": len(tables),
            "verifiedRows": {name: table["rows"] for name, table in sorted(tables.items())},
            "sqliteAsset": asset.name,
            "sqliteBytes": asset.stat().st_size,
            "huggingface": write_manifest(dataset, provenance),
            "release": write_manifest(release, provenance),
        }
        staging.rename(out)
    return report


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("database", type=Path)
    cli.add_argument("reference", type=Path, help="Committed compiler manifest at the supplied ledger revision")
    cli.add_argument("parquet", type=Path)
    cli.add_argument("out", type=Path)
    cli.add_argument("--commit", required=True)
    args = cli.parse_args()
    print(json.dumps(stage(args.database, args.reference, args.parquet, args.out, args.commit), indent=2))

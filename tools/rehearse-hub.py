"""Plan the dataset upload with the Hub SDK and validate file bytes without contacting the Hub."""
import argparse
import hashlib
import json
from pathlib import Path

from huggingface_hub import CommitOperationAdd, DatasetCard
from huggingface_hub.utils import filter_repo_objects


def plan(directory):
    manifest = json.loads((directory / "manifest.json").read_bytes())
    configs = DatasetCard.load(directory / "README.md").data.to_dict()["configs"]
    selected = sorted(filter_repo_objects(
        p.relative_to(directory).as_posix() for p in directory.rglob("*") if p.is_file()
    ))
    expected = manifest["files"]
    if set(selected) != set(expected) | {"manifest.json"}:
        raise ValueError("Upload selection differs from the staged inventory")
    tables = {f"data/{c['config_name']}.parquet" for c in configs}
    if tables != {f for f in selected if f.endswith(".parquet")}:
        raise ValueError("Dataset card and upload disagree")
    size = 0
    for relative in selected:
        op = CommitOperationAdd(relative, directory / relative)
        actual = {"bytes":op.upload_info.size,"sha256":op.upload_info.sha256.hex()}
        if relative in expected and actual != expected[relative]:
            raise ValueError(f"Upload bytes differ for {relative}")
        size += actual["bytes"]
    return {"ledgerCommit":manifest["ledgerCommit"],"uploadFiles":len(selected),"uploadBytes":size,
            "parquetTables":len(tables),"manifestSha256":hashlib.sha256((directory / "manifest.json").read_bytes()).hexdigest()}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("directory",type=Path)
    print(json.dumps(plan(cli.parse_args().directory),indent=2))

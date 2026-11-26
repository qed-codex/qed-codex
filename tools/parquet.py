"""Export every logical table and verify its ordered Parquet rows against the SQLite manifest."""

import argparse
import hashlib
import json
import sqlite3
import tempfile
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
from contextlib import ExitStack
from mirror_projection import project
from tables import ordered_tables, row_digest

BATCH = 65536
TYPES = {"INTEGER": pa.int64(), "TEXT": pa.string()}


def read_rows(path):
    for batch in pq.ParquetFile(path).iter_batches(batch_size=BATCH):
        yield from zip(*(column.to_pylist() for column in batch.columns), strict=True)


def export(database, reference, out):
    if out.exists():
        raise FileExistsError(f"Choose a new export directory: {out}")
    out.parent.mkdir(parents=True, exist_ok=True)
    expected = reference["tableContent"]
    with database.open("rb") as src:
        if hashlib.file_digest(src, "sha256").hexdigest() != reference["databaseSha256"]:
            raise ValueError("The reference manifest belongs to another database")
    with tempfile.TemporaryDirectory(dir=out.parent) as tmp, ExitStack() as stack:
        filtered, expected, excluded = project(database, Path(tmp)/"redistributable.sqlite3", expected)
        db = stack.enter_context(sqlite3.connect(filtered.resolve().as_uri()+"?mode=ro", uri=True))
        with filtered.open("rb") as src:
            mirror_sha = hashlib.file_digest(src,"sha256").hexdigest()
        stage = Path(tmp) / "parquet"
        stage.mkdir()
        files = {}
        for name, types, cursor in ordered_tables(db):
            fields = [c[0] for c in cursor.description]
            schema = pa.schema([(col, TYPES[typ]) for col, typ in zip(fields, types, strict=True)])
            path = stage / (name + ".parquet")
            with pq.ParquetWriter(path, schema, compression="zstd", version="2.6") as writer:
                while rows := cursor.fetchmany(BATCH):
                    arrays = [
                        pa.array(values, type=field.type)
                        for values, field in zip(zip(*rows), schema, strict=True)
                    ]
                    writer.write_table(pa.Table.from_arrays(arrays, schema=schema), row_group_size=BATCH)
            content = row_digest(fields, read_rows(path))
            if content != expected[name] or pq.read_schema(path) != schema:
                raise ValueError(f"Parquet verification failed for {name}")
            with path.open("rb") as src:
                sha = hashlib.file_digest(src, "sha256").hexdigest()
            files[name] = {"file": path.name, "bytes": path.stat().st_size, "sha256": sha, "content": content}
        if set(files) != set(expected):
            raise ValueError("Parquet table set differs from SQLite manifest")
        manifest = {"databaseSha256": mirror_sha, "sourceDatabaseSha256": reference["databaseSha256"],
                    "permissionRowsExcluded": excluded, "pyarrow": pa.__version__, "tables": files}
        (stage / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        stage.rename(out)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("database", type=Path)
    cli.add_argument("manifest", type=Path)
    cli.add_argument("out", type=Path)
    args = cli.parse_args()
    export(args.database, json.loads(args.manifest.read_text()), args.out)

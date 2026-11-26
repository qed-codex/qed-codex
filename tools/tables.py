"""Canonical row order and serialization for SQLite and Parquet verification."""

import hashlib
import json


def ordered_tables(db):
    """Yield each logical table as an ordered cursor, with declared column types."""
    tables = sorted(
        (name, kind)
        for schema, name, kind, *_ in db.execute("PRAGMA table_list")
        if schema == "main" and not name.startswith("sqlite_") and kind != "shadow"
    )
    db.execute("CREATE VIRTUAL TABLE temp.name_terms USING fts5vocab(main, 'names', 'instance')")
    for name, kind in tables:
        if kind == "virtual":
            if name != "names":
                raise ValueError(f"No logical representation for virtual table {name}")
            types = ["TEXT", "INTEGER"]
            cursor = db.execute("SELECT term, doc FROM temp.name_terms ORDER BY term COLLATE BINARY, doc")
        else:
            types = [r[0] for r in db.execute("SELECT type FROM pragma_table_info(?) ORDER BY cid", (name,))]
            columns = db.execute("SELECT name,pk FROM pragma_table_info(?) WHERE pk>0 ORDER BY pk", (name,))
            keys = ", ".join('"' + key.replace('"', '""') + '"' for key, _ in columns)
            if not keys:
                raise ValueError(f"No stable primary key for {name}")
            quoted_name = name.replace('"', '""')
            cursor = db.execute(f'SELECT * FROM "{quoted_name}" ORDER BY {keys}')
        yield name, types, cursor


def row_digest(fields, rows):
    encode = json.JSONEncoder(ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode
    digest = hashlib.sha256((encode(fields) + "\n").encode("utf-8"))
    total = 0
    for total, row in enumerate(rows, 1):
        digest.update((encode(row) + "\n").encode("utf-8"))
    return {"columns": fields, "rows": total, "sha256": digest.hexdigest()}

"""Build the redistributable view without retaining permission-only text in unused SQLite pages."""
import shutil
import sqlite3

from tables import row_digest


def populate_board(db):
    db.execute("""INSERT INTO most_wanted(rank,module)
        SELECT row_number() OVER (ORDER BY m.spine_rank ASC NULLS LAST, m.cut DESC, m.path COLLATE BINARY),m.id
        FROM modules m WHERE m.project=1 AND ((m.mask & 1) != 0 OR m.mask IS NULL) AND NOT EXISTS
        (SELECT 1 FROM informalizations r WHERE r.module=m.id AND r.entry_type='informalization')""")
    db.execute("""INSERT INTO wanted_source
        SELECT m.package,row_number() OVER (PARTITION BY m.package ORDER BY w.rank),m.id
        FROM most_wanted w JOIN modules m ON m.id=w.module""")

def project(source, destination, tables):
    """Return SQLite path, independently checkable table digests and exclusion count."""
    with sqlite3.connect(source.resolve().as_uri() + "?mode=ro", uri=True) as db:
        excluded = db.execute("SELECT count(*) FROM informalizations WHERE license='with-permission'").fetchone()[0]
    if not excluded:
        return source, tables, 0
    shutil.copyfile(source, destination)
    expected = tables.copy()
    with sqlite3.connect(destination) as db:
        db.execute("PRAGMA secure_delete=ON")
        db.execute("DELETE FROM informalizations WHERE license='with-permission'")
        db.execute("DELETE FROM wanted_source")
        db.execute("DELETE FROM most_wanted")
        populate_board(db)
        for metric, table, predicate in (
            ("informalizations", "informalizations", "entry_type='informalization'"),
            ("source_documentation", "informalizations", "entry_type='source-documentation'"),
            ("most_wanted", "most_wanted", "1"),
        ):
            db.execute(f"UPDATE summary SET value=(SELECT count(*) FROM {table} WHERE {predicate}) WHERE metric=?", (metric,))
        db.commit()
        db.execute("VACUUM")
        for table, key in (("informalizations","id"), ("most_wanted","rank"), ("summary","metric"),
                           ("wanted_source","package,rank")):
            rows = db.execute(f"SELECT * FROM {table} ORDER BY {key}")
            expected[table] = row_digest([r[0] for r in rows.description], rows)
    return destination, expected, excluded

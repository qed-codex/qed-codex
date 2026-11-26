"""Check the complete pinned import on the local site, board and both mirrors."""

import argparse
from pathlib import Path
import sqlite3
import pyarrow.parquet as pq
from verify_directory import Main


def check(database, site, mirrors):
    def record(slug):
        return Main(site / "proofs" / slug / "index.html")

    with sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True) as db:
        actual = dict(
            db.execute("SELECT license,count(*) FROM informalizations GROUP BY license")
        )
        assert actual == {"Apache-2.0": 312, "CC-BY-4.0": 8, "with-permission": 2044}
        modules = list(
            db.execute("""SELECT m.path, i.writer, m.mask, w.module FROM modules m
            LEFT JOIN informalizations i ON i.module=m.id LEFT JOIN most_wanted w ON w.module=m.id
            WHERE m.package='zeta23' ORDER BY m.path""")
        )
        assert len(modules) == 326
        assert [r[0] for r in modules] == Path(
            "packages/zeta23/modules.txt"
        ).read_text().splitlines()
        assert all(
            mask is None and wanted is not None
            for path, writer, mask, wanted in modules
        )
        assert sum(writer is None for _, writer, _, _ in modules) == 14

    for fmt in ["release", "huggingface"]:
        dest = mirrors / fmt
        for path in [
            "LICENSES/Apache-2.0.txt",
            "LICENSES/MIT.txt",
            "LICENSES/CC-BY-4.0.txt",
            "packages/zeta23/NOTICE",
        ]:
            assert (dest / path).read_bytes() == Path(path).read_bytes(), path
    (asset,) = (mirrors / "release").glob("*.sqlite3")
    with sqlite3.connect(asset.resolve().as_uri() + "?mode=ro", uri=True) as db:
        projected = list(
            db.execute("SELECT license,copyright,entry_type FROM informalizations ORDER BY id")
        )
    exported = pq.read_table(
        mirrors / "huggingface/data/informalizations.parquet",
        columns=["license", "copyright", "entry_type"],
    ).to_pylist()
    assert projected == [(r["license"], r["copyright"], r["entry_type"]) for r in exported]
    assert (
        len(projected) == 320
        and sum(lic == "Apache-2.0" and bool(c) and kind == "source-documentation" for lic, c, kind in projected) == 312
    )
    assert all(lic != "with-permission" for lic, _, _ in projected)
    for slug, addr in [
        ("riemann-hypothesis", "https://math.mit.edu/~drew/grh/"),
        (
            "zeta23",
            "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/AUDIT.md",
        ),
    ]:
        assert addr in record(slug).links
        assert "/proofs/" + slug + "/" in Main(site / "index.html").links
    print(
        f"326 module identities, 326 wanted, 312 Apache notices, {len(projected)} redistributable entries in each mirror, 2 verification records"
    )


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    for key in ["database", "site", "mirrors"]:
        cli.add_argument(key, type=Path)
    args = cli.parse_args()
    check(args.database, args.site, args.mirrors)

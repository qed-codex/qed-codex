"""Build a checksummed SQLite shared library for Python's sqlite3 module on Linux."""

import argparse
import hashlib
import io
import os
import shlex
import subprocess
import tempfile
import zipfile
from pathlib import Path
from urllib.request import urlopen

from build import BUILD_SQLITE

RELEASES = {
    BUILD_SQLITE: ("2024", "3460100", "77823cb110929c2bcb0f5d48e4833b5c59a8a6e40cdea3936b99e199dbbe5784"),
    "3.53.1": ("2026", "3530100", "36ad6e7f38540a3b21a2ac36340833f0a9e426bc1c752751c3ba669466827eae"),
}


def install(version):
    year, number, sha = RELEASES[version]
    archive = f"sqlite-amalgamation-{number}"
    with urlopen(f"https://sqlite.org/{year}/{archive}.zip", timeout=60) as response:
        data = response.read()
    if hashlib.sha256(data).hexdigest() != sha:
        raise ValueError(f"SQLite {version} archive checksum mismatch")
    dest = Path("inputs/sqlite") / version
    dest.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=dest) as tmp:
        source = Path(tmp) / "sqlite3.c"
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            source.write_bytes(z.read(f"{archive}/sqlite3.c"))
        library = Path(tmp) / "libsqlite3.so.0"
        flags = [
            "-DSQLITE_ENABLE_" + option
            for option in ("FTS5", "DBSTAT_VTAB", "COLUMN_METADATA", "MATH_FUNCTIONS", "RTREE")
        ]
        subprocess.run(
            [
                *shlex.split(os.environ.get("CC", "cc")),
                "-O2",
                "-fPIC",
                "-shared",
                "-Wl,-soname,libsqlite3.so.0",
                *flags,
                str(source),
                "-lm",
                "-o",
                str(library),
            ],
            check=True,
        )
        library.replace(dest / library.name)
    print(dest.resolve())


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("version", choices=RELEASES, default=BUILD_SQLITE, nargs="?")
    install(cli.parse_args().version)

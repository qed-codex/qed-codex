"""Check every advertised Mathlib documentation URL with paced HTTP HEAD requests."""
from source_registry import directory_proof
import csv
import json
import sqlite3
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

CONFIG = directory_proof()["packages"]["mathlib"]["moduleDocs"]


def check(path):
    url = CONFIG["base"] + quote(path.removesuffix(".lean") + ".html")
    req = Request(url, method="HEAD", headers={"User-Agent": "QED-Codex link verification (contact@qedcodex.org)"})
    try:
        with urlopen(req, timeout=30) as res:
            status = res.status
    except HTTPError as err:
        status = err.code
        err.close()
    except (URLError, OSError) as err:
        status = str(err)
    return path, url, status, datetime.now(timezone.utc).isoformat(timespec="seconds")


def paced(paths):
    for path in paths:
        yield path
        time.sleep(0.2)


if __name__ == "__main__":
    with sqlite3.connect(Path(sys.argv[1]).resolve().as_uri() + "?mode=ro", uri=True) as db:
        paths = [p for p, in db.execute("SELECT path FROM modules WHERE package='mathlib' ORDER BY path")
                 if p.split("/", 1)[0] in CONFIG["roots"]]
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["module", "url", "http_status", "checked_utc"])
    with ThreadPoolExecutor(max_workers=3) as pool:
        for row in pool.map(check, paced(paths), buffersize=3):
            out.writerow(row)
            sys.stdout.flush()

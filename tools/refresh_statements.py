"""Refresh the ledger from the official statement map or replay a recorded capture."""
import argparse
import fcntl
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

from check_links import capture as check_urls, verify_receipt
from statement_index import tsv
from statement_links import (CARD_FIELDS, CONSTANT_FIELDS, LINK_FIELDS, MAP_URL, SOURCE, current_rows,
                             map_rows, read_tsv, refresh_ledger, summary)

PROOF = SOURCE.parents[1]


def put(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def download(snapshot):
    snapshot.mkdir(parents=True)
    with urlopen(Request(MAP_URL, headers={"User-Agent":"QED Codex statement map refresh",
                                           "Cache-Control":"no-cache"}), timeout=45) as response:
        raw = response.read()
    (snapshot / "lean-map.tsv").write_bytes(raw)
    put(snapshot / "capture.json", {"url":MAP_URL, "utc":datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                    "bytes":len(raw), "sha256":hashlib.sha256(raw).hexdigest()})


def refresh(shore, snapshot, live):
    if live:
        download(snapshot)
    capture = json.loads((snapshot / "capture.json").read_text())
    path = snapshot / "lean-map.tsv"
    raw = path.read_bytes()
    if (capture["url"], capture["bytes"], capture["sha256"]) != (MAP_URL,len(raw),hashlib.sha256(raw).hexdigest()):
        raise ValueError("Statement map differs from its capture receipt")
    cards = map_rows(path, shore / "decls.csv.gz", shore / "constants.csv.gz")
    links = refresh_ledger(read_tsv(PROOF / "links.tsv"), current_rows(), cards)
    totals = summary(cards, links)
    urls = {r[2] for r in links} | {r["url"] for r in cards}
    receipt_path = snapshot / "outside-link-check.json"
    if live:
        put(receipt_path, check_urls(urls))
    receipt = verify_receipt(json.loads(receipt_path.read_text()), urls)
    with tempfile.TemporaryDirectory(dir=PROOF) as directory:
        stage = Path(directory)
        tsv(stage / "cards.tsv", CARD_FIELDS, ([c[k] for k in CARD_FIELDS] for c in cards))
        evidence = sorted({tuple(c[k] for k in CONSTANT_FIELDS) for c in cards if c.get("constant_module")})
        tsv(stage / "constant-matches.tsv", CONSTANT_FIELDS, evidence)
        tsv(stage / "links.tsv", LINK_FIELDS, links)
        (stage / "lean-map.tsv").write_bytes(raw)
        put(stage / "capture.json", capture)
        put(stage / "snapshots.json", {"source":capture,
            "cardsSha256":hashlib.sha256((stage / "cards.tsv").read_bytes()).hexdigest(),
            "constantMatchesSha256":hashlib.sha256((stage / "constant-matches.tsv").read_bytes()).hexdigest()})
        put(stage / "counts.json", totals)
        put(stage / "outside-link-check.json", receipt)
        for name in ("lean-map.tsv", "capture.json", "cards.tsv", "constant-matches.tsv", "counts.json", "snapshots.json"):
            os.replace(stage / name, SOURCE / name)
        for name in ("links.tsv", "outside-link-check.json"):
            os.replace(stage / name, PROOF / name)
    print(json.dumps(totals, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--shore", type=Path, default=Path("inputs/shore"))
    cli.add_argument("--replay", type=Path, help="Use captured lean-map.tsv, capture.json and outside-link-check.json")
    args = cli.parse_args()
    cache = Path("inputs/statement-snapshots")
    cache.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    with (cache / ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        refresh(args.shore, args.replay or cache / stamp, args.replay is None)

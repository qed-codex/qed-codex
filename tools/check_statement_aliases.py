"""Verify the historical statement URLs against the current card address ledger."""

import argparse
import csv
import gzip
import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


class Refresh(HTMLParser):
    def __init__(self):
        super().__init__()
        self.target = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and a.get("http-equiv", "").lower() == "refresh":
            match = re.fullmatch(
                r"\s*0\s*;\s*url\s*=\s*(.*?)\s*", a.get("content", ""), re.I
            )
            if match:
                self.target = match[1].strip("'\x22")


def probe(pair):
    old, expected = pair
    method = "GET" if expected and expected != old else "HEAD"
    try:
        with urlopen(
            Request(
                old, method=method, headers={"User-Agent": "QED-Codex URL verification"}
            ),
            timeout=20,
        ) as r:
            url = r.geturl()
            if url == old and expected != old and method == "GET":
                page = Refresh()
                page.feed(r.read(4096).decode())
                if page.target:
                    url = urljoin(old, page.target)
            return (
                old,
                "unchanged"
                if old == expected == url
                else "forwards"
                if url == expected
                else "unexpected",
                url,
            )
    except HTTPError as exc:
        return old, str(exc.code), ""
    except OSError as exc:
        return old, type(exc).__name__, ""


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("analysis", type=Path)
    a = cli.parse_args()
    with open("proofs/rh/sources/odesky/cards.tsv") as f:
        cards = {r["card_id"]: r["url"] for r in csv.DictReader(f, delimiter="\t")}
    with gzip.open(a.analysis / "results/phase-2/odesky-index.tsv.gz", "rt") as f:
        pairs = [
            (r["entry_url"], cards.get(Path(r["entry_url"]).stem))
            for r in csv.DictReader(f, delimiter="\t")
        ]
    start = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with ThreadPoolExecutor(max_workers=3) as pool:
        observed = list(pool.map(probe, pairs))
    unexpected = [
        (old, want, state, actual)
        for (old, want), (_, state, actual) in zip(pairs, observed, strict=True)
        if state
        != ("404" if want is None else "unchanged" if old == want else "forwards")
    ]
    print(
        json.dumps(
            {
                "startedUTC": start,
                "finishedUTC": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "counts": dict(sorted(Counter(r[1] for r in observed).items())),
                "unexpected": unexpected,
            },
            indent=2,
        )
    )

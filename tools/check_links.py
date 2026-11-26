"""Check each distinct outside address and bind the results to the verified ledger URL set."""

import argparse
import csv
import hashlib
import http.client
import json
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urldefrag

from statement_links import current_cards


def directory_urls(module_urls):
    return set(module_urls) | {r["url"] for r in current_cards().values()}


ATLAS = "https://nasqret.github.io/riemann-rev/atlas/"
AGENT = (
    "QED-Codex/1.0 (outside link verification; https://github.com/qed-codex/qed-codex)"
)


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.model = []
        self.in_model = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        if tag == "script":
            self.in_model = (
                attrs.get("id") == "atlas-data"
                and attrs.get("type") == "application/json"
            )

    def handle_data(self, text):
        if self.in_model:
            self.model.append(text)

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_model = False


def request(url, method):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(req, timeout=15) as res:
        return res.status, res.read() if method == "GET" else b""


def inspect(item):
    base, urls = item
    method = "GET" if any(fragment for _, fragment in urls) else "HEAD"
    for attempt in range(3):
        try:
            status, data = request(base, method)
            break
        except urllib.error.HTTPError as exc:
            status = exc.code
            if method == "HEAD" and status in (405, 501):
                method = "GET"
            elif status not in (429, 500, 502, 503, 504):
                break
            if status == 429:
                wait = exc.headers.get("Retry-After", "")
                if wait.isdigit() and int(wait) > 30:
                    break
                time.sleep(int(wait) if wait.isdigit() else 3)
        except (OSError, EOFError, http.client.HTTPException) as exc:
            status = type(exc).__name__
        if attempt < 2:
            time.sleep(attempt + 1)
    if status in (404, 410):
        return [(u, "dead", str(status)) for u, _ in urls]
    if not isinstance(status, int) or not 200 <= status < 300:
        return [(u, "unverified", str(status)) for u, _ in urls]
    anchors = Anchors()
    if method == "GET" and any(fragment for _, fragment in urls):
        anchors.feed(data.decode("utf-8", errors="replace"))
        anchors.close()
    atlas_ids = None
    if base == ATLAS and anchors.model:
        try:
            atlas_ids = {n["id"] for n in json.loads("".join(anchors.model))["nodes"]}
        except (ValueError, KeyError, TypeError):
            pass
    result = []
    for url, fragment in urls:
        fragment = unquote(fragment)
        if not fragment or fragment in anchors.ids:
            result.append((url, "ok", ""))
        elif base == ATLAS and fragment.startswith("n-") and atlas_ids is not None:
            resolved = fragment[2:] in atlas_ids
            result.append(
                (
                    url,
                    "ok" if resolved else "dead",
                    "" if resolved else "missing atlas node",
                )
            )
        else:
            result.append((url, "unverified", "fragment could not be resolved"))
    return result


def digest(urls):
    return hashlib.sha256(
        "".join(u + "\n" for u in sorted(set(urls))).encode()
    ).hexdigest()


def capture(urls, budget_seconds=600):
    groups = defaultdict(list)
    for url in sorted(set(urls)):
        base, fragment = urldefrag(url)
        groups[base].append((url, fragment))
    start = datetime.now(timezone.utc).isoformat(timespec="seconds")
    found = {"dead": [], "unverified": []}
    # Leave room in the build for SQLite verification if an entire host times out.
    deadline = time.monotonic() + budget_seconds

    def check_group(item):
        if time.monotonic() >= deadline:
            return [
                (url, "unverified", "link-check time budget reached")
                for url, _ in item[1]
            ]
        return inspect(item)

    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(check_group, groups.items()):
            for url, state, reason in result:
                if state != "ok":
                    found[state].append({"url": url, "reason": reason})
    return {
        "startedUTC": start,
        "finishedUTC": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "urlSetSha256": digest(urls),
        "destinations": sorted(set(urls)),
        "checkedURLs": len(set(urls)),
        **{
            key: sorted(values, key=lambda r: r["url"]) for key, values in found.items()
        },
    }


def verify_receipt(snapshot, urls, *, review=False):
    urls = set(urls)
    if review and snapshot["urlSetSha256"] != digest(urls):
        previous = set(snapshot["destinations"])
        verify_receipt(snapshot, previous)
        new = sorted(urls - previous)
        result = {**snapshot, "directoryURLs":len(urls), "checkedURLs":len(urls & previous),
                  "snapshotURLSetSha256":snapshot["urlSetSha256"], "urlSetSha256":digest(urls),
                  "dead":[r for r in snapshot["dead"] if r["url"] in urls],
                  "unverified":[r for r in snapshot["unverified"] if r["url"] in urls]}
        for url in new:
            reason = "pending trusted live build"
            result["unverified"].append({"url":url, "reason":reason})
            print(f"unverified outside link: {url} ({reason})",file=sys.stderr)
        return result
    if snapshot["urlSetSha256"] != digest(urls) or snapshot["checkedURLs"] != len(urls):
        raise ValueError(
            "Outside link receipt differs from the compiled URL set. Refresh the link check."
        )
    if "destinations" in snapshot and set(snapshot["destinations"]) != urls:
        raise ValueError("Outside link receipt destination inventory differs")
    seen = set()
    for state in ("dead", "unverified"):
        for r in snapshot[state]:
            url, reason = r["url"], r["reason"]
            if (
                url not in urls
                or url in seen
                or not isinstance(reason, str)
                or not reason
            ):
                raise ValueError("Invalid outside link result")
            seen.add(url)
            print(f"{state} outside link: {url} ({reason})", file=sys.stderr)
    print(
        f"Outside links: {len(urls)} distinct, {len(snapshot['dead'])} dead, "
        f"{len(snapshot['unverified'])} unverified.",
        file=sys.stderr,
    )
    return snapshot


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    with args.ledger.open(newline="") as f:
        urls = {r["url"] for r in csv.DictReader(f, delimiter="\t")}
    urls = directory_urls(urls)
    receipt = verify_receipt(capture(urls), urls)
    args.out.write_text(json.dumps(receipt, indent=2) + "\n")

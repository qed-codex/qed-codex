"""Capture the two card indexes and their statement chunks in site order."""
import argparse
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

from statement_index import BASE

AGENT = "QED Codex statement capture (contact@qedcodex.org)"


def capture(root):
    root.mkdir(parents=True, exist_ok=True)
    records = {}
    robots = RobotFileParser()

    def get(name, url):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        meta = path.with_suffix(path.suffix + ".json")
        if not (path.exists() and meta.exists()):
            if name != "robots.txt" and not robots.can_fetch(AGENT, url):
                raise ValueError(f"Capture disallowed for {url}")
            time.sleep(max(1.25, robots.crawl_delay(AGENT) or 0))
            status = 200
            try:
                with urlopen(Request(url, headers={"User-Agent": AGENT}), timeout=45) as response:
                    data = response.read()
            except HTTPError as exc:
                if name != "robots.txt" or exc.code != 404:
                    raise
                data, status = b"", 404
            receipt = {"url": url, "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                       "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "status": status}
            path.write_bytes(data)
            meta.write_text(json.dumps(receipt) + "\n")
        record = json.loads(meta.read_text())
        content = path.read_bytes()
        if (record["url"], record["bytes"], record["sha256"]) != (url, len(content), hashlib.sha256(content).hexdigest()):
            raise ValueError(f"Capture mismatch for {name}")
        records[name] = record
        return content.decode()

    robots.parse(get("robots.txt", urljoin(BASE, "/robots.txt")).splitlines())
    chunks = {}
    for index, url in (("index.html", BASE), ("definitions.html", urljoin(BASE, "definitions.html"))):
        for chunk in re.findall(r'data-chunk="(cards/[A-Za-z0-9_-]+\.html)"', get(index, url)):
            chunks[chunk] = None
    if not chunks:
        raise ValueError("No statement chunks found in the indexes")
    for chunk in chunks:
        get(chunk, urljoin(BASE, chunk))
    (root / "capture.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(chunks)} chunk files verified")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    capture(parser.parse_args().output)

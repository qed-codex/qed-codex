"""Select and snapshot live single-statement pages for the visual comparison."""
import argparse
import hashlib
import json
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

from bs4 import BeautifulSoup
from capture_statement_cards import AGENT
from import_permission_statements import cards
from statement_index import BASE
from statement_links import AUTHOR, read_tsv

SEED = "qed-permission-cards-20261124"
REPORT = Path("reports/permission-statements")


def comparable(statement, base):
    # Live permalinks may use a different relative spelling of the same link.
    for tag in statement.find_all(True):
        if tag.name == "a":
            tag.attrs = {"href":urljoin(base, tag["href"])}
        elif tag.name != "ol":
            tag.attrs = {}
    return " ".join(statement.decode_contents().split())


def sample(root):
    paths = defaultdict(set)
    for row in read_tsv(Path("proofs/rh/links.tsv")):
        if row["author"] == AUTHOR:
            paths[row["url"]].add(row["module"])
    population = [r for r in read_tsv(REPORT/"pages.tsv") if int(r["modules"])]
    chosen = sorted(population, key=lambda r: hashlib.sha256((SEED+"\0"+r["card_id"]).encode()).digest())[:30]
    ids = {r["card_id"] for r in chosen}
    originals = {k:a for k,a in cards(root) if k in ids}
    robot = RobotFileParser()
    robot.parse((root/"robots.txt").read_text().splitlines())
    cache = root/"single-pages"
    cache.mkdir(exist_ok=True)
    result = []
    for record in chosen:
        key,url = record["card_id"],record["url"]
        page = cache/(key+".html")
        metadata = page.with_suffix(".json")
        if not page.exists():
            if not robot.can_fetch(AGENT,url):
                raise ValueError(f"Disallowed: {url}")
            time.sleep(max(1.25,robot.crawl_delay(AGENT) or 0))
            with urlopen(Request(url,headers={"User-Agent":AGENT}),timeout=45) as response:
                data = response.read()
                final_url = response.geturl()
            page.write_bytes(data)
            metadata.write_text(json.dumps({"utc":datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "url":final_url,"sha256":hashlib.sha256(data).hexdigest()})+"\n")
        data = page.read_bytes()
        receipt = json.loads(metadata.read_text())
        assert receipt["sha256"] == hashlib.sha256(data).hexdigest()
        doc = BeautifulSoup(data.decode(),"html.parser")
        statement = doc.select_one(".stmt")
        if statement is None:
            raise ValueError(f"No statement container in {url}")
        source = originals[key]
        base = doc.find("base",href=True)
        live_base = urljoin(receipt["url"],base["href"]) if base else receipt["url"]
        match = comparable(statement,live_base) == comparable(source.select_one(".stmt"),BASE)
        path = min(paths[url])
        pkg = "riemann-hypothesis" if path.startswith("src/") else "mathlib"
        result.append({"id":key,"title":source.header.h3.get_text(" ",strip=True),"source":url,
                       "module":path,"package":pkg,"identicalStatementHTML":match,**receipt})
    (REPORT/"live-sample.json").write_text(json.dumps({"seed":SEED,"sample":result},ensure_ascii=False,indent=2)+"\n")
    print("Identical normalized statement markup:",sum(r["identicalStatementHTML"] for r in result),"of",len(result))


if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("capture",type=Path)
    sample(p.parse_args().capture)

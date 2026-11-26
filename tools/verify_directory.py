"""Recount the static selection, board population and package size."""
import argparse
import hashlib
import json
import sqlite3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree
from statement_links import unlinked_cards, card_label


class Main(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.attrs = {}
        self.links = set()
        self.text_by_href = {}
        self.in_title = self.in_footer = False
        self.title = ""
        self.metadata = {}
        self.canonical = ""
        self.footer_links = set()
        self.anchor = None
        self.anchor_text = []
        self.page = page
        self.feed(page.read_text())
        self.close()
        if self.anchor is not None:
            raise ValueError(f"Unclosed anchor in {page}")

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "footer":
            self.in_footer = True
        elif tag == "meta":
            self.metadata[attrs.get("property") or attrs.get("name")] = attrs.get("content")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs["href"]
        if tag == "main":
            self.attrs = attrs
        elif tag == "a":
            if self.anchor is not None:
                raise ValueError(f"Nested anchor in {self.page}")
            self.anchor = attrs.get("href", "")
            self.anchor_text = []
            self.links.add(self.anchor)
            if self.in_footer:
                self.footer_links.add(self.anchor)

    def handle_data(self, text):
        if self.in_title:
            self.title += text
        if self.anchor is not None:
            self.anchor_text.append(text)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "footer":
            self.in_footer = False
        if tag == "a" and self.anchor is not None:
            label = "".join(self.anchor_text).strip()
            if not label:
                raise ValueError(f"Empty anchor text in {self.page} for {self.anchor}")
            self.text_by_href[self.anchor] = label
            self.anchor = None


def check_agent_entry_points(db, site):
    guide = (site / "llms.txt").read_text(encoding="utf-8")
    assert "/informalizations.json" in guide, "Missing index link in llms.txt"
    entries = json.loads((site / "informalizations.json").read_text(encoding="utf-8"))
    assert isinstance(entries, list)
    expected = set(db.execute("""SELECT m.package, m.path, i.author, i.writer
                                 FROM informalizations i JOIN modules m ON m.id=i.module WHERE i.entry_type='informalization'"""))
    assert len(entries) == len(expected)
    assert {(e["package"], e["module"], e["author"], e["writer"]) for e in entries} == expected
    for entry in entries:
        address = urlsplit(entry["page"])
        page = site / unquote(address.path).lstrip("/") / "index.html"
        assert f'id="{unquote(address.fragment)}"' in page.read_text(encoding="utf-8"), entry["page"]
    return len(entries)


def verify(database, site, *, database_source_docs=True):
    with sqlite3.connect(f"{database.resolve().as_uri()}?mode=ro", uri=True) as db:
        indexed = check_agent_entry_points(db, site)
        modules = {mid:(pkg,path) for mid,pkg,path in db.execute("SELECT id,package,path FROM modules")}
        informalizations = {row[0] for row in db.execute("SELECT module FROM informalizations WHERE entry_type='informalization'")}
        links = {row[0] for row in db.execute("SELECT module FROM links")}
        spine = {row[0] for row in db.execute("SELECT id FROM modules WHERE spine_rank IS NOT NULL")}
        docs = {r[0] for r in db.execute("SELECT module FROM informalizations WHERE entry_type='source-documentation'")}
        static_ids = informalizations | docs | links | spine
        if database_source_docs:
            static_ids -= docs - informalizations
        eligible = {modules[mid] for mid in static_ids}
        actual = list(db.execute("SELECT rank,module FROM most_wanted ORDER BY rank"))
        wanted = list(db.execute("SELECT id,cut,path,spine_rank FROM modules WHERE project=1 AND ((mask & 1) != 0 OR mask IS NULL)"))
        wanted = sorted((r for r in wanted if r[0] not in informalizations),
                        key=lambda r: (r[3] is None, r[3] or 0, r[1] is None, -(r[1] or 0), r[2]))
        assert actual == [(rank, row[0]) for rank, row in enumerate(wanted, 1)]
        unmatched = unlinked_cards(url for (url,) in db.execute("SELECT DISTINCT url FROM links"))
        assert len(unmatched) == db.execute("SELECT value FROM summary WHERE metric='unmatched_statements'").fetchone()[0]
        issues = db.execute("SELECT count(*) FROM disputes").fetchone()[0]
    config = json.loads((site / "directory.json").read_text())
    sample_paths = {(s["package"],s["value"]):s["id"] for s in config["samples"] if s["type"]=="module"}
    found = set()
    parsed = {}
    for pkg,path in sorted(eligible):
        if (pkg,path) in sample_paths:
            page = site / "sample" / pkg / sample_paths[pkg,path] / "index.html"
        else:
            key = hashlib.sha256(path.encode()).hexdigest()[:16]
            page = site / "m" / "records" / pkg / key / "index.html"
            found.add(pkg+"/"+key)
        record = Main(page)
        parsed[page] = record
        assert record.attrs.get("data-ready") == "true" and record.attrs.get("data-original-path", path) == path
        proof = config["proof"]
        pin = proof["packages"][pkg]
        expected = f"{pin['url']}/blob/{pin['commit']}/{pin.get('repositoryFolder','')}{path}"
        assert expected in {unquote(url) for url in record.links if url}, path
    assert found == set(config["staticModules"]) == {p.parent.relative_to(site/"m"/"records").as_posix() for p in (site/"m"/"records").glob("*/*/index.html")}
    assert config["wantedCount"] == len(wanted)
    pages = list(site.rglob("*.html"))
    unmatched_page = site/"unmatched"/"index.html"
    listing = Main(unmatched_page)
    parsed[unmatched_page] = listing
    assert {u:t for u,t in listing.text_by_href.items() if u.startswith(("https://andrewodesky.com/rh/s/", "https://andrewodesky.com/rh/lean/"))} == {
        c["url"]:card_label(c) for c in unmatched}
    for page in set(pages) - parsed.keys():
        parsed[page] = Main(page)
    assert len({r.title for r in parsed.values()}) == len(pages), "Duplicate static page title"
    origin = parsed[site / "index.html"].canonical
    ledger = config["proof"]["repository"]
    footer = {ledger, ledger + "/blob/main/CONTRIBUTING.md", ledger + "/blob/main/LICENSE",
              "/about/", "https://creativecommons.org/licenses/by/4.0/"}
    expected_urls = set()
    link_origin = origin or "https://local.invalid/"
    for page, record in parsed.items():
        base = urljoin(link_origin, page.relative_to(site).as_posix())
        for href in record.links:
            path = urlsplit(urljoin(base, href or ""))
            if path.netloc == urlsplit(link_origin).netloc and path.path.startswith("/m/records/"):
                assert (site / path.path.lstrip("/") / "index.html").is_file(), (page, href)
        relative = page.relative_to(site).as_posix()
        url_path = relative.removesuffix("index.html")
        assert record.metadata.get("og:title") == record.title and record.title, relative
        assert record.metadata.get("description") and record.metadata["description"] == record.metadata.get("og:description"), relative
        assert footer <= record.footer_links, relative
        if relative == "probe.html":
            assert not origin and record.metadata.get("robots") == "noindex", relative
        if origin:
            assert record.canonical == urljoin(origin, url_path), relative
            assert record.metadata.get("og:image") == urljoin(origin, "qed-codex-logo.png"), relative
            if url_path not in {"m/", "d/", "404.html"}:
                expected_urls.add(record.canonical)
        else:
            assert not record.canonical and "og:image" not in record.metadata, relative
    sitemap = site / "sitemap.xml"
    assert sitemap.exists() == bool(origin)
    if origin:
        assert (site / "qed-codex-logo.png").is_file() and not (site / "probe.html").exists()
        listed = [node.text for node in ElementTree.parse(sitemap).iterfind(".//{*}loc")]
        assert sorted(expected_urls) == sorted(listed)
    files = [p for p in site.rglob("*") if p.is_file()]
    assert len(files) < 20000
    manifest = json.loads((site / "proof.json").read_text())
    piece_files = sum(1 for _ in (site / "db" / manifest["buildId"] / "p").iterdir())
    pages_per_piece = manifest.get("pagesPerPiece", 1)
    assert piece_files == (manifest["pageCount"] + pages_per_piece - 1) // pages_per_piece
    return {"indexedInformalizations":indexed,"withSourceDocumentation":len(docs),"unmatchedStatements":len(unmatched),"withInformalization":len(informalizations),"withOutsideLink":len(links),"withSpineRank":len(spine),
            "qualifyingModules":len(eligible),"sampleModulesOutsideSelection":len(set(sample_paths)-eligible),
            "standaloneModules":len(eligible|set(sample_paths)),"htmlFiles":len(pages),
            "sqlitePages":manifest["pageCount"],"pagesPerPiece":pages_per_piece,"pieceFiles":piece_files,
            "files":len(files),"bytes":sum(p.stat().st_size for p in files),"fileCap":20000,
            "remainingFiles":20000-len(files),"mostWanted":len(wanted),
            "withMeasuredCut":sum(cut is not None for _,cut,_,_ in wanted),"disputes":issues}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("database", type=Path)
    cli.add_argument("site", type=Path)
    cli.add_argument("--database-source-docs", action=argparse.BooleanOptionalAction, default=True)
    args=cli.parse_args()
    print(json.dumps(verify(args.database,args.site,database_source_docs=args.database_source_docs),indent=2))

"""Join the author's statement map to exact declarations and compiled constants."""
import csv
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import quote

from statement_index import BASE, address_name

SOURCE = Path("proofs/rh/sources/odesky")
MAP_URL = BASE + "lean-map.tsv"
AUTHOR = "Andrew O’Desky"
LINK_FIELDS = ("module", "author", "url", "declaration", "label")
MAP_FIELDS = ("page_id", "kind", "title", "address", "lean_name", "status")
CARD_FIELDS = ("card_id", "kind", "title", "url", "declaration", "module", "status")
CONSTANT_FIELDS = ("card_id", "declaration", "constant_owner", "constant_module")
CONSTANTS_SHA = "2964f5236046325ac7884906cb9517b0aa582330dd48a07eef291cb579444820"
DECLS_SHA = "bdfeae289f2db8b279816439049f26ba69ec993af2bab3b30d53340fe02493b9"


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def current_rows():
    pin = json.loads((SOURCE / "snapshots.json").read_text())
    path = SOURCE / "cards.tsv"
    if hashlib.sha256(path.read_bytes()).hexdigest() != pin["cardsSha256"]:
        raise ValueError("Statement ledger differs from the capture")
    cards = read_tsv(path)
    if "constantMatchesSha256" in pin:
        evidence = SOURCE / "constant-matches.tsv"
        if hashlib.sha256(evidence.read_bytes()).hexdigest() != pin["constantMatchesSha256"]:
            raise ValueError("Compiled constant evidence differs from the capture")
        matches = {(r["card_id"], r["declaration"]): r for r in read_tsv(evidence)}
        for r in cards:
            r.update(matches.get((r["card_id"], r["declaration"]), {}))
    return cards


def by_page(rows):
    return {r["card_id"]:r for r in rows}


def current_cards():
    return by_page(current_rows())


def card_label(card):
    return card["title"]


def unlinked_cards(link_urls):
    linked = set(link_urls)
    return sorted((c for c in current_cards().values() if c["url"] not in linked),
                  key=lambda c: (c["kind"], c["title"], c["url"]))


def add_constant_matches(rows, constants, structures):
    """A page with an exact project declaration keeps its declaration-level evidence."""
    linked = {r["card_id"] for r in rows if r["module"]}
    pending = [r for r in rows if r["card_id"] not in linked and r["declaration"]]
    wanted = {r["declaration"] for r in pending}
    matches = {}
    with constants.open("rb") as f:
        if hashlib.file_digest(f, "sha256").hexdigest() != CONSTANTS_SHA:
            raise ValueError("Unexpected pinned compiled constants")
    with gzip.open(constants, "rt", newline="") as f:
        for r in csv.DictReader(f):
            name = r["name"]
            if name not in wanted:
                continue
            owner = r["decl"]
            if r["origin"] == "mathlib" and r["module"].startswith("Mathlib."):
                match = ("", r["module"].replace(".", "/") + ".lean")
            elif (r["origin"] == "project" and r["aux_rule"] == "nested"
                  and r["shared_aux"] == "false" and owner == name.rpartition(".")[0]
                  and owner in structures and structures[owner] == r["file"]):
                match = (owner, r["file"])
            else:
                continue
            if matches.setdefault(name, match) != match:
                raise ValueError(f"Ambiguous compiled constant: {name}")
    for r in pending:
        r["constant_owner"], r["constant_module"] = matches.get(r["declaration"], ("", ""))


def map_rows(path, decls, constants):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        if tuple(reader.fieldnames or ()) != MAP_FIELDS:
            raise ValueError("Unexpected lean-map.tsv header")
        data = list(reader)
    if not data or {r["kind"] for r in data} != {"theorem", "definition"}:
        raise ValueError("Statement map is empty or contains unexpected kinds")
    wanted = {r["lean_name"] for r in data}
    with decls.open("rb") as f:
        if hashlib.file_digest(f, "sha256").hexdigest() != DECLS_SHA:
            raise ValueError("Unexpected pinned project declaration data")
    parents = {name.rpartition(".")[0] for name in wanted if name}
    structures = {}
    owners = {}
    with gzip.open(decls, "rt", newline="") as f:
        for r in csv.DictReader(f):
            name = r["decl"]
            if (name in parents and r["origin"] == "project"
                    and r["command_kind"] in {"structure", "class"}):
                if structures.setdefault(name, r["file"]) != r["file"]:
                    raise ValueError(f"Ambiguous structure: {name}")
            if name in wanted and r["origin"] == "project":
                previous = owners.setdefault(name, r["file"])
                if previous != r["file"]:
                    raise ValueError(f"Ambiguous declaration owner: {name}")
    cards = {}
    addresses = {}
    result = []
    for r in data:
        if None in r or r["lean_name"] is None or not all(r.get(k) and r[k].strip() for k in ("page_id","kind","title","address","status")):
            raise ValueError("Incomplete statement map row")
        key, name = r["page_id"], r["lean_name"]
        url = quote(r["address"], safe=":/%!$&'()*+,;=@-._~")
        address_name(url)  # Validate the address shape, regardless of the row's Lean name.
        page = (url, r["kind"], r["title"])
        if cards.setdefault(key, page) != page or addresses.setdefault(url, key) != key:
            raise ValueError(f"Inconsistent identity for statement {key}")
        result.append(dict(zip(CARD_FIELDS, (key, r["kind"], r["title"], url, name,
                                              owners.get(name, ""), r["status"]), strict=True)))
    add_constant_matches(result, constants, structures)
    return sorted(result, key=lambda r: tuple(r[k] for k in CARD_FIELDS))


def generated_links(rows):
    exact = {(r["module"], AUTHOR, r["url"], r["declaration"], r["title"]) for r in rows if r["module"]}
    module_links = {(r["constant_module"], AUTHOR, r["url"], "", r["title"])
                    for r in rows if r.get("constant_module")}
    return exact | module_links


def statement_links():
    return generated_links(current_rows())


def refresh_ledger(ledger, old_rows, new_rows):
    previous = generated_links(old_rows)
    by_old_url = {r["url"]:r["card_id"] for r in old_rows}
    current = by_page(new_rows)
    result = generated_links(new_rows)
    for r in ledger:
        row = tuple(r.get(k, "") for k in LINK_FIELDS)
        if row in previous:
            continue
        module, author, url, declaration, label = row
        if author == AUTHOR and url in by_old_url:
            card = current.get(by_old_url[url])
            if not card:
                continue
            url, label = card["url"], card["title"]
        result.add((module, author, url, declaration, label))
    return sorted(result)


def summary(rows, links):
    pages = by_page(rows)
    urls = {r["url"] for r in pages.values()}
    statement_rows = [r for r in links if r[2] in urls]
    linked = {r[2] for r in statement_rows}
    unmatched = [r for r in pages.values() if r["url"] not in linked]
    generated = generated_links(rows)
    missing = sorted({r["declaration"] for r in rows if r["declaration"] and not r["module"]})
    return {
        "pages":len(pages), "mapRows":len(rows),
        "byKind":dict(sorted(Counter(r["kind"] for r in pages.values()).items())),
        "distinctNames":len({r["declaration"] for r in rows if r["declaration"]}),
        "distinctProjectNames":len({r[3] for r in generated if r[3]}),
        "namesWithoutProjectDeclaration":missing,
        "statementDeclarationLinks":sum(bool(r[3]) for r in generated),
        "constantModuleLinks":sum(not r[3] for r in generated),
        "pagesMatchedByConstant":len({r[2] for r in generated if not r[3]}),
        "statementModuleLinks":len({(r[0],r[2]) for r in statement_rows}),
        "modulePagesWithStatementLink":len({r[0] for r in statement_rows}),
        "pagesWithModuleLink":len(pages)-len(unmatched),
        "unmatchedPages":len(unmatched),
        "unmatchedByKind":dict(sorted(Counter(r["kind"] for r in unmatched).items())),
        "ledgerRows":len(links), "ledgerModuleLinks":len({(r[0],r[2]) for r in links}),
        "modulePagesWithAnyLink":len({r[0] for r in links}),
    }

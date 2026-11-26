"""Build the permission ledger from the captured statement cards and reviewed module links."""
from source_registry import directory_proof
import argparse
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urljoin, urlsplit

from bs4 import BeautifulSoup, NavigableString
from check_informalization_pr import note_key, parse_note
from informalizations import render_informalization
from statement_index import BASE, tsv
from statement_links import AUTHOR, SOURCE, read_tsv

WRITER = "Andrew O'Desky"
FILE = note_key("dial481", WRITER) + ".md"
OPEN = re.compile(r"(?<!\\)(\$\$|\$|\\\(|\\\[)")
CLOSE = {"$": "$", "$$": "$$", r"\(": r"\)", r"\[": r"\]"}
SHA = re.compile(r"\\Sha(?![a-zA-Z])")
DASHINT = re.compile(r"\\dashint(?![a-zA-Z])")


def external(href):
    url = urlsplit(urljoin(BASE, href))
    if (url.scheme, url.netloc) != ("https", "andrewodesky.com"):
        raise ValueError(f"Unexpected statement link {href}")
    return quote(url.geturl(), safe=":/%#?&=+@!;,'*~$")


def prose(text):
    return re.sub(r"([\\`*_\[\]<>~])", r"\\\1", re.sub(r"\s+", " ", text))


def markdown(statement):
    formulas = []

    def text(value):
        parts = []
        pos = 0
        while found := OPEN.search(value, pos):
            parts.append(prose(value[pos:found.start()]))
            delimiter = found.group()
            end = re.search(r"(?<!\\)" + re.escape(CLOSE[delimiter]), value[found.end():])
            if not end:
                if delimiter == "$" and not value[found.end():].strip(" .,:;!?"):
                    parts.append(r"\$")
                    pos = found.end()
                    continue
                raise ValueError("Unpaired math delimiter: " + value[max(0, found.start()-50):found.end()+50])
            tex = value[found.end():found.end()+end.start()].strip()
            tex = SHA.sub(lambda _: r"\mathrm{Ш}", tex)
            tex = DASHINT.sub("⨍", tex)
            # Big delimiters pass through latex2mathml as literal names otherwise.
            fences = {"langle": "⟨", "rangle": "⟩", "lfloor": "⌊", "rfloor": "⌋"}
            tex = re.sub(r"(\\(?:big|Big)(?:g)?[lrm]?)\s*\\(langle|rangle|lfloor|rfloor)\b",
                         lambda m: m[1] + fences[m[2]], tex)
            # The source embeds math shifts inside a text run in one display.
            # Close and reopen the text run at each shift, preserving the words.
            def nested_math(m):
                return "".join(part if i % 2 else r"\text{" + part + "}"
                               for i, part in enumerate(m[1].split("$")) if part)
            tex = re.sub(r"\\text\{([^{}]*\$[^{}]*)\}", nested_math, tex)
            # Preserve TeX line-break commands while normalizing physical source lines.
            tex = re.sub(r"\s+", " ", tex)
            block = delimiter in ("$$", r"\[")
            formulas.append("block" if block else "inline")
            parts.append(("$$" if block else "$") + tex + ("$$" if block else "$"))
            pos = found.end()+end.end()
        return "".join(parts) + prose(value[pos:])

    def convert(node):
        if isinstance(node, NavigableString):
            return text(str(node))
        if node.name in ("ol", "ul"):
            items = []
            for n,item in enumerate(node.find_all("li",recursive=False), int(node.get("start",1))):
                marker = f"{n}. " if node.name == "ol" else "- "
                body = "".join(convert(c) for c in item.children).strip()
                continuation = "\n" + " " * len(marker)
                items.append(marker + body.replace("\n",continuation).rstrip())
            return "\n\n" + "\n".join(items) + "\n\n"
        # The live site's normal citation view shows the title, with the label hidden.
        if node.name == "span" and node.get("class") == ["xref-label"]:
            return ""
        inside = "".join(convert(c) for c in node.children)
        if node.name == "span" and node.get("class") in (["xref"], ["xref-title"]):
            return inside
        if node.name == "p":
            return "\n\n" + inside.strip() + "\n\n"
        if node.name in ("strong","em"):
            mark = "**" if node.name == "strong" else "*"
            return mark+inside.strip()+mark
        if node.name == "a":
            return "["+inside.strip()+"]("+external(node["href"])+")"
        raise ValueError(f"Unexpected markup in statement: {node.name}")

    body = "".join(convert(c) for c in statement.children)
    body = re.sub(r"\n[ \t]+\n", "\n\n", body).strip()
    return re.sub(r"\n{3,}", "\n\n", body), formulas


def cards(root):
    receipt = json.loads((root/"capture.json").read_text())
    pinned = json.loads(Path("reports/permission-statements/card-capture.json").read_text())
    identity = lambda rows: {name:(r["url"],r["bytes"],r["sha256"]) for name,r in rows.items()}
    if identity(receipt) != identity(pinned):
        raise ValueError("Snapshot differs from the reviewed card capture")
    chunks = {}
    for file,r in receipt.items():
        data = (root/file).read_bytes()
        if len(data) != r["bytes"] or hashlib.sha256(data).hexdigest() != r["sha256"]:
            raise ValueError(f"Captured file differs: {file}")
        if file.startswith("cards/"):
            doc = BeautifulSoup(data.decode(),"html.parser")
            chunks[file] = {a["id"]:a for a in doc.select("article.theorem-card")}
    seen = set()
    for file in ("index.html","definitions.html"):
        doc = BeautifulSoup((root/file).read_text(),"html.parser")
        for a in doc.select("article.theorem-card"):
            key = a["id"]
            if key in seen:
                raise ValueError(f"Duplicate card in indexes: {key}")
            seen.add(key)
            if a.has_attr("data-chunk"):
                a = chunks[a["data-chunk"]][key]
            yield key,a


def load(root, destination, report):
    receipt = json.loads((root / "capture.json").read_text())
    captured = datetime.fromisoformat(receipt["index.html"]["utc"]).astimezone(timezone.utc)
    dateline = f"As published on {captured.day} {captured:%B %Y}."
    mapping = defaultdict(lambda: defaultdict(set))
    for row in read_tsv(Path("proofs/rh/links.tsv")):
        if row["author"] == AUTHOR:
            names = mapping[row["url"]][row["module"]]
            if row["declaration"]:
                names.add(row["declaration"])
    known = {r["card_id"] for r in read_tsv(SOURCE/"cards.tsv")}
    proof = directory_proof()
    grouped = defaultdict(list)
    evidence = []
    used = set()
    errors = []
    for key, card in cards(root):
        url = external(card.header.h3.a["href"])
        title = card.header.h3.a.get_text(" ",strip=True)
        kind = card.header.select_one(".statement-kind").get_text(" ",strip=True)
        files = mapping.get(url, {})
        try:
            statement = card.find("div",class_="stmt",recursive=False)
            body, formulas = markdown(statement)
            html = render_informalization(body,BASE)
            if html.count("<math ") != len(formulas) or html.count('display="block"') != formulas.count("block"):
                raise ValueError(f"Math mismatch: {len(formulas)} expressions, {html.count('<math ')} rendered, {formulas.count('block')} display / {html.count('display='+chr(34)+'block'+chr(34))}")
            if re.search(r"<(?:mi|mo)>\\[A-Za-z]+</",html):
                unknown = sorted(set(re.findall(r"<(?:mi|mo)>(\\[A-Za-z]+)</",html)))
                raise ValueError("Unconverted TeX commands: " + " ".join(unknown))
            section = f"## {prose(title)}\n\n[{prose(kind)}]({url})\n\n{body}"
        except Exception as exc:
            errors.append((key,str(exc)))
            continue
        reason = "" if files else ("no module link in the frozen map" if key in known else "absent from the frozen map")
        evidence.append((key,url,kind,len(formulas),reason,len(files)))
        if files:
            used.add(url)
        for path, names in files.items():
            grouped[path].append((names,section))
    if errors:
        for key,err in errors:
            print(key,err)
        raise ValueError(f"{len(errors)} statements failed conversion")
    if used != set(mapping):
        raise ValueError(f"Missing mapped addresses: {sorted(set(mapping)-used)}")
    planned = {}
    for module,entries in grouped.items():
        pkg = "riemann-hypothesis" if module.startswith("src/") else "mathlib"
        meta = dict(module=module,declarations=sorted(set().union(*(ns for ns,_ in entries))),
                    author="dial481",writer=WRITER,origin="other-author",source=BASE,
                    source_commit=proof["packages"][pkg]["commit"],license="with-permission")
        data = "---\n"+json.dumps(meta,ensure_ascii=False,indent=2)+f"\n---\n\n{dateline}\n\n"+"\n\n".join(s for _,s in entries)+"\n"
        parse_note(data.encode(),maintainer=True)
        planned[destination/pkg/"informalizations"/module/FILE] = data
    for path,data in planned.items():
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(data)
    report.mkdir(parents=True, exist_ok=True)
    tsv(report/"pages.tsv",["card_id","url","kind_and_number","formulas","omission","modules"],evidence)
    print(f"{len(used)} pages loaded into {len(planned)} ledger files from {len(evidence)} captured pages")


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capture",type=Path)
    parser.add_argument("--packages",type=Path,default=Path("packages"))
    parser.add_argument("--report",type=Path,default=Path("reports/permission-statements"))
    args=parser.parse_args()
    load(args.capture,args.packages,args.report)

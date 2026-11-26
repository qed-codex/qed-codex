"""Audit the emitted MathML in every ledger entry or in a packaged site."""
import argparse
import json
import re
from collections import Counter, defaultdict
from functools import lru_cache
from html.entities import html5
from pathlib import Path
from unittest.mock import patch
from xml.etree import ElementTree as ET

import yaml

import informalizations

FORMULA = re.compile(r"<math\b[^>]*>.*?</math>", re.S)
TOKENS = {"mi", "mo", "mn", "ms", "mtext"}
ARITY = {"msub": 2, "msup": 2, "msubsup": 3, "munder": 2, "mover": 2,
         "munderover": 3, "mfrac": 2, "mroot": 2}


@lru_cache(maxsize=32768)
def inspect(markup):
    # HTML serialization can emit &nbsp;. Keep XML metacharacters encoded.
    xml = re.sub(r"&([A-Za-z][A-Za-z0-9]*;)",
                 lambda m: "".join(f"&#{ord(c)};" for c in html5[m[1]]), markup)
    issues = []
    nulls = []
    for elem in ET.fromstring(xml).iter():
        tag = elem.tag
        text = elem.text or ""
        if tag == "merror":
            issues.append(("merror", "conversion error"))
        if elem.get("mathvariant", "normal") != "normal":
            issues.append(("style", elem.get("mathvariant")))
        if tag in TOKENS:
            if "\\" in text and text != "\\":
                issues.append(("backslash", text))
            if not text or len(elem):
                if tag == "mo" and not len(elem) and elem.get("fence") == elem.get("stretchy") == "true":
                    nulls.append(elem.get("form"))
                else:
                    issues.append(("empty-or-nested-token", tag))
        if tag in ARITY and len(elem) != ARITY[tag]:
            issues.append(("arity", f"{tag} with {len(elem)} children"))
    return issues, nulls


def scan(records):
    kinds = defaultdict(Counter)
    examples = defaultdict(Counter)
    pages = Counter()
    distinct = set()
    total = formulas = 0
    for path, pairs in records:
        total += 1
        seen = set()
        for markup, tex in pairs:
            formulas += 1
            distinct.add(markup if tex is None else tex)
            issues, nulls = inspect(markup)
            if tex is not None:
                wanted = re.findall(r"\\(left|right)\s*\.", tex)
                directions = ["prefix" if x == "left" else "postfix" for x in wanted]
                if nulls != directions:
                    issues = [*issues, ("null-delimiter", "does not match source")]
            for kind, detail in issues:
                seen.add(kind)
                kinds[kind][detail] += 1
                if kind != "style":
                    examples[kind][tex if tex is not None else markup] += 1
        pages.update(seen)
    return {"records": total, "formulaOccurrences": formulas, "distinct": len(distinct), "affectedRecords": dict(pages),
            "violations": dict(kinds), "examples": dict(examples)}


def static_records(root, records_only=False):
    files = sorted(root.rglob("*.html"))
    for file in files:
        if records_only and file.relative_to(root).parts[:2] != ("m", "records") and file.relative_to(root).parts[0] != "sample":
            continue
        yield file, ((m[0], None) for m in FORMULA.finditer(file.read_text()))


def ledger_records(root):
    render = informalizations.render_math
    for file in sorted(root.glob("*/informalizations/**/*.md")):
        _, meta, body = file.read_text().split("---\n", 2)
        expressions = []

        def capture(tex, display):
            expressions.append(tex)
            return render(tex, display)

        with patch.object(informalizations, "render_math", capture):
            html = informalizations.render_informalization(body, yaml.safe_load(meta).get("source", "https://example.org/"))
        yield file, zip(FORMULA.findall(html), expressions, strict=True)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    target = cli.add_mutually_exclusive_group(required=True)
    target.add_argument("--site", type=Path)
    target.add_argument("--record-pages", type=Path, help="Pre-rendered modules and samples in this package")
    target.add_argument("--ledger", type=Path)
    args = cli.parse_args()
    if args.ledger:
        records = ledger_records(args.ledger)
    else:
        records = static_records(args.site or args.record_pages, records_only=bool(args.record_pages))
    report = scan(records)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    raise SystemExit(bool(report["violations"]))

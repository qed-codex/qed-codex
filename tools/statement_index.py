"""Statement ledger address validation and UTF-8 TSV output."""
import csv
import re
from urllib.parse import unquote, urlsplit

BASE = "https://andrewodesky.com/rh/"


def address_name(url):
    """Parse a canonical theorem address without altering Lean spelling."""
    parsed = urlsplit(url)
    if not url.startswith(BASE) or parsed.fragment or parsed.query:
        raise ValueError(f"Unexpected statement address {url}")
    path = url[len(BASE):]
    if path.startswith("s/") and len(path) > 2:
        return ""
    match = re.fullmatch(r"lean/([^/]+)/", path)
    if not match:
        raise ValueError(f"Unexpected statement address {url}")
    name = unquote(match[1], errors="strict")
    if "/" in name or any(ord(c) < 32 for c in name):
        raise ValueError(f"Invalid declaration segment in {url}")
    return name


def tsv(path, columns, rows):
    with path.open("w", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)

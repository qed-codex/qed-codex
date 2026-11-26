"""Check the packaged MathML against the cmap of the font served to its readers."""
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path

from fontTools.ttLib import TTFont

FONT = Path("fonts/stix-two-math.woff2")
DIGEST = "8b2a6834cfe1f4e0f3724ffa59fe92000013fc5a4c41e6a3f438006c26c60f0d"
FORMULA = re.compile(r"<math\b.*?</math>", re.DOTALL)


def italic_map():
    # Unicode compatibility decompositions include the italic h at U+210E
    # and the mathematical forms of dotless i, dotless j and variant Greek.
    mapping = {}
    for code in [0x210e, *range(0x1d400, 0x1d800)]:
        ch = chr(code)
        if code != 0x210e and not unicodedata.name(ch, "").startswith("MATHEMATICAL ITALIC "):
            continue
        tag, base = unicodedata.decomposition(ch).split()
        if tag == "<font>":
            mapping[chr(int(base, 16))] = ch
    return mapping


ITALIC = italic_map()


class Characters(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.characters = set()
        self.identifiers = []
        self.default_singles = 0
        self.default_style = False
        self.token = None

    def handle_starttag(self, tag, attrs):
        if tag == "mi":
            self.token = []
            self.default_style = dict(attrs).get("mathvariant") != "normal"

    def handle_data(self, text):
        self.characters.update(text)
        if self.token is not None:
            self.token.append(text)

    def handle_endtag(self, tag):
        if tag == "mi" and self.token is not None:
            value = "".join(self.token)
            if len(value) == 1:
                self.identifiers.append(value)
                self.default_singles += int(self.default_style)
            self.token = None


@lru_cache(maxsize=32768)
def characters(markup):
    parser = Characters()
    parser.feed(markup)
    parser.close()
    return parser.characters, parser.identifiers, parser.default_singles


def verify_math_font(site):
    file = site / FONT
    if hashlib.sha256(file.read_bytes()).hexdigest() != DIGEST:
        raise ValueError("STIX Two Math differs from the pinned Fontsource 5.3.0 asset")
    if not (file.parent / "OFL.txt").is_file():
        raise ValueError("Missing STIX Two Math license")
    with TTFont(file) as font:
        cmap = set(font.getBestCmap())
    counts = Counter()
    chars = set()
    identifiers = Counter()
    for page in sorted(site.rglob("*.html")):
        total = 0
        for match in FORMULA.finditer(page.read_text(encoding="utf-8")):
            used, singles, default_singles = characters(match[0])
            counts["defaultSingleIdentifiers"] += default_singles
            chars.update(used)
            identifiers.update(singles)
            total += 1
        counts["pages"] += bool(total)
        counts["formulas"] += total
    italics = {ITALIC[ch] for ch in identifiers if ch in ITALIC}
    missing = sorted(ord(c) for c in chars | italics if ord(c) not in cmap)
    if missing:
        raise ValueError("Missing math glyphs: " + ", ".join(
            f"U+{cp:04X} {unicodedata.name(chr(cp), 'unnamed')}" for cp in missing))
    return {**counts, "characters": len(chars), "nonWhitespaceCharacters": sum(not ch.isspace() for ch in chars),
            "singleCodepointIdentifiers": identifiers.total(),
            "alphabeticIdentifiers": sum(n for ch, n in identifiers.items() if ch.isalpha()),
            "italicCharacters": len(italics), "mathAlphanumeric": sum(0x1d400 <= ord(c) < 0x1d800 for c in chars),
            "letterlike": sum(0x2100 <= ord(c) < 0x2150 for c in chars), "missingGlyphs": len(missing),
            "fontBytes": file.stat().st_size, "sha256": DIGEST}


if __name__ == "__main__":
    print(json.dumps(verify_math_font(Path(sys.argv[1])), indent=2))

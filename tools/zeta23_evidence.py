"""Compare source-note glyphs to the review text fonts and the pinned math face."""

import argparse
import collections
import hashlib
import json
from pathlib import Path
import tarfile
import unicodedata

from fontTools.ttLib import TTFont
from import_lean_docs import scan


def coverage(archive, math_font, text_dir):
    cfg = json.loads(Path("packages/zeta23/import.json").read_text())
    with archive.open("rb") as stream:
        if hashlib.file_digest(stream, "sha256").hexdigest() != cfg["archiveSha256"]:
            raise ValueError("archive differs from import pin")
    text = set()
    fonts = {}
    for f in sorted(text_dir.glob("DejaVu*.ttf")):
        if f.name.startswith("DejaVuMath"):
            continue
        with TTFont(f) as font:
            text.update(font.getBestCmap())
        fonts[f.name] = hashlib.sha256(f.read_bytes()).hexdigest()
    if not fonts:
        raise ValueError("no review text fonts")
    assert (
        hashlib.sha256(math_font.read_bytes()).hexdigest()
        == "8b2a6834cfe1f4e0f3724ffa59fe92000013fc5a4c41e6a3f438006c26c60f0d"
    )
    with TTFont(math_font) as font:
        math = set(font.getBestCmap())
    chars = collections.Counter()
    dollars = []
    with tarfile.open(archive) as tar:
        for member in tar:
            prefix = "formal-math-" + cfg["commit"] + "/zeta23/"
            if (
                not member.name.startswith(prefix)
                or not member.name.endswith(".lean")
                or not member.isfile()
            ):
                continue
            _, notes = scan(tar.extractfile(member).read().decode())
            for name, value in notes:
                chars.update(ord(c) for c in value if not c.isspace())
                if "$" in value:
                    dollars.append(
                        [member.name.removeprefix(prefix), name, value.count("$")]
                    )
    missing = sorted(chars.keys() - math)
    return {
        "textFontSha256": fonts,
        "distinctNonspaceCharacters": len(chars),
        "missingFromMath": [
            dict(
                code=f"U+{c:04X}",
                glyph=chr(c),
                name=unicodedata.name(chr(c)),
                uses=chars[c],
                inTextFont=c in text,
            )
            for c in missing
        ],
        "missingFromBoth": [f"U+{c:04X}" for c in missing if c not in text],
        "dollarSignsInNotes": dollars,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ["archive", "math_font", "text_dir"]:
        parser.add_argument(key, type=Path)
    args = parser.parse_args()
    print(
        json.dumps(
            coverage(args.archive, args.math_font, args.text_dir),
            ensure_ascii=False,
            indent=2,
        )
    )

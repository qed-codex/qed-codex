"""Compile contributed Markdown into an inert HTML fragment with native MathML."""

import json
import re
import unicodedata
from functools import lru_cache
from html import unescape
from urllib.parse import urlsplit
from xml.etree import ElementTree

import mistune
import nh3
from latex2mathml.converter import Converter
from latex2mathml.symbols_parser import convert_symbol
from mistune.plugins.math import math, math_in_list, math_in_quote


class InformalizationRenderer(mistune.HTMLRenderer):
    def inline_math(self, text):
        return render_math(text, "inline")

    def block_math(self, text):
        return render_math(text, "block") + "\n"

    def image(self, text, url, title=None):
        # Images would fetch an unreviewed asset on every visit. Keep the caption and link.
        return self.link(text or "Image", url, title)


# The Mathematical Alphanumeric Symbols block leaves holes for older letters in
# Letterlike Symbols. The UCD font decomposition gives the base (also for Greek
# variants and digits). Prefer the mathematical block when both blocks encode it.
@lru_cache(maxsize=1)
def mathematical_alphabets():
    styles = ("sans-serif-bold-italic", "sans-serif-italic", "bold-italic",
              "sans-serif-bold", "sans-serif", "bold-script", "bold-fraktur",
              "double-struck", "monospace", "fraktur", "script", "bold", "italic")
    prefixes = [(style.replace("-", " ").upper().replace("SANS SERIF", "SANS-SERIF")
                 .replace("DOUBLE STRUCK", "DOUBLE-STRUCK") + " ", style) for style in styles]
    table = {}
    for start, end in ((0x2100, 0x2150), (0x1D400, 0x1D800)):
        for cp in range(start, end):
            glyph = chr(cp)
            decomposition = unicodedata.decomposition(glyph).split()
            if len(decomposition) != 2 or decomposition[0] != "<font>":
                continue
            name = unicodedata.name(glyph).removeprefix("MATHEMATICAL ")
            name = name.replace("BLACK-LETTER ", "FRAKTUR ")
            # These five italic double-struck symbols are a separate alphabet.
            if name.startswith("DOUBLE-STRUCK ITALIC "):
                continue
            for prefix, style in prefixes:
                if name.startswith(prefix):
                    table[style, chr(int(decomposition[1], 16))] = glyph
                    break
    table.update({("bold-sans-serif", ch): glyph for (style, ch), glyph in table.items()
                  if style == "sans-serif-bold"})
    table["italic", "h"] = "ℎ"
    return table


def styled_text(variant, text):
    chars = []
    for char in text:
        glyph = mathematical_alphabets().get((variant, char))
        if glyph is None and char.isalpha():
            raise ValueError(f"No Unicode {variant} character for {char!r} (U+{ord(char):04X})")
        chars.append(glyph or char)
    return "".join(chars)


class MathConverter(Converter):
    def _convert_command(self, node, parent, font=None):
        if node.token == r"\binom":
            # latex2mathml emits two fences and a fraction as siblings. Together
            # they are one operand, including when the binomial carries a script.
            parent = ElementTree.SubElement(parent, "mrow")
        super()._convert_command(node, parent, font)


def render_math(text, display):
    try:
        return convert_math(text, display)
    except Exception as error:
        # Report the token Mistune actually rendered, including for errors raised
        # while serializing deeply nested MathML. Some TeX exceptions have no message.
        formula = text.replace("\r", r"\r").replace("\n", r"\n")
        reason = type(error).__name__
        if str(error):
            reason += f": {error}"
        raise ValueError(f"cannot render formula `{formula}` ({reason})") from error


def convert_math(text, display):
    # The tokenizer accepts a braced operator name. TeX also accepts a single
    # letter as its argument, e.g. the norm operator in \operatorname N.
    text = re.sub(r"(?<!\\)(\\operatorname(?:withlimits|\*)?)(?![a-zA-Z])\s*([A-Za-z])",
                  r"\1{\2}", text)
    tree = MathConverter(display=display).convert_to_element(text)
    for elem in tree.iter():
        if elem.tag == "merror":
            raise ValueError("MathML conversion produced an merror")
        if elem.tag == "mo" and len(elem):
            # An mo is a token and cannot contain presentation markup. Keep a
            # named operator as a single token, and a compound operator as a row.
            leaves = [n for n in elem.iter() if not len(n)]
            if all((n.tag == "mo" or n.tag == "mi" and n.get("mathvariant") == "normal")
                   and (n.text or "").isalpha() for n in leaves):
                elem.text = "".join(n.text for n in leaves)
                del elem[:]
            else:
                elem.tag = "mrow"
        if elem.text:
            # The converter stores numeric references as literal text in its tree.
            elem.text = unescape(elem.text)
            if elem.tag == "mo" and elem.get("minsize") and elem.text.startswith("\\"):
                symbol = convert_symbol(elem.text)
                if symbol:
                    elem.text = chr(int(symbol, 16))
            variant = elem.get("mathvariant")
            if variant and variant != "normal":
                elem.text = styled_text(variant, elem.text)
                del elem.attrib["mathvariant"]
    return ElementTree.tostring(tree, encoding="unicode", short_empty_elements=False)


MARKDOWN = mistune.create_markdown(
    renderer=InformalizationRenderer(escape=True),
    plugins=["table", math, math_in_list, math_in_quote],
)

PROSE_TAGS = set(
    "h1 h2 h3 h4 h5 h6 p em strong a blockquote ul ol li code pre hr br table thead tbody tr th td".split()
)
MATH_TAGS = set(
    "math mrow mi mn mo mtext mspace ms mfrac msqrt mroot msup msub msubsup "
    "mover munder munderover mtable mtr mtd mstyle mphantom mpadded menclose "
    "mmultiscripts mprescripts none".split()
)
ATTRIBUTES = {
    "a": {"href", "title"}, "ol": {"start"},
    "math": {"display"}, "mi": {"mathvariant"}, "mstyle": {"mathvariant", "displaystyle", "scriptlevel"},
    "mo": {"stretchy", "fence", "separator", "form", "minsize", "maxsize", "movablelimits", "largeop", "accent"},
    "mover": {"accent"}, "munder": {"accentunder"}, "munderover": {"accent", "accentunder"},
    "mspace": {"width", "height", "depth"}, "mtable": {"columnalign", "rowalign"},
    "mtd": {"columnalign", "columnspan", "rowspan"}, "mfrac": {"linethickness"},
    "menclose": {"notation"},
}


def render_informalization(body, source_url):
    """Resolve Markdown links where the informalization was written, then sanitize its HTML."""
    source = urlsplit(source_url)
    if source.scheme not in ("http", "https") or not source.hostname:
        raise ValueError("An informalization's source must be an absolute HTTP(S) URL")
    cleaner = nh3.Cleaner(
        tags=PROSE_TAGS | MATH_TAGS,
        attributes=ATTRIBUTES,
        url_schemes={"https", "http"},
        url_relative=("rewrite_with_base", source_url),
    )
    return cleaner.clean(MARKDOWN(body))


def agreement_json(note, agreements, ledger_hashes):
    """Store agreement with identified versions of other informalizations of this module."""
    if not isinstance(agreements, dict):
        raise ValueError(f"agrees_with must map handle--writer-slug keys to SHA-256 digests in {note}")
    current = {}
    for author, digest in agreements.items():
        key = (note.parent, author)
        if author == note.stem:
            raise ValueError(f"Invalid agrees_with reference to {author!r} in {note}")
        if key in ledger_hashes and ledger_hashes[key] == digest:
            current[author] = digest
    return json.dumps(current, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

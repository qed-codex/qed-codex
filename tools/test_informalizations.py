"""Regression checks for the compile-time informalization renderer."""

import unittest
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

from math_scan import FORMULA, inspect, ledger_records, scan

import yaml

from informalizations import agreement_json, render_informalization


class Fragment(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.starts = []
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        self.starts.append((tag, dict(attrs)))

    def attrs(self, tag):
        return [attrs for name, attrs in self.starts if name == tag]


class InformalizationTests(unittest.TestCase):
    source = "https://example.org/commit/abc/results/phase-2/note.md"

    def test_reader_features(self):
        text = (
            "# Heading\n\nInline $x^2$ and code `$z$`.\n\n$$\n"
            r"\frac{a}{b}" "\n$$\n\n| Left | Right |\n| --- | --- |\n| 1 | 2 |\n\n"
            "[Related informalization](../notes.md#one)"
        )
        html = render_informalization(text, self.source)
        fragment = Fragment(html)
        self.assertEqual(fragment.attrs("math"), [{"display": "inline"}, {"display": "block"}])
        for tag in ("mfrac", "msup", "h1", "table", "tbody", "thead"):
            self.assertTrue(fragment.attrs(tag))
        self.assertIn("<code>$z$</code>", html)
        self.assertEqual(fragment.attrs("a")[0]["href"], "https://example.org/commit/abc/results/notes.md#one")

    def test_raw_markup_is_text_and_markup_attributes_are_limited(self):
        text = (
            '<button disabled>raw markup</button>\n\n'
            r'$\text{<button>math text</button>}$' "\n\n"
            r'$\href{https://example.org/}{x}$' "\n\n"
            '![figure](https://example.org/figure.png)'
        )
        html = render_informalization(text, self.source)
        fragment = Fragment(html)
        self.assertIn("&lt;button disabled&gt;", html)
        self.assertFalse(fragment.attrs("button"))
        self.assertFalse(fragment.attrs("img"))
        self.assertEqual([a["href"] for a in fragment.attrs("a")], ["https://example.org/figure.png"])
        self.assertTrue(all("href" not in attrs for tag, attrs in fragment.starts if tag != "a"))

    def test_unicode_math_alphabets(self):
        tex = r"\mathbb C\mathbb{HNPRZ}\mathcal B\mathscr e\mathfrak R\mathsf T\mathbf1\boldsymbol{\alpha}"
        html = render_informalization(f"${tex}$", self.source)
        glyphs = "".join(ET.fromstring(FORMULA.search(html)[0]).itertext())
        self.assertEqual(glyphs, "ℂℍℕℙℝℤℬℯℜ𝖳𝟏𝜶")
        with self.assertRaisesRegex(ValueError, "No Unicode double-struck character"):
            render_informalization(r"$\mathbb{\alpha}$", self.source)

    def test_recoverable_unbalanced_brace_still_renders_a_superscript(self):
        recovered = render_informalization("$x^{2$", self.source)
        self.assertEqual(recovered, render_informalization("$x^{2}$", self.source))
        power = ET.fromstring(FORMULA.search(recovered)[0]).find(".//msup")
        self.assertEqual(["".join(child.itertext()) for child in power], ["x", "2"])

    def test_named_and_compound_operators(self):
        tex = r"\mathop{\operatorname{avg}}_h+g_j\mathbin{\mathrm{div}}N+\mathbin{+\!+}+\operatorname N\mathfrak c"
        tree = ET.fromstring(FORMULA.search(render_informalization(f"${tex}$", self.source))[0])
        self.assertEqual(tree.find(".//msub/mo").text, "avg")
        self.assertIn("div", [e.text for e in tree.iter("mo")])
        self.assertIn("N", [e.text for e in tree.iter("mo")])
        self.assertIn("++", "".join(tree.itertext()))
        self.assertIsNotNone(tree.find(".//mrow/mo[.='+']/../mspace"))

    def test_binomial_is_one_operand_and_delimiters_are_glyphs(self):
        tex = r"\left.\bigl\{\binom{n}{k}^{-1}\bigr\}\bigl\|x\bigr\|\backslash\right."
        markup = FORMULA.search(render_informalization(f"${tex}$", self.source))[0]
        issues, nulls = inspect(markup)
        self.assertEqual(issues, [])
        self.assertEqual(nulls, ["prefix", "postfix"])
        tree = ET.fromstring(markup)
        power = tree.find(".//msup")
        self.assertEqual([e.tag for e in power[0]], ["mo", "mfrac", "mo"])
        self.assertEqual("".join(power[1].itertext()), "−1")
        self.assertIn("{(nk)−1}‖x‖", "".join(tree.itertext()))

    def test_every_formula_in_ledger(self):
        report = scan(ledger_records(Path("packages")))
        self.assertGreater(report["formulaOccurrences"], 0)
        self.assertEqual(report["violations"], {}, report["examples"])

    def test_agreement_binds_a_peer_in_the_same_module_at_a_specific_digest(self):
        note = Path("informalizations/RowSrc.lean/reviewer.md")
        digest = "e" * 64
        index = {
            (note.parent, "peer"): digest,
            (note.parent, note.stem): "a" * 64,
            (Path("informalizations/Main.lean"), "root-reader"): digest,
        }
        self.assertEqual(agreement_json(note, {}, index), "{}")
        self.assertEqual(agreement_json(note, {"peer": digest}, index), '{"peer":"' + digest + '"}')
        for invalid in (None, [], {"root-reader": digest}, {"peer": "a" * 64}, {"reviewer": "a" * 64}):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                agreement_json(note, invalid, index)

    def test_seed_matches_original_citations(self):
        folder, = [p for root in (Path("packages"),Path("proofs")) for p in root.glob("*/informalizations/**/GaloisRepresentations/IntegralStructures/RowSrc.lean")]
        path = folder / "dial481--codex-gpt-6-2-astra.md"
        if not path.exists():
            path = folder / "dial481.md"
        _, metadata, body = path.read_text().split("---\n", 2)
        source = yaml.safe_load(metadata)["source"]
        fragment = Fragment(render_informalization(body, source))
        urls = {a["href"] for a in fragment.attrs("a")}
        self.assertIn(source.rsplit("/", 2)[0] + "/spine.tsv", urls)
        self.assertTrue(fragment.attrs("math"))
        self.assertTrue(fragment.attrs("table"))


if __name__ == "__main__":
    unittest.main()

import unittest

from bs4 import BeautifulSoup
from import_permission_statements import markdown
from informalizations import render_informalization
from statement_index import BASE


class StatementConversion(unittest.TestCase):
    def test_delimiters_and_symbols(self):
        snippet = r'<p>\(\Sha + \dashint\) and \[\big\langle x \big\rangle + \big\lfloor y\big\rfloor\]. A stray $</p>'
        body, formulas = markdown(BeautifulSoup(snippet, "html.parser"))
        html = render_informalization(body,BASE)
        self.assertEqual(["inline","block"],formulas)
        for glyph in ("Ш","⨍","⟨","⟩","⌊","⌋","A stray $"):
            self.assertIn(glyph,html)
        self.assertNotIn("\\",html)

    def test_display_containing_math_shifts_in_text(self):
        snippet = r'<p>$$x=y\quad\text{for $x$ in $A$}.$$</p>'
        body, formulas = markdown(BeautifulSoup(snippet,"html.parser"))
        self.assertEqual(["block"],formulas)
        html = render_informalization(body,BASE)
        self.assertEqual(1,html.count('<math '))
        self.assertNotIn('$',html)

    def test_reference_uses_visible_title(self):
        snippet = ('<p>See <span class="xref">(<a href="lean/X/"><span class="xref-title">X</span>'
                   '<span class="xref-label">Theorem 1</span></a>)</span>.</p>')
        body, _ = markdown(BeautifulSoup(snippet, "html.parser"))
        self.assertEqual(body, "See ([X](https://andrewodesky.com/rh/lean/X/)).")

    def test_list_numbering_and_relative_links(self):
        snippet = '<ol start="3"><li><strong>A.</strong> <a href="lean/X/">See X</a></li></ol>'
        body, _ = markdown(BeautifulSoup(snippet,"html.parser"))
        html = render_informalization(body,BASE)
        self.assertIn('<ol start="3">',html)
        self.assertIn('href="https://andrewodesky.com/rh/lean/X/"',html)
        self.assertIn('<strong>A.</strong>',html)


if __name__ == "__main__":
    unittest.main()

import shutil
import tempfile
import unittest
from pathlib import Path
from math_font import verify_math_font


class MathCoverage(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.site = Path(folder.name)
        shutil.copytree("site/fonts", self.site / "fonts")

    def test_math_characters_and_implicit_italics(self):
        (self.site / "page.html").write_text("<p>unrelated 🧐</p><math><mi>h</mi><mi>η</mi><mi>ε</mi><mi>ℂ</mi><mi>𝔭</mi></math>")
        result = verify_math_font(self.site)
        self.assertEqual(result["formulas"], 1)
        self.assertEqual(result["characters"], 5)
        self.assertEqual(result["italicCharacters"], 3)
        self.assertEqual(result["missingGlyphs"], 0)

    def test_lists_missing_codepoints(self):
        (self.site / "page.html").write_text("<math><mtext>🧐🚗</mtext></math>")
        with self.assertRaisesRegex(ValueError, "U\\+1F697.*U\\+1F9D0"):
            verify_math_font(self.site)


if __name__ == "__main__":
    unittest.main()

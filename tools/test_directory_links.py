"""Regression cases for link labels, contribution modules and offline review."""

import contextlib
import csv
import gzip
import hashlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from build import link_rows
from statement_index import BASE
from statement_links import AUTHOR, LINK_FIELDS, add_constant_matches, generated_links, refresh_ledger, summary
from check_links import capture, verify_receipt
from verify_directory import Main


class DirectoryLinks(unittest.TestCase):
    def test_empty_anchor_is_detected_inside_nested_markup(self):
        with tempfile.TemporaryDirectory() as folder:
            page = Path(folder) / "index.html"
            page.write_text('<a href="s/ant/1/0001/"><span> </span></a>')
            with self.assertRaisesRegex(ValueError, "Empty anchor text"):
                Main(page)
            page.write_text(
                '<a href="s/ant/1/0001/"><span>ANT.1.0001</span> · Title</a>'
            )
            self.assertEqual(
                Main(page).text_by_href["s/ant/1/0001/"], "ANT.1.0001 · Title"
            )

    def test_contributed_link_module_path_and_optional_label(self):
        with tempfile.TemporaryDirectory() as folder:
            ledger = Path(folder) / "links.tsv"
            ledger.write_text(
                "module\tauthor\turl\tlabel\nsrc/Main.lean\tExample\thttps://example.org/a/\t\n"
            )
            self.assertEqual(
                list(link_rows({"src/Main.lean": 12}, ledger)),
                [(12, "Example", "https://example.org/a/", "", "")],
            )
            with self.assertRaisesRegex(ValueError, "unknown module src/Main.lean"):
                list(link_rows({}, ledger))

    def test_official_map_retains_secondary_names_and_contributed_rows(self):
        url = BASE + "lean/Example.primary/"
        card = dict(card_id="one",kind="theorem",url=url,title="Example")
        old = [{**card,"url":BASE+"s/old/","declaration":"Old","module":"src/Old.lean"}]
        current = [{**card,"module":"src/New.lean","declaration":name}
                   for name in ("Example.primary","Example.secondary")]
        current.append({**card,"card_id":"two","url":BASE+"s/two/","module":"","declaration":"Unknown"})
        contributed = ("src/Contributed.lean","Outside writer","https://example.org/a","","Additional")
        ledger = [dict(zip(LINK_FIELDS,r)) for r in generated_links(old) | {contributed}]
        updated = refresh_ledger(ledger, old, current)
        self.assertEqual(set(updated), generated_links(current) | {contributed})
        counts = summary(current, updated)
        self.assertEqual((counts["statementDeclarationLinks"],counts["statementModuleLinks"],counts["unmatchedPages"]), (2,1,1))
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "links.tsv"
            with path.open("w",newline="") as f:
                csv.writer(f,delimiter="\t").writerows([LINK_FIELDS,*sorted(generated_links(current))])
            owners = {(1,"Example.primary"),(1,"Example.secondary")}
            self.assertEqual(len(list(link_rows({"src/New.lean":1},path,owners))),2)
            with self.assertRaisesRegex(ValueError, "Unknown declaration"):
                list(link_rows({"src/New.lean":2},path,owners))

    def test_constant_fallback_is_module_level_and_skips_already_linked_pages(self):
        def row(page, name, module=""):
            return dict(card_id=page, kind="definition", url=BASE+"lean/"+page+"/",
                        title=page, declaration=name, module=module)

        rows = [row("one", "A.B.x"), row("one", "A.B.y"), row("one", "M.z"),
                row("two", "A.d", "src/A.lean"), row("two", "M.z"),
                row("three", "A.B.shared"), row("three", "X.y")]
        fields = ("name", "origin", "module", "decl", "file", "aux_rule", "shared_aux")
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "constants.csv.gz"
            with gzip.open(path, "wt", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(fields)
                for field in ("x", "y", "shared"):
                    writer.writerow(("A.B."+field, "project", "A", "A.B", "src/A.lean",
                                     "nested", "true" if field == "shared" else "false"))
                writer.writerow(("M.z", "mathlib", "Mathlib.M", "", "", "", "false"))
            with patch("statement_links.CONSTANTS_SHA", hashlib.sha256(path.read_bytes()).hexdigest()):
                add_constant_matches(rows, path, {"A.B":"src/A.lean"})
        links = generated_links(rows)
        self.assertEqual({(r[0], r[3]) for r in links},
                         {("src/A.lean", ""), ("Mathlib/M.lean", ""), ("src/A.lean", "A.d")})
        self.assertEqual({r["declaration"] for r in rows if r.get("constant_owner")}, {"A.B.x", "A.B.y"})
        counts = summary(rows, links)
        self.assertEqual((counts["pagesMatchedByConstant"], counts["constantModuleLinks"],
                          counts["unmatchedPages"]), (1, 2, 1))

    def test_new_link_in_fork_pr_can_wait_for_trusted_check(self):
        old, new = "https://example.org/a", "https://example.org/b"
        with (
            patch("check_links.request", return_value=(200, b"")),
            contextlib.redirect_stderr(io.StringIO()),
        ):
            snapshot = capture({old})
            with self.assertRaises(ValueError):
                verify_receipt(snapshot, {old, new})
            projected = verify_receipt(snapshot, {old, new}, review=True)
        self.assertEqual(projected["checkedURLs"], 1)
        self.assertEqual(
            projected["unverified"],
            [{"url": new, "reason": "pending trusted live build"}],
        )


if __name__ == "__main__":
    unittest.main()

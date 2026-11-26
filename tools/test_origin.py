"""Check publication rights at intake, in file history and in both mirror formats."""
from contextlib import chdir
import hashlib
import json
from pathlib import Path
import sqlite3
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from check_informalization_pr import InvalidInformalization, PUBLIC_MAX_BYTES, PUBLIC_MAX_DECLARATIONS, parse_note
from mirror_projection import populate_board
from mirrors import stage
from parquet import export, read_rows
from submission_order import submission_order
from tables import ordered_tables, row_digest


ROOT = Path(__file__).resolve().parents[1]


class OriginTests(unittest.TestCase):
    def test_public_limits_apply_to_utf8_bytes_and_declaration_count(self):
        meta = dict(module="src/M.lean", author="handle", declarations=[],
                    writer="Writer", origin="wrote", license="CC-BY-4.0", source_commit="0" * 40)

        def entry(body="Short."):
            return ("---\n" + json.dumps(meta) + "\n---\n" + body).encode()

        oversized = entry("λ" * (PUBLIC_MAX_BYTES // 2))
        with self.assertRaisesRegex(InvalidInformalization, "bytes"):
            parse_note(oversized)
        self.assertEqual(parse_note(oversized, maintainer=True)["writer"], "Writer")
        meta["declarations"] = ["n"] * (PUBLIC_MAX_DECLARATIONS + 1)
        with self.assertRaisesRegex(InvalidInformalization, "declarations"):
            parse_note(entry())
        self.assertEqual(parse_note(entry(), maintainer=True)["declarations"], meta["declarations"])

    def test_html_limit_counts_utf8_bytes_of_final_fragment(self):
        meta = dict(module="src/M.lean", author="handle", declarations=[], writer="Writer",
                    origin="wrote", license="CC-BY-4.0", source_commit="0" * 40)
        content = ("---\n" + json.dumps(meta) + "\n---\nλ").encode()
        size = len("<p>λ</p>\n".encode())
        with patch("check_informalization_pr.MAX_RENDERED_BYTES", size):
            self.assertEqual(parse_note(content)["module"], "src/M.lean")
        with patch("check_informalization_pr.MAX_RENDERED_BYTES", size - 1):
            with self.assertRaisesRegex(InvalidInformalization, f"rendered HTML is {size} UTF-8 bytes"):
                parse_note(content)

    def test_renderer_failure_outside_a_formula_is_a_clean_rejection(self):
        meta = dict(module="src/M.lean", author="handle", declarations=[], writer="Writer",
                    origin="wrote", license="CC-BY-4.0", source_commit="0" * 40)
        note = ("---\n" + json.dumps(meta) + "\n---\nText.").encode()
        with patch("check_informalization_pr.render_informalization", side_effect=RuntimeError("render failed")):
            with self.assertRaisesRegex(InvalidInformalization, "render failed"):
                parse_note(note)

    def test_parser_errors_are_rejections(self):
        for content, reason in [(b"\xff", "UTF-8"), (b"---\nvalue: 2000-02-31\n---\nBody", "invalid YAML")]:
            with self.subTest(reason=reason), self.assertRaisesRegex(InvalidInformalization, reason):
                parse_note(content)

    def test_permission_requires_maintainer_source_and_actual_writer(self):
        payload = dict(module="src/Main.lean", declarations=[], author="handle", writer="Example Writer",
                       source_commit="0"*40, origin="other-author", source="https://example.org/statement",
                       license="with-permission")
        def read(meta, maintainer):
            return parse_note(("---\n" + json.dumps(meta) + "\n---\nText.").encode(), maintainer=maintainer)

        self.assertIsNone(read(payload, True)["kind"])
        with self.assertRaises(InvalidInformalization):
            read(payload, False)
        for invalid in ({**payload,"source":""}, {**payload,"writer":""}, {**payload,"origin":"wrote"}):
            with self.assertRaises(InvalidInformalization):
                read(invalid, True)
        for origin, kind in [("wrote","human"), ("generated","ai"), ("other-author",None)]:
            fields = dict(license_source="https://example.org/terms",copyright="none in the source",
                          changes="none",notice="") if origin=="other-author" else {}
            self.assertEqual(read({**payload,"origin":origin,"license":"CC-BY-4.0",**fields},False)["kind"],kind)

    def test_open_imports_require_maintainer_origin_source_and_attribution(self):
        for license in ("Apache-2.0", "MIT", "CC0-1.0"):
            meta = dict(module="A.lean", declarations=[], author="dial481", writer="Author",
                        origin="other-author", source_commit="a"*40, source="https://example.org/A",
                        license=license, copyright="Copyright the upstream authors")
            def check(data, maintainer=True):
                return parse_note(("---\n"+json.dumps(data)+"\n---\nBody").encode(), maintainer=maintainer)
            self.assertIsNone(check(meta)["kind"])
            with self.assertRaises(InvalidInformalization):
                check(meta, False)
            for invalid in ({**meta, "origin":"wrote"}, {k:v for k,v in meta.items() if k!="source"}):
                with self.assertRaises(InvalidInformalization):
                    check(invalid)
            no_credit = {k:v for k,v in meta.items() if k!="copyright"}
            if license == "CC0-1.0":
                self.assertIsNone(check(no_credit)["kind"])
            else:
                with self.assertRaises(InvalidInformalization):
                    check(no_credit)

    def test_arrival_order_survives_edits_and_rename(self):
        with tempfile.TemporaryDirectory() as tmp, chdir(tmp):
            self.git("init","-q")
            folder = Path("notes")
            folder.mkdir()
            (folder/"z").write_text("original\n")
            self.commit()
            (folder/"a").write_text("second\n")
            self.commit()
            (folder/"z").rename(folder/"renamed")
            self.commit()
            (folder/"renamed").write_text("edited\n")
            self.commit()
            self.assertEqual(submission_order(folder), {"notes/renamed":1, "notes/a":2})

            new = Path("packages/example/informalizations")
            new.parent.mkdir(parents=True)
            folder.rename(new)
            self.commit()
            self.assertEqual(submission_order(new, previous=(folder,)), {
                str(new / "renamed"): 1, str(new / "a"): 2})

    def test_initial_public_order_precedes_later_contributions(self):
        with tempfile.TemporaryDirectory() as tmp, chdir(tmp):
            self.git("init", "-q")
            first = Path("packages/p/informalizations/X.lean/a.md")
            first.parent.mkdir(parents=True)
            first.write_text("first")
            Path("tools").mkdir()
            Path("tools/initial-ledger-order.json").write_text(json.dumps({
                "pathListSha256": hashlib.sha256((first.as_posix() + "\n").encode()).hexdigest(),
                "runs": [[1, 31]],
            }))
            self.commit()
            second = first.with_name("b.md")
            second.write_text("second")
            self.commit()
            self.assertEqual(submission_order(Path("packages")), {str(first): 31, str(second): 32})

    @staticmethod
    def git(*args):
        return subprocess.check_output(["git","-c","user.name=dial481","-c",
            "user.email=248182468+dial481@users.noreply.github.com",*args], text=True).strip()

    def commit(self):
        self.git("add","-A")
        self.git("commit","-qm","Record fixture")

    def test_permission_text_is_absent_from_parquet_and_sqlite_release(self):
        sentinel = "Fixture material reserved for site display"
        with tempfile.TemporaryDirectory() as tmp, chdir(tmp):
            dbpath = Path("site.sqlite3")
            with sqlite3.connect(dbpath) as db:
                db.executescript((ROOT/"tools/schema.sql").read_text())
                db.executemany("INSERT INTO modules(id,path,project,mask,trace_reached,package) VALUES(?,?,1,1,1,'riemann-hypothesis')",
                               [(1,"src/A.lean"),(2,"src/B.lean")])
                for mid, licence, origin, text in [(1,"CC-BY-4.0","wrote","Public example"),(2,"with-permission","other-author",sentinel)]:
                    db.execute("""INSERT INTO informalizations(module,author,writer,kind,origin,submitted_order,license,
                        source_commit,declarations_json,source_url,body,informalization_html)
                        VALUES(?,'example','Writer','human',?,1,?,'proof','[]','https://example.org/source',?,?)""",
                               (mid,origin,licence,text,text))
                db.execute("""INSERT INTO informalizations(module,author,writer,origin,submitted_order,license,
                    source_commit,declarations_json,source_url,body,informalization_html,copyright)
                    VALUES(1,'owner','Upstream','other-author',2,'Apache-2.0','proof','[]','https://example.org',
                           'Imported example','Imported example','Copyright Example')""")
                populate_board(db)
                db.executemany("INSERT INTO summary VALUES(?,?)",[("informalizations",3),("most_wanted",0)])
                content = {name:row_digest([col[0] for col in cursor.description],cursor)
                           for name,_,cursor in ordered_tables(db)}
            manifest = {"databaseSha256":hashlib.sha256(dbpath.read_bytes()).hexdigest(),"tableContent":content}
            ref = Path("reference.json")
            ref.write_text(json.dumps(manifest))
            for file in ["proofs/rh/proof.yml","proofs/rh/seed-license.txt","LICENSE"]:
                target = Path(file)
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes((ROOT/file).read_bytes())
            for source in ROOT.glob("packages/*/source.yml"):
                dest = source.relative_to(ROOT)
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_bytes(source.read_bytes())
            from shutil import copytree
            copytree(ROOT/"LICENSES","LICENSES")
            notice = Path("packages/fixture/NOTICE")
            notice.parent.mkdir(parents=True)
            notice.write_text("Upstream attribution.\n")
            self.git("init","-q")
            self.commit()
            export(dbpath,manifest,Path("parquet"))
            result = stage(dbpath,ref.resolve(),Path("parquet"),Path("mirrors"),self.git("rev-parse","HEAD"))
            self.assertEqual(result["permissionRowsExcluded"],1)
            asset = Path("mirrors/release",result["sqliteAsset"])
            self.assertNotIn(sentinel.encode(),asset.read_bytes())
            with sqlite3.connect(asset) as db:
                self.assertEqual(list(db.execute("SELECT body FROM informalizations ORDER BY id")),[("Public example",),("Imported example",)])
                self.assertEqual(list(db.execute("SELECT module FROM most_wanted")),[(2,)])
            rows = list(read_rows(Path("mirrors/huggingface/data/informalizations.parquet")))
            self.assertEqual(len(rows),2)
            self.assertIn("Apache-2.0",rows[1])
            self.assertIn("Copyright Example",rows[1])
            for directory in [Path("mirrors/huggingface"),Path("mirrors/release")]:
                for license in ("Apache-2.0","CC-BY-4.0","MIT"):
                    name = Path("LICENSES") / (license+".txt")
                    self.assertEqual((directory/name).read_bytes(),name.read_bytes())
                self.assertEqual((directory/notice).read_bytes(),notice.read_bytes())
            self.assertIn("Public example",rows[0])
            self.assertNotIn(sentinel,rows[0])
            with sqlite3.connect(dbpath) as db:
                self.assertEqual(db.execute("SELECT body FROM informalizations WHERE license='with-permission'").fetchone()[0],sentinel)


if __name__ == "__main__":
    unittest.main()

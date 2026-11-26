"""Disambiguate identically named records and retain the order of ledger contributions."""
import json
import sqlite3
import unittest
from pathlib import Path

from fixtures import parameters


class PackageIdentity(unittest.TestCase):
    def test_overlapping_module_and_declaration_names(self):
        queries = json.loads(Path("site/queries.json").read_text())
        with sqlite3.connect(":memory:") as db:
            db.executescript(Path("tools/schema.sql").read_text())
            for i, package in enumerate(("one", "two"), 1):
                db.execute("INSERT INTO modules(id,path,package,project,mask,trace_reached) VALUES(?,?,?,?,?,?)",
                           (i, "A.lean", package, 1, 1, 1))
                db.execute("INSERT INTO declarations VALUES(?,?,?,?,?,?,?,?)", (i,i,"X.same",1,1,"def",1,package))
                db.executemany("INSERT INTO shortnames VALUES(?,?,?,?,?)",
                               [("a","A","module",i,package),("same","X.same","declaration",i,package)])
                db.execute("INSERT INTO links VALUES(?,?,?,?,?)", (i,package,"https://example.org/"+package,package,"X.same"))
            for package in ("one","two","missing"):
                args = parameters("module","A.lean",0,package)
                facts = db.execute(queries["module"]["facts"],args).fetchall()
                args = parameters("declaration","X.same",0,package)
                decls = db.execute(queries["declaration"]["declarations"],args).fetchall()
                links = db.execute(queries["declaration"]["outside"],args).fetchall()
                expected = [] if package=="missing" else [package]
                self.assertEqual([r[1] for r in facts],expected)
                self.assertEqual([r[0] for r in decls],expected)
                self.assertEqual([r[0] for r in links],expected)

    def test_original_and_readable_proofs_share_a_theorem_name(self):
        queries = json.loads(Path("site/queries.json").read_text())
        with sqlite3.connect(":memory:") as db:
            db.executescript(Path("tools/schema.sql").read_text())
            for source in ("riemann-hypothesis", "grh-readable"):
                db.execute("INSERT INTO proofs(id, source, title) VALUES(?,?,?)", (source,source,source))
                db.execute("INSERT INTO proof_names VALUES(?,?,?)", ("riemannhypothesis",source,"riemannHypothesis"))
            hits = db.execute(queries["typeahead"]["proofs"], ("riemannhypothesis",)).fetchall()
            self.assertEqual([hit[-1] for hit in hits], ["riemann-hypothesis","grh-readable"])

    def test_private_and_same_short_names_round_trip(self):
        queries = json.loads(Path("site/queries.json").read_text())
        with sqlite3.connect(":memory:") as db:
            db.executescript(Path("tools/schema.sql").read_text())
            db.execute("INSERT INTO modules(id,path,package,project,mask,trace_reached) VALUES(1,'Mathlib/A.lean','mathlib',0,0,0)")
            names = ("Left.x", "Right.x", "_private.Mathlib.A.0.Hidden.x")
            for i, name in enumerate(names, 1):
                db.execute("INSERT INTO declarations VALUES(?,1,?,1,1,'def',0,'mathlib')", (i,name))
                db.execute("INSERT INTO shortnames VALUES('x',?,'declaration',?,'mathlib')", (name,i))
                args = parameters("declaration",name,0,"mathlib")
                rows = db.execute(queries["declaration"]["declarations"],args).fetchall()
                self.assertEqual([r[1] for r in rows], [name])

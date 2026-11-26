import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from prerender import proof_index_rows
from source_registry import distinct_spellings, populate_proofs


class SourceRegistryTests(unittest.TestCase):
    def test_contributions_include_role_modules_once(self):
        with sqlite3.connect(":memory:") as db:
            db.row_factory = sqlite3.Row
            db.executescript("""
                CREATE TABLE proofs(id, source, title);
                CREATE TABLE proof_modules(proof, module);
                CREATE TABLE proof_roles(proof, module, role);
                CREATE TABLE informalizations(module, entry_type, license);
                INSERT INTO proofs VALUES('matrix','example','Matrix');
                INSERT INTO proof_modules VALUES('matrix',1);
                INSERT INTO proof_roles VALUES('matrix',1,'solution'),('matrix',2,'statement'),('matrix',2,'solution');
                INSERT INTO informalizations VALUES
                    (1,'informalization','CC-BY-4.0'),(2,'informalization','CC-BY-4.0'),
                    (2,'informalization','MIT'),(2,'informalization','with-permission'),
                    (2,'source-documentation','Apache-2.0');
            """)
            self.assertEqual(proof_index_rows(db), [dict(id='matrix', source='example',
                                                          modules=1, documented=0, contributed=3)])

    def test_rejects_case_only_conflicts(self):
        for values in (["s/VP", "s/vp"], ["A/File.lean", "a/file.lean"]):
            with self.assertRaisesRegex(ValueError, "case-only"):
                distinct_spellings(values, "fixture")

    def test_shared_module_separate_sources_and_external_statement(self):
        with tempfile.TemporaryDirectory() as tmp, sqlite3.connect(":memory:") as db:
            db.executescript(Path("tools/schema.sql").read_text())
            sources = {}
            modules = ["A/X.lean", "B/X.lean", "Statement.lean", "Wrapper.lean"]
            for source in ("one", "two", "empty"):
                for path in modules:
                    db.execute("INSERT INTO modules(package,path,project) VALUES(?,?,1)", (source,path))
                for challenge in ("A","B"):
                    db.execute("INSERT INTO modules(package,path,project) VALUES(?,?,1)", (source,"ComparatorChallenges/"+challenge+".lean"))
                sources[source] = {"proofFiles": []}
                for challenge in (["A", "B"] if source == "one" else ["A"] if source == "two" else []):
                    folder = Path(tmp)/source/challenge
                    folder.mkdir(parents=True)
                    (folder/"config.json").write_text(json.dumps({"challenge_module":"ComparatorChallenges."+challenge,
                                                                "solution_module":"Wrapper","theorem_names":["Example.root"]}))
                    members = folder/"modules.txt"
                    members.write_text("A/X.lean\nB/X.lean\n")
                    record = folder/"proof.yml"
                    record.write_text(json.dumps(dict(id=source+"/"+challenge, title=challenge, members=str(members),root=modules[0],
                        declaration="Example.root",statement="ComparatorChallenges/"+challenge+".lean",solution=modules[3],artifacts=str(folder))))
                    sources[source]["proofFiles"].append(str(record))
            populate_proofs(db,sources)
            self.assertEqual(db.execute("SELECT count(*) FROM proof_modules").fetchone()[0],6)
            self.assertEqual(db.execute("SELECT count(*) FROM proof_modules pm JOIN modules m ON m.id=pm.module WHERE m.package='one' AND m.path='A/X.lean'").fetchone()[0],2)
            self.assertEqual(db.execute("SELECT count(*) FROM proof_modules pm JOIN proofs p ON p.statement_module=pm.module OR p.solution_module=pm.module").fetchone()[0],0)

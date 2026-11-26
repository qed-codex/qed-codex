import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from trail_pieces import NODES_PER_PIECE, write_trails


class TrailPieceTests(unittest.TestCase):
    def test_piece_contains_full_ancestry_and_unindexed_callers(self):
        with sqlite3.connect(":memory:") as db, tempfile.TemporaryDirectory() as tmp:
            db.executescript(Path("tools/schema.sql").read_text())
            db.execute("INSERT INTO modules(id,package,path,project) VALUES(1,'source','A.lean',1)")
            db.execute("INSERT INTO declarations(id,module,package,name,kind,kernel_mask) VALUES(7,1,'source','a.b','theorem',1)")
            leaf = NODES_PER_PIECE+1
            db.executemany("INSERT INTO trace VALUES(?,1,3,?,?,?,4)",
                           [(1,None,"root",None),(2,None,"helper",1),(leaf,7,None,2)])
            folder = Path(tmp)/"trails"
            write_trails(db,folder,Path.write_bytes)
            rows = json.loads((folder/"1").read_text())
            self.assertEqual(rows[str(leaf)],[2,"source","A.lean",3,4,1,"a.b"])
            self.assertEqual(rows["2"],[1,"source","A.lean",3,4,0,"helper"])
            self.assertEqual(rows["1"],[None,"source","A.lean",3,4,0,"root"])

    def test_verifier_rejects_a_changed_packed_ancestor(self):
        from verify import verify_trail_sample
        from package import store_gzip

        with sqlite3.connect(":memory:") as db, tempfile.TemporaryDirectory() as tmp:
            db.executescript(Path("tools/schema.sql").read_text())
            db.execute("INSERT INTO modules(id,package,path,project) VALUES(1,'s','A.lean',1)")
            db.execute("INSERT INTO declarations(id,module,package,name,kind,kernel_mask) VALUES(1,1,'s','x','def',0)")
            db.executemany("INSERT INTO trace VALUES(?,1,3,?,?,?,4)",
                           [(1,None,"ancestor",None), (2,1,None,1)])
            folder = Path(tmp) / "trails"
            write_trails(db, folder, store_gzip)
            self.assertEqual(verify_trail_sample(db, folder), 1)
            import gzip
            packed = json.loads(gzip.decompress((folder / "0").read_bytes()))
            packed["1"][3] += 1
            store_gzip(folder / "0", json.dumps(packed).encode())
            with self.assertRaisesRegex(ValueError, "target 2, node 1"):
                verify_trail_sample(db, folder)

"""Check GitHub issue-form ingestion without creating issues."""
import io
import json
import unittest
import sqlite3
from contextlib import redirect_stderr
from unittest.mock import patch

import disputes


class Ingestion(unittest.TestCase):
    def test_filters_paginates_and_maps(self):
        def issue(n, **overrides):
            return dict({"number": n, "state": "open", "labels": [{"name": "dispute"}],
                         "body": "### Package and module path\r\n\r\n`riemann-hypothesis:src/Main.lean`\r\n\r\n### Claim and evidence"}, **overrides)
        first = [issue(i, pull_request={}) for i in range(1, 100)] + [issue(100)]
        second = [issue(101, state="closed"), issue(102, labels=[{"name":"module-problem"}]), issue(103)]
        pages = [io.BytesIO(json.dumps(batch).encode()) for batch in (first, second)]
        with patch("urllib.request.urlopen", side_effect=pages) as fetch:
            loaded = disputes.snapshot({"riemann-hypothesis:src/Main.lean"})
            self.assertEqual(fetch.call_count, 2)
        self.assertEqual([r[0] for r in disputes.rows(loaded, {"riemann-hypothesis:src/Main.lean": 42})], [100, 103])
        with self.assertRaises(ValueError):
            list(disputes.rows(loaded, {}))

    def test_live_skips_bad_paths_and_reports_each_issue(self):
        bodies = ["No form", "### Package and module path\n\n`../riemann-hypothesis:src/Main.lean`", "### Package and module path\n\nriemann-hypothesis:src/Removed.lean",
                  "### Package and module path\n\nriemann-hypothesis:src/Main.lean"]
        batch = [{"state": "open", "labels": [{"name": "dispute"}], "number": i, "body": body}
                 for i, body in enumerate(bodies, 1)]
        with patch("urllib.request.urlopen", return_value=io.BytesIO(json.dumps(batch).encode())):
            snapshot = disputes.snapshot({"riemann-hypothesis:src/Main.lean"})
        with sqlite3.connect(":memory:") as db, redirect_stderr(io.StringIO()) as log:
            db.execute("CREATE TABLE disputes(number INTEGER, module INTEGER, url TEXT)")
            disputes.store(db, snapshot, {"riemann-hypothesis:src/Main.lean": 42})
            self.assertEqual(db.execute("SELECT number,module FROM disputes").fetchall(), [(4, 42)])
            expected = ["missing module path", "malformed module path", "unknown module path"]
            self.assertEqual(disputes.manifest_fields(db)["skippedDisputes"],
                             [{"number": i, "reason": reason} for i, reason in enumerate(expected, 1)])
            for i, reason in enumerate(expected, 1):
                self.assertIn(f"Skipped dispute #{i}: {reason}", log.getvalue())

    def test_frozen_snapshot_rejects_bad_paths(self):
        with sqlite3.connect(":memory:") as db:
            db.execute("CREATE TABLE disputes(number INTEGER, module INTEGER, url TEXT)")
            for path in ["", "../riemann-hypothesis:src/Main.lean", "riemann-hypothesis:src/Removed.lean"]:
                with self.subTest(path=path), self.assertRaisesRegex(ValueError, "Invalid or duplicate dispute"):
                    disputes.store(db, {"repository": disputes.REPO, "label": disputes.LABEL,
                                        "issues": [{"number": 1, "module": path}]}, {"riemann-hypothesis:src/Main.lean": 42})
            self.assertEqual(db.execute("SELECT * FROM disputes").fetchall(), [])
            self.assertEqual(disputes.manifest_fields(db), {})


if __name__ == "__main__":
    unittest.main()

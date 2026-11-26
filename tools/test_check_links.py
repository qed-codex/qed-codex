"""Exercise responses and atlas routes without contacting publishers."""

import contextlib
import io
import unittest
import urllib.error
from unittest.mock import patch

from check_links import ATLAS, capture, inspect, verify_receipt


class OutsideLinks(unittest.TestCase):
    def test_fragment_routes_share_one_request(self):
        urls = {ATLAS + "#n-good", ATLAS + "#n-removed"}
        model = b'<script type="application/json" id="atlas-data">{"nodes":[{"id":"good"}]}</script>'
        with patch("check_links.request", return_value=(200, model)) as request:
            receipt = capture(urls)
        request.assert_called_once_with(ATLAS, "GET")
        self.assertEqual(
            receipt["dead"],
            [{"url": ATLAS + "#n-removed", "reason": "missing atlas node"}],
        )
        with contextlib.redirect_stderr(io.StringIO()) as log:
            self.assertIs(verify_receipt(receipt, urls), receipt)
        self.assertIn(ATLAS + "#n-removed", log.getvalue())
        with self.assertRaisesRegex(ValueError, "differs"):
            verify_receipt(receipt, {ATLAS + "#n-good"})

    def test_unstarted_requests_remain_unverified_at_deadline(self):
        url = "https://example.org/statement/"
        with patch("check_links.request") as request:
            receipt = capture({url}, budget_seconds=0)
        request.assert_not_called()
        self.assertEqual(receipt["dead"], [])
        self.assertEqual(
            receipt["unverified"],
            [{"url": url, "reason": "link-check time budget reached"}],
        )

    def test_http_errors_distinguish_dead_and_unverified(self):
        url = "https://example.org/statement/"
        for status, outcome in [(404, "dead"), (410, "dead"), (403, "unverified")]:
            with (
                self.subTest(status=status),
                patch(
                    "check_links.request",
                    side_effect=urllib.error.HTTPError(url, status, "", {}, None),
                ),
            ):
                self.assertEqual(
                    inspect((url, [(url, "")])), [(url, outcome, str(status))]
                )
        error = urllib.error.HTTPError(url, 405, "", {}, None)
        with (
            patch("check_links.request", side_effect=[error, (200, b"ok")]) as fetch,
            patch("check_links.time.sleep"),
        ):
            self.assertEqual(inspect((url, [(url, "")])), [(url, "ok", "")])
        self.assertEqual([c.args[1] for c in fetch.call_args_list], ["HEAD", "GET"])


if __name__ == "__main__":
    unittest.main()

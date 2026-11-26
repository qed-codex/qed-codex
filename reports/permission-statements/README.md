# Andrew O’Desky’s statements

The directory displays Andrew O’Desky’s statements with his permission. The 26 November 2026 capture contains 2,029 pages. The official Lean map places 2,012 statements on 2,178 module pages, with 2,508 distinct statement-to-module links. Sixteen theorems and one definition have no matched module. The SQLite and Parquet mirrors exclude the permission-only entries. [Statements](https://andrewodesky.com/rh/) · [Page-by-page results](pages.tsv) · [Map and match counts](../../proofs/rh/sources/odesky/counts.json)

The capture fetched the two indexes and 88 card chunks sequentially with a pause between requests. The receipt records the time, address, size and SHA-256 of each response. Each entry displays the capture date and preserves the order of its statements. Cross-references use the title visible in the source’s default view. [Capture receipt](card-capture.json) · [Official map](../../proofs/rh/sources/odesky/lean-map.tsv)

## Replay the capture

From the repository root, use the recorded responses or fetch them in a fresh cache. The importer compares their hashes with the reviewed receipt. For a refresh, review the new receipt and the statement-to-module mapping before replacing the snapshot.

```sh
export LC_ALL=C
cards=inputs/permission-cards-nov26
.venv/bin/python tools/capture_statement_cards.py "$cards"
.venv/bin/python tools/import_permission_statements.py "$cards" --packages build/statement-replay --report build/statement-report
diff -u reports/permission-statements/pages.tsv build/statement-report/pages.tsv
```

The importer converts each statement to Markdown and renders its formulas. The earlier 24 November comparison also checked 30 pages against their live counterparts at 380 and 1280 px. [Sample](live-sample.json) · [Rendered comparisons](visual-checks.json) · [Glyph checks](sample-glyphs.json) · [Screenshots](screenshots/)

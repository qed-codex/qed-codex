# Staging page review

The local Pages preview contains 2,000 HTML pages with 2,000 distinct titles. The preceding build had 16 repeated titles across 42 pages. Record titles now include the original module path or qualified declaration name. The visible heading keeps the shorter identifier. [Package inventory](directory.json)

The home page and record source links name Levent Alpöge and link to the original proof revision. The kernel-mask credit links James Shore’s v0.2.1 dataset and Andrew Sutherland’s export. Shore identifies the export as the source of the used declarations and gives the digest of the input he used. [Original source](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005) · [Shore’s pinned input record](https://github.com/james-shore/rh-proof-dependencies/blob/v0.2.1/README.md#inputs) · [Sutherland’s kernel export](https://math.mit.edu/~drew/grh/)

Each page has a description, Open Graph title and description, and a footer linking the repository, contribution guide, both licenses and credits. The unmatched page lists 92 definition pages. Sibling declarations now label their theorem-use summary “Used by.”

## Browser results

Chromium, Firefox and WebKit passed the 14 native SQLite fixtures cold, warm and on immediate repeat, for 126 comparisons. Repeat queries fetched zero database files. The seven sample pages passed in each engine, including the source slices, source fallback, module and declaration links, layout, and contribution prefill. The directory and board checks passed in all three. [Browser results](browser.json) · [Fixture file counts](fixture-files.json)

The SQL console test adds 50 ms to every numbered database-page request. In all three engines, the indexed lookup `SELECT value FROM summary WHERE metric = 'modules'` returned **184,039**. A separate `SELECT count(*) FROM modules` ran into the 30-second limit. The query plan scans the unique path index. Its 599 database pages comprise 595 leaf pages and four interior pages at 32,768 bytes each. The message explains the network reads and points to `summary` and indexed filters. Other console checks, including cancellation and a subsequent lookup, passed. [Console regression test](../../tools/test-console.mjs)

## Unknown addresses

| Request | HTTP status | Visible result in all three browsers |
| --- | ---: | --- |
| `/qed-unlisted-test-path/` | 200 | “Search the proof” home page at the requested address |
| `/m/?p=src%2FQEDUnknownModule.lean` | 200 | “Module not found” and a link to search |
| `/d/?n=QED.UnknownDeclaration` | 200 | “Declaration not found” and a link to search |

The first response is the Pages fallback to the root document. Module and declaration lookups run in the browser after Pages serves their query-string templates. These are measurements of the local Wrangler preview.

## Build modes

| Local package | HTML pages | Files | Bytes | Sitemap URLs |
| --- | ---: | ---: | ---: | ---: |
| Preview with `--preview-probe` | 2,000 | 11,850 | 116,062,322 | 0 |
| Production rehearsal with `--base-url https://example.invalid` | 1,999 | 11,850 | 116,725,366 | 1,997 |

In the preview, `/probe.html` redirects to `/probe`, which returns the database test page. Both responses carry `X-Robots-Tag: noindex`, and the HTML also declares `noindex`. Production packaging excludes that page and its test client. Supplying the production origin emits absolute canonical links, the logo for social previews, and a sitemap of concrete pre-rendered URLs. The two generic record templates serve many query-string addresses and are excluded from the sitemap. A crawler requesting a generic template gets its generic metadata. A concrete pre-rendered URL identifies the record in the initial HTML.

Two preview packages reproduced the same full manifest. Relative to the declaration-address refresh, the deployment byte total and tree hash changed. The SQLite file, logical table digests and indexed site query plans match the preceding manifest. [Build manifest](manifest.json)

## Reproduce

Build the pinned database and the local preview using the [README commands](../../README.md#reproduce-the-database-and-local-preview). With the preview listening on loopback, run the following commands from the repository root.

```bash
export LC_ALL=C
origin=http://127.0.0.1:18741
node tools/gate3-evidence.mjs "$origin" inputs/fixtures.json inputs/page-review all
node tools/test-directory.mjs "$origin"
node tools/test-console.mjs "$origin"
.venv/bin/python tools/verify_directory.py build/rh.sqlite3 build/preview
LD_LIBRARY_PATH="$PWD/inputs/sqlite/3.46.1" .venv/bin/python tools/package.py build/rh.sqlite3 build/metadata-review --base-url https://example.invalid
.venv/bin/python tools/verify_directory.py build/rh.sqlite3 build/metadata-review
```

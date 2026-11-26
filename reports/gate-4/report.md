# Gate 4 · local review

The static package contains **2,047 qualifying module pages** and uses **11,903 of 20,000 file slots**, leaving **8,097**. These counts use the pinned SQLite 3.46.1 build and the frozen dispute snapshot. Other SQLite versions can change the physical size while preserving the ordered table contents. [Directory recount](directory.json) · [Package manifest](manifest.json)

| Measure | Count |
| --- | ---: |
| Modules with an informalization | 1 |
| Modules with at least one outside link | 1,888 |
| Modules with a spine rank | 200 |
| Distinct modules meeting any criterion | 2,047 |
| Standalone module pages including the additional BuildAid/D1 sample | 2,048 |
| HTML files including routes, declarations, board, console and probe | 2,057 |
| SQLite database pages at 32 KiB | 9,823 |
| Complete package | 113,228,229 bytes |

The compiler selects the union of the three criteria by module ID. Original query-string links open a compiled page for those modules; other module links go through indexed SQLite lookup. The verifier independently checks every qualifying page and its pinned source link. In three browsers a non-sample module and the opening board page both displayed with zero numbered database page reads. [Recount script](../../tools/verify_directory.py) · [Browser evidence](browser.json)

Declaration pages link each sibling name to its own record. Kernel use is summarized as “all five”, “none”, or the names of the matching theorems. Wrapped trail names keep their source and use links on the closing line.

The physical package figures above describe the original Gate 4 revision. The screenshots and browser checks use the terminology from the private launch review.

## Most-wanted informalizations

The board contains 146,283 project modules used by RH that have no contributed informalization. All have measured cuts. The 199 spine modules lead in ascending spine rank, starting with GaloisRepresentationsOfThetaLift.lean at rank 2. RowSrc at rank 1 already has an informalization. The remaining 146,084 modules follow in descending cut order, with original path breaking ties. Each page uses primary-key lookups, including the final page starting at 146,251. Kernel membership comes from James Shore’s data. [Query plans](manifest.json) · [Shore v0.2.1](https://github.com/james-shore/rh-proof-dependencies/releases/tag/v0.2.1)

Full-page screenshots show all 50 board entries and the console after a query for Main.lean.

| View | 1280 px light | 1280 px dark | 380 px light | 380 px dark |
| --- | --- | --- | --- | --- |
| Board | [PNG](screenshots/wanted-1280-light.png) | [PNG](screenshots/wanted-1280-dark.png) | [PNG](screenshots/wanted-380-light.png) | [PNG](screenshots/wanted-380-dark.png) |
| SQL console | [PNG](screenshots/sql-1280-light.png) | [PNG](screenshots/sql-1280-dark.png) | [PNG](screenshots/sql-380-light.png) | [PNG](screenshots/sql-380-dark.png) |

## SQL and contributions

The console at `/sql/` opens the packaged SQLite file read-only. Shared links put the SQL in the URL fragment and wait for the reader to run it. Chromium, Firefox and WebKit checked the indexed examples, FTS5, a window query, result limits, cancellation, reopening the connection and rejection of writes and attachment requests. The fourteen baseline fixtures also passed in all three cache states across all three browsers. [Console replay](../../tools/test-console.mjs) · [Local browser evidence](browser.json) · [Fixture file counts](fixture-files.json)

The contributed-informalization checker accepted seven valid informalization changes and rejected seventeen invalid changes, including wrong declaration ownership, a missing license and changes to another handle’s file. One code-only fixture went to ordinary code review. The GitHub workflow was exercised through its local validator; its hosted status job starts when the workflow lands on the default branch. [Cases and replay](informalization-checks.md)

## Disputes and mirrors

The live snapshot on 2026-11-23 contained zero open GitHub issues labelled `dispute`. The compiler pages through the issue list, reads the original module path from the issue form and inserts issue IDs, module IDs and links. The current form applies `module-problem`. A maintainer reviews the issue and adds `dispute` to include it in the build. Live ingestion logs and skips missing, malformed or unknown paths. A frozen snapshot with an invalid issue fails validation. The ingestion fixtures cover all three path errors, pagination, closed issues and pull requests. [Replay snapshot](../../proofs/rh/disputes.json) · [Ingestion tests](../../tools/test_disputes.py)

The mirror rehearsal stages one Hugging Face dataset configuration per Parquet table and a GitHub release asset containing the complete SQLite database. The staging tool checked the type and ordered content digest of all 11 Parquet configurations. The SQLite release asset is 321,880,064 bytes. Both staging directories include a file-hash manifest. [Mirror verification and reproduction](mirrors.md)

## Reproduce

Build and serve the package using the [README commands](../../README.md#reproduce-the-database-and-local-preview). The following checks run against the local files and preview. The package and Parquet manifests record both physical and logical hashes. [Parquet manifest](parquet.json)

```bash
export LC_ALL=C
.venv/bin/python tools/test_disputes.py
.venv/bin/python tools/test_informalization_pr.py build/rh.sqlite3 > inputs/informalization-checks.json
cmp reports/gate-4/informalization-checks.json inputs/informalization-checks.json
node tools/gate4-screenshots.mjs http://127.0.0.1:18741 inputs/gate4-screenshots
node tools/test-directory.mjs http://127.0.0.1:18741
node tools/test-console.mjs http://127.0.0.1:18741
```

At Gate 5, enabling discussion requires adding `https://giscus.app` to `script-src` for its loader and verifying the resulting policy in all three browsers.

Verify the review records with `(cd reports/gate-4 && sha256sum -c SHA256SUMS)`.

# Gate 3 · local directory review

The search home, three module pages and three declaration pages run against the pinned proof database. On the six sample records the browser displayed compiled HTML and read zero numbered database pages before interaction. The search home fetched the WASM engine and the interior bundle at idle. [Route checks](page-checks.json) · [Package manifest](manifest.json)

## Six records

| Record | What to check |
| --- | --- |
| `RowSrc.lean` | Import rank 688, cut 13,054 and spine rank 1. The informalization by `@dial481` links to its declaration. |
| `FrameLinearAlgebraFirst.lean` | Andrew O’Desky’s Slope inequality section links this module through the frame-codimension entry. [Statements of the Lean RH project](https://andrewodesky.com/rh/s/alg/5+/0115/) · [Pinned identifier join](https://github.com/qed-codex/riemann-hypothesis-rosetta/blob/d41bfe7e03a311b8340cbfcebbb3c5fc62ff3dd1/results/phase-2/odesky-entry-modules.tsv.gz) |
| `src/BuildAid/D1.lean` | Zero informalizations and zero outside links in the ledger. |
| `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` | The source slice starts at RowSrc line 6. Its trail has five sites. |
| `GlobalTheory.Mem.Top.Bl.anyGeometry` | A `def` at OverIx line 19. All five kernel bits are set. Its nine-site source trail ends at `riemannHypothesis`. The same file contains `geoOf` with mask 0. |
| `riemannHypothesis` | Main line 4 is the single site at the root of the source trace. |

James Shore supplied the kernel masks. The trail follows parent and calling-line pointers in Rosetta’s source trace. Each declaration has a pinned source link and a plain-text slice fetched from the pinned raw GitHub file. [Shore v0.2.1](https://github.com/james-shore/rh-proof-dependencies/releases/tag/v0.2.1) · [Original source](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005)

The updated home, RowSrc and slope screenshots show the unmatched-statements navigation and the credited outside-link labels. On the slope module the link reads “ALG.5+.0115 · Codimension bound from second moments”. The original compiler and Parquet manifests retain their measured schemas. [Current package hashes](../2026-11-23/manifest.json)

## Screenshots

| Page | 1280 px light | 1280 px dark | 380 px light | 380 px dark |
| --- | --- | --- | --- | --- |
| Search | [View](screenshots/home-1280-light.png) | [View](screenshots/home-1280-dark.png) | [View](screenshots/home-380-light.png) | [View](screenshots/home-380-dark.png) |
| RowSrc | [View](screenshots/rowsrc-1280-light.png) | [View](screenshots/rowsrc-1280-dark.png) | [View](screenshots/rowsrc-380-light.png) | [View](screenshots/rowsrc-380-dark.png) |
| Slope inequality module | [View](screenshots/slope-1280-light.png) | [View](screenshots/slope-1280-dark.png) | [View](screenshots/slope-380-light.png) | [View](screenshots/slope-380-dark.png) |
| BuildAid/D1 | [View](screenshots/d1-1280-light.png) | [View](screenshots/d1-1280-dark.png) | [View](screenshots/d1-380-light.png) | [View](screenshots/d1-380-dark.png) |
| Galois declaration | [View](screenshots/galois-1280-light.png) | [View](screenshots/galois-1280-dark.png) | [View](screenshots/galois-380-light.png) | [View](screenshots/galois-380-dark.png) |
| anyGeometry | [View](screenshots/anygeometry-1280-light.png) | [View](screenshots/anygeometry-1280-dark.png) | [View](screenshots/anygeometry-380-light.png) | [View](screenshots/anygeometry-380-dark.png) |
| riemannHypothesis | [View](screenshots/rh-1280-light.png) | [View](screenshots/rh-1280-dark.png) | [View](screenshots/rh-380-light.png) | [View](screenshots/rh-380-dark.png) |

The 28 Chromium captures show each complete page through its footer. The screenshot inventory records dimensions and SHA-256 for each PNG. [Screenshot inventory](screenshots.tsv)

## Fourteen native SQLite fixtures

The probe executes the same SQL and worker as the directory. Each engine ran each query cold, immediately repeated it, and ran it after opening the rank-two module in a separate context. The three browsers returned identical native results and database file counts. Every immediate repeat fetched zero database files. These are local measurements. [Per-browser results](fixture-files.json)

| Query | Cold files | After another module |
| --- | ---: | ---: |
| module · `RowSrc.lean` | 9 | 4 |
| typeahead · `RowS` | 3 | 1 |
| typeahead · `galois` | 3 | 1 |
| typeahead · `zero` | 3 | 1 |
| typeahead · `siegel` | 3 | 1 |
| typeahead · `a` | 4 | 2 |
| typeahead · `Α` | 3 | 1 |
| typeahead · `_aux` | 3 | 1 |
| search · `RowSrc` | 7 | 5 |
| search · `zero*` | 19 | 17 |
| search · `Formalism AND siegel*` | 16 | 14 |
| search · `map*` | 14 | 12 |
| declaration · `galoisLocalGlobalStrong_recParameter` | 5 | 3 |
| trail · `RowSrc to RH` | 13 | 11 |

## Rendering and contributions

The package contains 9,746 files totalling 103,569,937 bytes. Two independent builds reproduced the database and static tree. Nine SQL plans passed the index check. [Compiler manifest](manifest.json) · [Parquet manifest](parquet.json) · [Evidence file hashes](SHA256SUMS)

Static hosts map each pathname to one file. The two query-string routes select the matching pre-rendered sample during HTML parsing. Each of the six also has a standalone static page. For other records, opening the requested URL runs the same indexed SQL. The browser downloads the startup assets at idle and opens SQLite for interactive queries.

The compiler converts contributed Markdown and math to HTML and native MathML, disables raw HTML, and sanitizes the result against an element and attribute allowlist. The page policy permits local application assets, the GitHub raw source fetch, and the giscus frame origin. Discussion remains switched off. At Gate 5, add `https://giscus.app` to `script-src` for the loader and retest the live widget in Chromium, Firefox and WebKit with the launch policy. [Renderer and allowlist](../../tools/informalizations.py)

Open disputes take precedence over other status badges. Human review is recorded through the reviewed informalization kind. An explicit agreement identifies each peer informalization by author and ledger-file digest. Several informalizations without a recorded comparison show a count with comparison pending. The new-file editor uses the entered GitHub handle in both the filename and front matter. The issue form uses its module field ID for the path prefill. Both GitHub handoffs were checked locally. [Issue form](../../.github/ISSUE_TEMPLATE/module-problem.yml) · [GitHub form schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema)

## Reproduction

Follow the [build instructions](../../README.md#reproduce-the-database-and-local-preview) with the pinned SQLite runtime. With the local preview running, the following command replays the three-engine fixtures and interaction checks and creates the 28 screenshots. Screenshots depend on browser versions and installed system fonts.

```bash
node tools/gate3-evidence.mjs http://127.0.0.1:18741 inputs/fixtures.json inputs/gate3-evidence
```

Check the committed review evidence with `(cd reports/gate-3 && sha256sum -c SHA256SUMS)`.

# Discussion widget and SQLite page reads

The giscus sign-in control loaded in Chromium 159.0.8154.6, Firefox 159.0 and WebKit 27.2 with the default headers. The same widget failed in all three under `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp`. Each test visited an existing thread signed out. [Widget fixture](../../tools/check-giscus.mjs) · [Browser evidence](browsers.json)

The SQLite worker now reads each gzip asset with synchronous XMLHttpRequest and inflates it with the locked inflate build of pako 3.0.3. This lets query execution and the discussion iframe work with the default headers. The database SHA-256 is unchanged from Gate 2. The static package contains 9,729 files and 103,406,815 bytes. Two builds yielded the same package manifest. [Manifest](manifest.json)

## Browser measurements

Each engine ran fourteen fixtures against a local Wrangler Pages preview. Cold means a fresh browser context. Warm means the rank-two module has been opened. Every result matched native SQLite. Repeating each query immediately fetched zero database files. The table gives cold / warm database-file counts and two-way HTTP/1.1 bytes over loopback, including headers and framing. Cold / warm counts matched across engines. The JSON also records payload bytes, elapsed time and assets loaded by the query.

| Query | Database files | Chromium bytes | Firefox bytes | WebKit bytes |
| --- | ---: | ---: | ---: | ---: |
| module `RowSrc.lean` | 8 / 3 | 252,519 / 22,493 | 252,433 / 22,459 | 252,655 / 22,543 |
| typeahead `RowS` | 3 / 1 | 229,617 / 9,635 | 229,605 / 9,626 | 229,696 / 9,654 |
| typeahead `galois` | 3 / 1 | 230,298 / 10,295 | 230,288 / 10,286 | 230,356 / 10,314 |
| typeahead `zero` | 3 / 1 | 229,798 / 9,801 | 229,778 / 9,792 | 229,846 / 9,820 |
| typeahead `siegel` | 3 / 1 | 229,527 / 9,531 | 229,501 / 9,522 | 229,599 / 9,550 |
| typeahead `a` | 4 / 2 | 235,566 / 15,568 | 235,522 / 15,543 | 235,634 / 15,599 |
| typeahead `Α` | 3 / 1 | 231,085 / 11,090 | 231,060 / 11,081 | 231,153 / 11,109 |
| typeahead `_aux` | 3 / 1 | 225,060 / 5,056 | 225,018 / 5,047 | 225,110 / 5,075 |
| search `RowSrc` | 7 / 5 | 276,742 / 56,745 | 276,672 / 56,700 | 276,867 / 56,848 |
| search `zero*` | 19 / 17 | 403,235 / 183,238 | 403,071 / 183,085 | 403,610 / 183,575 |
| search `Formalism AND siegel*` | 16 / 14 | 387,909 / 167,912 | 387,770 / 167,786 | 388,210 / 168,202 |
| search `map*` | 14 / 12 | 344,006 / 124,025 | 343,882 / 123,901 | 344,294 / 124,246 |
| declaration `galoisLocalGlobalStrong_recParameter` | 5 / 3 | 242,135 / 22,130 | 242,091 / 22,103 | 242,229 / 22,187 |
| trail `galoisLocalGlobalStrong_recParameter` | 13 / 11 | 333,218 / 113,233 | 333,093 / 113,134 | 333,448 / 113,436 |

## Reproduce

Build and serve the package following the [project instructions](../../README.md). With the native fixtures generated and the local preview running, run the browser checks.

```bash
npx playwright install --with-deps chromium firefox webkit
node tools/check-giscus.mjs
for engine in chromium firefox webkit; do
  node tools/measure.mjs http://127.0.0.1:18741 inputs/fixtures.json "inputs/http-$engine.json" "$engine"
done
```

The giscus check needs network access to its public widget. Finding the visible sign-in control exercises both the iframe navigation and the embedded UI. Local byte counts depend on HTTP headers and browser version.

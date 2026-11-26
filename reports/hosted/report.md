# Hosted Gate 1 measurements

QED Codex served all fourteen native SQLite fixtures correctly from a Cloudflare Pages preview on 2026-11-23. The RowSrc module fetched eight database files cold and three after visiting the rank-two module. Every query met its applicable file budget. [Pinned package manifest](../gzip/manifest.json) · [Browser samples](browser.json)

## Transfer and teardown

The reviewed package contained 9,728 files (103,374,206 bytes). Wrangler uploaded 9,727 assets (103,374,010 bytes) and processed the 196-byte headers configuration separately. The five asset-upload request bodies contained 139,031,658 bytes including API serialization. The asset upload took 245.25 seconds and the full deployment took 255.271 seconds.

All 177 observed database responses used HTTP/2 and `Content-Type: application/gzip`. The `Content-Encoding` header was absent on every response. The compressed bytes produced by the packager reached the VFS directly.

Direct deletion completed in 3.38 seconds. The project deployment list was empty afterward. Fresh signed-out requests to the original address returned HTTP 403 for the root and HTTP 404 for both the proof manifest and a sampled database page.

## Browser queries

Cold starts in a fresh Chromium context. Warm starts in a separate fresh context after a visit to the rank-two module. The timer starts at form submission and ends when the result appears. Database files include the cold interior bundle. Database payload counts the gzip file bytes. Wire counts both directions of the browser’s encrypted TLS connection during the query, including on-demand app and WASM assets. It excludes the preceding HTML navigation, the primer query and TCP/IP framing. Navigation, TLS direction, database response sizes, and individual requests are available in the [browser samples](browser.json).

| Query | DB files cold / warm | DB payload B cold / warm | Wire B cold / warm | Time ms cold / warm |
| --- | ---: | ---: | ---: | ---: |
| `RowSrc.lean` | 8 / 3 | 245,305 / 19,769 | 872,670 / 21,295 | 3,045.7 / 178.3 |
| typeahead `RowS` | 3 / 1 | 226,898 / 8,765 | 851,412 / 9,304 | 1,167.8 / 153.2 |
| typeahead `galois` | 3 / 1 | 227,558 / 9,425 | 851,862 / 9,990 | 1,052 / 58.1 |
| typeahead `zero` | 3 / 1 | 227,064 / 8,931 | 851,717 / 9,494 | 1,118.3 / 55.9 |
| typeahead `siegel` | 3 / 1 | 226,794 / 8,661 | 851,056 / 9,207 | 1,136.9 / 57.6 |
| typeahead `a` | 4 / 2 | 231,955 / 13,822 | 857,057 / 14,902 | 1,801.6 / 257.4 |
| typeahead `Α` | 3 / 1 | 228,353 / 10,220 | 852,834 / 10,767 | 1,299.7 / 82.2 |
| typeahead `_aux` | 3 / 1 | 222,319 / 4,186 | 846,948 / 4,724 | 1,249.6 / 54 |
| search `RowSrc` | 7 / 5 | 270,533 / 52,400 | 897,366 / 55,234 | 1,546.5 / 371.4 |
| search `zero*` | 19 / 17 | 386,609 / 168,476 | 1,020,108 / 177,562 | 4,012.7 / 1,063.8 |
| search `Formalism AND siegel*` | 16 / 14 | 373,875 / 155,742 | 1,005,732 / 163,481 | 2,891.3 / 949.3 |
| search `map*` | 14 / 12 | 331,714 / 113,581 | 962,359 / 120,179 | 2,152.3 / 905.6 |
| `exact declaration` | 5 / 3 | 237,654 / 19,521 | 863,341 / 21,035 | 1,373.5 / 150.8 |
| `RH trail` | 13 / 11 | 321,788 / 103,655 | 951,910 / 109,527 | 2,734.6 / 696.9 |

The exact declaration and the five-site trail start at `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter`. Each of the fourteen immediate repeats fetched zero files and transferred zero TLS bytes. The cold full-text query `zero*` came closest to its budget at 19 of 20 database files.

## Replay on an authorized preview

Build the package and generate the native fixtures with the [pinned reproduction steps](../../README.md). Put the deployment hostname in a local file under the ignored inputs directory. The measurement script opens a TLS tunnel to that host, checks the query result against native SQLite, and writes relative database paths to its output. Timings and HTTP framing can vary by route and browser.

```bash
node tools/measure-hosted.mjs inputs/preview-host inputs/fixtures.json inputs/hosted-browser.json
```

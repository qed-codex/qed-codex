# Database source notes

The preview package has 7,293 files and 221,384,575 bytes. Its SQLite content matches main’s signed-off mirror-rehearsal manifest. [Verified package manifest](manifest.json) There are 3,673 database pieces, 1,253 trail files, 2,301 static module records, 26 other HTML pages and 40 other assets. The earlier package had 14,924 files. All 7,631 removed files belonged to modules whose only entries were source documentation. The 2,045 modules with contributed or permission entries still have static pages.

The directory verifier checked all packaged HTML links to static module records and all published-entry fragments. A local build with a production origin also checked the complete sitemap against the actual HTML tree. The agent guide links the pinned ledger and gives the Markdown path pattern.

## Browser comparison

Each browser opened the actual database route for every source-documentation-only module. Its serialized main element was compared with browser-parsed HTML from the full static reference. The check looked up each expected note heading by ID, checked the proof links and titles, and compared the entry’s source, copyright and licence against the database and source registry, including NOTICE where present. Each route with headings opened at its first heading fragment.

| Engine | Module comparisons | Note targets | Differences from full static reference | Full sweep checks | Sweep failures |
| --- | ---: | ---: | ---: | ---: | ---: |
| Chromium | 7,631 | 52,642 | 0 | 8,000 | 0 |
| Firefox | 7,631 | 52,642 | 0 | 7,325 | 0 |
| Webkit | 7,631 | 52,642 | 0 | 7,325 | 0 |

Compared with the previous staging build, 5,525 pages were byte-identical after main-element serialization. The other 2,106 gained one proof-membership paragraph. Removing that paragraph from the reference made every comparison equal. The additional labels occur on 429 3sum-apsp, 1,049 eth, 320 vp-vnp and 308 zeta23 pages. The remaining modules already named their proof. All three browsers also followed a live search result for `dirichlet_montgomery_taylor_on_critical_line` to its visible note heading.

## Preview measurements

One module per source was selected at the median length of its rendered documentation, breaking ties by module path. Each pair used a fresh browser context followed by a second navigation to the same page in the same tab. Time runs from navigation to the module’s populated contribution form. Received bytes were counted at a CONNECT tunnel through network idle, including TLS overhead. The measurements include the document, engine and database pieces. These are individual observations on the review preview. [Module paths and measurements](preview-timings.tsv)

Each cell gives cold milliseconds / received bytes followed by warm milliseconds / received bytes.

| Source | Chromium | Firefox | WebKit |
| --- | --- | --- | --- |
| 3sum-apsp | 4,691 / 1,225,427 → 561 / 3,139 | 1,774 / 1,225,145 → 505 / 3,157 | 1,494 / 1,255,095 → 557 / 15,145 |
| eth | 1,765 / 1,232,334 → 658 / 3,156 | 1,585 / 1,232,662 → 779 / 3,143 | 1,371 / 1,262,368 → 496 / 15,133 |
| openai-math | 2,000 / 1,213,920 → 480 / 3,148 | 1,360 / 1,214,312 → 675 / 3,150 | 1,228 / 1,243,984 → 678 / 15,131 |
| vp-vnp | 1,794 / 1,222,978 → 491 / 3,155 | 1,518 / 1,222,768 → 830 / 3,192 | 1,396 / 1,252,596 → 653 / 15,151 |
| zeta23 | 1,470 / 1,232,846 → 553 / 3,179 | 1,179 / 1,232,891 → 506 / 3,149 | 1,218 / 1,263,009 → 465 / 15,147 |

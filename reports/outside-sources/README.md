# Outside sources by module

The link ledger gains 146 placements on project modules. The directory also computes a current documentation URL on 8,432 of the 8,852 Mathlib package pages, selected by the documented roots in the registry. These generated URLs live in the module template. They do not occupy rows in the link table or appear in its Parquet export.

| Count | Ledger | Including generated documentation links on module pages |
| --- | ---: | ---: |
| Link placements | 2,979 | 11,411 |
| Distinct destination URLs | 2,056 | 10,488 |
| Modules with a link | 2,164 | 10,590 |

Six Mathlib modules already have a ledger link. The build's destination health check also includes unlinked catalogue pages, so its inventory has a different denominator.

## Michael O. Rubinstein

The source is Version 2 of *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, pinned to `278761172565a762b1e5642003b3b97547f71a57`. We counted file citations in the complete TeX source and linked to the PDF at the same revision. The ledger holds the credit, paper title and URL. [Paper](https://github.com/mrubinst/alpoge-claude-rh-explained/blob/278761172565a762b1e5642003b3b97547f71a57/zeta-paper_v2.pdf) · [Pinned TeX](https://github.com/mrubinst/alpoge-claude-rh-explained/blob/278761172565a762b1e5642003b3b97547f71a57/zeta-paper_v2.tex) · [Citation-by-citation join](rubinstein.tsv)

We found 167 occurrences ending in `.lean` with 133 distinct spellings. Another 35 file references use short names in explicitly identified directories. Across these 202 occurrences, 167 distinct printed spellings identify 141 original modules. Of the spellings, 166 refer to one module each. The paper uses `Statement.lean` for four different files, and identifies the intended file at each occurrence. All 202 references resolved to one module at the citation site. Zero were left out as ambiguous. Each module gets one link.

The narrower count of 45 distinct file references reproduces for filenames written inside `\texttt{…}`. Of those, 38 spellings have a unique literal path suffix. Reading their local context gives 46 different modules across those occurrences. This differs from the preliminary count of 42 modules. The complete join also covers `\path{…}`, path fragments split for typesetting, and the paper's directory lists. It uses declaration ownership, named uses in pinned source or an explicit directory to resolve duplicate basenames. Standalone identifiers outside file citations do not establish a link.

## Localized references

The OverIx module links to Jenny Lorraine Nielsen’s paper, Frank Chu’s question, Harry Tong’s compiled dependency findings and the Rosetta audit by dial481. The Main module links to Andrew Sutherland’s verification files. All five links are credited at module level. The full ledger check reported zero dead URLs and two unverified destinations. PhilArchive returned 403, and the generic checker could not resolve the GitHub fragment for Tong. The heading “Exact witness paths” is present in the pinned Markdown. The Chu and Tong labels reproduce their source headings. A Chromium visit to Nielsen’s PhilArchive record returned a 403 challenge, so its existing label is retained. The Rosetta link points to the published audit at `5f0eda0`. [Pinned report](https://raw.githubusercontent.com/harrytong/rh-verification/16b88c701bd7abddd93d49a9896cd4daab41f680/stage1/code/RH_critics_dependency_findings.md)

## Current Mathlib documentation

The template advertises the four documented directories and their four root modules. The 420 modules in MathlibTest, Cache, scripts, DownstreamTest and lakefile.lean have no generated documentation link. The registry rule applies uniformly to the 8,432 included paths.

On 24 November, a single paced pass over those 8,432 URLs returned HTTP 200 for 8,326 and another outcome for **106**. The checker issued HTTP HEAD requests with up to three in flight, admitting at most five new URLs per second. These are the observed responses at the times recorded. [Every URL, response and UTC time](documented-paths.tsv) · [Earlier random samples](mathlib-docs.tsv)

| Observed response | Paths |
| --- | ---: |
| 200 | 8,326 |
| 404 | 103 |
| 503 | 2 |
| [Errno 104] Connection reset by peer | 1 |

## Replay

Build the original directory database as described in the top-level README. Set `project` to the location of a Git repository containing the original proof at `40e56bab`. The extraction checks the SHA-256 of the paper source before matching citations.

```sh
export LC_ALL=C
curl -fLsS https://raw.githubusercontent.com/mrubinst/alpoge-claude-rh-explained/278761172565a762b1e5642003b3b97547f71a57/zeta-paper_v2.tex -o build/rubinstein-v2.tex
.venv/bin/python tools/rubinstein_links.py build/rubinstein-v2.tex build/rh.sqlite3 "$project" > build/rubinstein.tsv
cmp reports/outside-sources/rubinstein.tsv build/rubinstein.tsv
.venv/bin/python tools/check_mathlib_docs.py build/rh.sqlite3 > build/current-docs.tsv
```

The citation join replays offline from its pinned inputs. The documentation check records current responses and the time of each request.

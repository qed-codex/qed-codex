# Statement links through compiled constants

Seven more pages in Andrew O’Desky’s *Statements of the Lean RH project* now point to modules. Three cite fields of project structures and four cite Mathlib constants. Of 1,960 statement pages, 1,943 have a module link. The 17 unmatched pages comprise 16 theorems and one definition. [Author’s map](https://andrewodesky.com/rh/lean-map.tsv) · [Pinned map receipt](../../proofs/rh/sources/odesky/capture.json)

| Measure | Declaration join | With compiled constants |
| --- | ---: | ---: |
| Distinct statement-to-module links | 2,313 | 2,323 |
| Modules with a statement link | 2,038 | 2,044 |
| Linked statement pages | 1,936 | 1,943 |
| Unmatched theorems | 20 | 16 |
| Unmatched definitions | 4 | 1 |
| Distinct links including the atlas | 2,420 | 2,430 |
| Modules with any outside link | 2,074 | 2,080 |

The declaration join still supplies 2,716 links to named project declarations. For a page it misses, the refresh looks up each printed name verbatim in James Shore’s v0.2.1 constants table, built from Andrew Sutherland’s kernel export. For a project field it checks that the recorded owner is the immediately enclosing project structure or class and that its source file agrees with the declaration table. For a Mathlib constant it uses the recorded Mathlib module. The build checks that each resulting module exists. [Shore’s release](https://github.com/james-shore/rh-proof-dependencies/releases/tag/v0.2.1) · [Sutherland’s export](https://math.mit.edu/~drew/grh/)

The evidence ledger retains all 23 matching names. Its `constant_module` column contains the source file and `constant_owner` identifies the enclosing project structure. Names on the same page that resolve to the same module produce one link. The ten new rows in `links.tsv` have an empty declaration field, so they appear on module pages. The map was captured on 23 November 2026 at 22:07:36 UTC. [Evidence rows](../../proofs/rh/sources/odesky/constant-matches.tsv) · [Link ledger](../../proofs/rh/links.tsv) · [Generated counts](../../proofs/rh/sources/odesky/counts.json)

## Reproduce

From the repository root with the pinned inputs in the README, replay the map and compare the resulting ledger.

```sh
export LC_ALL=C
mkdir -p inputs/official-map-replay
cp proofs/rh/sources/odesky/{capture.json,lean-map.tsv} inputs/official-map-replay/
cp proofs/rh/outside-link-check.json inputs/official-map-replay/
.venv/bin/python tools/refresh_statements.py --replay inputs/official-map-replay
git diff --exit-code -- proofs/rh/links.tsv proofs/rh/sources/odesky proofs/rh/outside-link-check.json
```

The README’s build commands reproduce the SQLite, HTML and Parquet manifests. The preview package contains 2,235 HTML pages in 14,271 files. [Build manifest](manifest.json) · [Directory recount](directory.json) · [Parquet manifest](parquet.json)

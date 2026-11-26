# Gate 2 compiler and schema

The compiler reproduced 184,039 modules, 925,310 import edges, 1,063,284 project declarations and 641,100 source-trace rows from the pinned inputs. The SQLite package passes integrity and foreign-key checks. Its eight site query plans use indexed lookups. [Database manifest and plans](manifest.json) · [DDL](../../tools/schema.sql)

| Logical table | Rows or postings | Parquet bytes |
| --- | ---: | ---: |
| `declarations` | 1,063,284 | 18,176,589 |
| `disputes` | 0 | 437 |
| `imports` | 925,310 | 3,090,984 |
| `links` | 2,189 | 35,904 |
| `modules` | 184,039 | 4,362,212 |
| `names` | 7,466,902 | 29,099,907 |
| `informalizations` | 1 | 9,744 |
| `shortnames` | 1,247,323 | 32,198,382 |
| `summary` | 10 | 941 |
| `trace` | 641,100 | 9,586,622 |

The ten Parquet files total 96,561,722 bytes. The exporter reads every file back and checks column types, row order, counts and SHA-256 against the logical SQLite manifest. The empty disputes export retains its typed columns. The contentless FTS5 export contains the searchable term and document-ID pairs. [Parquet manifest](parquet.json) · [Canonical ordering](../../tools/tables.py)

SQLite 3.46.1 and 3.53.1 agree on all ten logical digests. Informalizations preserve the author handle, kind, tool, source revision, declaration names, license, optional source URL and Markdown body. The seed informalization and the 2,189 outside links come from the ledger. Kernel masks use James Shore’s CC0 release. [Shore v0.2.1](https://github.com/james-shore/rh-proof-dependencies/releases/tag/v0.2.1) · [Proof pins](../../proofs/rh/proof.yml)

The plan check permits the FTS5 MATCH traversal, the bounded queue of up to 20 search hits and the recursive trail queue. It rejected a deliberately unindexed filter on module paths. The read-only Actions workflow runs the compiler, plan verifier and Parquet round trip on pull requests and merges to main. Its build steps have run locally. A hosted Actions run awaits branch review. [Workflow](../../.github/workflows/compiler.yml) · [Reproduction](../../README.md#reproduce-the-database-and-local-preview)

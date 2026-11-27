---
{header}---

# QED Codex proof directory

Select a configuration to read a table. Its `train` split contains all rows in canonical order. The `names` configuration records term and document-ID pairs from the contentless FTS5 index. The other configurations use their SQLite column names and primary-key order. [File and content provenance](manifest.json)

In Hugging Face `datasets` 4.8.4, use `streaming=True` or read the Parquet file directly for a zero-row table. The materialized reader in that version raises an empty-split error.

{attribution}
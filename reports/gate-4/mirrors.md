# Mirror rehearsal

The Hugging Face staging directory contains one Parquet configuration per logical SQLite table. Each configuration uses a `train` split for the complete table and `modules` is the default. Separate configurations preserve the different column schemas. The release staging directory carries the SQLite file with the full ledger commit in its filename. Each target has its own file-hash manifest, the same ledger revision, credits and license notices. [Hugging Face configuration format](https://huggingface.co/docs/hub/datasets-manual-configuration)

The staging tool obtains the compiler manifest, proof pins and original license notices from Git at the exact revision. It checks the staged SQLite bytes against that compiler manifest, re-reads the staged Parquet rows in canonical order and checks the content digest of every table. The dataset card credits James Shore for the CC0 kernel data, links the source formalization and Rosetta analysis, and preserves the attribution of informalization text and outside explanations. [Staging tool](../../tools/mirrors.py)

## Reproduce

From the repository root, run the [README reproduction commands](../../README.md#reproduce-the-database-and-local-preview) and stage the mirrors for that checkout.

```bash
.venv/bin/python tools/mirrors.py build/rh.sqlite3 reports/public-tree/manifest.json \
  build/parquet build/mirror-replay --commit "$(git rev-parse HEAD)" > inputs/mirror-replay.json
```

For a consumer check, run this with Hugging Face `datasets==4.8.4` installed in a separate Python environment. It opens each configuration using local files, including the zero-row case. In this version the materialized reader raises an empty-split error for a zero-row configuration. Streaming mode and direct Parquet reads preserve the empty result and its schema. The environment variables keep Hub requests disabled.

```bash
HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python - <<'PY'
import json
from datasets import get_dataset_config_names, load_dataset

directory = "build/mirror-replay/huggingface"
expected = json.load(open("inputs/mirror-replay.json"))["verifiedRows"]
assert sorted(get_dataset_config_names(directory)) == sorted(expected)
for name, rows in expected.items():
    split = load_dataset(directory, name=name, split="train", streaming=True)
    assert (next(iter(split), None) is None) == (rows == 0)
PY
```

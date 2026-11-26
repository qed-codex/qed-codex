---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingStored.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingStored.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingStored.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Padding a sparse dictionary preserves its exact coefficients, key
uniqueness, validity, and list length. The ambient bit representation need
not compact or renumber the residual variables. 

### `weaken`

 Enlarging only the validity envelope does not alter any stored bit data. 

### `weaken_data_valid`

 The stronger, free-coordinate validity invariant remains available even
when a caller stores the dictionary in a full ambient validity envelope. 

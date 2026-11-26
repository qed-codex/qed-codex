---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorLoadBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorLoadBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorLoadBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Source-parameter bounds for the full key produced from an actual shifted
incidence matrix. Every incidence row and every retained coefficient is charged. 

### `matrixBound`

 Serialized full matrix, with the actual incidence count `D`. 

### `member_word_length_le`

 A member word is physically contained in its framed serialization. 

### `key_run_space`

 The actual key producer has this cost and all-prefix bound on the same
trace. The input matrix is produced by the real signed-row/shift relation. 

### `matrixEnvelope`

 The same physical matrix envelope specialized to the actual native input. 

### `generated_bounds`

 Bounds consumed by the paid per-head evaluator. Only the actual generated
matrix relation, actual word lengths and fixed source scalars enter. 

---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionAlgebra.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionAlgebra.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionAlgebra.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Algebra behind exhaustive maximal-nonzero-minor row selection.
Only original rows are selected; inverses occur solely in the correctness proof. 

### `minor`

 Restriction of an integer matrix to an ordered square pair of index tuples. 

### `qmatrix`

 The corresponding rational matrix, used only in algebraic certificates. 

### `appendIndex`

 Append a row or column index using the canonical sum-index equivalence. 

### `span_eq_of_borders_zero`

 Zero determinants of all one-row/one-column borders force rational spanning. 

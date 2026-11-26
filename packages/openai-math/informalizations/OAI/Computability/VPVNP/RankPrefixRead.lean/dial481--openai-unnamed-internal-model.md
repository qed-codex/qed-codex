---
{
  "module": "OAI/Computability/VPVNP/RankPrefixRead.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankPrefixRead.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankPrefixRead.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Macaulay readers for prefix rank queries

The greedy row scan reads a row prefix at its original addresses. The
column scan uses the same reader with row and column ports interchanged.
Renaming these ports preserves the exact instruction trace, including its
time and live stack-height bounds.


### `transpose`

 The coefficient routine of the transposed matrix, with its usual caller
convention. Only the physical addresses of its row and column ports change. 

### `prefixMatrix`

 Retain the first `r` rows of a matrix of encoded scalars. 

### `map_prefixMatrix`

 Applying any scalar interpretation before or after restricting to the
prefix yields exactly the matrix in the greedy rank formula. 

### `map_prefixMatrix_transpose`

 On the column scan the interpreted matrix is transposed before taking
the row prefix. 

### `CorrectSpace.transpose`

 Every original entry query gives one transpose query with exactly the
same cost, final auxiliary bank, and peak storage allowance. 

### `CorrectSpace.prefixMatrix`

 The ordinal of a row in a prefix is already its address in the original
matrix. No instructions or additional stack cells are required. 

### `CorrectSpace.transpose_prefix`

 The complete calling convention used for prefix ranks of the transpose. 

### `reader_transpose_prefix`

 The concrete three-way reader also accepts each transpose prefix with
the bounds established for the routed equation, affine, and power arms. 

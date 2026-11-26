---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Rank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Rank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Rank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual finite tensor rank

The natural tensor is the diagonal coefficient tensor. Its local restrictions
are exactly the tensors admitting the corresponding number of rank-one terms.
Every finite coefficient tensor has such a decomposition, obtained by expanding
its individual coefficients. Exact rank is therefore a genuine minimum.


### `natTensor`

 The diagonal tensor with `n` independent scalar products. 

### `rankAtMost_iff_natTensor_restricts`

 This equivalence exposes all three local matrices of the restriction. 

### `natTensor_add_pullback`

 The diagonal tensor on a sum of dimensions separates into its two blocks
under the actual standard bijection of finite coordinate sets. 

### `rankAtMost_card`

 Expand each actual coefficient into a separate rank-one tensor. 

### `natTensor_restricts_of_le`

 Selecting the first coordinates realizes the usual comparison of diagonal
tensors by actual local coefficient matrices. 

### `nonzero_restricts_natTensor_one`

 A nonzero coefficient can be selected and rescaled to obtain the scalar
unit tensor. No nonzero-rank assumption replaces this actual restriction. 

### `rank`

 The least size of an actual rank-one decomposition. 

### `rank`

 Exact rank is invariant under mutual local restriction. 

---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Flattening.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Flattening.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Tensor/Flattening.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# First-leg coefficient flattening

The invariant is the matrix rank of the actual coefficient array, with the
second and third coordinates paired into its rows. Local tensor restrictions
act by matrix multiplication on both sides. This invariant, unlike ordinary
tensor rank, is additive on full heterogeneous direct sums.


### `firstFlattening`

 Pair the last two legs; the first leg indexes matrix columns. 

### `flatteningRank`

 The finite dimension of the space spanned by the first-leg slices. 

### `card_le_flatteningRank_of_identity`

 An identity minor certifies a lower bound directly from coefficients. 

### `flatteningRank_le_of_rankAtMost`

 Flattening rank is bounded by every actual rank-one decomposition. 

### `flatteningRank_matrixCoefficients`

 The first-leg slices of a nonempty rectangular matrix multiplication tensor
are independent. The third matrix dimension supplies the selected common index. 

### `blockRows`

 Rows belonging to one summand embed into the full paired row family. 

### `insertBlockRows`

 Insert the two diagonal row blocks and fill both cross row families by zero. 

### `blockMatrix_rank`

 Ordinary matrix rank is additive on block diagonal matrices. This is a
statement about ranges of linear maps, with no tensor rank additivity premise. 

### `flatteningRank_blockSum_eq_blockMatrix_rank`

 The cross rows of a full tensor direct sum are all zero; removing exactly
these rows leaves the block diagonal matrix without changing its rank. 

### `flatteningRank`

 Actual first-leg matrix rank, invariant under mutual tensor restriction. 

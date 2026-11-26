---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Tensor/Matrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Tensor/Matrix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Tensor/Matrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Square matrix tensors in the restriction semiring

Dimension comparisons and multiplication are witnessed by the actual coordinate
maps. The cubic rank bound uses the ordinary sum over the three matrix indices.


### `matrixCoefficients_pullback_injective`

 Injective index maps preserve all three shared-index equalities of a matrix
tensor, including its zero coefficients. 

### `squareProductCoordinates`

 Pair the row indices and column indices separately, then enumerate each
pair by the standard equivalence with `Fin (n * m)`. 

### `square_product_pullback`

 The product of two square matrix tensors is the larger square tensor under
an explicit bijective relabeling of each local coordinate space. 

### `square_restricts_of_le`

 Taking the first `n` indices in each matrix direction is an actual local
restriction of the larger matrix multiplication tensor. 

### `square_rankAtMost_cubic`

 The usual cubic tensor decomposition, with one term for each triple of
matrix indices rather than one term for each ambient coefficient. 

### `square`

 The class of the actual `n` by `n` matrix multiplication tensor. 

### `rank_square_le`

 The rank here is the least size of an actual rank-one decomposition. 

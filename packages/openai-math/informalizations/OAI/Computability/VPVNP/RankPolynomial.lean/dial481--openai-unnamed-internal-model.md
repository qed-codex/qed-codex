---
{
  "module": "OAI/Computability/VPVNP/RankPolynomial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankPolynomial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankPolynomial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The determinant used for rank queries

Appendix D.2 of *VP and VNP differ over every field* forms a weighted Gram matrix
over a polynomial ring. The coefficient of degree `q` in its reverse characteristic
polynomial is a signed sum of squares of minors of the original rectangular matrix.
Each square is tagged by the sum of its one-based row and column indices.


### `indexWeight`

 Sum of the one-based indices selected for a minor. 

### `weightDiagonal`

 The diagonal tagging the one-based index of each row or column. 

### `weightedGram`

 The matrix `D₁(z) M D₂(z) Mᵀ`, with constant entries of `M` embedded by `C`. 

### `rankPolynomial`

 The determinant `det(1 - u G(z))` as a polynomial in `u` with coefficients in `K[z]`. 

### `weightedGram_minor`

 Cauchy–Binet expands each principal minor of the weighted Gram matrix. 

### `charpolyRev_coeff_eq_sum_compound`

 Each reverse characteristic coefficient is the signed trace of the corresponding
compound matrix, also when the requested minor size exceeds the dimension. 

### `rankPolynomial_coeff`

 The coefficient identity of Appendix D.2 over the coefficient ring, in every
characteristic. For `q` larger than a matrix dimension the sum of minors is empty. 

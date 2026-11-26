---
{
  "module": "OAI/Computability/VPVNP/SchurCoefficientQueries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SchurCoefficientQueries.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SchurCoefficientQueries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bivariate coefficient queries for the Schur product

Appendix D.2 of *VP and VNP differ over every field* uses the Schur product to
compute any specified coefficient of `det (1 - uM(z))`. Each query uses an
oracle for individual scalar coefficients of the matrix entries. Its two
recursive computations split the list of factors and the exponents of matrix
powers in half.


### `headFactorQuery`

 Query one bidegree of the first factor using only coefficients of matrix entries. 

### `streamedHeadFactorQuery`

 Compute a coefficient of the Schur factor with sequential scans of
both matrix indices and both degree splits. Each queried power of the
trailing matrix is also evaluated by streaming scans. 

### `balancedProduct`

 Query a consecutive block of factors. Each internal node splits the block
into two halves. Each root-to-leaf path makes exactly `depth` such splits. 

### `balancedBivariateProduct`

 Coefficient query for the factors of the Appendix D.2 determinant in
`R[z][[u]]`. Both degree splits stream over a single counter. The parameter
`depth = Nat.clog 2 count` suffices for any number of consecutive factors. 

### `determinantLeaf`

 Query a Schur factor by its absolute index, giving the identity series
at indices outside the matrix. 

### `determinantQuery`

 Compute a scalar bidegree of `det (1-uM(z))` without constructing its polynomial. 

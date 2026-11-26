---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BinomialMatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinomialMatrix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinomialMatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Consecutive binomial matrices

The matrix with entries choose (A + d) j factors into a lower
unitriangular Pascal matrix and an upper unitriangular translation matrix.
The upper factor is explicitly zero below the diagonal: natural subtraction
alone would give the wrong entries there.

All identities are obtained by casting integer-valued binomial coefficients,
so the determinant calculation remains valid in arbitrary characteristic.


### `B`

 The consecutive-integer binomial evaluation matrix. 

### `L`

 The lower unitriangular Pascal matrix. 

### `U`

 The upper unitriangular translation matrix, with explicit zero extension. 

### `choose_add_sum`

 Vandermonde convolution, extended by zero to any range containing j. 

### `factorization`

 The factorization is valid already over an arbitrary semiring. 

### `det_B`

 Consecutive binomial evaluation has determinant one in every
commutative ring, with no characteristic or size restriction. 

### `det_B_int`

 In particular, the determinant is exactly one over the integers. 

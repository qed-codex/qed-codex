---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/PolynomialFiltration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/PolynomialFiltration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/PolynomialFiltration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The explicit determinant filtration

We use positive dimensions `a+1` and `b+2`.  The two old copies are the
coefficients of `s` and `w`.  The new coordinates are quotient lifts `Q` and
kernel elements `K = W_j - S_(j+1)`.  The first input is unchanged throughout.
All statements below are coefficient identities over the coefficient field.


### `doubledPolynomialTensor`

 Two copies of convolution with their first input genuinely shared. 

### `binaryDotTensor`

 The two-dimensional dot pairing with a singleton first leg. 

### `doubledPolynomialTensor_product`

 The doubled coefficient tensor really is convolution tensored with the
two-dimensional dot pairing, after only coordinate equivalences. 

### `determinantInputMap`

 The quotient lifts are `S_0,...,S_(b+1),W_(b+1)`; the remaining
new vectors are `W_j-S_(j+1)` for `j=0,...,b`. 

### `determinantOutputMap`

 Coordinates of old output basis vectors in the new basis.  These are the
dual local substitutions required on the tensor's third leg. 

### `determinantAdaptedTensor`

 The whole transformed tensor, including the cross block. 

### `determinant_basis_change`

 The simultaneous basis change is an actual three-leg restriction.  In
particular no branch-specific first-input substitution is used. 

### `determinantGradedTensor`

 The two retained diagonal branches, still sharing the same first leg. 

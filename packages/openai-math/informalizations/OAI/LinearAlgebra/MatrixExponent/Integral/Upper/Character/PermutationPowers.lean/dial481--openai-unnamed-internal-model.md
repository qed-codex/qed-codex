---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Character/PermutationPowers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Character/PermutationPowers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Character/PermutationPowers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The exponents of the six permuted characters

The exponent identities below follow from evaluating the actual pairings at
dimension two. In particular, they do not depend on how the power-law witnesses
were chosen. Polynomial multiplication with one scalar input is identified
with the corresponding actual pairing by explicit coordinate equivalences.


### `polynomialTensor_one_left_class`

 Scalar polynomial input and full output give the first-leg pairing,
including the empty second input case. 

### `permuted_pX`

 The first-leg exponents of the six actual characters, with their
multiplicities. Uniqueness is forced by the value at dimension two. 

### `meanExponent`

 The average of the character's three pairing exponents. 

### `sum_exponents_permuted`

 A permutation cannot change the sum of the three exponents, since it
preserves the square matrix multiplication tensor at every dimension. 

### `permuted_polynomialTensor_one_left_vector`

 The six boundary values are the powers with exponents
`pX, pY, pX, pY, pZ, pZ`. 

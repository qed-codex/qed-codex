---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialTensor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialTensor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialTensor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The polynomial multiplication tensor

The coefficient tensor records ordinary, untruncated polynomial multiplication.
Evaluation at `a + b - 1` distinct field elements and uniform Lagrange
interpolation give an actual rank decomposition of that size.


### `polynomialTensor`

 Multiplication of polynomials with `a` and `b` coefficients, with every
output coefficient retained. 

### `polynomialTensor_eq_coeff`

 The tensor coefficient is the coefficient of the product of the two input
monomials. 

### `polynomialTensor_swap`

 Commuting the input factors only reindexes the equal-sized output space. 

### `polynomialTensor_one_left`

 With a scalar as the first input, multiplication is the identity pairing
between the second input and output coefficient coordinates. 

### `polynomialTensor_rankAtMost`

 Ordinary polynomial multiplication has an actual decomposition into
`a + b - 1` rank-one tensors. The degenerate empty-input cases are included. 

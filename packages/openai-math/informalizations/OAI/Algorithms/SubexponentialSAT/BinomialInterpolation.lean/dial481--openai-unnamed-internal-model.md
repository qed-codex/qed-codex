---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BinomialInterpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinomialInterpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinomialInterpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Interpolation at consecutive integer weights

The coefficient construction uses the inverse of an actual finite matrix.
It applies over any commutative ring whose evaluation matrix has unit determinant.
The binomial evaluation matrix has determinant one, including in small characteristic.


### `coefficients`

 The coefficients solving a square interpolation system. 

### `mulVec_coefficients`

 Inverting a matrix with unit determinant realizes any prescribed target. 

### `coefficients_unique`

 The coefficient vector is the unique solution of the interpolation system. 

### `isUnit_det_binomial`

 The determinant-one binomial matrix is invertible in every characteristic. 

### `binomialCoefficients`

 Coefficients realizing a target on the consecutive integer weights
`A, ..., A + R - 1`. These are integer binomial evaluations, not ordinary
univariate evaluations at the residues of these weights. 

### `existsUnique_binomial_interpolation`

 Arbitrary target values admit a unique binomial-basis coefficient vector. 

### `parityCoefficients`

 The coefficient vector used for the alternating target in equation (5.3). 

### `spectralValue`

 The scalar eigenvalue of the corrected permutation product. 

### `spectralValue_parity_of_mem`

 The corrected eigenvalue equals one at every integer weight in the chosen interval. 

### `extendCoefficients`

 Extend a finite coefficient vector by zero outside its specified range. 

### `sum_range_extendCoefficients`

 The zero extension connects finite-vector sums to the matrix construction's
natural-number-indexed sum over `range R`. 

### `sum_powersetCard_prod_indicator`

 The elementary symmetric sum of an indicator is the binomial coefficient
in the integer size of its support. The ambient set may be larger than the support. 

### `eval_esymm_indicator`

 Evaluating the actual elementary symmetric polynomial on an indicator
vector counts subsets of its support, with no division by factorials. 

### `eval_esymm_zero_one`

 The elementary symmetric value of a zero-one vector is a binomial
coefficient in the integer number of ones, subsequently cast to the ring. 

### `matrixEigenvalue_signIndicator`

 The actual matrix eigenvalue at a sign vector is the binomial-weighted
scalar from the interpolation argument. The weight is the integer number of
negative signs. 

### `matrixEigenvalue_parity_of_mem`

 With the parity-interpolation coefficients, the actual matrix eigenvalue
is one throughout the prescribed interval of integer weights. 

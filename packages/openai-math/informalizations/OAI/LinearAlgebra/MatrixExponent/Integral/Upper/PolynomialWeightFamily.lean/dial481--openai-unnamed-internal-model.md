---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialWeightFamily.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialWeightFamily.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialWeightFamily.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit polynomial families for diagonal weight degenerations

The diagonal degeneration has a polynomial coefficient family, not merely a
topological limit. Its constant coefficient is the retained tensor. Its degree
is controlled by the supported total weights. At every nonzero parameter its
evaluation is an exact restriction of the source tensor. These are the inputs
needed to extract tensor powers by finite interpolation.


### `weightedPolynomial`

 The monomial family associated to three integer coordinate weights. 

### `weightedPolynomial_eval`

 Polynomial evaluation agrees with the continuous coefficient family used
in the degeneration proof, including at the parameter zero. 

### `weightedPolynomial_coeff_zero`

 The constant coefficient keeps precisely the supported weight-zero terms. 

### `weightedPolynomial_natDegree_le`

 A degree bound is needed only on supported coefficients. Unsupported
coordinates are the zero polynomial, regardless of their assigned weights. 

### `weightedPolynomial_degree_le`

 The same degree bound in the form used by polynomial interpolation. 

### `weightedPolynomial_degree_le_one`

 A weight-zero/weight-one support split gives degree at most one. This is
the bound used by the determinant filtration and the three-sector split. 

### `weightedPolynomial_eval_mem_restrictionOrbit`

 Every nonzero evaluation has actual diagonal local restriction witnesses;
the polynomial family does not assume a character or a continuity principle. 

### `restrictionOrbit_trans`

 Actual local restriction witnesses compose without a limiting argument. 

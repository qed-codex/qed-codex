---
{
  "module": "OAI/Algorithms/SubexponentialSAT/GlobalPolynomial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/GlobalPolynomial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/GlobalPolynomial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The global counting polynomial

The polynomial is an actual finite sum of products of multivariate table polynomials
with univariate polynomial substitutions. Degree estimates work over arbitrary
commutative semirings, so in particular they do not assume that the prime-power
coefficient ring is a field or a domain.


### `compose`

 Substitute a univariate polynomial for each variable of a table polynomial. 

### `natDegree_compose_le`

 Individual table degrees and path degrees give a genuine composition bound.
No bound on the composed polynomial is assumed. 

### `eval_compose`

 Evaluating after polynomial substitution equals evaluating the table at the
values of the substituted paths. 

### `comp_compose`

 Univariate composition passes through multivariate table substitution. 

### `globalPolynomial`

 The polynomial H: sum over assignments of the product over all factors. 

### `eval_globalPolynomial`

 Evaluation commutes with the finite sum and product defining H. 

### `comp_globalPolynomial`

 In particular q = X + C θ expresses H(θ+Z) as the corresponding
sum of products with every incidence path shifted by θ. 

### `natDegree_globalPolynomial_le`

 Equation (4.2), with d later instantiated by p−1. The number of assignments
never enters the degree bound. 

### `eval_zero_globalPolynomial`

 An evaluation-at-zero interface for arbitrary finite tables. 

### `eval_zero_eq_nat_sum`

 The value is the image of the natural-number sum of products under the
canonical map into the coefficient ring. 

### `natDegree_globalPolynomial_lt`

 The strict QD budget used for interpolation, derived from the local
degree bounds and the factor-count bound. 

### `rowValue`

 The scalar polynomial obtained by applying a polynomial row to coordinates. 

### `coeff_rowValue_eq_eval_linearForm`

 The scalar coefficient is evaluation of a genuine linear form in X. 

### `natDegree_shift_le`

 Translation does not increase univariate degree, even with zero divisors. 

### `eq_C_add_sum_monomial_of_natDegree_le`

 Finite positive-degree expansion with the constant coefficient separated. 

### `exists_coefficient_lift_with_constant`

 Coefficients can be lifted through a surjective ring map while preserving
the degree bound and any prescribed lift of the constant coefficient. This is
the lifting step used to retain the exact coordinate selector at T = 0. 

### `natDegree_rowValue_le`

 Taking the linear form does not introduce a factor of the ambient dimension
into the path-degree bound. 

### `shifted_rowValue_expansion`

 The concrete shifted-row expansion needed by the symbolic incidence
argument: all coefficients are evaluations of linear forms in the input. 

### `eval_zero_rowValue`

 A row equal to the coordinate selector at zero recovers that coordinate. 

### `rowGlobalPolynomial`

 The source's sum of products using genuine polynomial rows, rather than
arbitrary assignment-dependent scalar paths. 

### `natDegree_rowGlobalPolynomial_le`

 The polynomial-row form of the global degree bound. 

### `eval_zero_eq_factor_count`

 Exact table interpolation and paths with the correct value at zero recover
the finite factor count, as an element of the coefficient ring. 

### `eval_zero_row_eq_factor_count`

 The same count identity for the source's polynomial-row construction. 

### `interpolatedTable`

 The explicit tensor-product Lagrange interpolant of a Boolean factor. 

### `interpolatedGlobalPolynomial`

 The source's H, with the factor polynomials constructed by interpolation. 

### `eval_zero_interpolatedGlobalPolynomial`

 H(0) is the exact factor count in the coefficient ring. 

### `natDegree_interpolatedGlobalPolynomial_le`

 The actual interpolated H satisfies the global degree bound. Its factor
degrees are proved from Lagrange interpolation, not postulated. 

### `integerLabel_globalPolynomial_spec`

 Literal integer-label specialization of both conclusions in Section 4.1.
The result constructs H and proves the displayed m*k*(p−1)*r bound. 

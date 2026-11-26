---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Moments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Moments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Moments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite coefficient-weighted moment extraction

The exponent used as a moment weight and the exponent used for coefficient
extraction are independent until the final diagonal sum.  The only support
hypothesis is containment of each input polynomial's support in the retained
finite index set.  In particular no independence of monomial functions on the
finite input set is assumed.

An additive-map corollary permits a final linear operation on canonical
representatives, such as evaluating the retained U polynomial at one.  It does
not assert that this operation is multiplicative on a truncated quotient.


### `exponent_le_total`

 Each coordinate exponent is bounded by the total exponent. 

### `retained`

 The finite set of exponents of total degree at most `N`.

This is a denotational finite-set construction; no runtime claim is made for
enumerating this set via the auxiliary coordinate box used in this definition.


### `weight`

 The scalar monomial weight at an input valuation. 

### `moment`

 A polynomial-valued moment; the moment index is not a formal variable. 

### `coeff_moment`

 Coefficient and moment indices need not agree. 

### `sum_weight_coeff_eq_eval`

 Evaluation is the coefficient-weighted sum over any retained set containing
the polynomial support.  Extra retained indices contribute zero. 

### `sum_coeff_moment_eq_sum_eval`

 Equations (4.6)-(4.7): the diagonal of all coefficient-weighted moments
recovers the sum of input-dependent polynomial evaluations. 

### `sum_coeff_moment_eq_sum_eval_of_totalDegree_le`

 The concrete degree hypothesis used by canonical truncation supplies the
support condition.  `M` may be any finite set containing all exponents through
degree `N`, including the manuscript's retained monomial list. 

### `sum_retained_coeff_moment_eq_sum_eval`

 The manuscript's degree-bounded moment extraction, with the finite retained
index set constructed explicitly. 

### `sum_map_coeff_moment_eq_sum_map_eval`

 Any additive map may be applied after canonical coefficient extraction.
Only additivity, not multiplicativity, is needed for the last operation. 

### `sum_eval_one_coeff_moment_eq_sum_eval_one_eval`

 The last operation in (4.7), on genuine polynomial representatives.
Taking U = 1 is used only after forming the complete moments. 

### `sum_slots_coeff_moment_eq_sum_slots_eval`

 A coefficientwise interface for nested polynomial representations.
The finite slots may, for example, be the retained U exponents at a fixed Z
coefficient.  Summing slots commutes with the complete moment calculation. 

### `sum_nested_moments_eq_sum_substX`

 Whole-polynomial moment extraction with U outermost, Z in the middle,
and the X variables innermost.  This is the representation used by Truncation.
Both U and Z remain formal in this identity. 

### `sum_nested_moments_eval_one_eq_sum_evalXU`

 The whole-polynomial form of (4.6)-(4.7), including U = 1 only after
the full canonical moments have been formed and their X coefficients extracted. 

### `sum_retained_nested_moments_eval_one_eq_sum_evalXU`

 The finite-type, degree-cutoff interface used by the counting module. 

---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SparsificationBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quantitative sparsification budgets

The old fixed-budget module is unchanged. This module uses its actual C, L, z
recurrence and proves a quadratic upper bound for a doubling search in the
inverse budget. The bound is deliberately coarser than the manuscript's
inverse-budget times logarithm estimate.


### `ReciprocalAdmissible`

 Exact natural-arithmetic test for the reciprocal budget 1/s. 

### `dyadic_witness`

 A completely discrete quadratic witness: test a power of two near s². 

### `exists_quantitative_witness`

 The constants K and T depend only on k, not on the inverse budget s. 

### `chooseExponent`

 The least passing doubling index; the candidate at index e is 2^e.
The candidate 1 is harmlessly rejected by the test's M ≥ 2 condition. 

### `chooseM_finite_execution`

 The scan tests doubling candidates, and its call count is bounded above. 

### `thresholdCap`

 A polynomial cap on every threshold through width k. 

### `reciprocalIndex`

 Conservative reciprocal rounding for a positive rational a/b ≤ 1.
This is ceil(b/a), with a minimum of two. Only the rounded index appears in
the exponents used by the doubling search. 

### `polynomialBound_at_reciprocalIndex`

 Every polynomial bound in the rounded inverse index becomes a polynomial
bound in the real reciprocal budget, uniformly in the numerator and denominator. 

### `rational_num_data`

 Positive rationals supply the positive natural numerator used by rounding. 

### `chooseForSigma`

 The complete selector accepts a rational budget directly. Numerator and
denominator are inspected only to compute the small reciprocal index. 

### `polynomialBound_at_sigma`

 A generic polynomial bound transported to the reciprocal of a rational.
Its witnesses are independent of the numerator and denominator. 

---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SmallInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SmallInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SmallInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Absorbing the finitely many small variable counts

These are inequalities of real powers and finite maxima.  They establish no
machine execution bound by themselves: a parser or solver must separately be
proved to obey the displayed polynomial/exhaustive-search upper bound.

The variable count is bounded, but the explicit input length remains arbitrary.
The finite-maximum lemmas therefore maximize coefficients and polynomial degrees
in the variable count, while retaining the polynomial dependence on input length.


### `savedExponential`

 The exponential part of the claimed time bound, including at zero variables. 

### `bruteForceFactor`

 The explicit loss for exhaustive search on variable counts at most `B`. 

### `inputPolynomial`

 A polynomial factor in explicit input length, with a safe value at length zero. 

### `packedDimension`

 The actual dimension obtained by packing at most `ell` bits into each coordinate. 

### `variables_le_packed_capacity`

 Packing at positive capacity covers every input bit. 

### `packedDimension_eq_zero_iff`

 Zero packed dimension really means zero bits, provided the capacity is positive. 

### `variables_le_threshold`

 The strict dimension cutoff implies the manuscript's weaker non-strict bit cutoff. 

### `bruteForce_le_saved`

 Explicit finite-threshold absorption, with the same factor as Section 6.4. 

### `nat_bruteForce_le_saved`

 The same bound for the natural-number exhaustive-search count. 

### `packed_bruteForce_le_saved`

 Direct form using the fixed bit capacity and dimension threshold. 

### `overhead_bruteForce_le_saved`

 Exhaustive search multiplied by any nonnegative input-dependent overhead. 

### `polynomial_bruteForce_le_saved`

 Polynomial time per candidate retains its input-length degree after absorption. 

### `inputPolynomial_mul`

 Polynomial factors multiply by adding degrees. 

### `inputPolynomial_mono_degree`

 Increasing the polynomial degree is harmless because the base is at least one. 

### `inputPolynomial_of_linear_bound`

 Linear control of variable count by encoding length transfers polynomial overhead. 

### `finiteCoefficient`

 A finite maximum of normalized coefficients. It is positive even at threshold zero. 

### `finiteDegree`

 Maximum degree across the finite set of small variable counts. 

### `coefficient_le_finiteCoefficient`

 The finite maximum dominates each normalized coefficient in its range. 

### `finite_polynomial_family_le_saved`

 Even when each small variable count has its own polynomial degree and coefficient,
finite maxima give one positive coefficient and one degree for all explicit input lengths. 

### `exists_uniform_finite_polynomial_bound`

 A genuine uniform bound for a finite family of input-length polynomials.
The coefficient and degree are chosen before both the input length and the
particular small variable count. 

### `finiteDegree_zero`

 At threshold zero, the finite maxima include exactly the zero-variable case. 

### `parsing_plus_bruteForce_le_saved`

 Parsing may be charged additively without changing the common polynomial degree.
The numerical coefficients are fixed independently of the input. 

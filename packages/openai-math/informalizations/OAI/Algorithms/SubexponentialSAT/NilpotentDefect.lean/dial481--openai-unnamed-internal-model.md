---
{
  "module": "OAI/Algorithms/SubexponentialSAT/NilpotentDefect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/NilpotentDefect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/NilpotentDefect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Divisibility of the marked defect

After the input coordinates have been substituted, the coefficient of U in
each incidence argument is divisible by p. Polynomial operations preserve
the stronger invariant that the coefficient of U^j is divisible by p^j.
This proves the high-U vanishing needed by canonical truncation.


### `PowerDivisible`

 The coefficient of the j-th power carries at least j copies of p. 

### `high_coeff_eq_zero`

 Nilpotence kills every complete high-degree coefficient, after evaluation. 

### `evalInputs`

 Identical to Truncation.substX; kept here to avoid a module import cycle. 

### `evalInputs_incidenceArgument`

 Substitution retains U as a formal variable. The entire U coefficient
is the lifted-value defect, without any termwise divisibility assertion. 

### `powerDivisible_incidenceArgument`

 The actual incidence polynomial has the divisibility invariant as soon
as its evaluated defect is divisible by p. No hypothesis on individual
symbolic monomials is used. 

### `powerDivisible_factor_product`

 Divisibility for the full product of actual table polynomials at the
actual marked incidence arguments. 

### `highU_factor_product`

 This is precisely the high-U premise of Truncation.canonical_substitution,
proved for the complete incidence-factor construction. 

### `unitInverse`

 A total inverse selector; its laws require a proved unit hypothesis.
This mathematical selector does not claim a computational cost. 

### `geometricInverse`

 Explicit finite geometric correction of an approximate inverse b. 

### `residueInverse`

 The residue inverse is lifted by any specified section, then corrected
by a finite geometric sum in the original ring. 

### `isUnit_of_nilpotent_kernel`

 A unit lifts along a surjection whose kernel consists of nilpotents.
The proof corrects any lifted inverse by the finite geometric-series unit. 

### `isUnit_of_lambda_residue_ne_zero`

 Concrete prime-power extension: every element with nonzero residue is
a unit. The residue field is the quotient by the reduced irreducible F. 

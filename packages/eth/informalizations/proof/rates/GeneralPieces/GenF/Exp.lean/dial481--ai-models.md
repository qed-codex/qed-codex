---
{
  "module": "proof/rates/GeneralPieces/GenF/Exp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Exp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Exp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponential of a formal power series without constant term

"Exponentials of these are formal power series in the x_n, x'_n" (Appendix B, the paragraph on
generating functions). For a commutative ℚ-algebra R and a set X of variables, `expW w` is
Σ_n wⁿ/n! for a power series w in the variables X over R without constant term: the coefficient of a
monomial of degree d is that of the finite sum over n ≤ d. Proved here: the constant term of e^w is
1,
e^{a+b} = e^a·e^b, a ring homomorphism applied to the coefficients commutes with the exponential,
and: if the coefficient of every monomial α in w is a rational number times ε^{wt α}, for an
additive weight wt, then so it is
in e^w, with a rational number that does not depend on ε or on R (`coeff_expW_of_weight`). 

 ### A sum over a triangle and over a square 

### `sum_triangle`

 If F i j = 0 for i + j ≥ N, the sum of F over i + j < N is the sum over i, j < N. 

 ### The definition 

### `expN`

 Σ_{n < N} wⁿ/n!. 

### `expW`

 e^w = Σ_n wⁿ/n!, for w without constant term: the coefficient of a monomial of degree d is taken
from the sum over n ≤ d. 

### `coeff_pow_eq_zero`

 wⁿ has no monomials of degree less than n. 

### `coeff_expW`

 More terms of the sum do not change the coefficient. 

### `coeff_mul_congr`

 The coefficient of α in a product depends only on the coefficients of the monomials of degree at
most that of α. 

### `coeff_pow_mul_pow_eq_zero`

 a^i·b^j has no monomials of degree less than i + j. 

 ### The rules 

### `constantCoeff_expW`

 The constant term of e^w is 1. 

### `add_pow_div`

 (a+b)ⁿ/n! = Σ_{i+j=n} (a^i/i!)·(b^j/j!). 

### `expW_add`

 e^{a+b} = e^a·e^b. 

### `map_expN`

 A ring homomorphism between rings of power series commutes with the finite sums. 

### `map_expW`

 A ring homomorphism applied to the coefficients commutes with the exponential. 

### `hom_expW`

 A ring homomorphism Φ of the ring of power series commutes with the exponential, if the
coefficient of α in Φ f depends only on the coefficients of f at the monomials of degree at most
that of α. 

 ### Coefficients that are numbers times powers of one element 

### `twF`

 The coefficient of every monomial α of a power series over ℚ is multiplied by ε^{wt α}. 

### `tw`

 This is a ring homomorphism, because the weight is additive. 

### `coeff_expW_of_weight`

 If the coefficient of every monomial α in w is q_α·ε^{wt α} with a rational number q_α, then its
coefficient in e^w is (the coefficient of α in e^q)·ε^{wt α}: the number is the same for every ε and
every R. 

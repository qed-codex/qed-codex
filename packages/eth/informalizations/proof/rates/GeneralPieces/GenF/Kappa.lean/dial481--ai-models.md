---
{
  "module": "proof/rates/GeneralPieces/GenF/Kappa.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Kappa.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Kappa.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 9 (Appendix B), on the operators Q_s: the coefficients of κ and κ', and those of e^κ and e^{κ'}

Two sentences of the proof. From the paragraph "Generating functions": κ = Σ_{j,n}
x_j·x'_n·Γ_{j,n}·ε₊^{j+n}, "because the sum over k is the left side of (49)", and "in the same way"
κ' = Σ_{j,n} x_j·x'_n·Γ_{j,n}·ε₋^{j+n}; here both are stated coefficient by coefficient
(`coeff_kap_false`, `coeff_kap_true`). From the paragraph "One Laurent polynomial":
"the coefficient of x^{μ'}·x'^{ν'} in e^κ is Γ_{μ',ν'}·ε₊^{|μ'|+|ν'|} for a number Γ_{μ',ν'}, and in
e^{κ'} it is Γ_{μ',ν'}·ε₋^{|μ'|+|ν'|}" (`coeff_expW_kap_false`, `coeff_expW_kap_true`).
A monomial x^{μ'}·x'^{ν'} is its exponent α here; |μ'| + |ν'| is `wtX α`, and the number Γ_{μ',ν'}
is `gam α`, the coefficient of the monomial in the exponential of the power series
Σ_{j,n} Γ_{j,n}·x_j·x'_n over ℚ. κ' is κ in the second reading, where the inner variable is ω₂ and
the inner family is B. 

 ### The weight of a monomial in the x_n, x'_n 

### `wtX`

 |μ'| + |ν'| for the monomial x^{μ'}·x'^{ν'}: the variables x_n and x'_n have weight n. 

### `wtX_list_sum`

 The weight of the monomial x^μ (or x'^μ) made from the list of the parts of μ is |μ|, if the
variable with index n has weight n. 

### `eq_add_single`

 A monomial of degree 2 in which two different variables occur is their product. 

 ### The numbers Γ 

### `GamX`

 Γ_{j,n} at the pair of variables (x_j, x'_n) with j, n ≥ 1, and 0 at all other pairs. 

### `kapQ`

 Σ_{j,n} Γ_{j,n}·x_j·x'_n, a power series over ℚ. 

### `gam`

 The number Γ_{μ',ν'}: the coefficient of x^{μ'}·x'^{ν'} in the exponential of Σ_{j,n}
Γ_{j,n}·x_j·x'_n. 

 ### The sum over k 

### `kapS_eq_P`

 The sum over k in the first reading: Γ_{p,q}·ε₊^{p+q}. 

### `kapS_eq_M`

 The sum over k in the second reading, where p is the index of x'_p and q that of x_q:
Γ_{q,p}·ε₋^{q+p}. 

### `entry_false`

 One entry of the bilinear form κ, first reading. 

### `entry_true`

 One entry of the bilinear form κ, second reading. 

 ### κ, κ' and their exponentials 

### `coeff_kap_false`

 The coefficients of κ: those of Σ_{j,n} Γ_{j,n}·x_j·x'_n, times ε₊^{j+n}. 

### `coeff_kap_true`

 The coefficients of κ': those of Σ_{j,n} Γ_{j,n}·x_j·x'_n, times ε₋^{j+n}. 

### `coeff_expW_kap_false`

 The coefficient of x^{μ'}·x'^{ν'} in e^κ is Γ_{μ',ν'}·ε₊^{|μ'|+|ν'|}. 

### `coeff_expW_kap_true`

 The coefficient of x^{μ'}·x'^{ν'} in e^{κ'} is Γ_{μ',ν'}·ε₋^{|μ'|+|ν'|}, with the same number. 

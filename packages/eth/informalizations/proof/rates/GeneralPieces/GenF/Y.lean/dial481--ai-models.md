---
{
  "module": "proof/rates/GeneralPieces/GenF/Y.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Y.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Y.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, paragraph "Generating functions": the series Y, and e^{B⁺}e^{B⁻} = Σ_ν x'^ν·Y(t^ν, ω₂)/ν!

The paper puts Y(a, ω) = Σ_r a[r]·ω^{r−h'} for a = t^μ of weight h'. Here `Yent e b τ σ` is the
entry (τ, σ) of its matrix, for the list b of the parts and with e x in the place of ω^x. The
operator a[r] raises the weight by r,
so the sum over r has one term. `Yent_cons` is the recursion Y(t_n·a, ω) = J_n^+(ω)·Y(a, ω) + Y(a,
ω)·J_n^-(ω), which is the recursion that defines the matrices a[r], multiplied by the powers of ω.
"Expanding the exponentials" is proved for the outer family (B in the first reading, A in the
second), applied to a monomial t^σ' (`bra_coeff_outer`, `Y1`): the series e^{B⁺}e^{B⁻}·t^σ'
satisfies
∂/∂x'_n (e^{B⁺}e^{B⁻}·t^σ') = J_n^+(v)·e^{B⁺}e^{B⁻}·t^σ' + e^{B⁺}e^{B⁻}·J_n^-(v)·t^σ'
(`pderiv_xo_outer`), which is the same recursion, and ν! times the coefficient of x'^ν is got by
differentiating once for every part of ν.
This takes the place of the count of the subsets with given multiplicities. The variables of the
inner family do not occur in this series (`pderiv_xi_outer`). 

 ### The series Y 

### `Yent`

 The entry (τ, σ) of Y(t^ν, ω) = Σ_r t^ν[r]·ω^{r−h}, where b lists the parts of ν, h is their sum
and e x stands for ω^x: t^ν[r] raises the weight by r, so only r = |τ| − |σ| contributes. 

### `Yent_nil`

 Y(1, ω) is the identity. 

### `Yent_cons`

 Y(t_n·t^ν, ω) = J_n^+(ω)·Y(t^ν, ω) + Y(t^ν, ω)·J_n^-(ω), entry by entry: the recursion for the
operators t^ν[r], multiplied by the powers of ω. 

 ### General rules 

### `der_prod`

 The product rule for a product over a multiset. 

 ### The outer family 

### `outer`

 e^{B⁺}·e^{B⁻}·t^σ'. 

### `cB`

 The coefficient of ∇_k in J_n^-(v), as a function of the variable beside which J_n^-(v) stands. 

### `pderiv_ket`

 ∂/∂x_i of e^{B⁻}·t^σ': one of the factors is differentiated. 

### `pderiv_xo_outer`

 ∂/∂x'_n (e^{B⁺}e^{B⁻}·t^σ') = J_n^+(v)·e^{B⁺}e^{B⁻}·t^σ' + e^{B⁺}e^{B⁻}·J_n^-(v)·t^σ'. 

### `pderiv_xi_outer`

 The variables of the inner family do not occur in e^{B⁺}e^{B⁻}·t^σ'. 

### `bra_coeff_outer`

 "Expanding the exponentials gives e^{B⁺}e^{B⁻} = Σ_ν x'^ν·Y(t^ν, v)/ν!": ν! times the
coefficient of x'^ν in e^{B⁺}e^{B⁻}·t^σ' has, at t^τ, the coefficient ⟨τ|Y(t^ν, v)|σ'⟩. 

### `Y1`

 The same with the definitions written out. 

### `op_eq_zero_of_zero_mem`

 t₀ does not occur: the entries of t^ν[r] in the rows of the monomials with t₀ vanish. 

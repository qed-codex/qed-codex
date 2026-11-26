---
{
  "module": "proof/rates/GeneralPieces/GenF/Y2.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Y2.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Y2.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, paragraph "Generating functions": e^{A⁺}·e^{A⁻} = Σ_μ x^μ·Y(t^μ, ω₁)/μ!

"Expanding the exponentials gives e^{A⁺}e^{A⁻} = Σ_μ x^μ Y(t^μ, ω₁)/μ!." Here the coefficients are
not found by expanding, but from the differential equations in the variables x_n: the derivative of
⟨e^{A⁺}·e^{A⁻}·w⟩ with respect to x_n is ⟨J_n^+·e^{A⁺}e^{A⁻}·w⟩ + ⟨e^{A⁺}e^{A⁻}·J_n^-·w⟩
(`pderiv_GG_xi`), and this is the recursion (O2), Y(t_n·a') = J_n^+·Y(a') + Y(a')·J_n^-.
`y0 a σ` is the linear form p ↦ ⟨t^σ| Y(a, u) p⟩ on the polynomials in the t_k, defined by this
recursion; on a monomial t^τ it is the entry (σ, τ) of the matrix of a[r], r = |σ| − |τ|, times
u^{r−|a|} (`y0_monomial`).
`Y2`: μ! times the coefficient of x^μ in ⟨e^{A⁺}e^{A⁻}·w⟩ is `y0` applied to w. 

 ### The linear form ⟨t^σ| Y(a, u) · ⟩ 

### `y0`

 p ↦ ⟨t^σ| Y(a, u) p⟩, by the recursion Y(t_n·a') = J_n^+(u)·Y(a') + Y(a')·J_n^-(u). 

### `JmU_monomial`

 J_n^-(u) on a monomial. 

### `y0_monomial`

 On the monomial t^τ: the entry (σ, τ) of the matrix of a[r], r = |σ| − |τ|, times u^{r−|a|}. 

 ### The differential equations of ⟨e^{A⁺}·e^{A⁻}·w⟩ 

### `GG`

 ⟨e^{A⁺}·e^{A⁻}·w⟩: the coefficient of t^σ in e^{A⁺}·e^{A⁻}·w. 

### `pderiv_GG_xo`

 The derivative with respect to a variable of the outer family falls on w. 

### `pderiv_GG_xi`

 The derivative with respect to the variable x_n of the inner family: ⟨J_n^+·e^{A⁺}e^{A⁻}·w⟩ +
⟨e^{A⁺}e^{A⁻}·J_n^-·w⟩, if w does not depend on x_n. 

### `Y2`

 "e^{A⁺}e^{A⁻} = Σ_μ x^μ·Y(t^μ, ω₁)/μ!": the derivative of ⟨e^{A⁺}e^{A⁻}·w⟩ with respect to the
variables x_n, n in a, has the constant term ⟨t^σ| Y(a, u) w₀⟩, w₀ the constant term of w, if w does
not
depend on the variables of the inner family. By `borel_zero` this is μ! times the coefficient of
x^μ. 

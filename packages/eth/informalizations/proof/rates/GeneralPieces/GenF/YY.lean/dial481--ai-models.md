---
{
  "module": "proof/rates/GeneralPieces/GenF/YY.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/YY.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/YY.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s: f₊ = ⟨Y(a, ω₁)·Y(b, ω₂)⟩ is μ!·ν! times the coefficient of x^μ·x'^ν in ⟨e^{A⁺}e^{A⁻}·e^{B⁺}e^{B⁻}⟩

The paper (proof of Lemma 9): "Expanding the exponentials gives e^{A⁺}e^{A⁻} = Σ_μ x^μ·Y(t^μ,
ω₁)/μ!, and likewise e^{B⁺}e^{B⁻} = Σ_ν x'^ν·Y(t^ν, ω₂)/ν!", and "let f₊ = ⟨Y(a, ω₁)·Y(b, ω₂)⟩".
Here the two expansions are hypotheses, in the
form of the interface statements below: `StY1`, `StY1'` for the family that is applied first,
`StY2`, `StXo` for the other. What is proved is their composition: the product of the two operators
is the sum over the
monomials t^τ in between (`map_eq_fP`), "by (O1)" only the τ of one weight contribute to the
coefficient of each power of the outer variable, and this sum is the entry of the product a[r]∘b[−r]
of matrices.
The result is the interface statement `StY` (`stY_of`), for both readings. 

### `StY1`

 The expansion of e^{B⁺}e^{B⁻}: ν! times the coefficient of x'^ν in e^{B⁺}e^{B⁻}·t^σ' has at t^τ
the coefficient ⟨τ|Y(t^ν, v)|σ'⟩ = ⟨τ|t^ν[r]|σ'⟩·v^{r−|ν|} with r = |τ| − |σ'|. 

### `StY1'`

 The variables of the inner family do not occur in e^{B⁺}e^{B⁻}·t^σ'. 

### `StOp0`

 t₀ does not occur: the entries of t^ν[r] in the rows of the monomials with t₀ vanish. 

### `StY2`

 The expansion of e^{A⁺}e^{A⁻}: μ! times the coefficient of x^μ in ⟨t^σ|e^{A⁺}e^{A⁻}·w⟩, written
as a derivative at 0, is a linear form applied to w, and on t^τ the form is
⟨σ|Y(t^μ, u)|τ⟩ = ⟨σ|t^μ[r]|τ⟩·u^{r−|μ|} with r = |σ| − |τ|. Here w is free of the variables of the
inner family. 

### `StXo`

 The derivatives with respect to the variables of the outer family pass through
⟨t^σ|e^{A⁺}e^{A⁻}·⟩. 

### `form_eq_sum`

 A linear form on the polynomials in the t_k is determined by its values on the monomials. 

### `map_eq_fP`

 ⟨Y(a, u)·Y(b, v)⟩ = Σ_r ⟨a[r]∘b[−r]⟩·u^{r−h'}·v^{−r−h}: if g has the coefficients ⟨τ|Y(b, v)|σ'⟩
and the form ℓ has the values ⟨σ|Y(a, u)|τ⟩, then ℓ applied to g is f₊. 

### `stY_of`

 μ!·ν! times the coefficient of x^μ·x'^ν in ⟨e^{A⁺}e^{A⁻}·e^{B⁺}e^{B⁻}⟩ is f₊ = ⟨Y(a, u)·Y(b,
v)⟩, from the expansions of the two pairs of exponentials. 

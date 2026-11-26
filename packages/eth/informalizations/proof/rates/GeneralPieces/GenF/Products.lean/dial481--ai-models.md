---
{
  "module": "proof/rates/GeneralPieces/GenF/Products.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Products.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Products.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, paragraph "Generating functions": e^{A⁻} and the products of four exponentials
Here u and v stand for the paper's ω₁ and ω₂ in the first reading, and for ω₂ and ω₁ in the second.
The inner variables are the x_n of A and the outer variables the x'_n of B (in the second reading,
those of B and of A).
A⁻ = Σ_n x_n·J_n^-(u) acts on `W`: J_n^-(u) is applied to the coefficient of every power of v and of
every monomial in the x_n, x'_n. Its exponential `Phi` is Σ_m (A⁻)^m/m!, a finite sum in the
coefficient
of every monomial in the x_n, x'_n. e^{B⁺} and e^{A⁺} are the multiplications by the exponentials of
B⁺ and of the part of A⁺ with l ≤ E, and e^{B⁻}·t^σ' is `ket`.
`plusSide` is ⟨e^{A⁺}·e^{A⁻}·e^{B⁺}·e^{B⁻}⟩ and `normal` is ⟨𝒩⟩ = ⟨e^{A⁺}·e^{B⁺}·e^{A⁻}·e^{B⁻}⟩, for
the monomials t^σ (coefficient taken) and t^σ' (argument), as power series in the x_n, x'_n over
`S`.
The reading is chosen by `rd`: `rd = false` is the first reading, the paper's order (in 𝓛₊);
`rd = true` is the second, in which the names A and B are exchanged (in 𝓛₋).
These are defined for every E; they are the paper's entries when |σ| ≤ E, because A⁺ is cut at l ≤ E
and e^{A⁺} stands leftmost, and then they do not depend on E. Definitions only. 

### `JmT`

 J_n^-(u), applied to the coefficient of every power of v. 

### `DD`

 The operator that stands beside each variable in A⁻: J_n^-(u) beside the inner variable with
index n, and 0 beside the outer variables. 

### `Phi`

 e^{A⁻}. 

### `plusSide`

 ⟨e^{A⁺}·e^{A⁻}·e^{B⁺}·e^{B⁻}⟩. 

### `normal`

 ⟨𝒩⟩ = ⟨e^{A⁺}·e^{B⁺}·e^{A⁻}·e^{B⁻}⟩. 

### `aL`

 The exponent of the monomial ∏_{n ∈ a} x_{ι n}, for a list a of parts. 

### `StTwoOrders`

 One half of the display in the proof of Lemma 9 that writes both orders of the products through
𝒩, as an equation between the entries ⟨t^σ| · t^σ'⟩: ⟨e^{A⁺}e^{A⁻}·e^{B⁺}e^{B⁻}⟩ = e^κ·⟨𝒩⟩, in 𝓛₊ in
the first reading
and in 𝓛₋ in the second (there A and B are exchanged and κ is κ'). It holds wherever A⁺ is cut. 

### `StN1`

 For |σ| ≤ E, the coefficient of every monomial in the x_n, x'_n in ⟨𝒩⟩ lies in 𝓛, and it is the
same element of 𝓛 in both readings. 

### `StN2`

 n_{∅,∅} = [σ = σ']. 

### `StN3`

 For σ = σ' = ∅ (the paper's case E = 0) we have ⟨𝒩⟩ = 1, wherever A⁺ is cut. 

### `StY`

 μ!·ν! times the coefficient of x^μ·x'^ν in ⟨e^{A⁺}e^{A⁻}·e^{B⁺}e^{B⁻}⟩ is ⟨Y(a,u)·Y(b,v)⟩ = Σ_r
⟨a[r]∘b[−r]⟩·u^{r−h'}·v^{−r−h}; a lists the parts of the inner, b of the outer family,
and σ, σ' have the same weight, as in the paper; all parts are positive, σ and σ' have no part 0 (t₀
is not used), and |σ| ≤ E. 

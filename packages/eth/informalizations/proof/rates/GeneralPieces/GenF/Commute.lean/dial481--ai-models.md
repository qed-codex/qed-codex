---
{
  "module": "proof/rates/GeneralPieces/GenF/Commute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Commute.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Commute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Lemma 9, paragraph "Generating functions": e^{A⁻}e^{B⁺} = e^κ·e^{B⁺}e^{A⁻} and the display that compares the two orders of the four exponentials

e^{A⁻} is a ring homomorphism. It maps B⁺ = Σ_k 𝖡_k·t_k to B⁺ + κ (`Phi_Bp`): A⁻ applied to B⁺ is κ =
Σ_{p,q} x_p·x'_q·J_p^-(ω₁)(J_q^+(ω₂)), where J_p^-(ω₁)(J_q^+(ω₂)) is the sum over k in the display
for κ
(`JmT_JpV`), and A⁻ applied to κ is 0. Hence e^{A⁻}(e^{B⁺}·w) = e^κ·e^{B⁺}·e^{A⁻}w
(`Phi_expW_Bp_mul`). Between e^{A⁺} on the left and e^{B⁻}·t^σ' on the right this is the display
with 𝒩 = e^{A⁺}e^{B⁺}e^{A⁻}e^{B⁻} (`stTwoOrders`): its first half, in 𝓛₊, for one value of the
Boolean `rd`, and its second half, in
𝓛₋ with A and B exchanged, for the other. In the Lean names the letters u and v stand for the
paper's ω₁ and ω₂. 

### `JmU_C_mul_X`

 J_p^-(ω₁) on a multiple of t_k. 

### `JmT_JpV`

 J_p^-(ω₁) applied to J_q^+(ω₂) is the sum over k in the display for κ. 

### `JmT_emb`

 J_p^-(ω₁) kills the series without t_k. 

### `kq`

 The coefficient of x_i·x_{i'} in κ. 

### `DD_sel`

 The operator beside x_i in A⁻, applied to the coefficient of x_v in B⁺. 

### `dsum_Bp`

 A⁻ applied to B⁺ is κ. 

### `Phi_Bp`

 e^{A⁻} maps B⁺ = Σ_k 𝖡_k·t_k to B⁺ + κ. 

### `Phi_expW_Bp_mul`

 e^{A⁻}·e^{B⁺} = e^κ·e^{B⁺}·e^{A⁻}. 

### `stTwoOrders`

 The display on the two orders, one half: e^{A⁺}e^{A⁻}·e^{B⁺}e^{B⁻} = e^κ·𝒩, as an equation
between the matrix entries. For one value of `rd` this is the equation in 𝓛₊, for the other (A and B
exchanged) the one in 𝓛₋. 

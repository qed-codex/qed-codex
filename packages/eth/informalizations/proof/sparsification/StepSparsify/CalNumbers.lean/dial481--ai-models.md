---
{
  "module": "proof/sparsification/StepSparsify/CalNumbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CalNumbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CalNumbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Calabro's numbers fit the bounds of the plan

This file proves `StAlphaS` and `StCalNumbers` of proof/sparsification/StepSparsify/Defs.lean.
Throughout K = max(k, 3), ε = 1/2^s, α = `alphaS k s` and τ = `tauOf s` = 2^(4s+17).
`stAlphaS`: with this ε the two numbers under a ceiling sign, x = 32(K−1)²·2^s and 2(K−1)²·2^s·⌈log₂
x⌉, are natural numbers, so the ceilings disappear.
`stCalNumbers`: K² ≤ α and 2 ≤ α are in `Cal.stAlpha`. By `Cal.stAlphaLe`, 32α ≤ (8K·2^s)³; as K ≤
3k and k ≤ k² ≤ 2^s, the base is at most 2^(2s+5), so 32α ≤ 2^(6s+15) ≤ τ² (`alpha_le`).
By fact (iv), β₁ + … + β_{k−1} ≤ 4·(32α)^(k−2) ≤ 4·τ^(2(k−2)) ≤ τ^(2k). By `Cal.stDegSum`, 2·(θ₀ + … +
θ_{k−1}) + 2 ≤ 18 + (32α)^(k−1) ≤ 18 + τ^(2(k−1)) ≤ τ^(2k) = 2^(2k(4s+17)).
For k = 1 the two sums are β₀ = 0 and θ₀ = 2. 

### `stAlphaS`

 α without fractions: α = 2(K−1)²·2^s·⌈log₂(32(K−1)²·2^s)⌉ with K = max(k, 3). 

### `eps_pos`

 ε = 1/2^s is positive. 

### `eps_le_one`

 ε = 1/2^s is at most 1. 

### `le_alphaS`

 2 ≤ α and K² ≤ α, for all k and s. 

### `alpha_le`

 32α ≤ τ², for k ≥ 1 and k² ≤ 2^s. 

### `stCalNumbers`

 Calabro's numbers fit the bounds of the plan: 1 ≤ α, k² ≤ α, and the two sums are small enough. 

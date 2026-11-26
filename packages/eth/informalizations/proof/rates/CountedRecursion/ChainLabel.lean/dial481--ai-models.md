---
{
  "module": "proof/rates/CountedRecursion/ChainLabel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ChainLabel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ChainLabel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The bounds for λ and B, from one depth to the next

`lamAt` and `bitsAt` (`RecursionDefs.lean`) are the bounds Λ_j, 𝔅_j for λ and B at the depth j of
the recursion from an outermost instance (ℓ, λ, B). For j < ℓ, Λ_j is the floor of ((ρ +
3ζ_j)g_j⁴Λ_{j+1} + (c/4)g_j⁴log(2Λ_{j+1}) + K_j²)/K_j² and 𝔅_j is the B' of Lemma 8 for Λ_{j+1},
𝔅_{j+1} (`lamAt_of_lt`, `bitsAt_of_lt`).
From this `chainLabel`: 1 ≤ Λ_j ≤ g_j⁴Λ_{j+1} + 1, 1 ≤ 𝔅_j, and the outer inequality of «K²L ≤ U +
2ζN + K² ≤ (ρ + 3ζ)N + (c/4)g⁴log(2λ) + K²» for the bounds. 

### `lamAt_self`

 At the depth ℓ the bound for λ is λ itself. 

### `bitsAt_self`

 At the depth ℓ the bound for B is B itself. 

### `lamAt_of_lt`

 Λ_j from Λ_{j+1}. 

### `bitsAt_of_lt`

 𝔅_j from Λ_{j+1} and 𝔅_{j+1}. 

### `zeta_bounds`

 0 < ζ_j ≤ 1/32. 

### `quotient_bounds`

 The number whose floor is Λ_j lies between 1 and g⁴Λ + 1. 

### `two_add_le_K_sq`

 2 + c/4 ≤ K_j². 

### `quotient_at`

 The facts on the quotient, for the numbers of the depth j and any Λ ≥ 1 one level up. 

### `lamAt_pos`

 1 ≤ Λ_j for every j ≤ ℓ. 

### `one_le_lamAt`

 Λ_j ≥ 1. 

### `one_le_bitsAt`

 1 ≤ 𝔅_j for every j ≤ ℓ. 

### `chainLabel`

 `ChainLabel` holds: for j < ℓ, 1 ≤ Λ_j, 1 ≤ 𝔅_j, Λ_j ≤ g_j⁴Λ_{j+1} + 1, and K_j²Λ_j ≤ (ρ +
3ζ_j)g_j⁴Λ_{j+1} + (c/4)g_j⁴log(2Λ_{j+1}) + K_j². 

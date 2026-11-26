---
{
  "module": "proof/rates/CountedRecursion/RoomWithin.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RoomWithin.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RoomWithin.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The room of the algorithm of the pieces

The paper bounds no memory. The largest label length of the recursion is Λ_j for some depth j ≤ ℓ;
with X_j = K_j(Λ_j + 𝔅_j), `room c Λ_j` = (2^{cΛ_j} + (2Λ_j)^c + 8)((2Λ_j)^c + 8) ≤
2^{cΛ_j}·X_j^{2c+3} (`room_le_aux`),
and c ≤ e_jK_j² (`c_le_e_mul`: e_j ≥ 2^{−j−1}, 2^j(c + 5)^jK_0² ≤ K_j²). So the room at Λ_j is at
most the bound of the theorem for depth j, with C₀ = 2c + 3, hence at most that of the outermost
instance (`levelBound_le_top`). 

### `room_le_aux`

 (u + P + 8)(P + 8) ≤ u·X^{2c+3}, for P ≤ X^c, 8 ≤ X, c ≥ 1, u ≥ 1. 

### `c_le_e_mul`

 c ≤ e_jK_j². 

### `roomIsWithinTheBoundFrom`

 `RoomIsWithinTheBoundFrom`, with C₀ = 2c + 3. 

### `roomIsWithinTheBound`

 `RoomIsWithinTheBound`. 

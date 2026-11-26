---
{
  "module": "proof/rates/CountedRecursion/TotalRoom.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/TotalRoom.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/TotalRoom.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sizes of the states of the tower

The paper bounds no memory. With X_j = K_j(Λ_j + 𝔅_j): X_j ≤ X_{j+1}^{c+5} (`ChainBase`), so X_j ≤
X_ℓ^{(c+5)^{ℓ−j}} ≤ X_ℓ^{K_ℓ} by (c + 5)^ℓ ≤ K_ℓ (`ChainLevels`).
So ∑_{j≤ℓ} X_j^C ≤ (ℓ + 1)·X_ℓ^{CK_ℓ}, and the bound `Tower.towerSize`, a polynomial of degree 3 in
ℓ times that, is at most X_ℓ^{(C+6)K_ℓ}, since ℓ + 3 ≤ X_ℓ. Natural numbers only, up to the last
line. 

### `towerSize_le`

 The bound for the tower from a bound for its parts: R ≤ mY with ℓ + 3 = m and Y ≥ 1 gives at
most 5m³Y. 

### `totalRoomFrom`

 `TotalRoomFrom`, with C₀ = C + 6. 

### `totalRoom`

 `TotalRoom`. 

---
{
  "module": "proof/networks/SingleBitPieces/SecPseudocode_Levels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/SecPseudocode_Levels.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/SecPseudocode_Levels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 8 of the paper: two facts on the numbers K_ℓ of display (38)

This file proves two elementary facts on the numbers K_ℓ of display (38): K_ℓ > 0 (`levelK_pos`) and
K_{ℓ+1} ≥ 19·K_ℓ (`levelK_succ_ge`). 

### `levelK_pos`

 K_ℓ is positive. 

### `levelK_succ_ge`

 K_{ℓ+1} ≥ 19·K_ℓ. 

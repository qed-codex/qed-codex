---
{
  "module": "proof/networks/Paper/SecPseudocode_Algorithm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecPseudocode_Algorithm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecPseudocode_Algorithm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 8 of the paper: the numbers K_ℓ and g_ℓ of display (38)

This file defines the numbers K_ℓ and g_ℓ = 3 K_ℓ⁸ of display (38), which set the levels of
Algorithm 1 of the paper, and proves simple facts about them:
K_{ℓ+1} = g_ℓ², K_ℓ ≥ 64, K_ℓ < K_{ℓ+1}, and ℓ < K_ℓ, so that K_ℓ grows without bound. 

 ## The levels: display (38) 

### `levelK`

 K_ℓ of display (38): K₀ = 64 and K_{ℓ+1} = 9 K_ℓ¹⁶. Same as in the paper. 

### `levelG`

 g_ℓ = 3 K_ℓ⁸ of display (38). Same as in the paper. 

### `levelK_succ`

 K_{ℓ+1} = g_ℓ² (display (38)). 

### `lt_levelK`

 K_ℓ grows without bound. 

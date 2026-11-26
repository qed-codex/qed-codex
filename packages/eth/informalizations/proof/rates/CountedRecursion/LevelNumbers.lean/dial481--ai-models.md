---
{
  "module": "proof/rates/CountedRecursion/LevelNumbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/LevelNumbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/LevelNumbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers K_ℓ and g_ℓ

Natural numbers only. Proof of Theorem A (b): (c + 5)K² ≤ 2^{x₀}K² ≤ g⁴/2, so the exponent of Ξ is
at most C₀K_{ℓ+1}² (`exponentFits`); and the first inequality k times (`chainLevels`). 

### `K_succ_eq`

 K_{j+1} = g_j². 

### `K_succ_sq`

 K_{j+1}² = g_j⁴. 

### `two_pow_le_K`

 2^{x₀} ≤ K_j. 

### `two_pow_mul_K_le_g`

 2^{x₀}K_j ≤ g_j. 

### `K_le_g`

 K_j ≤ g_j. 

### `two_pow_le_g`

 2^{x₀} ≤ g_j. 

### `g_pos`

 g_j ≥ 1. 

### `two_mul_pow_mul_K_sq_le`

 2^{x₀}K² ≤ g⁴/2, for x₀ ≥ 1. 

### `two_mul_c_mul_K_sq_le`

 (c + 5)K² ≤ 2^{x₀}K² ≤ g⁴/2. 

### `g_add_K_sq_le`

 g + K² ≤ g⁴, for x₀ ≥ 1. 

### `chainLevels`

 `ChainLevels`. 

### `exponentFits`

 `ExponentFits`. 

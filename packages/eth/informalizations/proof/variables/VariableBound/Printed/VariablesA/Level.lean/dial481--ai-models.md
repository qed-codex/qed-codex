---
{
  "module": "proof/variables/VariableBound/Printed/VariablesA/Level.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/VariablesA/Level.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/VariablesA/Level.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The level of n

For a sequence Q of levels, «the largest ℓ with K_ℓ ≤ n^(1/17)» is the ℓ with K_ℓ^17 ≤ n <
K_(ℓ+1)^17 (`MainTheoremForms.IsLevel`).
* `level_unique`: a number has at most one level. `isLevel_pick`: every n ≥ K₀^17 has a level, the
  one that `Q.pick` gives for ⌊n^(1/17)⌋; `level_eq_pick`: every level is that one.
* At the level ℓ of n: 2 ≤ K_ℓ ≤ n, 1 ≤ log K_ℓ ≤ log n, 0 < e_ℓ, (log n)^(−C₀) ≤ e_ℓ, and log n <
  17·C₀·log K_ℓ. 

### `K_strictMono`

 K_ℓ increases strictly with ℓ. 

### `level_unique`

 A number has at most one level. 

### `isLevel_pick`

 The level that `Q.pick` gives for ⌊n^(1/17)⌋ is the level of n, for n ≥ K₀^17. 

### `level_eq_pick`

 The level of n is the one picked. 

 ### What the hypothesis gives at the level of n 

### `one_le_lgK`

 1 ≤ log K_ℓ. 

### `e_pos`

 e_ℓ is positive. 

### `K_le_n`

 K_ℓ ≤ n at the level ℓ of n. 

### `lgK_le`

 log K_ℓ ≤ log n at the level ℓ of n. 

### `e_ge_n`

 (log n)^(−C₀) ≤ e_ℓ at the level ℓ of n. 

### `lg_lt`

 Step 5: log n < 17·C₀·log K_ℓ at the level ℓ of n. 

### `one_le_C₀`

 C₀ ≥ 1. 

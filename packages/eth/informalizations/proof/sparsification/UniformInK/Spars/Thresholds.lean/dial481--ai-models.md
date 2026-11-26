---
{
  "module": "proof/sparsification/UniformInK/Spars/Thresholds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Thresholds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Thresholds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The thresholds θ 0 = 1 and θ i = 4·τ^(2i−1) for i ≥ 1

This file proves `StThrU` and `StBetaSumU`. Here β 0 = 0 and β i = 4·τ^(2i−2) for i ≥ 1, so the term
i' = 0 of the sum vanishes and every product 2·θ(i−i')·β i' with 1 ≤ i' < i equals 32·τ^(2i−3);
so for i ≥ 2 the left-hand side of `ThrU.step` is (32i − 16)·τ^(2i−3), which is at most β i =
4·τ^(2i−2) as soon as 8i − 4 ≤ τ. 

### `thetaU_pos`

 The thresholds are positive, if τ is. 

### `mul_betaSU_le`

 τ·β r ≤ θ r. 

### `term_eq`

 One product in `ThrU.step`: 2·θ(i+1−j)·β(j+1) = 32·τ^(2i+1) for j ≤ i. 

### `sum_eq`

 The sum in `ThrU.step` at i + 2 equals 32·(i+1)·τ^(2i+1). 

### `step_le`

 `ThrU.step` for the thresholds `thetaU τ` and the bounds `betaSU τ`, if 8i ≤ τ + 4. 

### `betaSU_le`

 β k ≤ τ^(2k), if 2 ≤ τ. 

### `stThrU`

 The thresholds `thetaU τ` and the bounds `betaSU τ` have the three properties for width k, if 1
≤ k and 8k ≤ τ. 

### `stBetaSumU`

 β 0 + … + β (k-1) is at most τ^(2k), if 2 ≤ τ. 

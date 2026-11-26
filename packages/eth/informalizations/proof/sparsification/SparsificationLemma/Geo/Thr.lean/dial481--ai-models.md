---
{
  "module": "proof/sparsification/SparsificationLemma/Geo/Thr.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/Thr.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/Thr.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The thresholds θ 0 = 1, θ i = 4·τ^(2i−1) satisfy the conditions `ThrC`

`stThrGeo`: from `UniformInK.stThrU` (proof/sparsification/UniformInK/Spars/Thresholds.lean) and β 1 = 4.
`stDegGeo`: the bound on 2·(θ 0 + … + θ (k−1)) + 2 is `UniformInK.Budget.leafCU_add_two_le`
(proof/sparsification/UniformInK/Top/Budget.lean). 

### `stThrGeo`

 The thresholds `thetaU τ` with the numbers `betaSU τ` satisfy the four conditions, if 1 ≤ k and
8k ≤ τ. 

### `stDegGeo`

 2·(θ 0 + … + θ (k−1)) + 2 ≤ τ^(2k), if 1 ≤ k and 8 ≤ τ. 

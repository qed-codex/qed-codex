---
{
  "module": "proof/consequences/ThmCount/MEps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/MEps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/MEps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The closing remark of Appendix C: «a bound in Calabro's proof gives M(ε) = O(ε^{-2} log²(1/ε))»

At k = 3: x = 128/ε, α = ⌈(8/ε)·⌈log₂ x⌉⌉ (proof/sparsification/SparsificationLemma/Cal/Defs.lean).
For 0 < ε ≤ 1/2 put λ = log₂(1/ε) ≥ 1.
* `alpha_le`: ⌈log₂ x⌉ ≤ 8 + λ ≤ 9λ, so α ≤ 72·λ/ε + 1 ≤ 73·λ/ε.
* `stMEps`: so 2 + 4α·(32α) = 2 + 128α² ≤ 682114·ε^{-2}·λ².
* `stMEpsClauses`: an output of the procedure has at most (2·(θ₀ + θ₁ + θ₂) + 2)·n clauses
  (`SparsificationLemma.Sketch.clauses_le`), where θ_j = `SparsificationLemma.Cal.thetaC` α j (j < 3)
  are the thresholds of the procedure, taken to be Calabro's; and θ₀ + θ₁ + θ₂ ≤ 2 + 4α·(32α)
  (`SparsificationLemma.Cal.stDegSum`). 

### `alpha_le`

 At k = 3 and for 0 < ε ≤ 1/2: α ≤ 73·log₂(1/ε)/ε. 

### `sq_eq`

 ε^{-2}·log₂(1/ε)² is the square of log₂(1/ε)/ε. 

### `deg_le`

 At k = 3 and for 0 < ε ≤ 1/2: 2 + 4α·(32α) ≤ 682114·ε^{-2}·log₂(1/ε)². 

### `stMEps`

 The bound on the occurrences of a literal in the formula at a leaf, at k = 3, is
O(ε^{-2}·log²(1/ε)) for 0 < ε ≤ 1/2: the statement `ThmCount.StMEps`, with the constant 682114. 

### `stMEpsClauses`

 «gives M(ε) = O(ε^{-2} log²(1/ε))», at k = 3, for the outputs themselves: every output of the
procedure of Appendix C with the thresholds taken to be Calabro's has at most (A·ε^{-2}·log²(1/ε) + 2)·n
clauses, for 0 < ε ≤ 1/2. This is the statement `ThmCount.StMEpsClauses`, with A = 2·682114. 

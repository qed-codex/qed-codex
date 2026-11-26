---
{
  "module": "proof/sparsification/SparsificationLemma/Cal/Thr.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Thr.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Thr.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Calabro's thresholds satisfy the conditions `ThrC` with τ = α

This file proves `StThrCal`. Positivity, β₁ = 2 and α·β_r ≤ θ_r are read off the definitions and the
closed form of β_c. The condition at a size i ≥ 2 is
4·θ(i−1) + Σ_{i' < i} 2·θ(i−i')·β(i') ≤ β(i). Put S = Σ_{h=1}^{i−1} 2α·β(i−h)·β(h), so that β(i) =
2·S by the recursion. The term i' = 0 of the sum vanishes, as β₀ = 0, and the rest of the sum is S.
And
4·θ(i−1) = 2α·β(i−1)·β(1) is the term h = 1 of S, so the left side is at most 2·S = β(i). 

### `stThrCal`

 Calabro's thresholds satisfy the four conditions with τ = α, for every k and every α ≥ 1. 

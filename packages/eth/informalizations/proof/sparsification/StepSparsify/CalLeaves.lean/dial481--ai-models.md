---
{
  "module": "proof/sparsification/StepSparsify/CalLeaves.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CalLeaves.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CalLeaves.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Cutting the paths of the sparsification tree at a later depth

`leaves_eq_of_le` serves the bound 2^(⌊n/2^s⌋+1) on the number of leaves of the tree of Step 5 of
Appendix D with Calabro's thresholds, where ε = 1/2^s and K = max(k, 3).
It holds for every tree: if the procedure has stopped at every node listed when the paths are cut
after D₀ steps, then cutting them after D ≥ D₀ steps gives the same list.
With Calabro's thresholds every path stops within D₀ = (β₁ + … + β_{k−1})·n steps, so for that bound
it suffices to count the leaves for this D₀. 

### `leaves_eq_of_le`

 If the procedure has stopped at every node that is listed when the paths are cut after D₀ steps,
then cutting them after D ≥ D₀ steps gives the same list. 

### `yC_mono`

 y grows with k. 

### `yC_le`

 y with K = max(k, 3) in the place of k, and with α Calabro's parameter for k and 1/2^s, is at
most 1/2^s. 

### `stCalLeaves`

 The tree with Calabro's thresholds has at most 2^(⌊n/2^s⌋+1) leaves, wherever the paths are cut
from (β₁ + … + β_{k−1})·n steps on. 

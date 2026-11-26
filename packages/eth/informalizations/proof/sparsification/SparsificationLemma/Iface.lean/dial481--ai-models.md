---
{
  "module": "proof/sparsification/SparsificationLemma/Iface.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Iface.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Iface.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The facts on finite sets that the walk of the tree needs, for thresholds with `ThrC`

This file proves `StIfaceC`: it collects the structure `Iface` of
proof/sparsification/SparsifyWidthK/Interfaces.lean. That the root and both children of a node are
nodes is proved in proof/sparsification/UniformInK/Spars/Step.lean, and the bound on the size of a
leaf, the two children computed and the equivalence of a node with its children in
proof/sparsification/SparsifyWidthK, all for thresholds that are at least 1; the bounds on the two
counters are `stBoundC`. It is the twin of proof/sparsification/UniformInK/Spars/Iface.lean. 

### `stIfaceC`

 All that the walk of the tree needs to know about the rule on finite sets, for thresholds with
`ThrC` and any D ≥ (β 0 + … + β (k-1))·n. 

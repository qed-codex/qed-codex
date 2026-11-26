---
{
  "module": "proof/sparsification/UniformInK/Spars/Iface.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Iface.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Iface.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The facts on finite sets that the walk of the tree needs, for the thresholds `thetaU τ`

This file collects the structure `Iface` of proof/sparsification/SparsifyWidthK/Interfaces.lean from
the interface statements of proof/sparsification/UniformInK/Spars/Defs.lean. The bound on the size
of a leaf, the two children computed and the
equivalence of a node with its children are proved in proof/sparsification/SparsifyWidthK for any
thresholds, and are used here with the thresholds `thetaU τ`. It is the counterpart of
`WidthK.ProgMain.iface` in proof/sparsification/SparsifyWidthK/ProgMain.lean. 

### `ifaceU`

 `StIfaceU` from the statements on nodes and on thresholds. 

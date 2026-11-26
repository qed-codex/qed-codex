---
{
  "module": "proof/sparsification/SparsificationLemma/StepSparsifyDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/StepSparsifyDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/StepSparsifyDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Definitions for Step 5 of Appendix D and for Appendix C

The list of all nodes of the tree of a step function (`nodesOf`), the number Δ of an output
(`StepSparsify.DeltaOf`) and the largest number of literals in a clause (`StepSparsify.widthOf`).
This file has definitions only. The theorems are in
proof/sparsification/SparsificationLemma/Nodes.lean,
proof/sparsification/SparsificationLemma/StepSparsify.lean and
proof/sparsification/SparsificationLemma/Sketch.lean. 

### `nodesOf`

 All nodes of the tree below s, with paths cut after d steps: s, then the nodes below its first
child, then those below its second child. 

### `DeltaOf`

 Δ of a formula Φ on the variables below n: the larger of 2 and the largest number of clauses of
Φ in which one variable v < n occurs («Δ the larger of 2 and the largest number of its clauses in
which one variable occurs»). 

### `widthOf`

 The largest number of literals in a clause of φ, and 0 if φ has no clause («the largest number
of literals in a clause of its input»). 

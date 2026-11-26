---
{
  "module": "proof/sparsification/SparsificationLemma/Side.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Side.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Side.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # No choice depends on the side list

This file proves four statements of proof/sparsification/SparsificationLemma/Defs.lean: `StSide`,
`StUnchanged`, `StOutputsSame` and `StNodup`.
The rule looks only at the first component of a node. So a map that changes only side lists, or
forgets them, carries one step to one step, and therefore the leaves of one tree to the leaves of
the other, in the same order (`Groundwork.Sparsify.leaves_sim`).
For `StOutputsSame`: the output `out` keeps only the side clauses of one literal, and the clauses xᵢ
∨ ¬xᵢ have two. `StNodup` holds because `out` writes every clause once. 

### `stSide`

 The tree that starts with the side list X has the same first components, and X behind every side
list. 

### `stUnchanged`

 The first components of the nodes are the nodes of the unchanged procedure. 

### `sideU_append_taut`

 The clauses xᵢ ∨ ¬xᵢ do not reach the output: they have two literals. 

### `stOutputsSame`

 The outputs are those of the tree whose root has the n clauses xᵢ ∨ ¬xᵢ as its side list. 

### `stNodup`

 No output has a clause twice. 

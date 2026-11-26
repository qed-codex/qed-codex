---
{
  "module": "proof/consequences/CountKSat/StepCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/StepCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/StepCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Counting along the tree: the count at a node is the sum of the counts at its two children

This file proves two of the interface statements of `proof/consequences/CountKSat/Interfaces.lean`
(the names `St…`): `StStepCount` and `StRootCount`.
A node is a pair (s, X) of the formula s that the branching rule looks at and a side list X; what is
counted at it is `leafF`, the formula X ++ s.

* `cntN_split`: let every petal Q ∈ P come from a clause C of s whose literals all lie in the heart
  H or in Q. Then the assignments that satisfy X ++ s are
  those that satisfy the light child (they make H true) and those that satisfy the heavy child
  together with «every literal of H is false», and no
  assignment does both. This is the idea of Dell, Husfeldt, Marx, Taslaman and Wahlén (arXiv 1206.1775,
  Appendix A).
* `cntN_step`: the same for one step of the program `stepC`. It needs no hypothesis on the node.
* `cntN_root`: the root has the count of the formula it was made from.

The proofs work on lists. The key fact is `holds_addP`: `addP A s` holds exactly if A and s hold. 

### `Holds`

 The truth values v make a literal of every clause of x true. 

### `holds_append`

 A formula in two parts holds exactly if both parts hold. 

### `holds_addP`

 `addP A s` holds exactly if A and s hold: a clause that `addP` drops contains a clause of A. 

### `holds_singleton`

 A formula with the one clause H holds exactly if a literal of H is true. 

### `holds_negU`

 The unit clauses `negU H` hold under an assignment b exactly if b makes no literal of H true. 

### `holds_petals`

 If no literal of the heart H is true and s holds, then the petals hold. 

### `card_split`

 If L means «P and Q» and R means «P and not Q», then the number of a with P a is the sum of the
numbers for L and for R. 

### `pickK_petals`

 Every petal Q that `pickK` returns comes from a clause of s whose literals lie in the heart or
in Q. 

### `cntN_split`

 The count of X ++ s is the count of the light child (H added) plus the count of the heavy child
(P added) with «H is false» on the side list. 

### `cntN_step`

 The count at a node is the sum of the counts at its two children. 

### `cntN_root`

 The count at the root of the tree of ψ is the count of ψ. 

 ### The interface statements of `proof/consequences/CountKSat/Interfaces.lean` proved by this file 

### `stStepCount`

 `cntN_step`, in the form of the interface. 

### `stRootCount`

 `cntN_root`, in the form of the interface. 

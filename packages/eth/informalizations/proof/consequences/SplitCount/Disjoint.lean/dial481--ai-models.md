---
{
  "module": "proof/consequences/SplitCount/Disjoint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Disjoint.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Disjoint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 6: «no two of which share a satisfying assignment»

A node of the tree is a pair (s, X): the formula s that the branching rule looks at, and the side
list X. What is counted at it is X ++ s (`leafF`). The light child gets the heart H as a clause; the
heavy child gets the petals, and on its side list one unit clause per literal of H, saying that the
literal is false (`negU H`).
* `holds_light`, `holds_heavy`: an assignment satisfies the light child exactly if it satisfies the
  node and makes a literal of H true, and the heavy child exactly if it satisfies the node and makes
  no literal of H true.
* `stDisjoint`: so it satisfies the node exactly if it satisfies one of the children, and never
  both.
* `stDisjointLeaves`: no assignment satisfies two different leaves: by induction on the depth; an
  assignment that satisfies a leaf satisfies every node above it (`holds_of_leaf`).
The facts on `addP`, `negU` and `pickK` are proved, as private theorems that an importing file
cannot use and for truth values in place of assignments, in
proof/consequences/CountKSat/StepCount.lean. 

### `holds_addP`

 `addP A s` holds exactly if A and s hold: a clause that `addP` drops contains a clause of A. 

### `holds_singleton`

 A formula with the one clause H holds exactly if a literal of H is true. 

### `holds_negU`

 The unit clauses `negU H` hold under an assignment b exactly if b makes no literal of H true. 

### `holds_petals`

 If no literal of the heart H is true and s holds, then the petals hold. 

### `pickK_petals`

 Every petal Q that `pickK` returns comes from a clause of s whose literals lie in the heart or
in Q. 

### `holds_light`

 An assignment satisfies the light child exactly if it satisfies the node and makes a literal of
the heart true. 

### `holds_heavy`

 An assignment satisfies the heavy child exactly if it satisfies the node and makes no literal of
the heart true. 

### `stDisjoint`

 «no two of which share a satisfying assignment», at one node: an assignment satisfies the node
exactly if it satisfies one of the two children, and it never satisfies both. 

### `holds_of_leaf`

 An assignment that satisfies a leaf of the tree below x satisfies x. 

### `stDisjointLeaves`

 «no two of which share a satisfying assignment», for the outputs: no assignment satisfies the
formulas of two different leaves of the tree below any node, cut at any depth. 

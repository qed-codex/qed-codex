---
{
  "module": "proof/consequences/SplitCount/Tree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Tree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Tree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 6, step 2

«their form of the Sparsification Lemma turns a k-CNF on n variables, for any ε > 0, into at most
2^{εn} k-CNFs on the same variables, each with O(n) clauses, no two of which share a satisfying
assignment, so that their numbers of satisfying assignments add up.»
The bounds on the tree are those of proof/consequences/CountKSat/ (`CountKSat.SparsifiesC`, given by
`CountKSat.stProgC` at the thresholds of `WidthK.stExistsTau`), whose root carries the clauses xᵢ ∨
¬xᵢ on its side list. They are carried over to the tree of this folder, whose side list starts empty
and whose nodes carry n in unary:
* `leaves_map`, `round_iterate_map`: if a map f of nodes commutes with two step functions, the
  leaves and the stacks of the walk from f x are the images of those from x;
* `stepC_withSide`: the step `stepC` only puts clauses in front of the side list and never reads it,
  so it commutes with appending t to the side list (`withSide t`); `stepPlain` commutes with putting
  n beside the node, by definition;
* `cntN_withSide`: the clauses xᵢ ∨ ¬xᵢ are always true, so they do not change the number of
  satisfying assignments.
The result is `sparsifiesPlain_of` and `stStepTwo`. 

### `leaves_map`

 If f commutes with the step functions, the leaves below f x are the images of the leaves below
x. 

### `round_map`

 If f commutes with the step functions, it commutes with one round of the walk. 

### `round_iterate_map`

 If f commutes with the step functions, it commutes with any number of rounds of the walk. 

### `withSide`

 The node x with the clauses t appended to its side list. 

### `stepC_withSide`

 The step of the tree only puts clauses in front of the side list and never reads it. 

### `length_leafF_le`

 The formula of a node is not longer than with clauses appended to the side list. 

### `mem_leafF_withSide`

 A clause of the formula of a node is still there after clauses are appended to the side list. 

### `cntN_withSide`

 The clauses xᵢ ∨ ¬xᵢ on the side list do not change the number of satisfying assignments. 

### `sparsifiesPlain_of`

 The bounds of proof/consequences/CountKSat/ on the tree whose root has the clauses xᵢ ∨ ¬xᵢ on
its side list hold for the tree whose side list starts empty and whose nodes carry n in unary. 

### `stStepTwo`

 **Step 2.** For every k and ε > 0 some threshold parameter τ gives a tree that sparsifies width
k for counting, from the root with the empty side list: the bounds of `CountKSat.stProgC` at the
thresholds of `WidthK.stExistsTau`, carried over by `sparsifiesPlain_of`. 

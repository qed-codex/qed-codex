---
{
  "module": "proof/consequences/PrintedOrder/AddUp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/AddUp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/AddUp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 6: «no two of which share a satisfying assignment, so that their numbers of satisfying assignments add up»

Proofs of `StAddUp`, `StCovered`, `StRootSame`, `StTreeAddsUp` and `StStepAdds` of
proof/consequences/PrintedOrder/Defs.lean.
* `stAddUp`: for every list of formulas. The assignments to x₀ … xₙ₋₁ that satisfy some formula of
  the list are the disjoint union of those that satisfy the first formula and those that satisfy
  some later one (`card_some`, by induction on the list).
* `stCovered`: an assignment satisfies a node of the tree exactly if it satisfies some leaf below
  it, by induction on the depth from the first half of `SplitCount.stDisjoint`.
* `stRootSame`: the formula at the root (clauses in a normal form, no clause twice, only the
  inclusion-minimal clauses) has the satisfying assignments of the given formula
  (`SparsificationLemma.sat_rootP`).
* `treeAddsUpFrom`, `stepAddsFrom`: the sums over the leaves and over the two children, from the
  statements named, which are hypotheses there; `stTreeAddsUp`, `stStepAdds`: the same on their
  proofs. 

### `cntN_eq`

 The number of satisfying assignments on n variables, written with `Holds`. 

### `card_some`

 If no assignment satisfies two formulas at different places of the list L, the number of
assignments to x₀ … xₙ₋₁ that satisfy some formula of L is the sum of the numbers of satisfying
assignments of the formulas of L. 

### `stAddUp`

 **«no two of which share a satisfying assignment, so that their numbers of satisfying
assignments add up»**, for every formula ψ and every list L of formulas, on n variables: if no
assignment satisfies two formulas at different places of L, and an assignment satisfies ψ exactly if
it satisfies some formula of L, then the number of satisfying assignments of ψ is the sum of those
of the formulas of L. 

### `stCovered`

 An assignment satisfies a node of the counting tree exactly if it satisfies some leaf below it,
at every depth of the cut. By induction on the depth, from the first half of
`SplitCount.stDisjoint`. 

### `stRootSame`

 The formula at the root (with the empty side list) has the satisfying assignments of the given
formula. 

### `treeAddsUpFrom`

 **The numbers of the leaves add up to that of the given formula**, from four statements taken as
hypotheses: no two leaves share a satisfying assignment (`SplitCount.StDisjointLeaves`); an
assignment satisfies a node exactly if it satisfies some leaf below it (`StCovered`); the root has
the satisfying assignments of the given formula (`StRootSame`); then the numbers add up (`StAddUp`). 

### `stTreeAddsUp`

 **The numbers of the leaves add up to that of the given formula**, for all thresholds, every
width and every depth of the cut: `treeAddsUpFrom` on the proofs of its four hypotheses. 

### `stepAddsFrom`

 The same for one step of the tree, from two statements taken as hypotheses: the two children of
a node share no satisfying assignment and an assignment satisfies the node exactly if it satisfies
one of them (`SplitCount.StDisjoint`); then the numbers add up (`StAddUp`, for the list of the two
children). 

### `stStepAdds`

 The number of satisfying assignments of a node is the sum of those of its two children:
`stepAddsFrom` on the proofs of its two hypotheses. 

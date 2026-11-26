---
{
  "module": "proof/sparsification/SparsificationLemma/Gen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Gen.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Gen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification for all thresholds with `ThrC`

This file proves `StGen` and `StTreeG` of proof/sparsification/SparsificationLemma/Defs.lean.
`Gen.withSideClauses` is about the tree of proof/consequences/CountKSat/Defs.lean, whose side list
starts with the n clauses xᵢ ∨ ¬xᵢ. It applies `CountKSatRate.Tree.tree_of`
(proof/consequences/CountKSatRate/Tree.lean), which holds for all
thresholds and bounds that satisfy `Iface` and `Refines`, with `stIfaceC`: the depth is at most D,
and a budget of (k−1)·n is spent τ at a time, at the second child of a step. As in
proof/sparsification/UniformInK/Tree/Tree.lean, `length_occ_le_of_none` of
proof/rates/PaddedDescent/F/MarkDeg.lean bounds the number of clauses of a leaf in which a variable
occurs. For the last part of `StGen`, that no node has more clauses than ψ, the invariant of the
tree is carried along together with «at most as many clauses as ψ»,
which both children inherit by `Shrink.length_step_le`.
`stGen` moves these facts to the tree that starts with the empty side list, by `StSide`.
`stTreeG` takes everything from `Gen.withSideClauses` except the identity of the counts. That
identity comes from `StExactlyOne` and `StCountOfExactlyOne`: the count of ψ is the sum of the
counts of the outputs; by
`StOutputsSame` the outputs are the formulas `out x` of the tree whose side list starts with the
clauses xᵢ ∨ ¬xᵢ, and `out x`, `leafM x` and `leafF x` have the same satisfying assignments. 

### `ok_of`

 The set of clauses of a k-CNF on n variables satisfies the condition `Ok` on the formula at the
root. 

### `length_rootP_le`

 The formula at the root has at most as many clauses as ψ. 

### `InvL`

 The invariant of the tree of proof/consequences/CountKSatRate/Tree.lean with the node predicate
of `StIfaceC`, together with «the formula of the node has at most as many clauses as ψ». 

### `withSideClauses`

 The tree whose side list starts with the clauses xᵢ ∨ ¬xᵢ, for thresholds with `ThrC`, τ ≥ 1 and
D ≥ (β 0 + … + β (k-1))·n. B is any bound for the side list: n·τ + k·(k−1)·n ≤ B·τ.
The number of leaves; what holds at a leaf; the stack of the depth-first walk. 

### `cntN_leafM`

 `leafM x` and `leafF x` have the same number of satisfying assignments, if every clause of the
side list is some xᵢ ∨ ¬xᵢ or has one literal. 

### `cntN_out`

 `out x` has the clauses of `leafM x`, so it has the same number of satisfying assignments. 

### `occN_out_le`

 A variable occurs in at most as many clauses of `out x` as of `leafM x`. 

### `stGen`

 The general theorem, from `StSide`: the facts of `Gen.withSideClauses`, moved to the tree that
starts with the empty side list. 

### `stTreeG`

 What the walk of the tree needs, for all thresholds with `ThrC` and k² ≤ τ, from `StExactlyOne`,
`StCountOfExactlyOne` and `StOutputsSame`: the identity of the counts is derived from «each
satisfying assignment of the input satisfies exactly one output». 

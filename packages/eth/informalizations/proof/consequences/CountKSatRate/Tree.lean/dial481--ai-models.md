---
{
  "module": "proof/consequences/CountKSatRate/Tree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Tree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Tree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification lemma for counting at width k, with a short side list

This file proves `StTreeK`, one of the interface statements of
proof/consequences/CountKSatRate/Interfaces.lean. It says of the tree of `stepC (theta τ) k` what
`StProgC` of
proof/consequences/CountKSat/Interfaces.lean says, with a sharper bound on the side list: at most 2n
clauses if τ ≥ k². Only the step to a heavy child (the child that gets the petals,
proof/consequences/CountKSat/Defs.lean) lengthens the
side list, by at most k clauses, and it adds q units to the counter t of the invariant `GC` of
proof/consequences/CountKSat/ProgC.lean. So (length of the side list)·q ≤ n·q + k·t holds at every
node. Here q = τ and t ≤ kn.
The file follows proof/consequences/CountKSat/ProgC.lean, with this bound in place of the bound by
the number of steps, and uses its lemmas on hearts and on the clauses xᵢ ∨ ¬xᵢ.
`StTreeK` also says what `PaddedDescent.F.StCountM` asks of a formula. The formula part x.1 of a
leaf, without its side list, has no empty clause and every variable occurs in at most leafC τ k of
its
clauses; this is `length_occ_le_of_none` of proof/rates/PaddedDescent/F/MarkDeg.lean, and the proof
follows `leaf_spec` there. Every clause of a side list is some xᵢ ∨ ¬xᵢ or has one literal. 

### `SideT`

 What holds of the side list X when the heavy steps so far have used t units, q each: |X|·q ≤ n·q +
k·t, every clause has at most 2 literals on variables
below n, all clauses xᵢ ∨ ¬xᵢ are there, and every other clause has exactly one literal. 

### `GT`

 The invariant of the counting tree: the invariant of
proof/sparsification/SparsifyWidthK/ProgMain.lean for the formula, and `SideT` for the side list. 

### `GT_step`

 Both children of a node satisfy the invariant after one more step; at the heavy child the second
counter grows by q. 

### `sideT_taut`

 The side list of the root satisfies `SideT` with no unit used. 

### `tree_of`

 The sparsification lemma for counting with the side list bounded by B, for any thresholds and
bounds that satisfy `Iface` and `Refines`. Every leaf satisfies the invariant. 

### `stTreeK`

 The sparsification lemma for counting at width k with a side list of at most 2n clauses: the
interface statement `StTreeK`. 

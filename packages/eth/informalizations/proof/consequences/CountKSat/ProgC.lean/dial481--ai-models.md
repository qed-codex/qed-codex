---
{
  "module": "proof/consequences/CountKSat/ProgC.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/ProgC.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/ProgC.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification lemma for counting, for the program on pairs

This file proves `StProgC`, one of the interface statements of
proof/consequences/CountKSat/Interfaces.lean. It is the sparsification lemma in the counting form of
Dell, Husfeldt, Marx,
Taslaman and Wahlén (arXiv 1206.1775, Appendix A), with the unit clauses {¬ω}, ω ∈ H, kept on a side
list as in Appendix C of the paper (H, called the heart here, is the set of literals on which a step
branches).
The side list starts with the n clauses xᵢ ∨ ¬xᵢ, so that every variable below n occurs in every
leaf. The tree of `stepC` below the root has few leaves, the formula of every leaf has few clauses
and contains
every variable below n, the counts of the leaves add up to the count of ψ, and the stack of the
depth-first walk stays small. The lemmas on trees of
proof/machines/StepMachines/Math/SparsifyTree.lean are applied to pairs (formula, side list). The
invariant is that of
proof/sparsification/SparsifyWidthK/ProgMain.lean for the formula, together with a bound on the side
list. The facts on finite sets, the thresholds and the refinement of the
program are those proved in proof/sparsification/SparsifyWidthK. That the counts of the two children
of a node add up (`StStepCount`), that the root has the count of ψ
(`StRootCount`) and that such a quantity is the sum over the leaves (`StSumLeaves`) are taken as
hypotheses; they are interface statements too.
The proof of `sparsifiesC_of` follows that of `sparsify_prog_of` in
proof/sparsification/SparsifyWidthK/ProgMain.lean. 

 ### The invariant on pairs 

### `SideOK`

 What holds of the side list after p steps: at most n + k·p clauses, each of at most 2 literals
on variables below n, among them all xᵢ ∨ ¬xᵢ. 

### `GC`

 The invariant of the counting tree: the invariant of `WidthK.ProgMain` for the formula, and
`SideOK` for the side list. 

### `clause_of_G`

 The clauses of the formula of a node have at most k literals, on variables below n. 

### `pick_spec`

 A heart that the search finds has at most k literals, on variables below n. 

### `stepC_some`

 The two children of a step of the counting tree, written out. 

### `GC_step`

 Both children of a node satisfy `GC` with one more step (p + 1); the second child h, which gets
the shortened clauses P and, on its side list, the negations of the literals of H, also has its
counter t raised by q (t + q). 

### `length_taut`

 There are n clauses xᵢ ∨ ¬xᵢ. 

### `mem_taut`

 The members of `taut n`. 

### `sideOK_taut`

 The side list of the root satisfies `SideOK` with no step done. 

### `sparsifiesC_of`

 The sparsification lemma for counting, for one n, any thresholds θ and any bounds D, T, q, leafB
for which the facts on finite sets (`Iface`) and the
refinement (`Refines`) hold. hv bounds the number of steps on a path that go to the second child. 

### `stProgC`

 The sparsification lemma for counting, for the thresholds `theta τ`, from the three interface
statements on counts. 

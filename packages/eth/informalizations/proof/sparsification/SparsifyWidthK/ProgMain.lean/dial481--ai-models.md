---
{
  "module": "proof/sparsification/SparsifyWidthK/ProgMain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/ProgMain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/ProgMain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification lemma for width k, for the program on lists

This file proves `StProg`: the tree of the program `stepK` below `rootP ψ` has few leaves, every
leaf has few clauses, ψ is satisfied exactly if some leaf
is, and the stack of the depth-first walk stays small. `StProg` and the ten statements it is proved
from are interface statements of
SparsifyWidthK/Interfaces.lean: nine are about finite sets and thresholds, and `StRefines` says that
the program computes the rule on finite sets.
The lemmas on trees of StepMachines/Math/SparsifyTree.lean are applied to the program directly, with
the invariant «s is in normal form, and the set of
its clauses is a node of the tree of the rule». 

### `mem_toFin`

 The members of `toFin s` are the clauses of s, read as sets. 

### `subP_iff_subset`

 The test `subP D C` says that D, read as a set, is contained in C. 

### `toFin_addP`

 As sets, `addP A s` consists of the clauses of A and the clauses of s that contain no clause of
A. 

### `nf_addP`

 `addP` keeps the normal form. 

### `nf_length_eq`

 A formula in normal form has as many clauses as its set of clauses has members. 

### `toFin_singleton`

 The set of clauses of a formula with one clause. 

### `NF_singleton`

 A formula with one clause, in which no literal occurs twice, is in normal form. 

### `sat_toFin`

 Truth values satisfy the set of clauses of x exactly if every clause of the list x has a true
literal. 

### `G`

 The invariant of the tree of ψ: s is in normal form, and its set of clauses is a node with the
counters p (steps) and t (units used by heavy steps). 

### `step_spec`

 One step of the program is one step of the rule: the two lists it returns are in normal form,
and as sets they are the light and the heavy child. 

### `G_step`

 Both children of a step satisfy the invariant: one more step, and q more units at the heavy
child. 

### `card_le_of_clause`

 If every clause of F lies inside a clause of F₀, and these have at most k literals, then F has
at most |F₀|·2^k clauses. 

### `sparsify_prog_of`

 The sparsification lemma for the program `stepK`, for any thresholds θ and any bounds D, T, q,
leafB for which the facts on finite sets (`Iface`) and
the refinement (`Refines`) hold. hv bounds the number of heavy steps on a path. 

### `litsBelow`

 The literals on variables below n. 

### `Ok`

 The condition on the formula at the root: nonempty clauses of at most k literals on variables
below n. 

### `card_litsBelow`

 There are at most 2n literals on variables below n. 

### `iface`

 The facts on finite sets that `sparsify_prog_of` needs, for the thresholds `theta τ`, collected
from the interface statements. 

### `stProg`

 The sparsification lemma for width k for the program `stepK (theta τ) k`, from the other
interface statements. 

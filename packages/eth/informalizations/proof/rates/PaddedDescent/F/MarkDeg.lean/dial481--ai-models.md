---
{
  "module": "proof/rates/PaddedDescent/F/MarkDeg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkDeg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkDeg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers: how often a variable occurs at a leaf, and how many clauses touch a node

This file proves `StLeaf`, one of the interface lemmas of
proof/rates/PaddedDescent/F/Interfaces.lean: a leaf of the sparsification tree at width k has
nonempty clauses only, and
every variable occurs in at most leafC τ k of them. The reason is the definition of a leaf in
proof/sparsification/SparsifyWidthK/Defs.lean: no nonempty set of fewer than j literals lies in
θ (j − its size) or more clauses of size j, so a literal lies in fewer than θ (j − 1) clauses of
size j ≥ 2, and in at most one clause of size 1.
The invariant of the tree and the step from lists to finite sets are those of
proof/sparsification/SparsifyWidthK/ProgMain.lean and
proof/sparsification/SparsifyWidthK/Refine.lean.
It also proves `length_tch_le` and `length_tch_le_of_wfL`: if every variable occurs in at most Δ
clauses of the layers, at most qv g n · Δ clauses touch a node, because a node holds qv g n
variables. 

 ### A leaf, as a finite set of finite sets 

### `card_filter_mem_le_one`

 A literal lies in at most one set of size 1. 

### `card_filter_mem_le`

 At a leaf whose clauses have 1 to k literals, a literal lies in at most θ 0 + … + θ (k − 1)
clauses. 

 ### A leaf, as a list of lists 

### `length_occ_le`

 In a list in normal form, the clauses with the variable v are at most those with the literal v
and those with the literal ¬v. 

### `length_occ_le_of_none`

 Where `stepK` has no answer, every variable occurs in at most 2·(θ 0 + … + θ (k − 1)) clauses. 

### `leaf_spec`

 Every leaf of the tree of `stepK (theta τ) k` below `rootP ψ` is in normal form, has nonempty
clauses only, and every variable occurs in at most leafC τ k of
its clauses. ψ has variables below n and nonempty clauses of at most k literals. 

 ### The clauses that touch a node 

### `map_getD_range`

 Reading a list at the places 0, 1, … gives the list back. 

### `length_filter_range`

 Counting the places of a list by a property of the entry is counting the entries. 

### `map_snd_cls`

 The clauses of `cls Ls`, without the numbers of their layers, are the layers one after the
other. 

### `length_cls`

 `cls Ls` has as many entries as the layers have clauses. 

### `countP_block_le`

 A clause with a variable among a·q, …, a·q + q − 1 is counted at one of these variables. 

### `length_tch_le`

 If every variable occurs in at most Δ clauses of the layers, at most qv g n · Δ of these clauses
touch the node a. 

### `qv_pos`

 A node holds at least one variable if there is a node and a variable. 

### `length_tch_le_of_wfL`

 At most qv g n · Δ clauses touch a node, for well-formed layers and at least one node, also if
there is no variable: then there is no clause. 

### `stLeaf`

 A leaf of the tree at width k has nonempty clauses only, and every variable occurs in at most
leafC τ k of them: the interface lemma `StLeaf`. 

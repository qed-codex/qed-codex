---
{
  "module": "proof/sparsification/SparsifyWidthK/Refine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Refine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Refine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The program of the sparsification of a k-CNF follows the rule on finite sets

`pickK` (`SparsifyWidthK/DefsProg.lean`) works on lists of lists of literals; the rule `Rule` and
the leaves `Leaf` (`SparsifyWidthK/Defs.lean`) are stated for finite sets of
finite sets. A list s in normal form (`NF s`: no literal twice in a clause, no clause twice as a
set) is read as the set `toFin s`. This file proves:
* `overP` and `minusP` compute `over` and set difference, and the list of petals is in normal form;
* the masks pick exactly the sublists of a clause of at most k literals, so every subset of a clause
  is among the candidate hearts;
* the pairs (j, h) are tried with j upwards and, for each j, h downwards; so where `pickK` answers,
  `Rule` holds, and where it does not, `Leaf` holds;
* `rootP ψ` is in normal form and stands for the inclusion-minimal clauses of ψ (two lemmas of
  `StepMachines/Math/SparsifyProg.lean`).
Together these are `stRefines : StRefines`, one of the interface statements of
`SparsifyWidthK/Interfaces.lean`. 

 ### Lists in normal form as sets of sets 

### `mem_toFin`

 The members of `toFin s` are the clauses of s, read as sets. 

### `card_toFin`

 A list in normal form has as many clauses as its set of sets has members. 

### `NF_filter`

 Dropping clauses keeps the normal form. 

### `subP_iff'`

 `subP D C` tests inclusion of the sets of literals. 

### `toFin_overP`

 `overP s j H` lists the clauses of size j that contain H: it computes `over`. 

### `length_overP`

 The number that the search compares with the threshold is the number of clauses of size j over
H. 

### `toFinset_minusP`

 `minusP H C` computes the set difference C ∖ H. 

### `toFin_petals`

 The second component of the answer of `tryP` stands for the petals. 

### `NF_petals`

 The list of petals is in normal form: different clauses over H stay different without H. 

 ### The masks and the candidate hearts 

### `maskP_sublist`

 A mask picks a sublist. 

### `exists_mask`

 Every sublist of a clause of at most k literals is picked by one of the masks of length k. 

### `mem_heartsP`

 The candidate hearts are exactly the sublists of length h of the clauses of length j. 

 ### The order of the search 

### `mem_pairsK`

 The pairs that are tried: 1 ≤ h < j ≤ k. 

### `Before`

 The pair x = (j', h') comes before y = (j, h) in the search: j' < j, or j' = j and h' > h. 

### `pairwise_pairsK`

 `pairsK k` lists its pairs in the order `Before`. 

### `head`

 If `(l.filterMap f).head?` is `some b`, then b is the result of f at some entry of l, and f has
no result at the entries before it. 

### `head`

 If `(l.filterMap f).head?` is `none`, then f has no result at any entry of l. 

### `pickK_some`

 An answer of `pickK` is the answer of `tryP` at some pair, and `tryP` has no answer at the pairs
that come before it. 

### `pickK_none`

 Where `pickK` has no answer, `tryP` has none at any pair. 

 ### The search finds the rule 

### `tryP_some`

 An answer of `tryP` at the pair (j, h) is a heart of size h for the clauses of size j, without
repeated literals, with its petals. 

### `tryP_none`

 Where `tryP` has no answer at (j, h), no set of size h is a heart for the clauses of size j. The
threshold is at least 1, so a
heart lies inside some clause and is among the candidates. 

### `not_heart_of_none`

 The same for a set H of any size: H is not a heart for size j if `tryP` has no answer at (j, |H|). 

### `rule_of_pickK`

 An answer of `pickK` satisfies `Rule`: smallest clause size that has a heart, then a heart of
the largest size. 

### `leaf_of_pickK`

 Where `pickK` has no answer, no clause size up to k has a heart. 

 ### The root 

### `toFin_rootP`

 `rootP ψ` stands for the inclusion-minimal clauses of ψ (`toFinset_rootP` of
`StepMachines/Math/SparsifyProg.lean`). 

### `NF_rootP`

 `rootP ψ` is in normal form (from `nodeP_root` of `StepMachines/Math/SparsifyProg.lean`). 

 ### The statement of the interface 

### `refines`

 If the thresholds θ 1, θ 2, … are at least 1, then `pickK θ k` follows the rule on finite sets,
its petals are in normal form, and
`rootP` gives the inclusion-minimal clauses in normal form. 

### `stRefines`

 `StRefines`, one of the interface statements of `SparsifyWidthK/Interfaces.lean`. 

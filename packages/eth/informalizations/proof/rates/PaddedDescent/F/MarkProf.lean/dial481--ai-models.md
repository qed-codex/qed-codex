---
{
  "module": "proof/rates/PaddedDescent/F/MarkProf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkProf.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkProf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers: every set of clauses has exactly one profile

Here `Ls` is a list of formulas, the layers; their clauses are numbered together (`cls`), and the
layer of a clause is the index of its formula. A set P of clause indices
determines, for every layer, how many of its members each node owns and how many lie among the
clauses whose marks two nodes compare. These numbers are the digits of exactly one
number y below `nProf` whose unused places are 0 (`sum_digit_eq`, `adm_match_iff`). That y is
admissible exactly if every layer has at most w members of P: a clause has one owner,
so the owned members add up to the members of the layer (`sum_oc`); a clause of at most k literals
touches at most k nodes and has at most k − 1 links, so the compared members add up
to at most k − 1 times that number (`sum_pw_le`). The result is `stProfSum`, the interface statement
`StProfSum`. No state of the network occurs in this file. 

 ### Digits 

### `sum_digit_eq`

 Exactly one number below (M+1)^Q has prescribed digits t q ≤ M at the places q < Q, and none if
some t q exceeds M. 

### `place_dec`

 The place (A·g + A')·R + i determines i, A' and A. 

### `sum_map_range`

 A sum over `List.range` is the sum over `Finset.range`. 

### `mu_comm`

 The profile's number for two nodes does not depend on their order. 

### `mu_of_le`

 For a ≤ b the profile's number is the digit at the place (a·g + b)·R + i, where R is the number
of layers. 

### `pw_comm`

 The number of compared members does not depend on the order of the two nodes. 

 ### Clauses, touched nodes, owners, links 

### `clAt_wf`

 A clause of well-formed layers has 1 to k literals on variables below n. 

### `home_lt`

 The home of a variable below n is a node below g. 

### `tset`

 The nodes below g that the clause e touches. 

### `mem_tset`

 Membership in `tset`. 

### `tset_nonempty`

 A clause touches some node below g. 

### `card_tset_le`

 A clause touches at most k nodes. 

### `ownB_iff`

 What `ownB` says: a is touched, and no smaller node is. 

### `linkB_iff`

 What `linkB` says: a < b are touched, and no node between them is. 

### `card_owner`

 Exactly one node below g owns a clause. 

### `card_links_le`

 A clause has at most k − 1 links. 

 ### The two sums of a layer 

### `sum_oc`

 The owned members of a layer, summed over the nodes, are the members of the layer. 

### `mem_tst`

 Membership in `tst` for a' < a. 

### `sum_pw_le`

 The compared members of a layer, summed over the pairs of nodes, are at most k − 1 times the
members of the layer. 

### `pw_le_length`

 At most as many members are compared as there are compared clauses. 

 ### The profile of a set of clauses 

### `adm_iff`

 What `adm` says. 

### `tgt`

 The digit that the profile of P has at the place q. 

### `tgt_place`

 The digit of P at the place (A·g + A')·R + i, where R is the number of layers. 

### `tgt_le`

 The digits of P are at most the number of clauses. 

### `adm_match_iff`

 y is an admissible profile of P exactly if the caps hold for P and y has the digits of P. 

### `stProfSum`

 `StProfSum`. 

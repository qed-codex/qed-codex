---
{
  "module": "proof/rates/PaddedDescent/F/MarkVal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkVal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkVal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers: the value of the network of one profile

The clauses come as a list `Ls` of formulas, the layers; `cls Ls` lists all clauses, each with the
number of its layer, and a clause is named by its position in that list.
The plain functions `markF` present the network `markN` (StMarkPresents). The value of the network
of the profile y is the signed number of pairs (σ, P), where σ is an
assignment and P a set of clauses that σ violates, such that P has the profile y (StMarkVal). The
steps: if the states of two nodes have the profile, their
interaction is 1 if the marks that they compare agree and 0 otherwise, because the code of the
labels can be read back; the states at which all weights are
nonzero and all marks agree are exactly the states of the pairs (σ, P), because the nodes that a
clause touches form a chain; at such a state the profile's numbers count members of P. 

### `encCat`

 The codes of the strings of a list of layers, written one after the other, can be read back. 

### `encLen`

 The length of the codes of the strings of a list of layers, written one after the other. 

 ### The lists of clause indices 

 ### The state of a pair (σ, P) 

### `st`

 The state word of the node a: the values of its variables, then the marks of the clauses that
touch it. 

 ### The weight without the profile 

### `base`

 Variables beyond n are false, and every literal of a marked clause whose variable lies at the
node a is false in the state z. 

### `ownC`

 The number of marked clauses of layer i that the node a owns, in the state z. 

### `sgE`

 The number of marked clauses of the layers after the first that the node a owns, in the state z. 

### `prof`

 The state z of the node a has the numbers that the profile y prescribes. 

### `mW_eq`

 The weight is the sign if the state is consistent and has the profile, and 0 otherwise. 

 ### The network of one profile 

### `ctx`

 The context with the numbers g, n, β, b in unary. 

### `sum_words_eq`

 The sum over all labels of length c of «A is the label and B is the label». 

### `length_mlab`

 The label that a state with the profile writes has the prescribed length. 

### `Ψ_eq`

 The interaction of two nodes whose states have the profile is 1 if their strings agree in every
layer, and 0 otherwise. 

 ### The quantities of the profile at the state of (σ, P) 

### `length_filter_eq_card`

 The length of a filtered list without repetitions is the number of elements of the set that it
lists. 

### `prof_st_iff`

 The states of (σ, P) have the profile y exactly if P has it. 

 ### Every clause has one owner 

### `layer_lt`

 The layer of a clause of the list of all clauses is below the number of layers. 

### `clAt_mem`

 A clause of the list of all clauses is a clause of some layer. 

### `div_qv_lt`

 The home of a variable below n is a node below g. 

### `tch_lt`

 A node that a clause touches is below g. 

### `exists_owner`

 Every clause has an owner. 

### `owner_unique`

 A clause has at most one owner. 

### `sum_owner`

 Counting the clauses of P with a property p owner by owner counts each once. 

### `prod_sign_st`

 The signs of the nodes at the states of (σ, P) multiply to the sign of P. 

 ### Good states are the states of the pairs (σ, P) 

### `Gd`

 All weights without the profile are nonzero and all strings agree. 

### `st_good`

 The states of (σ, P) are good if σ violates all clauses of P. 

### `st_inj`

 The states determine σ and P. 

### `mark_eq`

 In a good state all marks of a clause agree. 

### `ext_getD`

 Two words of the same length with the same bits are equal. 

### `st_surj`

 Every good family of states is the family of the states of some (σ, P). 

### `sum_good`

 A sum over the good states is a sum over the pairs (σ, P). 

 ### The value of the network of one profile 

### `term_eq`

 One term of the value: the product of the signs at a good family of states with the profile, and
0 elsewhere. 

### `markVal`

 The value of the network of the profile y: the signed number of pairs (σ, P), P a set of clauses
that σ violates, with that profile. 

### `eq_replicate`

 A number in unary is the list of that many units. 

### `stMarkVal`

 The value of the network of one profile, admissible or not. 

### `stMarkPresents`

 The plain functions markF present the network markN. 

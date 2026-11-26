---
{
  "module": "proof/rates/PaddedDescent/F/MarkSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkSize.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers: the size of the network of an admissible profile

This file proves the interface statement `StMarkSized` of
proof/rates/PaddedDescent/F/Interfaces.lean (`stMarkSized`): the network `markN` of an admissible
profile has size
`Pb`, entries 0, 1, −1, and at most `Ub` shared bits. The clauses come as a list `Ls` of layers,
each a list of clauses, and a profile prescribes its numbers of set marks layer by layer.
Two counts carry the proof. A clause touches a chain of nodes, so at one node it has at most two
links (`card_links_at_le`), and with at most k literals at most k − 1 links in all
(`card_links_le`). An admissible profile prescribes at
most as many set marks as two nodes compare, and at most (k − 1)·w set marks in a layer; together
with the length of the code of a label this bounds the capacities at a
node (`sum_mcap_le`) and their sum (`U_markN_le`). That at most qv g n · Δ clauses touch a node is
`Deg.length_tch_le_of_wfL` of proof/rates/PaddedDescent/F/MarkDeg.lean. 

 ### The links of a clause 

### `linkB_iff`

 a and b are neighbours in the chain of clause e exactly when a < b, e touches both, and e
touches no node between them. 

### `link_left_unique`

 The upper end of a link determines its lower end. 

### `link_right_unique`

 The lower end of a link determines its upper end. 

### `card_touched_le`

 The number of nodes that a clause touches is at most its number of literals. 

### `card_links_lt`

 A clause that touches a node has fewer links than touched nodes. 

### `length_filter_eq_card`

 The length of a filtered list of the numbers below M, as the number of elements of a finite set. 

### `countP_cls`

 The list `cls` holds as many entries of layer i as layer i has clauses. 

### `card_links_le`

 A clause of k literals has at most k − 1 links, and an empty clause has none. 

### `sum_length_tst_le`

 All the strings of layer i together have at most k − 1 bits for each clause of the layer, if the
clauses have at most k literals. 

### `card_links_at_le`

 At a node a, a clause has at most two links, and none if it does not touch a. 

### `sum_length_tst_node_le`

 All the strings that a node a shares with the other nodes together have at most twice as many
bits as clauses touch a. 

 ### The size of the network 

### `sum_map_range`

 The sum of a list indexed by the numbers below R, as a sum over a finite set. 

### `ceil_le`

 A string of t bits has at most t blocks. 

### `mu_comm`

 The number that a profile prescribes for two nodes does not depend on their order. 

### `tst_comm`

 The clauses whose marks two nodes compare do not depend on the order of the nodes. 

### `mcap_comm`

 The capacities are symmetric. 

### `adm_iff`

 `adm` is true exactly when, in every layer, the four conditions below hold. 

### `mu_le_of_adm`

 An admissible profile prescribes for two different nodes at most as many set marks as they
compare. 

### `mcap_le`

 The capacity of a pair is at most (2 + β) bits for each bit of its strings. 

### `sum_mcap_le`

 The capacities at a node a sum to at most 2(2 + β) bits for each clause that touches a. 

### `sum_erase_fin`

 A sum over the other nodes, as a sum over numbers. 

### `abs_boole_le`

 A number that is 0 or 1 is at most 1 in absolute value. 

### `sized_markN`

 The network of an admissible profile has size P, with entries 0, 1, −1, if at every node P
bounds qv plus the number of touching clauses, and
2(2 + β) times that number. 

 ### The shared bits 

### `sum_erase_eq_two_mul`

 A symmetric table summed over the ordered pairs of different numbers below g is twice its sum
over the pairs a' < a. 

### `ceil_le_succ`

 A string of t bits has at most t / b + 1 blocks. 

### `sum_div_le`

 Rounding down term by term gives at most the rounded-down quotient of the sum. 

### `sum_lt_eq_sum_product`

 The sum over a' < a < g as a sum over all pairs. 

### `U_markN_le`

 A bound on the shared bits of the network of an admissible profile whose clauses have at most k
literals. 

### `stMarkSized`

 The network of an admissible profile of well-formed layers, each variable in at most Δ clauses,
has size `Pb`, entries 0, 1, −1, and at most `Ub` shared bits. 

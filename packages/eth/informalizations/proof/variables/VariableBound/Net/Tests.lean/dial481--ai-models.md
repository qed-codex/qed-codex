---
{
  "module": "proof/variables/VariableBound/Net/Tests.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Tests.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Tests.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3: the tests of the objects

The nodes that an object touches form a chain a₁ < … < a_t, and its tests are the pairs of
neighbours. So an object of kind κ has at most k − 1 + κ tests (`card_links_le`,
`sum_length_tst_le`: T_κ is at most
k − 1 + κ times the number of objects of kind κ), and at most two tests at one node
(`card_links_at_le`, `sum_length_tst_node_le`). There are m objects of kind 0 and I = Σ_j |Λ_j| of
kind 1.
The total U of the network of a profile is twice the sum of the c_(a,b) over the pairs a < b
(`U_eq`). 

 ### The tests of one object 

### `linkB_iff`

 a and b are neighbours in the chain of the object e exactly when a < b, e touches both, and e
touches no node between them. 

### `link_left_unique`

 The upper end of a link determines its lower end. 

### `link_right_unique`

 The lower end of a link determines its upper end. 

### `card_links_lt`

 An object that touches a node has fewer links than touched nodes. 

### `length_filter_eq_card`

 The length of a filtered list of the numbers below M, as the number of elements of a finite set. 

### `card_links_le`

 Step 3: «an object of kind κ has at most k − 1 + κ tests»; here with the number of literals of
its clause in place of k. 

 ### Sums over pairs of nodes 

### `sum_map_range`

 The sum of a list indexed by the numbers below R, as a sum over a finite set. 

### `sum_erase_fin`

 A sum over the other nodes, as a sum over numbers. 

### `sum_erase_eq_two_mul`

 A symmetric table summed over the ordered pairs of different numbers below g is twice its sum
over the pairs a' < a. 

### `sum_lt_eq_sum_product`

 The sum over a' < a < g as a sum over all pairs. 

 ### The number of tests of all objects of a kind 

### `sum_length_tst_le'`

 Step 3, «The total»: T_κ, the number of tests of the objects of kind κ, is at most k − 1 + κ
times the number of these objects, if Φ has clauses of at most k literals (`WfD`). Sum over all
pairs of numbers below g. 

### `sum_length_tst_le`

 Step 3, «The total»: T_κ = Σ_(a < b < g) t_(a,b,κ) is at most k − 1 + κ times the number of
objects of kind κ, if Φ has clauses of at most k literals (`WfD`). 

### `card_kind_zero`

 There are m objects of kind 0 (for well-formed data, `WfD`). 

### `card_kind_one`

 There are I = Σ_j |Λ_j| objects of kind 1 (for well-formed data, `WfD`). 

 ### The tests at one node 

### `card_links_at_le`

 At a node a, an object has at most two links, and none if it does not touch a. 

### `sum_length_tst_node_le`

 Step 3, «The parameters»: «an object has at most two tests at a». All the strings that a node a
< g shares with the other nodes together have at most twice as many bits as objects touch a. 

 ### The total 

### `capD_comm`

 c_(a,b) = c_(b,a). 

### `capD_eq`

 c_(a,b) as a sum over the two kinds. 

### `length_rep`

 A number written in unary has that length. 

### `U_eq`

 Step 3, «The total»: U = 2·Σ_({a,b}) c_(a,b), for the network of the profile y. 

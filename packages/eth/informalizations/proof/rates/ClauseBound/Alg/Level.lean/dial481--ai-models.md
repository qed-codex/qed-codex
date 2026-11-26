---
{
  "module": "proof/rates/ClauseBound/Alg/Level.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Level.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Level.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Facts for one level

An instance on p·d nodes is laid out on a grid with p rows and d columns, and the factor d^|R| times
its value is the sum of the terms Z_ι over all patterns ι. This file holds facts used
at such a level: sums over lists as sums over ranges and over a filterMap, an arithmetic bound, a
bound on the absolute value of the value of a network, and the fact that the network
that is rebalanced has p nodes, each of them d merged nodes of the grid (it is the row network, or
the grid is square). 

 ### Helpers 

### `sum_map_range`

 A sum over a list of numbers 0, …, n − 1 is a sum over a range. 

### `filterMap_spec`

 A filterMap in which every element is either dropped, and then counts 0, or kept, and then
counts the value of its image. 

### `le_mul_div_succ`

 x ≤ y·(x / y + 1) for y > 0. 

### `card_add_card_pairs_le`

 The nodes and the pairs a < b of a set of g elements are together at most g² things. 

### `abs_value_le`

 A network on the nodes J with at most 2^n states a node and all weights W and interactions Ψ at
most 2^B in absolute value has a value Z with |Z| ≤ 2^{|J|·n + |J|²·B}. 

### `parts_eq`

 The network that is rebalanced has p nodes, each of them d merged nodes of the grid: it is the
row network, or the grid is square. 

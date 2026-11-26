---
{
  "module": "proof/networks/Groundwork/Grid/Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 One level of the recursion (Section 5, proof of Proposition 3): the clique on the grid. Every
edge that joins two rows and two columns is a diagonal of
exactly one rectangle, so Z is the half-edge sum ZG with the crossing at every rectangle. 

 ### Indicators 

### `boole_congr`

 Indicators of equivalent propositions are equal. 

### `boole_and3`

 The indicator of a conjunction of three propositions is the product of their indicators. 

### `prod_ind`

 A product of indicators is the indicator of «all of them hold». 

 ### The edges of the grid 

### `symm_iff`

 The two copies of every edge agree if and only if they agree on the edges inside rows, on the
edges inside columns and on
the two diagonals of every rectangle. 

### `symm_eq_prod`

 The product of all equalities ℓ w w' = ℓ w' w is the product of those inside rows, those inside
columns, and of the
crossing over the rectangles. 

### `Ω_eq_product`

 The rectangles, sorted by pairs of rows. 

### `prod_Ω_rows`

 A product over the rectangles, sorted by pairs of rows. (`to_additive` makes the same lemma for
sums, `sum_Ω_rows`.) 

 ### Z in half-edge form 

### `mem_halfEdges`

 The half-edge labellings of Inst.Z_eq_halfEdges are those with the default label at every node
itself. 

### `Z_eq_symm`

 Z in half-edge form. 

### `Z_eq_ZG_X`

 The half-edge form on the grid. 

### `card_Ω`

 The number of rectangles is C(g,2)². 

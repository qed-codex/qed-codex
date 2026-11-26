---
{
  "module": "Nc/Hc/Vnp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Hc/Vnp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Hc/Vnp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The Hamiltonian cycle polynomial is in VNP

A cycle through all vertices is written as the order in which it visits them from a fixed first vertex on, with one
bit for every position and vertex. A product of local tests singles out the bit tables that are such orders.


### `cycleOf`

 The cycle that visits the vertices in the order π. 

### `sum_cycles_eq_sum_orders`

 Every cycle through all vertices visits them in exactly one
order that begins with the first vertex. 

### `pos`

 The bit "position i holds vertex u". 

### `clash`

 The pairs of bits that exclude each other: two of one position or two of one vertex. 

### `orderTest`

 The test that the bits are a bijection between positions and vertices. 

### `orderEdges`

 The edges between consecutive positions. 

### `hcWit`

 The witness: the test, the first vertex at the first position, and the edges. 

### `orderBits`

 The table of bits of an order. 

### `exists_order_of_test_ne_zero`

 A table of bits passes the test only if it is the table of a bijection
between the positions and the vertices. 

### `genHC_eq_sum_wit`

 The Hamiltonian cycle polynomial is the sum of the witness over all tables of
bits. 

### `csize_hcWit`

 The witness has polynomial size and degree. 

### `quartic_bound`

 A polynomial bound in the form of the definition of VP. 

---
{
  "module": "proof/networks/Groundwork/Grid/Size.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/Size.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/Size.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Counts for one level of the recursion, for the network in which the rows of the grid are merged:
its size is g³λ; its bits are the g²(g−1)λ of the vertical
edges plus what the rectangles cost, each rectangle counted twice; and bounds on the magnitudes of
its functions. 

 ### Helpers 

### `abs_boole_le`

 An indicator is 0 or 1. 

### `abs_prod_le_pow`

 A product of integers of absolute value at most 2^B. 

### `abs_mul_prod_le`

 Factors 0, ±1 times factors of absolute value at most 2^b. 

### `sum_le_card_mul`

 A sum of numbers that are at most c is at most their number times c. 

### `two_mul_pairs`

 2·#{a < b} = g(g−1). 

### `card_lt_le`

 There are at most g² pairs of columns. 

### `cap_bound`

 gL + (at most 2mL for each rectangle of two rows) ≤ g²mL. 

### `sum_erase_le`

 A sum over the g − 1 other elements of numbers that are at most g²c is at most g³c. 

### `sum_erase_eq`

 A sum over ordered pairs of distinct elements of a function of the unordered pair counts each
pair a < b twice. 

### `card_state`

 A row has g·g² half-edges. 

### `card_labels_le`

 The number of labels of two rows. 

### `sum_Ω_swap`

 A sum over the rectangles of the transposed grid. 

### `four_mul_card_Ω_le`

 4R ≤ g⁴. 

 ### The row network 

### `rowNet_c_le`

 Two rows have capacity at most g²mL if every rectangle is charged at most 2mL bits. 

### `rowNet_shaped'`

 The shape of the row network when every rectangle is charged at most 2mL bits, m ≥ 1. 

### `abs_rowNet_Ψ_lt`

 The interaction of two rows is a product of at most g² values of the functions at the
rectangles. 

### `rowNet_sized'`

 The shape and the magnitudes of the row network when every rectangle is charged at most 2mL
bits, m ≥ 1. 

### `U_rowNet`

 U counts ordered pairs, so every rectangle counts twice. 

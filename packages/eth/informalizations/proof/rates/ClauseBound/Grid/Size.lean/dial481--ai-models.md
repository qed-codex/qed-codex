---
{
  "module": "proof/rates/ClauseBound/Grid/Size.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Grid/Size.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Grid/Size.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Sizes of the row network of a grid with p rows and d columns

The file proof/networks/Groundwork/Grid/Size.lean counts the rectangles of a square grid and bounds
the size of its row network. Here the same is done for a grid
whose number p of rows and number d of columns may differ:

* there are C(p,2)·C(d,2) rectangles (`card_Ω_pd`);
* two rows share at most d²·mL bits if every rectangle is charged at most 2mL bits
  (`rowNet_c_le_pd`);
* the row network is a network of size m·(p·d²·L) whose values are at most 2^(dB + d²b) in absolute
  value (`rowNet_shaped_pd`, `rowNet_sized_pd`);
* its total U, which counts ordered pairs of rows, is p(p−1)·d·L plus twice the bits charged for the
  rectangles (`U_rowNet_pd`).

L is the number of bits of a label (λ in the paper). The paper has m = 1. The column network is the
row network of the transposed grid, that is, with p and d
exchanged, so only rows are treated. 

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

 Twice the number of pairs a < b of a set of n elements is n(n−1). 

### `card_lt_le`

 There are at most d² pairs of columns. 

### `sum_erase_le`

 A sum over the p − 1 other elements of numbers that are at most c is at most pc. 

### `sum_erase_eq`

 A sum over ordered pairs of distinct elements of a function of the unordered pair counts each
pair a < b twice. 

### `card_state_pd`

 A row has d nodes with pd half-edges each, so its states are the strings of p·d²·L bits. 

### `card_labels_le`

 The number of labels of two rows. 

 ### The rectangles 

### `card_Ω_pd`

 The number of rectangles of a grid with p rows and d columns is C(p,2)·C(d,2). 

 ### The row network 

### `rowNet_c_le_pd`

 Two rows have capacity at most d²·mL if every rectangle is charged at most 2mL bits. 

### `rowNet_shaped_pd`

 The shape of the row network when every rectangle is charged at most 2mL bits, m ≥ 1: its size
is m·(p·d²·L). 

### `abs_rowNet_Ψ_lt`

 The interaction of two rows is a product of at most d² values of the functions at the
rectangles. 

### `rowNet_sized_pd`

 The shape and the magnitudes of the row network when every rectangle is charged at most 2mL
bits, m ≥ 1. 

### `U_rowNet_pd`

 The total U of the row network: it counts ordered pairs of rows, so every vertical edge and
every rectangle counts twice. 

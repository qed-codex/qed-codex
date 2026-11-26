---
{
  "module": "proof/rates/ClauseBound/Rec/CountRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/CountRow.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/CountRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The mean number of blocks with an odd number of entries 11

For a label β on n positions that are cut into δ blocks, odd(β) is the number of blocks with an odd
number of entries 11, and μ is the mean of odd(β) over all β, rounded down.
This file shows 2μ ≤ δ (`two_mul_mu_le`) and a closed form of μ (`mu_eq`).

A label is the family of its parts in the blocks, so odd(β) is the number of marked places of a
choice of one element from each of δ finite sets, where the marked elements of
the set of block b are the labels on b with an odd number of entries 11. At most half of the labels
on a block are marked, which gives the bound on the mean.
The auxiliary statements are in the namespace `ClauseBound.Rec.CountRow`. 

 ### The mean of the number of marked places 

### `card_marked`

 The share of the choices that are marked at the place b is |S b|/|Ω b|. 

### `sum_marked`

 The sum of the number of marked places over all choices is the number of choices times Σ_b |S
b|/|Ω b|. 

 ### At most half of the labels on a set of positions have an odd number of entries 11 

### `prod_sg`

 The product of the signs of a label is −1 if the number of entries 11 is odd, and 1 otherwise. 

### `two_mul_card_odd_add`

 On a set of N positions, twice the number of labels with an odd number of entries 11, plus 2^N,
is the number of all labels. 

### `two_mul_card_odd_le`

 Twice the number of labels with an odd number of entries 11 is at most the number of all labels. 

 ### A label as a choice of one label on every block 

### `oddSet`

 The labels on block b with an odd number of entries 11. 

### `mean`

 The mean of odd(β) over all β. 

### `card_blk_filter`

 The number of entries 11 of β in block b, counted in the part of β in that block. 

### `odd_eq`

 odd(β) is the number of blocks in which the part of β is marked. 

### `card_lab`

 There are 4^n labels. 

### `card_choices`

 There are 4^n choices of one label on every block. 

### `sum_odd`

 The sum of odd(β) over all β is 4^n times the mean. 

### `mu_le_mean`

 μ is at most the mean. 

### `mean_lt`

 The mean is below μ + 1. 

### `mean_le`

 The mean is at most δ/2. 

### `share_eq`

 The share of the marked labels on a block of N ≤ h positions is (1 − 2^{−N})/2, written with the
denominator 2^{h+1}. 

### `mean_eq`

 The mean with the denominator 2^{h+1}. 

### `two_mul_mu_le`

 2μ ≤ δ. 

### `mu_eq`

 μ in closed form: the sum of (2^{n_b} − 1)·2^{h − n_b} over the blocks b, where n_b is the
number of positions of b, divided by 2^{h+1} and rounded down. 

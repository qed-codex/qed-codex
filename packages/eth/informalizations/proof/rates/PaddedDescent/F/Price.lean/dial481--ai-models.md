---
{
  "module": "proof/rates/PaddedDescent/F/Price.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Price.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Price.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The cheaper side network has U ≤ Ubar

`min_price_le` bounds the smaller of the prices `priceRow` and `priceCol` of a choice `y` of pieces
(the part of the total U of the row and of the column side network that the rectangles add) by
ρ·g⁴·n + g⁴/2, with ρ = (log₂ 12)/4 ≈ 0.896, not the ρ = 11/12 of Lemma 2. This file proves ρ <
717/800 and
turns the bound into the natural number `Ubar g n`. 

### `rho_lt`

 ρ = (log₂ 12)/4 < 717/800, because 12²⁰⁰ < 2⁷¹⁷. 

### `min_price_nat`

 The cheaper price plus the g²(g−1)n bits of the straight edges is at most the natural number
`Ubar g n`, by `min_price_le` and ρ < 717/800. 

### `U_side_le`

 The side that `sideCtx` chooses has U ≤ Ubar. 

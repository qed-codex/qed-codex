---
{
  "module": "proof/rates/PaddedDescent/F/ArithLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithLevel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 What one level of the recursion does to the numbers of an instance (label length, bits per
entry), as inequalities between natural numbers about the functions Pn, Ubar, lamNext, bNext,
instLen of PaddedDescent.F.Prog. No programs occur here. 

 ### One level: the label length 

### `mul_Ubar_le`

 800·Ubar ≤ 800g³Λ + 717g⁴Λ + 400g⁴ + 800. 

### `lamNext_mul_le`

 D·K²·lamNext ≤ D·Ubar + 3g³Λ + 6g⁴Λ + D·K², with D = `Dcol`. 

### `lamNext_contract`

 The contraction of one level. With Q = g⁴Λ (the square of the number of nodes times the label
length) before the level and
Q' = K²·lamNext after it: Q' ≤ (8963/10000)·Q + g⁴. 

 ### One level: the number of bits of an entry 

### `bNext_le`

 The entries after one level have at most g³B + 2g⁴Λ bits. 

### `bNext_le'`

 A weaker form of `bNext_le`: 6g³B + 8g⁴Λ instead of g³B + 2g⁴Λ. 

 ### The exponents of the budgets of one level 

### `mul_Pn_mul_le`

 The states of a class: K times the exponent is at most 4g⁴Λ. 

### `mul_Pn_eq`

 The labels inside a class: g times the exponent is 2g⁴Λ. 

### `four_mul_nRect_le`

 The number of rectangles is at most g⁴/4. 

### `nRect_le`

 The number of rectangles is at most g⁴. 

### `pow_le_two_pow_mul`

 The colourings: K^g ≤ 2^{Kg}. 

### `pow_le_two_pow_sq`

 The colourings: K^g ≤ 2^{g·g}. 

### `instLen_le`

 The length of an instance: the number of table entries of a row times a polynomial factor. 

 ### The next level is much bigger 

### `six_cube_mul_cube_le`

 6g³·K³ ≤ (g·g)³, if 2K ≤ g. 

### `pow_facts`

 24K³ ≤ 16(g·g)³ and 2K² ≤ (g·g)², if 2K ≤ g. 

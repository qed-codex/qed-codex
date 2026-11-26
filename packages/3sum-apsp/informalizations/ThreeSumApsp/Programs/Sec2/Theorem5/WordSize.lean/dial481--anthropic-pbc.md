---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/WordSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/WordSize.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/WordSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 in the light language: the limits

Section 2.4.4, "Word size": all numbers that the algorithm forms have polynomially many values, so
they fit in a word; the same holds for the addresses.  This file has no program in it.  For L = 19m,
D = 4^m with m ≥ 1, N ≥ D^18 and w wanted positions with w · 2^m ≤ N² it shows:

* the input, the output and the work area together have at most N^4 cells (`cells_le_pow_four`);
* the powers b^{L+1} with b ≤ 10 are at most N³, and the square of the number of bands is at most
  N^4 (`pow_succ_le_cube`, `numBands_succ_sq_le`).


### `thm5Par`

 The parameters of Theorem 5: L = 19m. 

### `four_pow_eighteen_le`

 N ≥ 4^18. 

### `one_le_of_D_pow_le`

 N ≥ 1. 

### `levels_add_two_le`

 L + 2 ≤ N. 

### `D_le_of_D_pow_le`

 D ≤ N. 

### `ten_pow_levels_le_sq`

 10^L ≤ N². 

### `seven_pow_levels_le_sq`

 7^L ≤ N². 

### `K_levels_le`

 K ≤ N. 

### `K0_sq_levels_le`

 K₀² ≤ N. 

### `D_rpow_neg_le_one`

 D^{-1/18} ≤ 1. 

### `numBands_mul_ten_pow_le`

 The encodings of all the row bands have at most 2 N² cells. 

### `numBands_sq_le`

 There are at most 16 N² tiles. 

### `numBands_le_two_mul`

 There are at most 2N bands. 

### `le_sq_of_mul_two_pow_le`

 w ≤ N². 

 ## The number of cells 

### `cells5_eq`

 The work area, written out. 

### `end5_eq`

 The work area starts at the free pointer. 

### `cells_le_pow_four`

 **The space**: the input (3 + 2 N D + 2 w cells), the output (w cells) and the work area have at
most N^4 cells together. 

 ## The word 

### `pow_le_pow_of_D_pow_le`

 The powers of N increase. 

### `ten_pow_succ_le_cube`

 10^{L+1} ≤ N³. 

### `pow_succ_le_cube`

 b^{L+1} ≤ N³ for every base b ≤ 10. 

### `numBands_succ_sq_le`

 (nB + 1)² ≤ N^4. 

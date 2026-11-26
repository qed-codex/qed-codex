---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Limits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Limits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Limits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 4.4: the limits of the programs with rational parameters

`lim31` gives the limits within which the programs run, in two regimes: for m < m₀ queries compute
inner products; for m ≥ m₀ the limits are those of Theorem 30 plus the numbers formed in the
computation of L and t. They are what the programs need (`lim31_ok`), they allow exactly the cells
of the structure (`lim31_space`), and they are polynomial in N (`small_lim31`): every summand is at
most a constant, which depends on the parameters only, times ((N + 1) (D₀ + 1))^(20 + 2c).


 ## The limits 

### `extraWord31`

 The numbers that the computation of L and t and the comparison with the threshold form. 

### `wordSmall31`

 The word bound when m is below the threshold. 

### `word30At`

 The word bound of Theorem 30 at the parameters of the programs. 

### `lim31`

 The limits of the programs. 

### `Lim30.of_word_le`

 Larger words do no harm. 

### `lim31_ok_small`

 Below the threshold every number that the programs form is a summand of the word bound. 

### `lim31_ok_large`

 From the threshold on the word bound of Theorem 30 covers 4^m and the inner products, and the
numbers on the way to L and t are added to it. 

### `lim31_ok`

 The limits are what the programs need. 

### `lim31_facts`

 The limits allow for the nesting of calls and for the numbers of the input. 

 ## The limits are polynomial in N

All limits are at most `slopeConst31 G` times the polynomial B = ((N + 1) (D₀ + 1))^(20 + 2c): the
summands that grow with N and D₀ are at most a numeral times B, and each summand that depends on the
parameters only occurs in `slopeConst31 G`. 

### `slopeConst31`

 The constant factor in the polynomial bound on the limits; it depends on the parameters only. 

### `slopeExp31`

 The exponent of two in the polynomial bound on the limits: the number of binary digits of the
constant factor. 

### `blockAt_le`

 The base address of the block of Theorem 30 is polynomial in N, for a free pointer behind an
input of 3 + 2 N D₀ + 3 w cells, w ≤ N². 

### `limPoly31`

 The polynomial B = ((N + 1) (D₀ + 1))^(20 + 2c). 

### `slopeConst31_mul`

 The constant times B, summand by summand. 

### `small_of_le`

 Limits below the constant times B are small. 

### `am_add_pm_le`

 The numbers a m and p m on the way to L and t. 

### `wordSmall31_le`

 The word bound below the threshold. 

### `word30At_add_le`

 The word bound from the threshold on. 

### `small_lim31`

 **The limits are polynomial in N.** 

 ## Cells and natural numbers 

### `lim31_space`

 The limits allow exactly the cells of the structure. 

### `lim31_natCast_le`

 A natural number up to the free pointer fits in a word. 

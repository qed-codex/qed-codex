---
{
  "module": "ThreeSumApsp/Spec/Sec2/Theorem5/Layout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Layout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Layout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One computable layout of the tiling

The statements of Section 2.3.4 about the tiling hold for every `Layout`: every numbering of the
rows and columns of a block by strings, and every table of `K₀²` subsets of size `m`.  A
program needs one layout that it can compute.  In `stdLayout` the rows and columns of a block are
numbered by the base-3 codes of their strings, the columns of `X` by base-4 codes, and the block
product `(g, h)` of a tile gets the subset number `g K₀ + h` of the enumeration `unrank`.

The strings of Lemma 9 are glued from an inner part, at the levels of a set `Q`, and an outer part,
at the other levels.  Their codes are formed digit by digit:

1. the digits of a glued string are the digits of its two parts, interleaved along the mask of `Q`
   by `weaveList` (`ofFn_glue`), because the `k`-th level of `Q` has exactly `k` levels of `Q` below
   it (`Finset.card_filter_lt_orderEmbOfFin`, `count_take_maskOf`);
2. so `outDigitsOfPos` lists the digits, and `outCodeOfPos` is the code, of the output string of a
   position `(I, J)` (Section 2.4.4, `codeO_outStrOfPos`, `digitList_outCodeOfPos`);
3. and `gluedCode` is the code of the left or right string with given parts (`codeL_leftStrOf`,
   `codeR_rightStrOf`).  The input array of a band holds the entries of `X` or `Y` at these codes
   and 0 elsewhere (`bandArrayL_at`, `bandArrayL_eq_zero`, and the same for `R`).


 ## The layout 

### `tableIndex_lt`

 `g K₀ + h` is below `binom(L, m)` for `g, h < K₀`. 

### `stdLayout`

 The computable layout: the rows and columns of a block are numbered by the base-3 codes of their
strings, the columns of `X` by base-4 codes, and the block product `(g, h)` of a tile gets the
subset number `g K₀ + h` of the enumeration `unrank`. 

### `codeOuter_rowIdx`

 The row with number `k` of a block is indexed by the string with code `k`. 

### `codeOuter_colIdx`

 The column with number `k` of a block is indexed by the string with code `k`. 

### `ofFn_rowIdx`

 The string that indexes the row with number `k` of a block consists of the base-3 digits of
`k`. 

### `ofFn_colIdx`

 The string that indexes the column with number `k` of a block consists of the base-3 digits of
`k`. 

### `codeInner_innerIdx`

 The column with number `k` of `X` is indexed by the string with code `k`. 

### `maskOf_table`

 The mask of the subset of a block product. 

 ## Counting the levels of a set below a level 

### `count_take_maskOf`

 The entries `true` (and `false`) among the first `n` entries of the mask of `Q` count the levels
of `Q` (and outside `Q`) below `n`. 

 ## The code of a glued string 

### `ofFn_glue`

 The digits of a string glued from `inner` at the levels of `Q` and `outer` at the other levels
are interleaved along the mask of `Q`. 

### `code_glue`

 The code of a string of digits glued from `inner` at the levels of `Q` and `outer` at the other
levels, by Horner's rule on the interleaved digits. 

 ## The digits and the code of the output string of a position 

### `outDigits`

 The digits of the output string whose inner set has the mask `mask`, with `m` levels, and whose
row and column have the digits `rI` and `rJ` in base 3: 9 at the levels of the set, and `3 x + y` at
the other levels, where `x` and `y` run through `rI` and `rJ`. 

### `length_outDigits`

 An output string has one digit for each level. 

### `getD_outDigits_of_true`

 The digit at a level of the inner set is 9. 

### `getD_outDigits_of_false`

 The digit at a level outside the inner set is `3 x + y` for the next digits `x` of the row and
`y` of the column. 

### `lt_of_mem_outDigits`

 The digits of an output string are below 10. 

### `codeO_outStrOf`

 The code of the output string with inner set `Q`, row `r` and column `c`. 

### `maskNo`

 The number, in the enumeration `unrank`, of the subset of the block product of the position
`(I, J)`. 

### `maskNo_lt`

 The subset of a position is one of the subsets of size `m`. 

### `outDigitsOfPos`

 The digits of the output string of the position `(I, J)`, from the block numbers and the base-3
digits of the offsets of `I` and `J`. 

### `outCodeOfPos`

 The code of the output string of the position `(I, J)`: Horner's rule on its digits. 

### `length_outDigitsOfPos`

 The output string of a position has `L` digits. 

### `digitList_outCodeOfPos`

 The digits of the code of the output string of a position. 

### `codeO_outStrOfPos`

 `outCodeOfPos` computes the code of the output string of a position, for the computable layout.


 ## The codes of the left and right strings, and the input arrays of the bands 

### `gluedDigits`

 The digits of the left string with inner set given by `mask`, outer part with the digits `o` and
inner part with the digits `i`: `o_j` at the `j`-th level outside the set, and `3 + i_j` at the
`j`-th level of the set.  The right string with the same parts has the same digits. 

### `length_gluedDigits`

 A left or right string has one digit for each level. 

### `lt_of_mem_gluedDigits`

 The digits of a left or right string are below 7. 

### `gluedCode`

 The code of the left string, and of the right string, with inner set given by `mask`, outer part
with code `r` and inner part with code `k`. 

### `gluedCode_lt`

 The code of a left or right string of `L` levels is below `7^L`. 

### `codeStr_glue`

 Left and right strings at once: over an alphabet of seven letters in which the outer letter
number `i` has the digit `i` and the inner letter of the pair `p` the digit 3 plus the digit of `p`,
the string glued from the inner letters of `π` and the outer letters of `r` has the code
`gluedCode`. 

### `codeL_leftStrOf`

 The code of the left string with inner set `Q`, outer part `r` and inner part `π`. 

### `codeR_rightStrOf`

 The code of the right string with inner set `Q`, inner part `π` and outer part `c`. 

### `gluedCode_table_left`

 `gluedCode` at the subset of the block product `(g, h)`, a row number and a column number is the
code of a left string. 

### `gluedCode_table_right`

 `gluedCode` at the subset of the block product `(g, h)`, a column number of the block and a row
number of `Y` is the code of a right string. 

### `bandArrayL_at`

 The input array of a row band, entry by entry: at the code `gluedCode` of the subset of the
block product `(g, h)`, the row `r` of the block and the column `k`, it holds the entry of (the
padded) `X` in row `(β K₀ + g) N₀ + r` and column `k`. 

### `bandArrayR_at`

 The input array of a column band, entry by entry: at the code `gluedCode` of the subset of the
block product `(g, h)`, the column `c` of the block and the row `k`, it holds the entry of (the
padded) `Y` in row `k` and column `(β K₀ + h) N₀ + c`. 

### `bandArrayL_apply_eq_zero`

 The input array of a row band is 0 at every left string whose inner set is not in the table. 

### `bandArrayR_apply_eq_zero`

 The input array of a column band is 0 at every right string whose inner set is not in the
table. 

### `bandArrayL_eq_zero`

 The input array of a row band is 0 at every place that is not a code `gluedCode` as in
`bandArrayL_at`. 

### `bandArrayR_eq_zero`

 The input array of a column band is 0 at every place that is not a code `gluedCode` as in
`bandArrayR_at`. 

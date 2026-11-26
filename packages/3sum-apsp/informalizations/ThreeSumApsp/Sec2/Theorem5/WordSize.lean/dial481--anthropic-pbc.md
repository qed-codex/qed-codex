---
{
  "module": "ThreeSumApsp/Sec2/Theorem5/WordSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Theorem5/WordSize.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Theorem5/WordSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 2.4.4: the remaining minutiae and the word size

* Minutiae.  The `K₀²` subsets, the tiles and the positions of `W` number `O(N² / D^{1/18})` in all
  (`minutiae_total_le`), because `K ≤ N` (`K_le_of_D_pow_le`), there are at most `4N²/N₀` tiles
  (`card_tiles_mul_N0_le`), `|W| ≤ 2^{-m} N²`, and `N, N₀ ≥ 2^{m/9}` (`two_rpow_le_of_D_pow_le`,
  `two_rpow_le_N0`).
* Word size.  An entry of an input array is an entry of `X` or `Y` or 0 (`abs_bandArrayL_le`,
  `abs_bandArrayR_le`); an encoded number is a `±1` combination of at most `7^L` of them
  (`abs_encodingL_le`, `abs_encodingR_le`); a value of `Pruned` is a sum of at most `10^L` products
  of two encoded numbers (`abs_Pruned_le`); and `10^L ≤ N²` by equation (6) (`ten_pow_le_sq`).


 ### The remaining minutiae 

### `two_rpow_ninth_le`

 `2^{m/9} ≤ 2^m`. 

### `one_le_saving_mul`

 A number that is at least `2^{m/9}` is at least 1 after multiplication by `2^{-m/9}`. 

### `K_le_of_D_pow_le`

 Section 2.4.4, in "the remaining minutiae": "K ≤ N". 

### `card_tiles_mul_N0_le`

 Section 2.4.4, in "the remaining minutiae": "there are at most 4N²/N₀ tiles", where `N` is the
padded size. 

### `two_rpow_le_of_D_pow_le`

 Section 2.4.4, in "the remaining minutiae": `N ≥ 2^{m/9}`. 

### `two_rpow_le_N0`

 Section 2.4.4, in "the remaining minutiae": `N₀ ≥ 2^{m/9}`. 

### `minutiae_parts`

 The three counts of "the remaining minutiae" (Section 2.4.4), one by one: the subsets in the
table, the tiles, and the positions of `W`. 

### `minutiae_total_le`

 Section 2.4.4: "O(L) operations per subset, per tile, and per position of W, which is
O(L 2^{-m/9} N²) in all": the number of these objects, with the `K₀²` subsets counted as at most
`K`, as the paper does ("as K ≤ N").  Here `N` is the size of the input.  The constant is
`18 = 1 + 16 + 1`, because the padding at most doubles `N`. 

 ### The word size 

### `sum_table_eq_zero_or`

 The subsets in the table are distinct (Section 2.3.4), so a sum over the table that selects the
subset `Q` is one of its terms or 0. 

### `abs_bandArrayL_le`

 Section 2.4.4, word size: "The input entries are of this size, by assumption." Every entry of
the input array of a row band is an entry of `X` or 0.

NOTE.  `0 ≤ A` is needed only when `N = 0`. 

### `abs_bandArrayR_le`

 Section 2.4.4, word size: "The input entries are of this size, by assumption." Every entry of
the input array of a column band is an entry of `Y` or 0.

NOTE.  `0 ≤ B` is needed only when `N = 0`. 

### `abs_encodeWith_le`

 A combination of the entries of an array, with a product of coefficients 0, 1 or -1 for each
entry, is at most the number of entries times the largest absolute value of an entry. 

### `abs_encodingL_le`

 Section 2.4.4, word size: "Every number in an encoding […] is a ±1 combination of at most 7^L
input entries", so its absolute value is at most `7^L` times the largest absolute value of an input
entry.  For the encoding of `a`. 

### `abs_encodingR_le`

 Section 2.4.4, word size: "Every number in an encoding […] is a ±1 combination of at most 7^L
input entries".  For the encoding of `b`. 

### `abs_Pruned_le`

 Section 2.4.4, word size: "every value computed by Pruned is a sum of at most 10^L products of
two encoded numbers". 

### `ten_pow_le_sq`

 Section 2.4.4, word size: "10^L ≤ N² by (6)", for `L = 19m` and `N ≥ D^18`. 

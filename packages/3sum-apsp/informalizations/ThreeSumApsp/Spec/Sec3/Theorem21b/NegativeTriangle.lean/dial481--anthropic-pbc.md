---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem21b/NegativeTriangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21b/NegativeTriangle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21b/NegativeTriangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Negative Triangle from Exact Triangle, on lists of integers

For Theorem 21(b), after [VW13, Proposition 3.4]: whether a triangle has negative weight is
expressed by O(log U) equations between binary prefixes of the shifted weights.

* The weights in `[-U, U]` are shifted to the natural numbers `x = w(a,b) + U`, `y = w(b,c) + U`,
  `v = 2U - w(a,c)`, so that a triangle is negative exactly if `x + y < v`.  The routine computes
  the prefixes `⌊z/2^ℓ⌋` (`prefQ`) of all the numbers `2x`, `2y`, `2v`, which are at most `6U`, at
  once (`negStart`, `bounds_of_mem_negStart`, `zipWith_shiftQ`, `map_shiftR`).
* For each level `ℓ` and for `e = 2` and `e = 3` the reduction makes the instance of Exact Triangle
  with the weights `⌊2x/2^ℓ⌋`, `⌊2y/2^ℓ⌋` and `e - ⌊2v/2^ℓ⌋` (`negThird`, `triOf_level`).  There is
  a negative triangle if and only if one of these instances, at a level `ℓ < L` where `3U < 2^L`,
  has a zero triangle (`hasNegativeTriangle_iff_exists_level`).


 ## The instances of the levels 

### `map_prefQ_start`

 At the top level the prefixes are zero. 

### `negStart`

 The shifted and doubled weights: `2x = 2 (w(a,b) + U)`, `2y = 2 (w(b,c) + U)`,
`2v = 2 (2U - w(a,c))`, one list after the other. 

### `negThird`

 The third list of the instance for the level `ℓ` and the number `e`: the weights
`e - ⌊2v/2^ℓ⌋`.  A zero triangle is a triple with `⌊2v/2^ℓ⌋ = ⌊2x/2^ℓ⌋ + ⌊2y/2^ℓ⌋ + e`. 

### `bounds_of_mem_negStart`

 The numbers of the start are between 0 and `6U`. 

### `abs_le_of_mem_negThird`

 The numbers of the third list are at most `6U` in absolute value. 

### `prefQ_two_mul`

 The prefix of twice a natural number that is written as an integer. 

### `getD_map_entry`

 An entry of a matrix to whose entries a function has been applied. 

### `triOf_level`

 The instance made of the lists of the level `ℓ` is the instance of the reduction. 

### `hasNegativeTriangle_iff_exists_level`

 **Negative Triangle by prefixes.**  If `3U < 2^L`, then there is a negative triangle if and only
if, at one of the levels `ℓ < L` and for `e = 2` or `e = 3`, the instance made of the prefixes has a
zero triangle. 

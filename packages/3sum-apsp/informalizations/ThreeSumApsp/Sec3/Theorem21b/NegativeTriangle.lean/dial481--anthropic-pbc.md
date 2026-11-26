---
{
  "module": "ThreeSumApsp/Sec3/Theorem21b/NegativeTriangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21b/NegativeTriangle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21b/NegativeTriangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(b): Negative Triangle reduces to Exact Triangle

[VW13, Theorem 3.3] in the form needed for Theorem 21(b): one question about a negative triangle
becomes `O(log U)` questions about a zero triangle.  Shifting the weights turns "the triangle is
negative" into `x + y < v` for natural numbers (`S_neg_iff`).  Let the gap at level `ℓ` be
`⌊2v/2^ℓ⌋ - ⌊2x/2^ℓ⌋ - ⌊2y/2^ℓ⌋` (`prefixGap`).  If `x + y < v`, the gap at level 0 is
`2(v - x - y) ≥ 2`, which is why the numbers are doubled; from one level to the next a gap of at
least 4 stays at least 2, and the gap is below 2 once `2^ℓ > v`.  So at some level the gap is
exactly 2 or exactly 3, and conversely a gap of at least 2 gives `x + y < v`
(`lt_iff_exists_prefixGap`).  "The gap is `e`" is an exact condition on a triangle (`negToExact`,
`negToExact_isZeroTriangle_iff`).  Together: `hasNegativeTriangle_iff` and
`theorem_21b_negative_to_exact`.


### `prefixGap`

 The gap at level `ℓ`: the difference `⌊2v/2^ℓ⌋ - ⌊2x/2^ℓ⌋ - ⌊2y/2^ℓ⌋` of the prefixes of `2v`,
`2x` and `2y`. 

### `add_lt_of_two_le_prefixGap`

 A gap of at least 2 gives `x + y < v`: with `X`, `Y`, `V` for the three prefixes,
`2x + 2y < (X + Y + 2) 2^ℓ ≤ V 2^ℓ ≤ 2v`. 

### `pow_le_of_two_le_prefixGap`

 A gap of at least 2 needs `2^ℓ ≤ v`: the prefix `V` of `2v` is at least 2, so
`2 · 2^ℓ ≤ V 2^ℓ ≤ 2v`. 

### `two_le_prefixGap_succ`

 A gap of at least 4 leaves a gap of at least 2 at the next level: a prefix at level `ℓ + 1` is
half the prefix at level `ℓ`, rounded down, so the new gap is at least `(4 - 1)/2`. 

### `exists_prefixGap_eq`

 Climbing from a level at which the gap is at least 2, the first level at which the gap is below
4 has gap 2 or 3.  There is such a level, because a gap of at least 2 needs `2^ℓ ≤ v`. 

### `lt_iff_exists_prefixGap`

 For Theorem 21(b), after [VW13, Proposition 3.4]: whether a triangle has negative weight is
expressed by O(log U) equations between binary prefixes of the shifted weights.
One way to write this: for natural numbers with `v < 2^L`, `x + y < v` if and only if
at one of the levels `ℓ < L` the gap `⌊2v/2^ℓ⌋ - ⌊2x/2^ℓ⌋ - ⌊2y/2^ℓ⌋` is exactly 2 or exactly 3.
(This form need not be literally the one of [VW13].) 

### `negToExact`

 The Exact Triangle instance for the level `ℓ` and the exact value `e`.  The weights `w(a,b)`,
`w(b,c)` and `w(a,c)` in `[-U, U]` are first shifted to the natural numbers `x = w(a,b) + U`,
`y = w(b,c) + U` and `v = 2U - w(a,c)`, so that the triangle is negative exactly if `x + y < v`;
then `x` and `y` are replaced by the prefixes `⌊2x/2^ℓ⌋` and `⌊2y/2^ℓ⌋`, and `v` by `e - ⌊2v/2^ℓ⌋`.


### `negToExact_bound`

 The weights of these instances are at most `6U` in absolute value. 

### `negToExact_isZeroTriangle_iff`

 A triangle has weight zero in the instance for `ℓ` and `e` exactly if the gap at level `ℓ` is
`e`. 

### `S_neg_iff`

 A triangle is negative exactly if the shifted weights satisfy `x + y < v`. 

### `hasNegativeTriangle_iff`

 The reduction of [VW13, Theorem 3.3], for weights in `[-U, U]` with `3U < 2^L`: there is a
negative triangle if and only if, at one of the levels `ℓ < L` and for `e = 2` or `e = 3`, the
instance made of the prefixes has a zero triangle. 

### `negToExactList`

 The list of the instances for all levels `ℓ < L` and `e = 2` or `e = 3`. 

### `theorem_21b_negative_to_exact`

 The combinatorial content of [VW13, Theorem 3.3] in the form needed for **Theorem 21(b)**:
whether an instance with weights in `[−U, U]` has a negative triangle is decided by asking
`O(log U)` times whether there is a zero triangle, each time after changing the weights, edge by
edge, to numbers of absolute value `O(U)`.  The instances are obtained from the given one by
applying to each weight a function that depends only on `U`, on the number of the instance and on
which of the three parts' pairs the edge joins.  There are at most `2⌊log₂ U⌋ + 6` of them, and
their weights are at most `6U` in absolute value. 

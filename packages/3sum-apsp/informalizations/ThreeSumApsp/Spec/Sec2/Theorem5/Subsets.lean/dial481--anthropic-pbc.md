---
{
  "module": "ThreeSumApsp/Spec/Sec2/Theorem5/Subsets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Subsets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Subsets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The subsets of size `m` of `{1, …, L}`, enumerated

Section 2.3.4: "We fix K₀² ≤ K distinct subsets of {1, …, L} of size m, one for each block product
of the grid, the same in every tile."  A subset is a *mask*: the list of `L` truth values saying
which levels belong to it, level 1 first (`maskSet`, `maskOf`).  The subsets of size `m` are
enumerated with those containing level 1 first, and so on recursively: `unrank L m r` is number `r`
in this order.

* The masks `unrank L m r` with `r < (L choose m)` have length `L` and `m` entries `true`, and they
  are distinct, because `rank` recovers `r` (`length_unrank`, `count_unrank`, `rank_unrank`).  So
  their sets of levels are distinct subsets of size `m` (`card_maskSet_unrank`,
  `eq_of_maskSet_unrank_eq`).
* A program lists them in a table without arithmetic, each mask from the one before it: the first
  mask is `true^m false^{L-m}` (`unrank_zero`), and two consecutive masks are
  `pre true false false^a true^b` and `pre false true true^b false^a` (`unrank_succ_shape`).


 ## The enumeration 

### `unrank`

 The mask number `r` (counted from 0) among the masks of length `L` with `m` entries `true`. 

### `rank`

 The position of a mask in the enumeration.  A mask that begins with `false` comes after all the
masks with the same number of entries `true` that begin with `true`; if the rest `l` of the mask has
`k > 0` entries `true`, there are `(|l| choose k - 1)` of them. 

### `length_unrank`

 A mask of the enumeration has length `L`. 

### `count_unrank`

 A mask of the enumeration has `m` entries `true`. 

### `count_false_unrank`

 A mask of the enumeration has `L - m` entries `false`. 

### `rank_unrank`

 `rank` undoes `unrank`. 

### `eq_of_unrank_eq`

 Different numbers give different masks. 

 ## Masks and sets of levels 

### `maskSet`

 The set of levels of a mask. 

### `maskOf`

 The mask of a set of levels. 

### `length_maskOf`

 The mask of a set of levels has one entry for each level. 

### `getD_maskOf`

 The entry of the mask at a level says whether the level belongs to the set. 

### `card_maskSet`

 The number of levels of a mask is the number of its entries `true`. 

### `card_maskSet_unrank`

 The set of levels of a mask of the enumeration has `m` elements. 

### `maskOf_maskSet`

 The mask of the set of levels of a mask of length `L` is that mask. 

### `eq_of_maskSet_unrank_eq`

 Different numbers give different sets of levels. 

 ## From one mask to the next 

### `unrank_zero`

 The first mask: `m` times `true`, then `L - m` times `false`. 

### `unrank_last`

 The last mask: `L - m` times `false`, then `m` times `true`. 

### `unrank_succ_shape`

 Two consecutive masks of the enumeration: write the first one as
`pre ++ [true, false] ++ false^a ++ true^b`, with the last occurrence of `true, false`; then the
next one is `pre ++ [false, true] ++ true^b ++ false^a`. 

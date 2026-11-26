---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem21b/FindNegativeTriangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21b/FindNegativeTriangle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21b/FindNegativeTriangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Finding a negative triangle by halving

[VW18, Lemma 4.1], one of the reductions behind Theorem 21(b): an algorithm that
decides whether a graph has a negative triangle also finds one.  The search keeps three offsets and
a side length `h` such that the `h × h × h` sub-instance at these offsets has a negative triangle
(`NegAt`), and replaces `h` by `⌈h/2⌉`.

* The sub-instance is an instance of its own, made of three blocks of the matrices (`subMat`,
  `hasNegativeTriangle_subMat_iff`), so the decision algorithm can be asked about it.
* Each of the three ranges `[o, o + h)` is covered by its two halves `[o, o + ⌈h/2⌉)` and
  `[o + h - ⌈h/2⌉, o + h)`, which overlap in one place if `h` is odd.  So one of the eight triples
  of halves (`octants`) has a negative triangle (`NegAt.split`).
* At side length 1 the sub-instance is the triangle (`NegAt.triangle`).
* The side lengths `⌈n/2⌉, ⌈⌈n/2⌉/2⌉, …, 1` that the search goes through (`halvingChain`) add up to
  at most `2n` (`sum_halvingChain_le`).


 ## Sub-instances 

### `NegAt`

 The sub-instance on the vertices `a0 + a`, `b0 + b`, `c0 + c` with `a, b, c < h` has a negative
triangle. 

### `hasNegativeTriangle_triOf_iff`

 A negative triangle of an instance read from three lists, with the vertices as numbers. 

### `hasNegativeTriangle_subMat_iff`

 The instance made of the three blocks has a negative triangle if and only if the sub-instance
has one. 

### `hasNegativeTriangle_iff_negAt`

 The whole instance is the sub-instance at the offsets 0 with side `n`. 

### `NegAt.triangle`

 A sub-instance of side 1 that has a negative triangle is a negative triangle. 

 ## The step of the search 

### `octants`

 The eight triples of halves: 0 stands for the lower half of a range and 1 for the upper
half. 

### `le_one_of_mem_octants`

 The entries of an octant are 0 or 1. 

### `exists_half`

 A number below `h` lies in the lower or in the upper half of `[0, h)`. 

### `NegAt.split`

 **The step of the search.**  If the sub-instance of side `h` has a negative triangle and
`h/2 ≤ h' ≤ h`, then so has one of the eight sub-instances of side `h'` made of lower and upper
halves. 

 ## The chain of side lengths 

### `halvingChain`

 The side lengths after `n`: `⌈n/2⌉`, then `⌈⌈n/2⌉/2⌉`, and so on down to 1.  Empty for `n ≤ 1`.


### `halvingChain_of_lt`

 The chain is empty for `n ≤ 1`. 

### `halvingChain_of_le`

 The chain starts with `⌈n/2⌉` for `n ≥ 2`. 

### `bounds_of_mem_halvingChain`

 Every side length of the chain is at least 1 and smaller than `n`. 

### `sum_halvingChain_le`

 The side lengths of the chain add up to at most `2n` (to at most `2n - 2`, for `n ≥ 1`). 

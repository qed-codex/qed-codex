---
{
  "module": "ThreeSumApsp/Spec/Sec5/Corollary39/MaxTriangleSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec5/Corollary39/MaxTriangleSearch.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec5/Corollary39/MaxTriangleSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Max-Weight Triangle from Exact Triangle (proof of Corollary 39)

Proof of Corollary 39: "By [VW13, Theorem 3.3], finding a maximum weight triangle costs O(log² n)
times as much" as deciding whether there is a triangle of weight zero.  The weight W of a maximum
weight triangle is found by a search with decisions of the form: is there a triangle of weight at
least w?  These are instances of Negative Triangle (`neg_iff_atLeast`).  A triangle of weight
exactly W is then found by three searches with decisions of the form: is there a triangle of weight
W with a ≥ a₀, b ≥ b₀, c ≥ c₀?  These are instances of Exact Triangle with the same vertex sets, in
which the other vertices are switched off by a large weight (`zero_iff_exactFrom`).  What the four
searches find is a triangle of maximum weight (`isMax_of_searches`).


 ## Switching off rows and columns 

### `maskL`

 The matrix in the list l, with Big added to the entries in the rows below r₀ and in the columns
below c₀. 

### `length_maskL`

 It has n² entries. 

### `getD_maskL`

 The entry (i, j) of the matrix with rows and columns switched off. 

### `getD_affL`

 The entry (i, j) of the matrix of the numbers m y + c. 

 ## The two kinds of decisions 

### `AtLeast`

 Some triangle has weight at least W. 

### `ExactFrom`

 Some triangle with a ≥ a₀, b ≥ b₀, c ≥ c₀ has weight exactly W. 

### `S_triOf`

 The weight of a triangle, in terms of the three lists. 

### `abs_S_le`

 The weight of a triangle is between -3U and 3U. 

### `neg_iff_atLeast`

 That some triangle has weight at least W, as an instance of Negative Triangle: the negated
weights, with W - 1 added to the third matrix. 

### `zero_iff_exactFrom`

 That some triangle with a ≥ a₀, b ≥ b₀, c ≥ c₀ has weight W, as an instance of Exact Triangle:
a triangle with a vertex that is switched off has a weight above 0. 

### `maskL_le`

 If the entries are at most U in absolute value, they are at most 7U + 1 after rows and columns
have been switched off. 

 ## The end of the four searches 

### `isMax_of_searches`

 What the four searches find is a triangle of maximum weight. 

### `exactFrom_zero`

 If some triangle has weight at least W and none has weight at least W + 1, some triangle has
weight exactly W. 

### `not_exactFrom`

 No vertex has a number from n on. 

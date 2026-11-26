---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/TimeBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/TimeBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/TimeBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39, minimum and maximum weight: the two claims about triangles in the light language

Proof of Corollary 39: "finding a maximum weight triangle costs O(log² n) times as much".  The
arithmetic that turns the time functions of the two hosts into the bounds of the claims
`Claim.VW13_Theorem_3_3_max` and `Claim.MinTriangleFromMax`, with "the problem is solved in time T"
read by `lightModel5` (`claim_VW13_Theorem_3_3_max`, `claim_minTriangleFromMax`).  With A := T + n²
(1 + log U) and Λ := log U + log n + 1, every search has O(Λ) rounds, a round of the searches for
the vertices takes O(A) steps, and a round of the search for the weight takes O(Λ A) steps
(`softO_maxTriTime`).


### `lv_le`

 The number of powers of two up to n is O(log n + 1). 

 ## The time of maxTri 

### `TimePar`

 The quantities in the time of maxTri: the size n, the bound U on the weights and a real number
u ≥ U, the time Tn of the solver of Exact Triangle, and an upper bound tau on its time at the two
bounds at which it is called. 

### `Ok`

 What is known about the quantities. 

### `work`

 A := T + n² (1 + log U). 

### `levels`

 Λ := log U + log n + 1. 

### `Ok.sq_le_work`

 n² ≤ A. 

### `Ok.one_le_work`

 1 ≤ A. 

### `tau_le_work`

 T ≤ A. 

### `Ok.log_nonneg`

 log n ≥ 0. 

### `Ok.one_le_levels`

 1 ≤ Λ. 

### `scale`

 The scale of the bound: powers of A and of Λ. 

### `softO_maxTriTime`

 **The time of maxTri** is O(A Λ²): every search has O(Λ) rounds, and n² and the times of the
solver are at most A. 

### `claim_VW13_Theorem_3_3_max`

 **Max-Weight Triangle from Exact Triangle.** 

### `claim_minTriangleFromMax`

 **Min-Weight Triangle from Max-Weight Triangle.** 

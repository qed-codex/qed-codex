---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/TimeBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/TimeBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/TimeBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The (min,+)-product from Negative Triangle: the claim

[VW18, Theorem 4.2] in the form needed for Theorem 21(b).  The three hosts
(finding from deciding, all pairs from finding, the product from all pairs) are composed, and their
time functions are bounded with the two properties of a good running time: T(s)/s is nondecreasing,
and T(s) ≥ s² (1 + log u).

Each host has one bound, up to a constant factor: finding costs O(T(n)) (findTime_dominated: the
side lengths of the search add up to at most 2n, and T(h) ≤ (h/n) T(n)); all pairs cost
O(n² T(⌈n^{1/3}⌉)) (pairsTime_dominated: there are O(n²) rounds, rounds_le); the product costs
O(log u) calls (mpTime_dominated, mpRounds_le).  claim_VW18_Theorem_4_2 puts the three together.


 ## Good running times 

### `sq_le`

 A good running time is at least s². 

### `one_le`

 A good running time is at least 1. 

### `le_mul_div`

 T(h) ≤ h T(s)/s for h ≤ s. 

### `const_mul`

 C T is a good running time for C ≥ 1. 

### `cbrtLeast_eq_cbrtCeil`

 The least s with s³ ≥ n is ⌈n^{1/3}⌉. 

 ## The parameters of a bound 

### `Run`

 What a bound on the time of a host speaks about: a bound T on the time Tn of the solver, and an
instance of size n with a bound U ≤ u on its numbers. 

### `Run.Valid`

 The solver keeps to its bound, and the instance is valid. 

### `Run.Good`

 The run is valid, and the bound on the time of the solver is a good running time. 

### `Run.Quadratic`

 The run is valid, and the bound on the time of the solver is at least n². 

### `Run.Valid.solver_le`

 The solver on the instance of the run keeps to its bound. 

 ## Finding from deciding 

### `roundBound_dominated`

 The round of the search that goes to the side length n costs O(T(n)):
8 (Tn + 150 n² + 130) ≤ 8 (T + 150 T + 130 T). 

### `search_dominated`

 The rounds of the search cost O(T(n)): T(h) ≤ h (T(n)/n), and the side lengths add up to at most
2n. 

### `findTime_dominated`

 **Finding from deciding**: the time grows by a constant factor only. 

 ## All pairs from finding 

### `rounds_le`

 The number of rounds of "all pairs" is at most 9n². 

### `pairsTime_dominated`

 **All pairs from finding**: O(n²) questions at the size ⌈n^{1/3}⌉. 

 ## The product from all pairs 

### `mpRounds_le`

 The number of rounds of the search is O(log u). 

### `mpTime_dominated`

 **The product from all pairs**: O(log u) calls, if a call takes at least n² steps. 

### `claim_VW18_Theorem_4_2`

 **[VW18, Theorem 4.2]: the (min,+)-product from Negative Triangle.** 

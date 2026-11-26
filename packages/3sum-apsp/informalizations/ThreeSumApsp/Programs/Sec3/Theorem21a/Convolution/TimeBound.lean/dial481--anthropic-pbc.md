---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/TimeBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/TimeBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/TimeBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Convolution-3SUM from Exact Triangle: the claim

Theorem 21(a), after [VW13, Theorem 4.3].  The arithmetic that turns the
host `isHost_c3` into the transfer of running times: if Exact Triangle is solved in time T, then
Convolution-3SUM on N numbers of absolute value at most u is solved in time
O(N^{3/2}) (1 + log u) + 2 (⌊√N⌋ + 1) T(⌊√N⌋ + 1, 3u) (`c3_solvedIn_explicit`,
`claim_VW13_Theorem_4_3`).

The host's own work is a cubic polynomial in ⌊√N⌋ (`exists_c3Own_le`), and the instances have
⌊√N⌋ + 1 ≤ 2 √N vertices per part (`natSqrt_succ_le`).


### `natSqrt_succ_le`

 `⌊√N⌋ + 1 ≤ 2 N^{1/2}` for `N ≥ 1`. 

### `isBigOPow_natSqrt_succ`

 `⌊√N⌋ + 1 = O(N^{1/2})`. 

### `c3Own`

 The host's own work: its time over a solver that takes no time. 

### `c3Time_eq`

 The time of the host is its own work and 2 (⌊√N⌋ + 1) runs of the solver. 

### `exists_c3Own_le`

 The host's own work is a cubic polynomial in ⌊√N⌋, so it is O(N^{3/2}). 

### `c3_solvedIn_explicit`

 Convolution-3SUM from Exact Triangle, with the explicit bound, where C is the constant of the
host's own work.  The weights of the instances are bounded by 2U + 1 ≤ 3u, because 1 ≤ U ≤ u.  The
factor 1 + log u is not needed here; it is the form in which the claim is stated. 

### `claim_VW13_Theorem_4_3`

 [VW13, Theorem 4.3] for programs of the light language: Convolution-3SUM from Exact Triangle. 

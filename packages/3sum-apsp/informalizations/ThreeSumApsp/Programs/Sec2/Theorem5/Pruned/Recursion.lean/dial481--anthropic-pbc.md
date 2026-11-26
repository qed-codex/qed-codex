---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Recursion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Recursion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Recursion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The pruned recursion (Section 2.4.2), recursive as printed

pruned(n, ea, eb, l, len, out, sp, p10).  The set S passed to the call is the increasing list of len
codes at l; ea and eb are the addresses at which the parts of the two encodings below the current
vertex begin; the array that is returned is written to the len cells from out, in the order of the
list.  The frame of a call with n ≥ 1 starts at sp: 11 cells for the bounds of the ten slices, len
cells for the codes without their first digits, len cells for the list of a child, len cells for the
values of a child.

(1) If n = 0: the product of the two numbers looked up, for each code of the list
    (`prunedBody_ends_zero`).
(2) The slices S_z are segments of the list (segBounds); S_λ is the merge of the slice at z_ij and
    the slice at z₀ (`prunedSlice_ends`, then union).
(3) For each term λ with S_λ ≠ ∅: the recursive call.
(4) The slice of the result at z_ij is C_{P_ij} restricted to S_{z_ij} (pick, writing); the slice at
    z₀ is the sum of the ten C_λ restricted to S_{z₀} (pick, adding, after the cells have been
    cleared).  Steps (3) and (4) for one term are `prunedChild_ends`.

One round of the loop over the ten terms is `prunedRound_ends`; the case n ≥ 1 is
`prunedSetup_ends` followed by the loop (`prunedBody_ends_succ`); `PrunedCtx.entry` is the induction
on n.  What the calls do to the memory is proved in Pruned/Memory.lean; here each call is one step.


 ## The program 

### `NN`

 The number n of levels that are left. 

### `PA`

 Where the part of the first encoding below the current vertex begins. 

### `PB`

 Where the part of the second encoding below the current vertex begins. 

### `PL`

 The list of the codes that are passed to the call. 

### `LEN`

 The length of that list. 

### `OUT`

 Where the values are written. 

### `SP`

 The frame of the call; it begins with the bounds of the ten slices. 

### `P10`

 The table of the powers of ten. 

### `PW`

 10^(n-1); for n = 0 the product of the two numbers looked up. 

### `RES`

 Results of calls that are not used. 

### `COD`

 The codes without their first digits. 

### `CH`

 The list of the child. 

### `VAL`

 The values of the child. 

### `NXT`

 The frame of the child. 

### `Z0`

 The position of the slice at z₀. 

### `NZ0`

 The length of the slice at z₀. 

### `LAM`

 The term λ. 

### `POS`

 The position of the slice at the output variable of λ. 

### `NPOS`

 The length of that slice (0 for λ = P₀). 

### `NCH`

 The length of the list of the child. 

### `prunedSlice`

 Step (2), first half: the position and the length of the slice at the output variable of λ. 

### `prunedChild`

 Steps (3) and (4) for a term λ with S_λ ≠ ∅. 

### `prunedRound`

 One round of the loop over the ten terms. 

### `prunedSetup`

 What a call with n ≥ 1 does before the loop: the slices are found, the parts of the frame get
their addresses, and the cells of the slice at z₀ are cleared. 

### `prunedBody`

 pruned(n, ea, eb, l, len, out, sp, p10). 

 ## What the proofs assume 

### `PrunedCtx`

 What the recursion assumes about its surroundings: the limits, its own place in the program, and
the entries of the four helpers, all with the constant h. 

### `PrunedPost`

 What a call of pruned achieves. 

### `PrunedIH`

 What the recursion may assume about the calls with n levels left: what `PrunedSpec` says, with
the running time of the program. 

 ## Step (1) 

### `prunedBody_ends_zero`

 The case n = 0. 

 ## One round of the loop 

### `roundState`

 The state in the loop over the ten terms: t is the term; res, pos, npos and nch are what the
locals RES, POS, NPOS and NCH hold. 

### `RoundInv`

 The invariant of the loop, before round t. 

### `prunedSlice_ends`

 Step (2), first half: the slice at the output variable of the term t begins at
segStart n codes t and is the first list of the round. 

### `prunedChild_ends`

 Steps (3) and (4) for a term t whose list is not empty: the recursive call and the two calls of
pick lead to the invariant of the loop (`RoundInv`) before round t + 1. 

### `prunedRound_ends`

 **One round of the loop**: steps (2), (3) and (4) for the term t. 

 ## The case n ≥ 1 

### `loopTime`

 The running time of the loop over the ten terms. 

### `loopTime_add_le`

 The loop, segBounds, fill and 66 more steps are the time of the call. 

### `prunedSetup_ends`

 Before the loop: afterwards the invariant of the loop (`RoundInv`) holds for t = 0. 

### `prunedBody_ends_succ`

 **The case n + 1**: the frame is set up, and the loop runs through the ten terms. 

 ## The recursion 

### `PrunedCtx.entry`

 **The pruned recursion meets its entry**, with the constant 50 h + 2000, where h is a common
constant of the four helpers. 

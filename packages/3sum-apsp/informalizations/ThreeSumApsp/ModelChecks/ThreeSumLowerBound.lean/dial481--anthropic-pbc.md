---
{
  "module": "ThreeSumApsp/ModelChecks/ThreeSumLowerBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ModelChecks/ThreeSumLowerBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ModelChecks/ThreeSumLowerBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM needs linear time on the word RAM

A check of the definition of "solved in time T on the word RAM" (`SolvedInTimeAt`; the model is that
of Section 2): it cannot be met for free.  A program that takes fewer than
`(n - 2) / 2` steps leaves one of the numbers unread (`exec_congr`, `exists_offset_notMem`).  On the
instance 1, -1, 1, 1, …, which has no solution, and on the instance with 0 at the place of the
unread number, which has one, it gives the same verdict.  The same holds for "solved in time
`O(n^r)`" in the sense of `EndStatement.lean` (`not_endStatement_solvedInTime_threeSum`, by
`agreement_solvedInTime`).


 ## Two instances of 3SUM that differ in one cell 

### `oddVec`

 The numbers `1, -1, 1, 1, …`: the second is -1, all others are 1. 

### `oddVec_eq_or`

 Each of the numbers `1, -1, 1, 1, …` is 1 or -1. 

### `not_threeSum_oddVec`

 The numbers `1, -1, 1, 1, …` are odd, so no three of them sum to 0. 

### `threeSum_update_oddVec`

 With 0 at a place `p ≥ 2` the numbers `1, -1, 1, 1, …` have a solution: `1 + (-1) + 0 = 0`. 

### `smallInst`

 Numbers of absolute value at most 1 as an instance of 3SUM with the bound `U = n^κ`. 

### `natAbs_oddVec_le`

 The numbers `1, -1, 1, 1, …` have absolute value 1. 

### `natAbs_update_oddVec_le`

 The numbers `1, -1, 1, 1, …` with one of them replaced by 0 have absolute value at most 1. 

### `loadWords_update_eq`

 A change of the number at place `p` changes the starting memory in the cell `1 + p` only. 

### `not_solvedInTimeAt_threeSum`

 For no exponent `a < 1`, no `e` and no `κ` does a program decide 3SUM in `O(n^a (log n)^e)`
time, because it cannot read its input. 

### `bigO_zero_of_neg`

 A bound `O(n^r)` of `EndStatement.lean` with a negative exponent `r` is a bound `O(1)`. 

### `not_endStatement_solvedInTime_threeSum`

 For no rational exponent `r < 1` does a program decide 3SUM in `O(n^r)` time in the sense of
`EndStatement.lean`, the sense of the five claims. 

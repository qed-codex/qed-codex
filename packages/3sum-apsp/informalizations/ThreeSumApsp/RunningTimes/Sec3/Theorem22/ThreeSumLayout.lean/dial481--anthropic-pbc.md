---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Theorem22/ThreeSumLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22/ThreeSumLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22/ThreeSumLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM: from a solver of the task to a program for the layout of the end statement

3SUM (Theorem 22).  `realized_threeSum`: if the task `s3Task` is solved in time T, then
`EndStatement.ThreeSum` is solved on the word RAM within a constant times T.

The input is n in cell 0 and the n numbers in the cells 1, …, n; the free pointer is n + 1
(`threeSumInst`).  The task speaks of the vector that is read from the list of the numbers, which is
the vector of the instance (`vecOf_ofFn`).  So the input meets the task's precondition
(`pre_threeSum`), and the result of a solver is the right verdict (`post_threeSum`).


### `vecOf_ofFn`

 The numbers of a list made from a function are the values of the function. 

### `threeSumInst`

 The instance of the task: the numbers stand from cell 1 on. 

### `pre_threeSum`

 The input of the end statement meets the precondition of the task. 

### `post_threeSum`

 The result of a solver of the task is the right verdict of the end statement's 3SUM. 

### `wrap3Sum`

 What connects 3SUM in the layout of the end statement with the task. 

### `realized_threeSum`

 **3SUM**: if the task is solved in time T, then 3SUM is solved on the word RAM within a constant
times T. 

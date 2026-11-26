---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Theorem19/Layout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem19/Layout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem19/Layout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Exact Triangle: from a solver of the task to a program for the layout of the end statement

Exact Triangle (Theorem 19).  `realized_exactTriangle`: if the task `etTask` is solved in
time T, then `EndStatement.ExactTriangle` is solved on the word RAM within a constant times T.

The input is n in cell 0 and the three matrices of weights from the cells 1, 1 + n² and 1 + 2n²; the
free pointer is 1 + 3n² (`triangleInst`).  The task speaks of the instance that is read from the
three lists, which is the instance itself (`triOf_rowMajor`).  So the input meets the task's
precondition (`pre_exactTriangle`), and the result of a solver is the right verdict
(`post_exactTriangle`).


### `triOf_rowMajor`

 The instance that is read from the three lists is the instance. 

### `input_exactTriangle`

 The input: the size and the three matrices, row by row. 

### `abs_le_of_mem_exactTriangle`

 The entries of the three matrices are within the bound. 

### `triangleInst`

 The instance of the task: where the three matrices stand. 

### `pre_exactTriangle`

 The input of the end statement meets the precondition of the task. 

### `post_exactTriangle`

 The result of a solver of the task is the right verdict of the end statement's Exact
Triangle. 

### `wrapTriangle`

 What connects Exact Triangle in the layout of the end statement with the task. 

### `realized_exactTriangle`

 **Exact Triangle**: if the task is solved in time T, then Exact Triangle is solved on the word
RAM within a constant times T. 

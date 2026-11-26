---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Theorem22/ApspLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22/ApspLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22/ApspLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# APSP: from a solver of the task to a program for the layout of the end statement

APSP (Theorem 22).  `realized_apsp`: if the task `apTask` is solved in time T, then
`EndStatement.APSP` is solved on the word RAM within a constant times T.

The input is n in cell 0, the adjacency matrix from cell 1 and the weights from cell 1 + n².  The
answer goes to the 2n² cells from 1 + 2n², and the free pointer is 1 + 4n² (`apspInst`).  The task
speaks of the graph with weights in `WithTop ℤ` that is read from the two lists, which is the graph
of the instance (`graphOf_apsp`).  So the input meets the task's precondition (`pre_apsp`), and what
a solver leaves in the output cells is what `EndStatement.APSP` asks for (`post_apsp`).


### `apspAdj`

 The adjacency matrix of an instance, as it is written into the memory. 

### `apspWeights`

 The weights of an instance, as they are written into the memory. 

### `input_apsp`

 The input: the size and the two matrices, row by row. 

### `graphOf_apsp`

 The graph that is read from the two lists is the graph of the instance. 

### `abs_le_of_mem_apspWeights`

 The weights are within the bound. 

### `apspInst`

 The instance of the task: where the two matrices and the answer stand. 

### `pre_apsp`

 The input of the end statement meets the precondition of the task. 

### `post_apsp`

 What the task leaves in the output cells is a right answer of the end statement's APSP. 

### `wrapApsp`

 What connects APSP in the layout of the end statement with the task.  The program always
accepts: the answer is in the output cells. 

### `realized_apsp`

 **APSP**: if the task is solved in time T, then APSP is solved on the word RAM within a constant
times T. 

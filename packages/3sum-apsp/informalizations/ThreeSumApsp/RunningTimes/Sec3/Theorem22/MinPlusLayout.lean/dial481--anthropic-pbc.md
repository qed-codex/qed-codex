---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Theorem22/MinPlusLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22/MinPlusLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22/MinPlusLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The (min,+)-product: from a solver of the task to a program for the layout of the end statement

The (min,+)-product (Theorem 22).  `realized_minPlusProduct`: if the task `mpTask` is
solved in time T, then `EndStatement.MinPlusProduct` is solved on the word RAM within a constant
times T.

The input is n in cell 0, the first matrix from cell 1 and the second from cell 1 + n².  The product
goes to the n² cells from 1 + 2n², and the free pointer is 1 + 3n² (`minPlusInst`).  The input meets
the task's precondition (`pre_minPlusProduct`).  A solver leaves the list `minPlusList` in the
output cells, and each of its entries is a minimum as `EndStatement.MinPlusProduct` asks for: it is
attained, and it is a lower bound (`post_minPlusProduct`).


### `input_minPlusProduct`

 The input: the size and the two matrices, row by row. 

### `length_input_minPlusProduct`

 The input takes 1 + 2n² cells. 

### `abs_le_of_mem_minPlusProduct`

 The entries of the two matrices are within the bound. 

### `minPlusInst`

 The instance of the task: where the two matrices and the product stand. 

### `pre_minPlusProduct`

 The input of the end statement meets the precondition of the task. 

### `post_minPlusProduct`

 What the task leaves in the output cells is the (min,+)-product as the end statement asks for
it. 

### `wrapMinPlus`

 What connects the (min,+)-product in the layout of the end statement with the task.  The program
always accepts: the answer is in the output cells. 

### `realized_minPlusProduct`

 **The (min,+)-product**: if the task is solved in time T, then the product is computed on the
word RAM within a constant times T. 

---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Corollary15_16/Layout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Corollary15_16/Layout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Corollary15_16/Layout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The thin matrix product and the lopsided triangle problems in the layout of the word RAM

A solver of the thin matrix product, of #Lop-AE-SparseTri or of Lop-AE-SparseTri gets its sizes, the
bound on the entries and its addresses as arguments.  The three problems on the word RAM have one
layout: the cells 0, 1, 2 hold N, D and the number w of wanted positions, then come X, Y, the rows
and the columns of the wanted positions, then the output.

One more procedure, `thinTop`, is appended to the program of the solver: it reads N, D, w, forms the
bound N^e by e multiplications (the instances have the bound U = N^κ on their entries, for a fixed
exponent κ; e = κ for the matrix product, e = 0 for matrices of zeros and ones), computes the
addresses, calls the solver, and returns 1.

* `pre_toThinU`: the input is an instance of the task;
* `thinTop_ends`: the run of the outermost call;
* `small_limN`, `input_le_limN`: the limits are polynomial in N and D, and the input fits;
* `realizedN`: from a solver to the word RAM; `realized_thinProduct` and `realized_lop` (with
  `realized_lopCount` and `realized_lopDetect`) are its uses.


 ## The outermost procedure 

### `thinTop`

 The outermost procedure.  Local 1 is N, 2 is the bound N^e, 3 is D, 4 is w; 5 to 9 are the
addresses of Y, of the rows, of the columns, of the output, and the free pointer. 

### `thinProb`

 A problem in the layout of the thin matrix product. 

### `thinTaskOf`

 A task with the calling convention of the thin matrix product. 

### `toThinU`

 The instance of the task, with the bound U that is handed to the solver. 

### `outputEnd`

 The free pointer: the first cell after the output. 

### `length_input`

 The input: three numbers, the two matrices, and the rows and the columns of the wanted
positions. 

### `seg_memOf_of_eq`

 A part of a list lies in the memory that holds the list. 

### `seg_input_X`

 The matrix X in the input. 

### `seg_input_Y`

 The matrix Y in the input. 

### `seg_input_rows`

 The rows of the wanted positions in the input. 

### `seg_input_cols`

 The columns of the wanted positions in the input. 

### `pre_toThinU`

 The instance lies in the memory that holds the input. 

### `thinEntry_eq`

 The entries that the task asks for are the entries of the product. 

### `runLimits`

 The limits of the run on an instance, if the solver needs nd. 

### `memOf_input_N`

 The first three cells of the input hold N, D and the number of wanted positions. 

### `pow_frame`

 The bound N^e is formed in local 2. 

### `thinTop_ends`

 The run of the outermost call. 

 ## The limits are polynomial in N and D 

### `length_W_le`

 There are at most N² wanted positions. 

### `polyBound_four`

 A bound in N, D, the number of wanted positions and N^e is a bound in N and D. 

### `polyBound_three`

 The same without the bound on the entries. 

### `small_limN`

 The limits are polynomial in N and D. 

### `input_le_limN`

 Every number of the input fits in a word. 

 ## From a solver to the word RAM 

### `realizedN`

 **If a task with the calling convention of the thin matrix product is solved, the problem is
solved on the word RAM** within a constant times the time of the solver.  The bound that is handed
to the solver is N^(e κ). 

 ## The three problems 

### `out_eq`

 The answers that the tasks ask for are the wanted entries of the product. 

### `realized_thinProduct`

 **The thin matrix product**: if the task is solved in time T, the wanted entries are computed on
the word RAM within a constant times T. 

### `zeroOne_le`

 The entries of matrices of zeros and ones are at most 1 = N^0. 

### `pre_lop`

 The instance of the two lopsided triangle tasks lies in the memory that holds the input. 

### `realized_lop`

 **The two lopsided triangle problems**: what differs between them is how the answers are read
off the memory (hpost). 

### `realized_lopCount`

 **#Lop-AE-SparseTri**: if the task is solved in time T, the problem is solved on the word RAM
within a constant times T. 

### `realized_lopDetect`

 **Lop-AE-SparseTri**: if the task is solved in time T, the problem is solved on the word RAM
within a constant times T. 

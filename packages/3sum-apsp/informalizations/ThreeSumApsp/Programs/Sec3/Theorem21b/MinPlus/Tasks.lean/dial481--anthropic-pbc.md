---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/Tasks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/Tasks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/Tasks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The two tasks between Negative Triangle and the (min,+)-product

[VW18, Theorem 4.2], one of the reductions behind Theorem 21(b), goes from
deciding Negative Triangle to the (min,+)-product in three steps: finding a negative triangle
([VW18, Lemma 4.1]), finding for all pairs `(i, j)` at once whether some `k` has `X[i,k] + Y[k,j] <
V[i,j]`, and a search for all entries of the product at once.  Each step is a host over an arbitrary
solver of the task below it (isHost_find, isHost_pairs, isHost_mp).  This file fixes the two tasks
in the middle, findTask and pairsTask.


### `FindInst`

 Three matrices of weights, and the place for the three vertices of a triangle. 

### `FindInst.Pre`

 The place for the answer lies below the free pointer and does not meet the three matrices. 

### `findPre_of_arrays`

 Three matrices one after the other, with a place for an answer below them and the free pointer
behind them, are an instance. 

### `findTask`

 **Finding a negative triangle**: find(n, U, ab, bc, ac, res, fr) returns 1 if there is a
negative triangle, and then the cells res, res + 1, res + 2 hold the vertices `a`, `b`, `c` of one;
it returns 0 if there is none. 

### `PairsInst`

 Three `n × n` matrices, and the place for `n²` flags. 

### `PairsInst.Pre`

 The three matrices and the place for the flags lie below the free pointer; the place for the
flags does not meet the matrices. 

### `PairsInst.Pre.keep`

 An instance stays where it is if no cell below the free pointer changes, except the flags. 

### `pairFlags`

 The flags: cell `i n + j` holds 1 if `X[i,k] + Y[k,j] < V[i,j]` for some `k < n`, and 0 if
not. 

### `pairsTask`

 **All pairs**: allPairs(n, U, x, y, v, out, fr) writes the `n²` flags to out. 

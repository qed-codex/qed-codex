---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/BruteForce.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/BruteForce.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/BruteForce.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The wanted entries of a thin matrix product, as inner products

X is an N × D matrix at the address x and Y a D × N matrix at y, both row by row, with entries of
absolute value at most U; the cells from wi and from wj on hold the rows and the columns of w wanted
positions.  thinBrute(N, D, w, U, x, y, wi, wj, out, fr) computes every wanted entry (XY)[I, J] as
the inner product of row I of X and column J of Y, and writes it to the cells from out on.  It is
right on every instance for which D U² fits in a word, so that no partial sum overflows; it is what
the solver of Theorem 5 falls back to outside the regime of the theorem.  At most
40 (w + 1) (D + 1) steps.

bruteInner_spec treats the inner product: after t rounds the sum holds the first t terms
(brutePartial), which stay within a word (abs_brutePartial_le).  bruteRound_spec treats one wanted
position, and thinBrute_spec the loop over the positions.


### `Pos`

 Local 10 of thinBrute: the number of the position. 

### `Idx`

 Local 11 of thinBrute: the index t of the inner product. 

### `CellX`

 Local 12 of thinBrute: the address of X[I, t]. 

### `CellY`

 Local 13 of thinBrute: the address of Y[t, J]. 

### `Sum`

 Local 14 of thinBrute: the sum. 

### `bruteInner`

 The inner product. 

### `bruteRound`

 One wanted position: the inner product, the store, and the step to the next position. 

### `thinBruteBody`

 thinBrute(N, D, w, U, x, y, wi, wj, out, fr). 

### `bruteLocs`

 The locals of thinBrute: the arguments, the number i of the position, the index t, the two
addresses px and py, and the sum s.  In the place of U stands whatever number u has been passed: the
program never reads it. 

 ## The partial sums 

### `brutePartial`

 The first n terms of the inner product. 

### `brutePartial_succ`

 One more term. 

### `abs_bruteTerm_le`

 A term of the inner product is at most U². 

### `abs_brutePartial_le`

 The first n terms add up to at most n U². 

 ## The program 

### `bruteInner_spec`

 **The inner product** of row I of X and column J of Y. 

### `BruteInv`

 Before position i: the locals are as in bruteLocs, with anything in the scratch locals, the
entries of the positions before i are in the output, and nothing else has changed. 

### `bruteRound_spec`

 **One wanted position.** 

### `thinBrute_spec`

 **The brute force is right on every instance** for which D U² fits in a word.  It needs N + 1
cells above the free pointer only as room for addresses that are formed and never used. 

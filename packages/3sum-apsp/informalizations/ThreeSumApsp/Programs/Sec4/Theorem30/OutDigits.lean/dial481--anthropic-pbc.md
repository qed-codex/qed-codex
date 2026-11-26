---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/OutDigits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/OutDigits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/OutDigits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The digits of the output string of a position

Proof of Theorem 30, "Query": "Given (I, J), we find its tile from the bands of row I and column J,
the subset Q of its block product, and its output string w (whose variables at the levels outside Q
we read off the row and column of (I, J) within the block product), all in O(L) operations". The
routine walks the mask of the subset: it writes the digit 9 at a level of the subset (levelInner),
and otherwise 3 x + y for the next base-3 digits x and y of the offsets of I and J (levelOuter). The
invariant OutDigits.Inv says what has been written before level l; each of the two branches takes it
from l to l + 1 (OutDigits.inner, OutDigits.outer).


 ## The program 

### `BlockI`

 The local variables of outDigits: the arguments gI, gJ, dI, dJ, aMASK, K0, L, wd, then the
address of the mask of the subset, the level, and the number of levels outside the subset so far. 

### `levelInner`

 A level of the subset: wd[level] := 9; level := level + 1. 

### `levelOuter`

 A level outside the subset: wd[level] := 3 dI[outer] + dJ[outer]; outer := outer + 1;
level := level + 1. 

### `outDigitsWalk`

 The walk along the mask: while level < L, treat the level according to mask[level]. 

### `outDigitsBody`

 outDigits(gI, gJ, dI, dJ, aMASK, K0, L, wd) writes the L digits of the output string at wd. 

 ## The pure side: the digit at one level 

### `length_mask`

 The mask has one entry for each level. 

### `length_digits`

 The output string has one digit for each level. 

### `getD_digits_inner`

 The digit at a level of the subset. 

### `getD_digits_outer`

 The digit at a level outside the subset, and the room behind the pointer. 

### `base_add_le`

 The mask of the subset lies inside the table of the K0² masks. 

 ## The invariant and the two branches 

### `Inv`

 The state before level l: the first l digits have been written, and no cell outside wd has
changed. 

### `read_mask`

 The cell of the mask that the test of level l reads. 

### `inner`

 wd[level] := 9; level := level + 1. 

### `outer`

 wd[level] := 3 dI[outer] + dJ[outer]; outer := outer + 1; level := level + 1. 

### `walk`

 The walk along the mask writes the digits of the output string. 

### `index_le`

 The numbers on the way to the address of the mask fit in a word. 

### `outDigits_spec`

 **outDigits** meets its specification. 

---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/CopyBlock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/CopyBlock.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/CopyBlock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Copying a block of a matrix

A routine for the hosts of [VW18, Theorem 4.2], one of the reductions behind Theorem 21(b).
subCopy(s, h, src, r0, c0, dst) copies the h × h block with upper left corner (r0,
c0) of the s × s matrix at src (row major) to dst (row major), one row at a time, with the routine
copy.  The destination lies behind the matrix.

The specification is subCopy_meets: afterwards the list subMat s h r0 c0 L stands at dst, and no
other cell has changed.  The proof is a loop over the rows with the invariant SubCopy.Inv; that
row i of the block is a piece of row r0 + i of the matrix is SubCopy.row_eq.


 ## The program 

### `Side`

 The local variables of subCopy: the arguments s (Side), h (Block), src, r0, c0, dst; the row i;
and the result of copy, which is not used. 

### `subCopyBody`

 subCopy(s, h, src, r0, c0, dst): for i < h, copy the h cells from src + (r0 + i) s + c0 to
dst + i h.  pCopy is the number of the procedure copy. 

### `subCopyTime`

 The number of steps of subCopy. 

 ## The specification 

### `row_eq`

 Row i of the block is a piece of row r0 + i of the matrix. 

### `Inv`

 The state before row i is copied: the first i rows of the block B stand at dst, and no cell
outside the h² cells from dst has changed. 

### `subCopy_meets`

 **subCopy** writes the block of the matrix L at src to dst and changes nothing else.  The block
lies within the matrix and the destination behind it (hplace); the destination lies within the
memory, and one more level of calls is allowed (hlim). 

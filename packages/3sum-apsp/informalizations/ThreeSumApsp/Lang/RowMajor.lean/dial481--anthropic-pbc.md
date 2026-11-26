---
{
  "module": "ThreeSumApsp/Lang/RowMajor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/RowMajor.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/RowMajor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Reading the trusted layout

Matrices are written row by row (`rowMajor`), and an input is a concatenation of lists.  This file
says which number is in which cell (`getD_rowMajor`, `seg_memOf`, `matAt_of_seg`).


### `getD_rowMajor`

 The entry `(i, j)` of an `n × m` matrix is at place `i m + j`. 

### `mem_rowMajor_self`

 Every entry of a matrix stands in the list of its rows. 

### `memOf_append_left`

 A cell in the first part of a concatenation. 

### `memOf_append_right`

 A cell after the first part of a concatenation. 

### `seg_memOf`

 A part of a concatenation is a segment of the memory. 

### `seg_first`

 The first of two lists after the size. 

### `seg_second`

 The second of two lists after the size. 

### `matAt_of_seg`

 A matrix written row by row. 

### `rowByRow_eq`

 A square matrix written row by row: the two definitions agree. 

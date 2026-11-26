---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/CellDependencies.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/CellDependencies.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/CellDependencies.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The memory map of Theorem 5: what depends on which cells

SharedReady.dirs lists the cells of the directory that the solver reads. SharedTables are the tables
of the shared block without the directory and the encodings; they depend only on the cells between
these two (SharedTables.congr), and all that the shared stage leaves behind depends only on the
cells of the shared block, without the last of the 32 cells of the directory, which the shared stage
does not use (SharedReady.congr, SharedReady.of_agree).


 ## The directory 

### `SharedReady.dir_read`

 Cell j of the directory, with the address in the form in which the evaluation of mem[b0 + j]
meets it. 

### `SharedReady.dirs`

 The cells of the directory that the solver reads, one equation for each. 

 ## Only the shared block matters 

### `SharedTables.congr`

 The tables lie between the directory and the encodings: they are still there in a memory that
agrees on these cells. 

### `SharedReady.congr`

 What the shared stage leaves behind is kept by a memory that agrees on the cells of the shared
block, but for cell 31 of the directory, which the shared stage does not use. 

### `SharedReady.of_agree`

 What the shared stage leaves behind is kept by a memory that agrees on all cells below the end
of the shared block, but for cell 31 of the directory. 

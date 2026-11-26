---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Directory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Directory.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Directory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The cells of the directory, by name

The routines of Section 4 find the sizes and the addresses of the tables in the directory, the
first cells of the block.  `DirCells p b0 μ` says what the cells that they read hold, one equation
for each cell, under the name that the cell has in the program texts (`Dir.bands`, `Dir.encA`, …).
A proof that treats `x := mem[b0 + Dir.bands]` names the equation `bands`.  The shared stage
establishes all of them (`SharedReady.dirCells`).


### `DirCells`

 What the cells of the directory that the routines of Section 4 read hold. 

### `_root_.Light.Sec2.SharedReady.dirCells`

 After the shared stage the directory holds what `DirCells` says. 

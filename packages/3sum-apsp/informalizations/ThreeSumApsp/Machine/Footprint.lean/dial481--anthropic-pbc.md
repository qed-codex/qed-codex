---
{
  "module": "ThreeSumApsp/Machine/Footprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/Footprint.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/Footprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# What a run of the word RAM reads and writes

* One step writes at most one cell (`step_mem`) and reads at most two (`reads`, `card_reads_le`,
  `step_congr`).
* A run that ends within `t` steps changes at most `t` cells (`changed_cells`) and depends on at
  most `2t` cells (`exec_congr`); two runs from one configuration have the same result
  (`exec_unique`).


 ## One step 

### `step_mem`

 One step changes at most one cell. 

### `reads`

 The cells that an instruction reads. 

### `card_reads_le`

 An instruction reads at most two cells. 

### `step_congr`

 A step from a second configuration at the same position whose memory agrees on the cells that
are read: the same verdict, or the same next position, and every cell on which the memories agreed
is a cell on which they agree afterwards. 

 ## Runs 

### `changed_cells`

 A run of `t` steps changes at most `t` cells. 

### `exec_congr`

 A run of `t` steps reads at most `2t` cells: a run from the same position on a memory that
agrees on these cells gives the same verdict after the same number of steps. 

### `exec_unique`

 Two runs of a program from the same configuration have the same result. 

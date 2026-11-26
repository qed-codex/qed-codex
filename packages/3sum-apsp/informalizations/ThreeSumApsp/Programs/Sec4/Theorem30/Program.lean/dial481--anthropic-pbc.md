---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Program.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Program.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Program.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30 on the word RAM: the program

`program30` is the list of procedures: those of Section 2 (numbers 0 to 28, of which the
preprocessing uses the shared stage), the routines of Section 4 (40 to 53), preCore, queryAt and the
two procedures of the offline form (54 to 57), and the two main procedures of Theorem 30 (80 and
81); the unused numbers hold the empty statement.

The first 58 procedures (`base58`) are also the beginning of the programs for Corollaries 26, 31
and 32.  So the assumptions of the earlier files are discharged for every program `base58 ++ R` that
begins with them: it meets the specifications of the preprocessing and of a query at a given place
of the memory (`preCore_base58`, `queryAt_base58`).  With `theorem_30_of` and `theorem_30_wanted_of`
this gives Theorem 30 and its offline form without hypotheses (`wordRam_theorem_30`,
`wordRam_theorem_30_wanted`).


### `base58`

 The procedures number 0 to 57: Section 2's program for the thin matrix product (0 to 28), eleven
unused numbers, the routines of Section 4, the two routines that know the memory map, and the two
routines of the offline form. 

### `at_base58`

 A procedure of base58 is a procedure, with the same number, of every program that begins with
base58. 

### `cShared30`

 The constant of the shared stage. 

### `shared_base58`

 The shared stage, in every program that begins with base58. 

### `preCore_base58`

 **The preprocessing at a given place of the memory**, in every program that begins with base58.


### `queryAt_base58`

 **A query at a given place of the memory**, in every program that begins with base58. 

### `program30`

 The program of Theorem 30. 

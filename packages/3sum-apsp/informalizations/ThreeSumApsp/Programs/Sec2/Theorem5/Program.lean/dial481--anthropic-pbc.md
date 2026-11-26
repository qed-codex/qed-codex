---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Program.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Program.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Program.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5: the program

The list of the procedures of Theorem 5's program, in the order of their numbers.  An entry is the
specification of a procedure together with a bound on its time, a constant times a shape.  In every
program that begins with this list, the procedures that the shared stage calls meet their entries
with the constant cShared5 (sharedCallees_of_prefix), and those that the solver calls with the
constant cMain5 (mainCallees_of_prefix).


### `program5`

 The program of Theorem 5.  The numbers of the procedures begin with 1; number 0 is empty. 

### `length_program5`

 The program has 26 procedures. 

### `at_prefix`

 A procedure of program5 is a procedure, with the same number, of every program that begins with
program5. 

 ## All entries 

### `cShared5`

 The constant of the procedures that the shared stage calls. 

### `cMain5`

 The constant of the procedures that the solver calls. 

### `sharedCallees_of_prefix`

 The procedures that the shared stage calls meet their entries. 

### `mainCallees_of_prefix`

 **The procedures that the solver calls meet their entries**, in every program that begins with
program5. 

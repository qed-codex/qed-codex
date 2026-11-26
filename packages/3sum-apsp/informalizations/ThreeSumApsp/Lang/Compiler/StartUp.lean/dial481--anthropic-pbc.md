---
{
  "module": "ThreeSumApsp/Lang/Compiler/StartUp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/StartUp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/StartUp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The start-up code

A compiled program may start on any memory: nothing is assumed about the cells below -2.  Its first
three instructions and its start-up code write everything that the compiled statements rely on.
`startMem F N m` is the memory in which the outermost statement starts, if the run starts in m.

* `rel_startMem`: it represents the state in which the local variables 1 and 2 hold the two
  arguments (the contents of the cells -1 and -2) and all other local variables hold 0.
* `agreeOutside_startMem`: it differs from m only in the registers for 1, 0, -1, in the pool, in FP
  and in the outermost frame.
* `steps_start`: the machine gets from position 0 to the outermost statement in N + F + 9 steps.

The code has three pieces: the numbers 1, 0, -1 (`headStraight`), the pool (`poolCode`), the
outermost frame (`frameCode`).  There is no store among them, so the cells that a piece may change
are read off its text (`agreeOutside_effects`).  What a piece writes is found by running it: the two
loops unrolled in the code are inductions (`effects_poolCode`, `effects_zeroCode`).


 ## The numbers 1, 0, -1 

### `effects_headStraight_consts`

 The three registers after the first three instructions. 

 ## The pool 

### `effects_poolCode`

 After `poolCode N` the pool holds the numbers 0, …, N. 

### `poolMem`

 The memory after the first three instructions and the code for the pool. 

### `poolMem_consts`

 The code for the pool leaves the numbers 1, 0, -1 in their registers. 

 ## The outermost frame 

### `writesIn_zeroCode`

 The instructions of `zeroCode` write into the outermost frame. 

### `effects_zeroCode`

 The local variables of the outermost frame hold zeros. 

### `effects_frameCode`

 The code for the outermost frame: FP, then zeros, then the two arguments. 

 ## The memory in which the outermost statement starts 

### `startMem`

 The memory after the first three instructions and the start-up code. 

### `agreeOutside_startMem`

 The start-up code changes only the registers for 1, 0, -1, the pool, FP and the outermost
frame. 

### `rel_startMem`

 After the start-up code the memory represents the state in which the outermost statement
starts: the local variables 1 and 2 hold the two arguments, all others 0.  Nothing is assumed about
the cells below -2 of the initial memory. 

 ## The run from the first instruction to the outermost statement 

### `steps_start`

 From the first instruction to the outermost statement. 

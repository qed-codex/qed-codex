---
{
  "module": "Nc/Uni/Prog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Uni/Prog.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Uni/Prog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A tape program that simulates a pointer machine


### `bw`

 A word of bits, ended. 

### `cont`

 The content of a record: kind and columns. 

### `rec'`

 A record, as it is written. 

### `tp`

 A side of a tape. 

### `rgs`

 The sides of all register tapes. 

### `runs_rep`

 Loops with a fixed body. 

### `cn`

 The three words of a round of the counter. 

### `cn1`

 The next number. 

### `emCt`

 Emissions of a round of the counter. 

### `i0`

 The first words: registers 0, counter 1. 

### `i1`

 The first address. 

### `emIn`

 Emissions at the start. 

### `cw`

 A column of the variables of all bits. 

### `ldc`

 The columns of the record that is loaded. 

### `alc`

 The columns of the record that is allocated. 

### `rgw`

 What a step writes on a register tape. 

### `emSt`

 Emissions of a step. 

### `st0`

 Before the columns. 

### `st1`

 A column. 

### `st2`

 After the columns. 

### `dimSt`

 Dimension of a step. 

### `emEd`

 Emissions at the end. 

### `ed1`

 Emissions at the end, the registers. 

### `emAp`

 Emissions of the phase that appends the lookups to the list. 

### `XP`

 Runs of the program. 

### `emX`

 Emissions of the program. 

### `dimX`

 Dimension of the program. 

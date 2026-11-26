---
{
  "module": "Nc/Uni/PM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Uni/PM.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Uni/PM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Pointer machines

Every step loads one record and allocates one record, at the next address.


### `Mach`

 A pointer machine with modes M, kinds of records K, weights in A. The variables of a step are: the 5 registers,
the 3 fields of the record that is loaded, the new address. 

### `Mach.Rl`

 rules 

### `Mach.src`

 mode before 

### `Mach.dst`

 mode after 

### `Mach.rd`

 the bit that is read from the input 

### `Mach.lk`

 kind of the record that is loaded 

### `Mach.la`

 the register with its address 

### `Mach.ak`

 kind of the record that is allocated 

### `Mach.af`

 its fields 

### `Mach.dr`

 the registers after the step 

### `Mach.wt`

 weight 

### `Mach.m0`

 first mode 

### `Mach.mh`

 last mode 

### `Mach.kN`

 kind of the record with address 0 

### `rv`

 A register as a variable. 

### `Rec`

 Records: kind, address, fields. 

### `Step`

 A step: a rule and the values of the variables. 

### `ld`

 The record that is loaded. 

### `al`

 The record that is allocated. 

### `wts`

 The weight of a list of steps. 

### `State`

 States. 

### `State.mode`

 mode 

### `State.regs`

 registers 

### `State.heap`

 records 

### `State.n`

 last address 

### `State.inp`

 the rest of the input 

### `Fire`

 A step is possible. 

### `nxt`

 The state after a step. 

### `Seq`

 Accepting runs. 

### `GV`

 Runs that are checked globally: loads may refer to any record. 

### `Closed`

 The heap is closed. 

### `gv_iff`

 The global check is the same as the check step by step, if the heap is closed. 

### `Seq.le`

 All values of the variables are at most the number of steps. 

### `SumTo`

 The accepting runs from a state are finitely many; their weights have the sum S, their lengths are at most B. 

### `SumTo.halt`

 The end. 

### `SumTo.fin`

 One step: finitely many possibilities. 

### `SumTo.none`

 No step. 

### `SumTo.one`

 Exactly one step. 

### `SumTo.two`

 Exactly two steps. 

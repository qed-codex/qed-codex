---
{
  "module": "proof/rates/PaddedDescent/F/Data.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Data.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Data.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Tables, instances and networks as data

Explicit tables, instances as data, networks given by plain functions. 

### `Tab`

 The tables of an instance on K nodes with ℓ-bit labels: K rows; row v has 2^((K−1)ℓ) entries. 

### `PInst`

 An instance as data: (ℓ in unary, tables). The number K of nodes is not stored; it is known from
the level. 

### `Lvl`

 One step of the schedule, «g·g nodes → K nodes»: (K, g), both in unary. 

### `look`

 The entry at the query q = (v, labels): the labels (the empty word at v itself) are written one
after the other and read as a number. 

### `instOf`

 The instance that a table stands for. 

### `zval`

 The sum Z of an instance given as data, on K nodes. 

### `unflat`

 The labels at v written by the word w of (K−1)·ℓ bits. 

### `tabulate`

 The table of the function F of queries. 

### `WF`

 I is an instance on K nodes with label length between 1 and Λ and entries of absolute value at
most 2^B. 

### `freeM`

 A machine that has its answer at once and calls all its states small. Only used to quote the
value theorems of
StepMachines/Prog/NetVal.lean, which take a `PNet`. 

### `FNet`

 A network given by plain functions. 

---
{
  "module": "Nc/Dl/Tab.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Dl/Tab.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Dl/Tab.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Tables of the dealing program

Names of the values that the dealing program computes, and the steps that compute them.


### `Nm`

 Names of values. 

### `Nm.zero`

 empty 

### `Nm.part`

 part of the input 

### `Nm.q`

 state 

### `Nm.flag`

 flags of a row 

### `Nm.rd`

 row data 

### `Nm.row`

 is the row valid? 

### `Nm.kR`

 keys of units written 

### `Nm.kC`

 keys of units read 

### `Nm.dg`

 instructions for diagonal units 

### `Nm.dn`

 number of units as a digit 

### `Nm.dO`

 outcome as a digit 

### `Nm.ch`

 keys of new units 

### `Nm.slp`

 value of a step of the straight-line program 

### `Nm.num`

 number of units of a move 

### `Nm.cond`

 conditions 

### `Nm.cut`

 is the unit cut? 

### `Nm.cont`

 content of a cut unit 

### `NN`

 Numbers of units at the beginning. 

### `SlpTab`

 The straight-line program of a plan: digits `Fin D`; the numbers of units and the outcomes are inputs. 

### `SlpTab.fn`

 the functions 

### `SlpTab.inp`

 inputs 

### `SlpTab.kcur`

 is a unit current in the end? 

### `SlpTab.kcut`

 is a unit cut? 

### `SlpTab.kcons`

 is a unit given in a slot? 

### `SlpTab.knum`

 number of units of a move 

### `SlpTab.kcond`

 conditions: the outcome of a move is good; the numbers of units are valid 

### `SlpTab.valid`

 validity 

### `SlpTab.kgrp`

 groups 

### `Codes`

 Codes of names, digits and row data, keys of units. 

### `Codes.nm`

 names 

### `Codes.dc`

 digits 

### `Codes.rc`

 row data 

### `Codes.key`

 keys of copies of units 

### `Codes.dkey`

 keys of second copies 

### `NmT`

 Abbreviation. 

### `dt`

 A digit as a tree. 

### `un`

 Unary operation on digits: `dst := f (value of x)`. 

### `bin`

 Binary operation on digits. 

### `con`

 Constant. 

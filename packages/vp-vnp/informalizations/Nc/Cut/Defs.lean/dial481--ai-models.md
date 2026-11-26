---
{
  "module": "Nc/Cut/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The cut: definitions

An automaton (`mu`, `i`, `e`) with tapes `S` and one input, `K` blocks of `T` steps. Parties: the blocks
(`Fin.castAdd K κ`) and `K` input parties (`Fin.natAdd K κ`), which hold the parts of the input, `ℓ` letters each.
The input is treated as one more tape (`none`), written by the input parties and read by the blocks.
All segments written by party `a` and read by party `b` are put into one string, which is cut into units.


### `joinSeg`

 The segments on all tapes (the tape `none` is the input) as one word with separators. 

### `strOf`

 The string from one party to another. 

### `vec`

 What a block emits, if `R s b` is what it writes for party `b` on tape `s` and `C s b` what it reads from
party `b` on tape `s`. 

### `partyW`

 The weight of what party `p` writes and reads: a block from state `q κ` to `q (κ + 1)`, or an input party with
its part of the input. 

### `RowData`

 The row data of a party on a tape: whether it writes nothing on the tape, the first and the last party that
reads what it writes (if it writes nothing: twice the last party of the rows before). 

### `RowOk`

 The segments written by a party on a tape are as the row data say. 

### `prevHi`

 The last party of the row before (0 for the first row). 

### `ValidRows`

 The row data on all tapes are those of a staircase. 

### `parts`

 The parts of a word: `ℓ` letters each. 

### `sideString`

 The string on a side: for every block the label and the string of the law. 

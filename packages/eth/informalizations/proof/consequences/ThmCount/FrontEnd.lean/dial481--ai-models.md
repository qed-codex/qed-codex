---
{
  "module": "proof/consequences/ThmCount/FrontEnd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/FrontEnd.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/FrontEnd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem C from Theorem D(b): the front end and the last step

No sentence of the paper stands behind this file: the paper derives Theorem C otherwise (see the
head of proof/consequences/ThmCount/Defs.lean).
* `stFrontEnd`: the function `frontEnd` is polynomial time and maps the plain code of a 3-CNF φ to
  1³0 followed by the plain code of `Wrap.pad4 φ`. It is built like `Wrap.frontEnd`
  (proof/machines/Wrap/FrontEnd.lean), which writes the compact code, and uses its pieces
  `Wrap.addFour`, `Wrap.slotNat`, `Wrap.slotBits` with their certificates.
* `stPadKeepsCount`: the four forced variables keep the number of satisfying assignments: a
  satisfying assignment of `pad4 φ` is a satisfying assignment of φ with the value 1 on the four new
  variables.
* `stInputLength`, `stLastStep`. 

### `encPlain`

 1³0, then the plain code at width 3, from the number of variables in unary, the number w of bits
of a slot in unary, and the clauses with numbers as variables. 

### `frontEnd`

 The front end: read the plain code as n and the clauses, add the four clauses of one literal,
write 1³0 and the plain code for n + 4 variables. 

### `encPlain_toN`

 On N in unary, w = ⌊log₂(2N)⌋ + 1 in unary and a formula on N variables with numbers as
variables, `encPlain` is the code of (3, formula). 

### `frontEnd_enc`

 The front end maps the plain code of φ to the code of (3, `pad4 φ`), if every clause of φ has at
most 3 literals. 

### `encPlain_polyT`

 Writing the code is polynomial time, with the number of variables and the number of bits of a
slot in unary. 

### `frontEnd_polyT`

 The front end is polynomial time. 

### `stFrontEnd`

 There is a polynomial-time front end: the statement `ThmCount.StFrontEnd`. The front end is
`frontEnd`. 

### `holds_pad4`

 An assignment satisfies `pad4 φ` exactly if, read on the old variables, it satisfies φ, and it
gives the four new variables the value 1. 

### `numSat_pad4`

 The four forced variables keep the number of satisfying assignments. 

### `dropFour_binary`

 A number in n + 5 bits without its four highest bits is the number in n + 1 bits. 

### `stPadKeepsCount`

 The four forced variables keep the number of satisfying assignments, and the number in n + 5
bits without its four highest bits is the number in n + 1 bits: the statement
`ThmCount.StPadKeepsCount`. 

### `stInputLength`

 The plain code of a 3-CNF on n variables has length at most 25·(n+2)^4: the statement
`ThmCount.StInputLength`. 

### `stLastStep`

 The last step is polynomial time: the statement `ThmCount.StLastStep`. 

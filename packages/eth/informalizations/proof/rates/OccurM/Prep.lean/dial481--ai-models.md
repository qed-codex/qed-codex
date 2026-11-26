---
{
  "module": "proof/rates/OccurM/Prep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Prep.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Prep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The preparation

Before the network of a formula is built, the variables that occur are numbered; in the proof of
Theorem A (d) they are renamed as in Section 2, in time polynomial in m log n. This development has
two programs for it, `VariableBound.Rename.rencC` for the compact code and
`VariableBound.Rename.renc` for the code with N in unary, and the formula
`VariableBound.Rename.ren φ`, whose code both return. Here their properties are collected in the
form of `OccurM.Prepares`.

* `prepares_rencC`, `prepares_renc`: the renamed formula that `Prepares` and `PreparesUnary` ask for
  is `ren φ`. `preparation`: the two, and that both programs are polynomial-time.
* `ClausesOccur.someVariableOccurs`: a formula with at least two clauses, none written twice,
  contains a variable. 

### `prepares_rencC`

 The program for the compact code numbers the variables that occur; it returns the code of
`ren φ`. 

### `prepares_renc`

 The program for the code with N in unary numbers the variables that occur; it returns the code
of `ren φ`. 

### `preparation`

 The two named preparations number the variables that occur, and they are polynomial-time. 

### `someVariableOccurs`

 A formula with at least two clauses, none written twice, contains a variable: its first two
clauses differ, so one of them is not empty. 

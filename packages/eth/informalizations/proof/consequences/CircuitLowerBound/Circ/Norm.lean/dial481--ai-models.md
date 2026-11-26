---
{
  "module": "proof/consequences/CircuitLowerBound/Circ/Norm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Circ/Norm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Circ/Norm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Every circuit can be written as data in which a gate reads inputs and earlier gates only

A gate that names a wire that does not exist yet reads 0 there. Such a gate is replaced by a gate
that reads the wire 0 and ignores it: the function of the gate gets the value 0 built in. All wires
keep their values (`Norm.wires_norm`), so the circuit computes the same function with the same
number of gates (`stNorm`). The auxiliary statements are in the namespace `CircuitLowerBound.Norm`. 

### `op'`

 The function of the gate G when there are n wires: an input that names a wire that does not
exist is read as 0. 

### `ng`

 The gate G as data, when there are n wires. 

### `norm`

 The circuit as data, when there are n wires before its first gate. 

### `value_ng`

 The gate `ng w.length G` has the value of G. 

### `wires_norm`

 All wires keep their values. 

### `wf_norm`

 Every gate reads earlier wires only. 

### `stNorm`

 Every circuit on m ≥ 1 input bits can be written as data in which every gate reads inputs and
earlier gates only, with the same number of gates. 

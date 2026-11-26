---
{
  "module": "proof/consequences/SizeCircuit/Compare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Compare.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Compare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: the circuit compares the number of ones with s

Facts on `compareGates` of proof/consequences/SizeCircuit/CircuitDefs.lean, for «a circuit with O(n)
gates of two inputs tests whether |S| = s»: under all values of the wires that obey its gates, its
last wire is 1 exactly if the digit wires write the number s (`compareGates_spec`); its gates read
earlier wires only (`wfa_compareGates`). 

 ### Numbers and their digits 

### `testBit_num`

 Digit i of the number with the digits b 0, …, b (L − 1) is b i. 

### `num_eq_iff`

 The digits b 0, …, b (L − 1) write s exactly if s has at most L digits and these are its digits. 

 ### The gates 

### `gval_const`

 The gate with a constant value. 

### `gval_digit`

 The gate "the wire i, and the wire j has the value t". 

### `length_compareGates`

 The comparison has one gate for each digit and one more. 

### `prevW_eq`

 In the chain that begins at the wire N + 1 and starts from the wire N, the wire before place i
is N + i. 

### `compareGates_spec`

 **The comparison.** Under values v of the wires that obey the gates of the comparison, its last
wire is 1 exactly if the digit wires write the number s. 

### `wfa_compareGates`

 The gates of the comparison read earlier wires only, if there is a wire 0 and the digit wires
exist. 

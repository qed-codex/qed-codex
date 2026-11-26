---
{
  "module": "proof/consequences/CircuitLowerBound/Circ/Blocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Circ/Blocks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Circ/Blocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Circuits as lists of gates: wires, blocks, chains, numbers in binary

General facts for circuits that are written block by block, with the numbers of the wires in closed
form; they serve the circuit lower bound for E^NP (Section 7 of the paper: E^NP does not have
circuits of linear size).

* `Obeys v n C`: in the values v of the wires, the gates of the list C, whose wires are n, n + 1, …,
  have their values. `WFa n C`: these gates read wires before their own. Both split along `++` and
  along
  `(List.range w).flatMap f` with pieces of equal length. The values of the wires of a circuit on an
  input obey the circuit (`obeys_wires`).
* Chains of gates that compute the AND or the OR of many wires (`chain_all`, `chain_any`).
* `num b w`: the number with the binary digits b 0, …, b (w − 1), lowest first; the chains of half
  adders and of full adders (`half_adder`, `full_adder`). 

 ### Gates 

### `B4`

 The values of a function of two bits at 00, 01, 10, 11. 

### `opFst`

 The first input. 

### `opAndN`

 The first input and not the second. 

### `gval`

 The value of a gate in the values v of the wires. 

 ### Lists of gates 

### `Obeys`

 In the values v, the gates of the list, whose wires are n, n + 1, …, have their values. 

### `WFa`

 The gates of the list, whose wires are n, n + 1, …, read wires before their own. 

 ### The wires of a circuit 

### `wires_input`

 The input wires carry the input. 

### `obeys_wires`

 The values of the wires of a circuit on an input obey the circuit. 

 ### Chains 

### `prevW`

 The wire before place i of a chain that begins at the wire `off` and starts from the wire
`init`. At i = (length of the chain) it is the last wire of the chain. 

### `chain_all`

 A chain of gates «the wire before, and p i». 

### `chain_any`

 A chain of gates «the wire before, or p i». 

 ### Numbers in binary 

### `num`

 The number with the binary digits b 0, …, b (w − 1), lowest first. 

### `half_adder`

 A chain of half adders: s i = a i ⊕ c i, c (i+1) = a i ∧ c i. 

### `full_adder`

 A chain of full adders: s i = a i ⊕ d i ⊕ c i, c (i+1) = (a i ∧ d i) ∨ ((a i ⊕ d i) ∧ c i). 

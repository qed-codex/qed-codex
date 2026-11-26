---
{
  "module": "proof/consequences/SizeCircuit/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: the circuits are computed in polynomial time

`certGates_sizeGates`: from n in unary and s in binary, the list of gates `sizeGates n s` of
proof/consequences/SizeCircuit/CircuitDefs.lean is computed in polynomial time (`Groundwork.PolyT`).
The paper does not say this; it is needed because the formula Γ is written by a machine.

The n steps of the addition are a fold along the n strokes of the unary number. A fold is polynomial
time if its step is and the words of all its states have polynomial length. The step is written
without case distinction on lists (`addStepE`). The states are short because, by `iterate_spec`,
they hold at most 3n wire numbers (in three lists of at most n each) and 5n gates, all naming wires
below 6n. 

 ### The step 

### `addStepE`

 `addStep` written with lengths, places and `drop`. 

### `addStep_eq`

 The two ways to write the step agree. 

### `addStep_polyT`

 The step is polynomial time, as a function of n in binary and the state. 

 ### The words of the states are short 

### `len_list_le'`

 The word of a list whose elements have words of length at most B has length at most (number of
elements)·(B + 2) + 2. 

### `len_list_le`

 The word of a list of at most L elements with words of length at most B. 

### `len_nat_le`

 The word of a number x ≤ M has length at most 3M + 2. 

### `len_gate_le`

 The word of a gate that names wires up to M has length at most 6M + 18. 

### `lt_of_wfa`

 Gates that read earlier wires only name wires below the number of all wires. 

### `stateLen`

 The bound on the length of the words of the states. 

### `stateLen_pb`

 The bound is below a polynomial. 

### `len_iterate_le`

 After k ≤ n steps the word of the state has length at most `stateLen m`, for every m ≥ n. 

 ### The addition 

### `foldl_eq_iterate`

 A fold along a list of strokes that applies f at each stroke applies f as often as the list is
long. 

### `added_polyT`

 The addition is polynomial time in n in unary. 

 ### The comparison, and the circuit 

### `compareGates_polyT`

 The gates of the comparison are polynomial time in (N, s, the list of digit wires). 

### `certGates_sizeGates`

 **The circuits are computed in polynomial time** from n in unary and s in binary. 

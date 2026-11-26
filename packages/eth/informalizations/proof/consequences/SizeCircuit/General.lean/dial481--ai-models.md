---
{
  "module": "proof/consequences/SizeCircuit/General.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/General.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/General.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: clauses that force the values of the gates

Proofs of `StForces` and `StUniqueExtension` of proof/consequences/SizeCircuit/Defs.lean. The paper:
«a new variable for each gate, clauses of at most 3 literals that force it to equal the value of the
gate».

The clauses of all gates hold under an assignment a exactly if a obeys the circuit
(`CircuitLowerBound.Blocks.Obeys`: the variable of every gate has the value of the gate;
`holds_wiresFormula`). Two assignments that obey a circuit whose gates read earlier wires only, and
agree on the inputs, agree on all wires (`obeys_unique`, by induction over the gates). The values of
the wires on the input (`wireVal`) obey the circuit. 

 ### Formulas 

### `holds_nil`

 The formula without clauses holds. 

### `holds_cons`

 A formula with one more clause holds exactly if that clause has a true literal and the rest
holds. 

### `holds_append`

 Two formulas written one after the other hold exactly if both hold. 

### `holds_congr`

 Whether a formula holds depends only on the values of the variables that occur in it. 

 ### One gate 

### `forces_table`

 The table behind `stForces`: for bits x, y, z and a function of two bits with the values b0, b1,
b2, b3 at 00, 01, 10, 11, the four clauses "not (inputs x, y and the wrong value z)" hold exactly if
z is the value of the function at x, y. 

### `stForces`

 **`StForces`.** «clauses of at most 3 literals that force it to equal the value of the gate»:
the four clauses of a gate hold exactly if the variable of its wire has the value of the gate, and
each has at most 3 literals. 

### `holds_gateClauses`

 The four clauses of a gate hold exactly if the variable of its wire has the value of the gate. 

 ### All gates 

### `holds_zipIdx`

 The clauses of the gates of K, numbered from j on, hold under a exactly if a obeys K with the
wires n + j, n + j + 1, …. 

### `holds_wiresFormula`

 The clauses of all gates hold under a exactly if, under a, the variable of every gate has the
value of the gate. 

### `wfa_of_wf`

 If every gate reads earlier wires only, counted by its place in the list (`WF`), then also
counted gate by gate (`WFa`). 

### `obeys_unique`

 Two assignments that obey a circuit whose gates read earlier wires only, and agree on the wires
below n, agree on the wires of all gates. 

 ### The values of the wires on an input 

### `wireVal`

 The value of the wire i of the circuit K on the input x (0 if there is no such wire). 

### `obeys_wireVal`

 The values of the wires obey the circuit. 

### `wireVal_input`

 The input wires carry the input. 

### `eval_eq_wireVal`

 The output of a circuit is the value of its last wire. 

### `wireVal_of_le`

 Beyond the last wire the value is 0. 

 ### Assignments on finitely many variables 

### `ext_of_lt`

 Below N, the assignment b on N variables, read on all numbers, has the value of b. 

### `ext_of_le`

 From N on, the assignment b on N variables, read on all numbers, is 0. 

### `stUniqueExtension`

 **`StUniqueExtension`.** For every non-empty circuit K on n inputs whose gates read earlier
wires only, every assignment of x₀ … xₙ₋₁ extends in exactly one way to the variables of the gates
so that the clauses of all gates hold, and then the variable of the last wire has the value of the
circuit. 

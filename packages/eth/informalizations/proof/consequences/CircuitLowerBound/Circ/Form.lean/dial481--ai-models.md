---
{
  "module": "proof/consequences/CircuitLowerBound/Circ/Form.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Circ/Form.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Circ/Form.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The formula «some clause is violated by the assignment that the circuit C computes»

Let G be the circuit that computes clause number j of the formula of a table from the bits of j. The
check circuit consists of G, three copies of C that read the three variables of the clause off the
output
wires of G, three gates that compare the outputs of the copies with the three signs, and two gates
for the conjunction. It outputs 1 on j if and only if clause number j is violated by the assignment
i ↦ C(i). The formula has one variable for every wire of the check circuit, four clauses for every
gate, and one clause that says that the last wire is 1.

The proofs work with assignments a : ℕ → Bool of values to the wires and with the equations of the
gates (`GE`). `seg`: if the equations of a relocated copy of a circuit hold, the wires of the copy
carry the values of
the wires of the circuit. `stForm_of` proves the interface statement `StForm` from `StClauseCirc`.
The auxiliary statements are in the namespace `CircuitLowerBound.Form`. 

 ### The wires of a circuit 

### `length_wires`

 There is one more wire for every gate. 

### `getD_wires_of_lt`

 The wires that are there at the start keep their values. 

### `forall_append`

 A statement on all gates of a list, with their numbers, for two lists one after the other. 

### `getD_wires_gate`

 The wire of a gate carries the value of the gate on the wires that it reads. 

### `eval_eq`

 The output of a circuit is the value of its last wire. 

 ### Assignments of values to wires, and the equations of the gates 

### `GE`

 The gates of K, whose wires are N, N + 1, …, have the right values under a. 

### `exists_ge`

 The values of the wires on an input satisfy the equations of the gates. 

### `seg`

 A copy of the circuit C on L inputs, with the wire k of C moved to the wire ρ k, where the gates
go to N, N + 1, …: if the equations of the gates of the copy hold under a, then the wire ρ k carries
the value of
the wire k of C on the input that the wires ρ 0, …, ρ (L − 1) carry. 

 ### One variable for every wire 

### `gateCl`

 The four clauses of a gate whose wire is i. 

### `ex3`

 A clause of three literals is satisfied if one of the three is. 

### `dG`

 A gate for the places where there is none. 

### `tseitin`

 The clauses of all gates of a circuit on n inputs. 

### `shape_tseitin`

 The clauses have three literals, and their variables are wires. 

 ### The check circuit 

### `rho`

 Where the wire k of a circuit on L inputs goes in a copy: an input to the wire that the list o
names at the place off + k, the gate number t to the wire N + t. 

### `reloc`

 The copy. 

### `fin`

 The last five gates: the outputs of the three copies, which have c gates each and begin at the
wire N, are compared with the three signs; then the conjunction. 

### `check`

 The check circuit; N is the number of the wires of G, inputs included. 

### `wf_check`

 In the check circuit every gate reads inputs and earlier gates only. 

### `copy_out`

 The output wire of a copy carries the output of the circuit on the input that the wires named by
o carry. 

### `check_out`

 What the last wire of the check circuit says, if the equations of all gates hold: each of the
three copies of C, on the input that the output wires of G carry, differs from the sign wire. 

### `sat_psi`

 The formula is satisfiable if and only if some assignment satisfies the equations of all gates
and gives the wire «out» the value 1. 

### `take_drop_eq`

 A part of a list, entry by entry. 

### `not_all_iff`

 Not all clauses of the formula of a table are satisfied: some clause is violated. 

 ### The formula and its properties 

### `form_spec`

 The properties of the formula, for a circuit G with output wires o that computes the clauses of
the formula of the table e. 

### `nF`

 The number of the input bits of the check circuit, cut off so that it can be written in unary. 

### `cK`

 The check circuit, from the table, L in unary, the parameter P and the circuit C. 

### `F`

 The number of variables, in unary, and the formula. 

 ### Polynomial time 

### `stForm_of`

 The formula that says «some clause of the formula of the table e is violated by the assignment
that the circuit C computes», from the circuit that computes a clause from its number. 

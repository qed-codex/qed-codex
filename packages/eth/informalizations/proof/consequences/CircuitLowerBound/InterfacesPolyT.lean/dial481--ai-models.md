---
{
  "module": "proof/consequences/CircuitLowerBound/InterfacesPolyT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/InterfacesPolyT.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/InterfacesPolyT.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the interface statements on circuits, formulas and polynomial-time functions

As in `Interfaces.lean`: definitions `St… : Prop` only. `PolyT f`
(proof/machines/ToTuring/PolyT.lean) says that f is computed in polynomial time on a multi-stack
machine. A number that bounds the length of a list comes in unary, as a `List Unit`. 

 ### Circuits as data 

### `GateD`

 A gate as data: its values at 00, 01, 10, 11, and the numbers of the two wires that it reads. 

### `toC`

 The circuit of a list of gates given as data. 

### `WF`

 On n input bits, gate t reads inputs and earlier gates only. 

### `StNorm`

 Every circuit on m ≥ 1 input bits can be written as data in which every gate reads inputs and
earlier gates only, with the same number of gates. 

### `StClauseCirc`

 The circuit that computes clause number j of the formula of a table from the bits of j. It has
nb inputs and 3·(L+1) output wires: for each of the three literals the L bits of the variable,
lowest first, and the sign.
Its size is at most a₀·(L+1) + g(e): the number a₀ does NOT depend on the table. 

### `Shaped3`

 Clauses of at most 3 literals, variables below Nv, no clause twice. 

### `StForm`

 The formula that says «some clause of the formula of the table e is violated by the assignment
that the circuit C computes». It has at most 3·|C| + a₀·(L+1) + g(e) variables: a₀ does NOT depend
on the table. 

 ### The chains and the formulas are computed in polynomial time 

### `StCertTabF`

 The formula of a table is written out in time polynomial in its length; the last argument is a
list at least as long as the formula has clauses. 

### `StFlip`

 At the last place of a chain, the question about the first number of the chain is answered by
trying all assignments, in time polynomial in m. 

 ### The two forms of E^NP 

### `StRestart`

 A machine that is started again after every answer can be replaced by an oracle machine. 

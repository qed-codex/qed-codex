---
{
  "module": "proof/consequences/CircuitLowerBound/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7) from the interface statements

`no_linear_circuits`: the language `L0` is not decided by circuits of linear size. Suppose it is,
with the constant c₀. Take the machine N of the algorithm for c₀, its table e, and a chain a of e
that starts beyond all thresholds. Along the chain,
«`Phi m` is satisfiable» passes from each number to the next and back, because `Phi m` says that N
accepts the next number, and N accepts a number if and only if its formula is satisfiable. At the
last place the formula says the opposite of the
formula at the first place: a contradiction. 

### `phi_vars`

 The variables of `Phi m` have m bits. 

### `sat_by_circuit`

 A circuit that decides the language on the words of length m computes a satisfying assignment of
`Phi m`, if there is one. 

### `room`

 Room, and time, for a number L of a chain and a parameter P ≤ 3L. 

### `no_linear_circuits`

 The language is not decided by circuits of linear size. 

### `corCircuits'_of`

 The circuit lower bound for E^NP (Section 7), with the second form of E^NP, from the interface
statements. 

### `corCircuits_of`

 The circuit lower bound for E^NP (Section 7), from the interface statements. 

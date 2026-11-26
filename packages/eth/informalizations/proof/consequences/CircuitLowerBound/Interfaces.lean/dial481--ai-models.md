---
{
  "module": "proof/consequences/CircuitLowerBound/Interfaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Interfaces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Interfaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the interface statements, as propositions

The main statements that one file needs from another are written here as definitions `St… : Prop`;
the others are written in other files. Nothing is proved and nothing is assumed: this file has no
theorem. One file proves `theorem st… : St…`; a file that needs the statement takes it
as a hypothesis; `proof/consequences/CircuitLowerBound/Main.lean` takes them all as hypotheses, and
another file feeds the proofs in. 

### `StTab`

 Every machine has a table: the formula of the table is satisfiable if and only if the machine
accepts 1^P 0 y for some y within 2^bt steps. 

### `StCode`

 Every table has arbitrarily large numbers. 

### `StChain`

 The chains. 

### `StVars`

 The variables of the formula of a table have L bits. 

### `StGreedy`

 The search finds a satisfying assignment if there is one. 

### `StAlg`

 The algorithm. For every c₀ ONE machine N: (1) if N accepts 1^m 0 y, then `Phi m` is
satisfiable; (2) for every table e there is m₀ such that for all m ≥ m₀ on a chain of e: if a
circuit with at most c₀·(m+1) gates computes a satisfying
assignment of `Phi m`, then N accepts 1^m 0 y for some y within 2^(m/8) steps. N is chosen before e,
and m₀ after e. 

### `StENP'`

 The language is in E^NP, second form. 

### `StENP`

 The language is in E^NP, first form. 

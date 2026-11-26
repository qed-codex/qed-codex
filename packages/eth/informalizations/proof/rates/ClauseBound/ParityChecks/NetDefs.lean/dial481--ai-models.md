---
{
  "module": "proof/rates/ClauseBound/ParityChecks/NetDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/NetDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/NetDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sums of the parity checks as sums over marks in layers: definitions and interface lemmas

A check number j becomes a dummy variable, number n + j; the incidence (e, j) becomes the clause
number e of ψ with the literal (n + j, false) of that dummy variable added. Then every sum that the
choice of the checks and the final count need is
a sum `truncW` over the assignments of n + r variables, with layers of clauses: all clauses, the
incidences, and, for `sumB` only, the clauses not yet decided; a mark in layer i has the weight
ws_i, and the number of marks
in layer i lies between lo_i and hi_i. A state of the choice is (j, t, Lam): Lam is the list of the
r checks, each a list of numbers of clauses; the checks before j are complete; check j has been
decided for
the clauses before t. 

### `incL`

 The incidences of the checks before j, each with its dummy literal, and those of check j
without. 

### `sumB`

 The sum for B_i (the quantity `_root_.ParityChecks.Bint`; `StBridgeB` states how the two are
related) in the state (j, t, Lam). 

### `sumA`

 The sum for A (the quantity `_root_.ParityChecks.Aint`; `StBridgeA` states how the two are
related) in a state with the checks before j complete. 

### `sumF3`

 The sum for the final count. 

### `Vof`

 The clauses that ξ violates, as a set of numbers of clauses. 

### `Lof`

 The check number j as a set. 

### `Dof`

 The clauses from number t on. 

### `WfC`

 The checks are lists without repetition of numbers of clauses. 

 ### Bridge.lean: the three sums are 2^r times B_i, A and the count, modulo 2^{M+1} 

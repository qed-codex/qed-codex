---
{
  "module": "proof/machines/StepMachines/Math/Sparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Sparsify.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Sparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Lemmas for the sparsification of a 3-CNF (Impagliazzo, Paturi, Zane): formulas as finite sets of
clauses,
their reduction to inclusion-minimal clauses, what holds at a node of the branching tree, and a
double counting of clauses.
Literals are elements of any type α; a clause is a Finset α, a formula a Finset (Finset α). 

### `Sat`

 The truth values v of the literals satisfy F: every clause has a true literal. 

### `Reduced`

 No clause properly contains another. 

### `red`

 The inclusion-minimal clauses. 

### `over`

 The i-clauses of F that contain S. 

### `ones`

 The 1-clauses of F. 

### `sat_red`

 sat(red F) = sat(F). 

### `Inv`

 The invariant at a node of the tree: F is reduced, and N is a set of 2-clauses of F
with at most τ clauses at each literal. 

### `Node`

 What holds of a node F of the tree of φ, with counters p and q: every clause of F is a subset
of a clause of φ, and for some N with `Inv` the potentials |N| + (τ+1)·|ones F| and |N| + 2τ·|ones
F| are at least
p and q. 

### `mul_card_le`

 Double counting: i-subsets of U, each point in at most d of them. 

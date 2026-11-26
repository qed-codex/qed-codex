---
{
  "module": "proof/rates/CountedRecursion/Base.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Base.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Base.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The solver at the level 0

Proof of Theorem A (b): for ℓ = 0, brute force sums 2^{λK₀(K₀−1)/2} ≤ 2^{e₀K₀²λ} terms, each at a
cost of at most (K₀(λ+B))^{C₅}. At ℓ = 0 the solver is brute force on K₀ = 2^{x₀} nodes, with its
queries written as queries of the solver and its answers read as integers. The count is
`brute_within`;
the constructions around it (`mapAsk`, `readAs`, `mapIn`, `ite`, `mapOut`) take no step and together
make the states larger by 1 (only `ite` adds to the size). The states have size at most 3X² + 13X +
22 ≤ X⁶ for X = K₀(λ + B) ≥ 2: C₅ = 6, one constant for all x₀ (`solverBase`). 

### `size_listUnit`

 A list of n units has size 2n + 1. 

### `tables_readTables`

 The tables read back from the answers of `W`, `readTables (answersOf K lam W)`, give the same
oracle `tables K lam` as `W` itself. 

### `base_room_le`

 The bound on the states: 3X² + 13X + 22 ≤ X⁶ for X = K(λ + B). 

### `solverBase`

 `SolverBase`, with C₅ = 6. 

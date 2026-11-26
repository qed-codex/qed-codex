---
{
  "module": "proof/rates/CountedToPadded/Levels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Levels.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Levels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sequence of levels

Proof of `SolverOfMachineLevelsFrom` (Defs.lean), and of `CliqueLevels.SolvesOfSolvesInFactor`
(CliqueLevelsStatement.lean). The field of the sequence of levels that takes the most work is that
the solver is right: `solver_right`. 

### `bound_mono`

 The printed bound grows with e and with B. 

### `le_bound`

 The printed bound is at least K(λ + B), for e ≥ 0, C₀ ≥ 1 and K ≥ 1, λ ≥ 1. 

### `size_query_le`

 A query that the tables answer has size at most K + 2Kλ + 2. 

### `solver_right`

 The solver is right when the padding string has 2^need units. 

### `solverOfMachineLevelsFrom`

 The main statement follows from `StPlug` and the statements of Defs.lean on the run, the tables,
the number between e_ℓ and 2e_ℓ, the exponent, polynomial time and the program that picks the level. 

### `solvesOfSolvesInFactor`

 The form with all states within the polynomial factor gives the form with all states within the
whole bound, for e ≥ 0. 

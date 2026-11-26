---
{
  "module": "proof/rates/CountedRecursion/EndSolves.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/EndSolves.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/EndSolves.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem A (b) as `CliqueLevels.Solves` has it

* `recursionSolvesFrom : RecursionSolvesFrom`. The machine `cliqueMachine c x₀ Alg` is
  `recursionWith c x₀ Alg` with the input (ℓ, λ, B), with answers that are integers (`ReadAsRuns`)
  and with an integer as its result. Three times the bound for C₁, and twice the bound on the sizes
  for C₁ with the room of the algorithm (`RoomIsWithinTheBound`, constant C₂), are within the bound
  for C₁ + C₂ + 1. 

### `recursionSolvesFrom`

 **Theorem A (b)**, in the form of `CliqueLevels.Solves`, from the form with the algorithm of the
pieces. 

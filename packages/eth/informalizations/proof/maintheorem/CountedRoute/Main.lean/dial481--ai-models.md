---
{
  "module": "proof/maintheorem/CountedRoute/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/CountedRoute/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/CountedRoute/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The chain from counted operations: the proofs

* `onEveryMachineWithQueryAccessFrom`: the step from counted operations to the padding string
  (`QueryMachines.Bridge.SolverOfMachineLevels`) gives, for a machine E with the printed hypothesis,
  a polynomial-time solver with a sequence of levels for the numbers e′_ℓ in [e_ℓ, 2e_ℓ];
  `ThmVariables.numberBetween_cut` gives the clause that a number in [e′_ℓ, 2e′_ℓ] can be computed;
  e′_ℓ ≤ 2e_ℓ ≤ 2a/√(log K_ℓ) (`QueryMachines.Bridge.CutNumberFacts`). The chain for
  every solver (`NamesInOrder.OnEverySolver`; for Step 6 `MainRoute.BothBoundsOnEverySolver`) is
  applied to this solver, and the names are rewritten.
* `onTheCountedRecursionFrom`: the machine of Theorem A (b) on the pieces of Appendix B meets the
  hypothesis (`CountedInstance.TheRecursionMeetsTheHypothesis`).
* `closedStatementsFrom`: the closed statements are read off. 

### `onEveryMachineWithQueryAccessFrom`

 The chain from counted operations, from the step to the padding string and the chains for every
solver. 

### `onTheCountedRecursionFrom`

 The chain on the machine of Theorem A (b). 

### `closedStatementsFrom`

 The closed statements, read off the chain on the machine of Theorem A (b). 

### `onEveryMachineWithQueryAccess`

 **The chain from counted operations.** 

### `onTheCountedRecursion`

 **The chain on the machine of Theorem A (b).** 

### `mainTheoremHolds`

 **The Main Theorem** of the paper, on Theorem A (b) in counted operations. 

### `corMinHolds`

 **Corollary 11**, on Theorem A (b) in counted operations. 

### `thmVariablesBHolds`

 **The conclusion of Theorem D (b)**, on Theorem A (b) in counted operations. 

### `boundInMHolds`

 **The first sentence of Theorem A (c)**, at α′ = 1/2, on Theorem A (b) in counted operations. 

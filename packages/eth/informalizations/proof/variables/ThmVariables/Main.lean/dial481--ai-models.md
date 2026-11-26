---
{
  "module": "proof/variables/ThmVariables/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/ThmVariables/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/ThmVariables/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) with the printed hypothesis: the end theorems

The two hypotheses of EveryMachine.lean are fed in: the step from counted operations to the padding
string for the named solver (`QueryMachines.Bridge.solverOfMachineLevels`,
proof/rates/CountedToPadded) and Theorem D (a) for every machine that computes the function of Steps
1 to 5 of Appendix D (`RecursionToBound.thmVariablesAForEveryMachine`,
proof/variables/RecursionToBound).
* `solverFromMachine`: from every machine with query access as in the printed hypothesis, a solver
  with a sequence of levels.
* `partAForEveryMachine`: every machine that runs the named algorithm on the solver that the machine
  with query access gives has the bound.
* `partA`: Theorem D (a). It is taken from `partAForEveryMachine`; `partAFromThePaddingString`
  (PartA.lean) with `solverFromMachine` and `RecursionToBound.thmVariablesAWithNumberBetween` gives
  the same proposition. 

### `solverFromMachine`

 From every machine with query access as in the printed hypothesis of Theorem D (a): a
polynomial-time solver with a sequence of levels for the same K_ℓ and for the number in [e_ℓ, 2e_ℓ],
cut at 1. 

### `partAForEveryMachine`

 **Theorem D (a) for every machine that runs the named algorithm** on the solver that the machine
with query access gives. 

### `partA`

 **Theorem D (a)**, with the hypothesis in counted operations and table queries. 

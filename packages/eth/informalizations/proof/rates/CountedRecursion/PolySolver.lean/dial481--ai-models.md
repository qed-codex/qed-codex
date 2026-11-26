---
{
  "module": "proof/rates/CountedRecursion/PolySolver.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolySolver.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolySolver.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The solver has polynomial-time steps

One certificate for each machine of SolverDefs.lean, written along its definition with the rules of
PolyRules.lean. The procedure of the lemma on groupings up to its call (`groupingCall`) has its
certificate from the first half of `GroupingPoly`; here it is a hypothesis. 

### `patternValue_poly`

 Z_ι. 

### `capsLoop_poly`

 The numbers c^row_i or c^col_i. 

### `sumAndDivide_poly`

 The sum over the patterns and the division. 

### `numbersOn_poly`

 The loop for K and g, on ℓ − 1. 

### `levelSolver_poly`

 The solver at a level ℓ ≥ 1. 

### `brute_poly`

 Brute force. (The same stands in proof/threesat/Printed/Achievable.lean; it is said again here
so that the certificates stand on `Printed.Programs` alone.) 

### `baseSolver_poly`

 The solver at the level 0. 

### `solver_poly`

 **The solver has polynomial-time steps.** 

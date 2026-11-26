---
{
  "module": "proof/variables/SparsifyThenCount/PlanUsed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/PlanUsed.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/PlanUsed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The plan is used: proofs

* `stPlanUsed : StPlanUsed`. The plan on the code of (k, φ) depends only on k and n (`planD_enc`),
  so it is enough to look at the formula without clauses. For it the merged exponent `eBD` is `eD`,
  because the algorithm for the bound in m
  is taken only if there is a clause (`eBD_nil`). Without a plan `eD` is n. The clause `timeN` of
  `Alg`, at q = 1, then gives 2^n ≤ D·2^(D·k²·n·rn(n)). This is false as soon as D·k²·rn(n) ≤ 1/2
  and n ≥ 2(D + 1) (`not_le_bound`).
* `stRateZero : StRateZero`: log y/√y tends to 0, and y = log₂(n+4) tends to infinity. 

### `planD_enc`

 On the code of (k, φ), k ≥ 1, φ a k-CNF on n variables, the plan is that for k and n: it does
not depend on φ. 

### `isKCNF_nil`

 The formula without clauses is a k-CNF. 

### `eBD_nil`

 On the code of the formula without clauses the merged exponent is the exponent of the plan, or n
if there is none. 

### `not_le_bound`

 2^n is not within D·2^(D·k²·n·r), rounded down, if D·k²·r ≤ 1/2 and n ≥ 2(D + 1). 

### `stPlanUsed`

 If some function A with the exponent function `VariableBound.eBD S pick slU` is an algorithm for
the rates rn and rm, and rn tends to 0, then for every width k ≥ 1 and all large n the plan exists
on the code of (k, φ), for every k-CNF φ on n
variables. 

### `stRateZero`

 The rate log₂ log₂(n+4)/√(log₂(n+4)) tends to 0. 

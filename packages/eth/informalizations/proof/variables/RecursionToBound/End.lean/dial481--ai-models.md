---
{
  "module": "proof/variables/RecursionToBound/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) along the printed Step 5: the end

Let M compute `count S n₁ Q.pick num` with the exponent `expo S n₁ Q.pick num`, for n₁ large. Let x
be the code of (k, φ), with ℓ the level of n, 3 ≤ k ≤ (log n)^(1/4) and φ a k-CNF on n variables;
write e = e_ℓ and X = k²·e·n·log(k/e).

* The output is right (`CountIsRight`, a hypothesis here).
* M takes at most q·(|x| + 2^(expo x) + 1)^q steps, and |x| + 1 ≤ (n+2)^(5k) ≤ 2^{10·k·log n}.
* The function takes k′ = `widthOr3 φ`, and 3 ≤ k′ ≤ k (`WidthOnTheCode`, a hypothesis;
  `cutOffIsIdle`). «The bound increases with k» (`PairsToBound.expVariablesA_mono`).
* The exponent is read from the plan `planAt` at (k′, n, the level), an optional value; where there
  is no plan the exponent is n. If n < n₁ there is no plan: «For the finitely many smaller n ≥ K₀^17
  … trying all assignments is within the bound» (`MainTheoremForms.StepSparsifySmallStmt`): n ≤ c·X
  and k·log n ≤ c·X.
* If n ≥ n₁ and there is a plan, the exponent is `needOutputs` + `needWalk` at k′; if there is none,
  the exponent is n, which is below that sum (`PlanFailsOnlyAboveN`, a hypothesis). The sum is at
  most A·X (`exponentIsWithinTheBound`). And k·log n ≤ e·n ≤ X
  (`MainTheoremForms.StepSparsifyLargeStmt`).

So with a = c + A + 1: 1 ≤ a·X, the exponent is at most a·X and k·log n ≤ a·X;
`steps_le_timeVariablesA` turns this into the bound with the constant 12·q·a. That a machine exists
is `CountKSatRate.stPaddedW` with `CountIsPolynomialTime` (a hypothesis). 

### `steps_le_timeVariablesA`

 The running time q·(len + 2^E + 1)^q of a machine that is given a padding string of 2^E units,
against the bound of Theorem D (a). If 1 ≤ a·X, E ≤ a·X and k·log n ≤ a·X for X = k²·e·n·log(k/e), n
≥ 4 and len + 1 ≤ (n+2)^(5k), then q·(len + 2^E + 1)^q ≤ 2^{12qa·X}, rounded down. 

### `thmVariablesAForEveryMachine_of`

 Theorem D (a) for every machine that computes the named function. Four statements on the
function are hypotheses: it is right, it is polynomial-time, it sparsifies unless the exponent
exceeds n, and it reads the width and the level from the code. `exponentIsWithinTheBound` and
`cutOffIsIdle` are used directly. 

### `thmVariablesAWithNumberBetween_of`

 Theorem D (a) with the printed clause on the number in [e_ℓ, 2e_ℓ], from the form for every
machine that computes the named function. 

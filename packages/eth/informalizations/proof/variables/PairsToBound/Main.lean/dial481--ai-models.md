---
{
  "module": "proof/variables/PairsToBound/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (b) from Theorem D (a): the main statement

Step 6 of Appendix D. Let x be the code of (k, φ), with k ≥ 1, n ≥ 4 and φ a k-CNF on n variables,
let k′ = `widthOr3 φ` be the width that the algorithm uses, and X = k²·n·log log n/√(log n).

* If the test is true, then n ≥ K₀^17 and k′ ≤ (log n)^(1/4). By `mainRegimeBound` the machine M of
  Theorem D (a), on the code rewritten at k′, puts out the count within 2^{C₁·k′²·n·log log n/√(log
  n)} ≤ 2^{9C₁·X} steps (`main_case_le`).
* If the test is false, the machine Mb puts out the count on x within 2^{c·n}·n^{c·k} steps. Either
  k′ > (log n)^(1/4), and then n ≤ 9·X (`le_of_wide`), or n < K₀^17, and then n ≤ √(17·log K₀)·X
  (`le_of_small`); and k·log n ≤ X (`mul_lg_le_expN`). The numbers are put together in
  `fall_back_case_le`.
* In both cases |x| + 1 ≤ (n+2)^(5k) (`UniformInK.Time.length_enc_succ_le`) ≤ 2^{10·X}
  (`length_le_rpow`), and the power q of the choice multiplies the constant (`choice_le`).

The constant C is chosen after the solver, its levels, a, M, C′, Mb, c and q, and before k, n and φ.
`thmVariablesBFromThmVariablesA` adds that such machines exist: a machine that tries all assignments
(`exhaustiveMachineExists`), the front end and the test (`frontEndAndTestExist`) and the choice
(`TwoMachines.everyTwoMachinesCanBeChosenBetween`).
`thmVariablesAImpliesThmVariablesB` applies Theorem D (a) to the pairs of Appendix A on the pieces
of Appendix B (`thePairsSatisfyTheHypothesis`), takes e_ℓ ≤ (3x₀+6)/√(log K_ℓ) from
`thetaOfThePairs`, and then applies `thmVariablesBFromThmVariablesA`. 

### `everyChoiceMeetsThmVariablesB`

 **The main statement** (Step 6 of Appendix D): every machine that chooses, by the printed test,
between a machine with the conclusion of Theorem D (a) behind the front end and a machine that tries
all assignments meets the bound of Theorem D (b). 

### `thmVariablesBFromThmVariablesA`

 Existence and the main statement in one: for every machine with finite alphabets and the
conclusion of Theorem D (a) there are a machine that tries all assignments, a front end, a test and
a machine that chooses between the two machines, as in Step 6 of Appendix D; and every such choice
meets the bound of Theorem D (b). 

### `thmVariablesAImpliesThmVariablesB`

 Theorem D (b) from Theorem D (a) and Theorem B, along Step 6 of Appendix D: the pairs of
Appendix A on the pieces of Appendix B meet the hypothesis of (a); (a) gives a machine; e_ℓ ≤
(3x₀+6)/√(log K_ℓ); the choice around that machine meets the bound of (b). 

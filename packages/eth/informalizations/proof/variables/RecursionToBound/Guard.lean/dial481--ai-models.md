---
{
  "module": "proof/variables/RecursionToBound/Guard.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Guard.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Guard.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The guard of the plan

The function of Theorem D (a) (proof/variables/RecursionToBound/Defs.lean) has a guard that the
paper (Step 5 of Appendix D) does not have: if the exponent of the padding string, computed from the
input, exceeds n, the function tries all assignments. The guard cannot be dropped, because a
solver's exponent can be computed only under a bound given in unary.

**What is proved.** `planFailsOnlyAboveN : PlanFailsOnlyAboveN`: for a polynomial-time solver and
all n₁, k, n, i, r: if the plan is `some v`, then n₁ ≤ n, v = `needOutputs` + `needWalk` and v ≤ n;
if the plan is `none` and n₁ ≤ n, then n < `needOutputs` + `needWalk`. So for n ≥ n₁ the guard is
the only reason for which the function does not sparsify.

**How.** A polynomial-time solver has two properties (`ClauseBound.Alg.Solver.Poly.needC_eq`,
`ClauseBound.Alg.Solver.Poly.needC_some`): the exponent computed under a bound, if there is one, is
the exponent; and there is one whenever the exponent is at most the bound. They are carried upwards
to the exponent of the networks (`needNetC`), to the exponent for one Δ (`needAtC`), and to the
maximum over all Δ (`needOutputsC`, by `foldr_bind_max`), each time as a pair of lemmas: if the
value computed under the bound is there, it is the exact value; if it is missing, the exact value
exceeds the bound. 

### `needNetC_eq_some`

 The exponent of the networks computed under a bound, if there is one, is the exponent of the
networks. 

### `lt_needNet_of_none`

 If the exponent of the networks computed under a bound is missing, the exponent of the networks
exceeds the bound. 

### `needAtC_eq_some`

 The exponent for one Δ computed under a bound, if there is one, is the exponent for this Δ. 

### `lt_needAt_of_none`

 If the exponent for one Δ computed under a bound is missing, the exponent for this Δ exceeds the
bound. 

### `needOutputsC_eq_some`

 The maximum over Δ computed under a bound, if there is one, is the maximum over Δ. 

### `lt_needOutputs_of_none`

 If the maximum over Δ computed under a bound is missing, the maximum over Δ exceeds the bound. 

### `planFailsOnlyAboveN`

 For n ≥ n₁ the function sparsifies unless the exponent exceeds n; and where there is a plan, it
is the sum of the exponent for the outputs and the exponent for the walk. 

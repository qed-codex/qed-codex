---
{
  "module": "proof/variables/VariableBound/Paper/Forms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Forms.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Forms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The statements of `MainTheoremFormsStatement.lean` for formulas over x₀ … xₙ₋₁

**What is proved.** `together_of`: every proof of `SatM.TargetUniform` gives ONE Turing machine and
ONE constant C for `MainTheoremForms.TogetherAllOccur`, that is, the bound of Theorem 1 (k ≥ 1, m ≥
2, n ≥ 4, all variables occur), the bound of Theorem D (b)
(k ≥ 1, n ≥ 4, any number of clauses, variables need not occur) and the bound of Corollary 11, all
with log m and log n themselves and with no factor in front. Its steps are `mainTheoremFor_of` and
`thmVariablesBFor_of`; also
`corMinIsMainTheorem` (the bounds of Corollary 11 and of Theorem 1 are the same) and `clauseCount`
(a k-CNF on n variables has at most (2n+1)^k clauses).

**How.** No new mathematics. `together_of` keeps the machine of the given proof
(`UniformInKStatement.lean`: log₂(m+2), log₂(n+4), a factor C in front), its constant C becomes 3C,
and the rest is the
arithmetic of proof/variables/VariableBound/Paper/Arith.lean. 

 ### More time is allowed 

### `countsWithin_mono`

 A machine that counts within t steps counts within t' ≥ t steps. 

 ### Counting 

### `corMinIsMainTheorem`

 After Corollary 11: «This is the Main Theorem.» For every machine and every constant the bound
of Corollary 11 and the bound of Theorem 1 are the same. 

### `thmVariablesBFor_of`

 From the bound in n of `UniformInKStatement.lean` with the constant C to the bound of Theorem D (b)
with the constant 3C, for the same machine. 

### `mainTheoremFor_of`

 From the bound with the minimum of `UniformInKStatement.lean` (for k ≥ 1, n ≥ 1, all variables
occurring) with the constant C to the bound of Theorem 1 with the constant 3C, for the same machine. 

### `together_of`

 Every proof of `SatM.TargetUniform` gives one machine and one constant for Theorem 1, Theorem D (b)
and Corollary 11 in the paper's wording. 

### `clauseCount`

 A k-CNF on n variables has at most (2n+1)^k clauses. 

---
{
  "module": "proof/sparsification/UniformInK/Top/Budget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Budget.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Budget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The parameters of the top level fit, and a bound on the stack of the walk

`stParU : StParU`: for τ = 2^(4s+17) and β = `betaU k s`, leafCU τ k + 2 ≤ 2^β (a leaf has at most
leafCU τ k · n clauses), and τ is at least k² and 8k as soon as s ≥ `s0U k`.
`stack_le`: the stack of the walk through the counting tree has length at most 2^(betaU k s + 5k +
10 + (k+3)·size n) for τ = 2^(4s+17).
The counterpart of proof/rates/ClauseBound/ParityChecks/BudgetOL.lean, whose lemmas on powers of two
are used; here bsumU τ k = τ^(2k) is exactly 2^β
(`bsumU_tauOf`), and a path of the counting tree has at most bsumU τ k · n steps. 

### `leafCU_add_two_le`

 2·(θ 0 + … + θ (k-1)) + 2 ≤ τ^(2k) for k ≥ 1 and τ ≥ 8. 

### `stack_le`

 The stack of the walk: stackLenCU k τ n (inLen k n) ≤ 2^(betaU k s + 5k + 10 + (k+3)·size n) for
τ = 2^(4s+17). 

### `stParU`

 leafCU τ k + 2 ≤ 2^(betaU k s) for τ = 2^(4s+17) and k ≥ 1; and k² ≤ τ, 8k ≤ τ if s ≥ s0U k. 

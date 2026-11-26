---
{
  "module": "proof/rates/ClauseBound/ParityChecks/BudgetOL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/BudgetOL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/BudgetOL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What a pad of length 2^(restO …) suffices for

`stBudgetO : StBudgetO`: the list of profiles, the lists of the checks, the rounds of the walk
through the counting tree and its stack. Statements about natural numbers; every factor is
bounded by a power of two, and each of the four summands of `restO` pays for one of the four
budgets. The last two budgets and their proofs are those of
proof/rates/ClauseBound/TopN/Budget.lean. 

### `mul_le_pow`

 A product of numbers below powers of two. 

### `add_le_pow`

 A sum of two numbers below powers of two. 

### `succ_le_size`

 n + 1 ≤ 2^(size n). 

### `clause_le`

 The word of a clause: k·(3n+5) + 10 ≤ 2^(k + size n + 4). 

### `bsum_le`

 bsum τ k ≤ 2^β. 

### `inLen_le`

 The length of the code of an instance: inLen k n ≤ 2^(3k + 1 + (k+1)·size n). 

### `nProf_le`

 The list of profiles: (M + 1)^(g·g·3) ≤ 2^(g·g·3·size M). 

### `checks_le`

 The lists of the checks: 8(6n+1)(m+1)(size m + 2) + 8 ≤ 2^(3·size m + 3·size n + 12). 

### `stack_le`

 The stack of the walk. 

### `le_four`

 Each of four summands is at most the sum. 

### `stBudgetO`

 The four budgets. 

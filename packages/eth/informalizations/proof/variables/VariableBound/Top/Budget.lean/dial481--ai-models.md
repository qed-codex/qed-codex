---
{
  "module": "proof/variables/VariableBound/Top/Budget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/Budget.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/Budget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What a pad of length 2^(restD …) suffices for

`stBudgetD : UniformInK.StLeavesU → StBudgetD`: the list of profiles, the list of checks, the rounds
of the walk through the counting tree and its stack. Each of the four summands of `restD` pays for
one of the four budgets.
The first two budgets are proper to this file: a profile has two kinds of marks in place of three
layers, and the second summand of `restD` is the bit length of the
second budget itself. The last two budgets are those of
proof/sparsification/UniformInK/Top/Budget.lean, and its lemmas are used. 

### `nProf_le`

 The list of profiles: (M + 1)^(g·g·2) ≤ 2^(g·g·2·size M). 

### `stBudgetD`

 For k ≥ 1 and s ≥ s0U k, a number F ≥ 2^(restD k K n s) is at least the first, second and fourth
budgets, and F + 1 is at least the third, given the bound for the number of leaves
(`UniformInK.StLeavesU`). 

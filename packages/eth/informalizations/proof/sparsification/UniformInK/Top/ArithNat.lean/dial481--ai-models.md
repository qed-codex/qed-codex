---
{
  "module": "proof/sparsification/UniformInK/Top/ArithNat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/ArithNat.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/ArithNat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The arithmetic of the exponent: natural numbers, for an arbitrary β

Inequalities between natural numbers in the arithmetic of the exponent, for an arbitrary natural
number β: 2 ≤ 2^β for β ≥ 1, and lower bounds on `WofU β K`.
The last statement, `stBetaU`, says that, for k ≥ 1, β = `betaU k s` has k ≤ β and β + 3 ≤ 2^β, and
that β + 1 ≤ 35·k·(s+1).
Notation as in proof/sparsification/UniformInK/Top/ArithDefs.lean. 

### `two_le_D`

 2 ≤ 2^β if 1 ≤ β. 

### `WofU_ge`

 Lower bounds on `WofU β K`: with b = β + 3, D = 2^β and Y = `K.size`, it is at least b·D, b²·Y,
b², b·Y, Y, b, D and 1. 

### `k_le_betaU`

 k ≤ `betaU k s`. 

### `b_le_DU`

 β + 3 ≤ 2^β for β = `betaU k s` and k ≥ 1. 

### `betaU_le_lin`

 β + 1 ≤ 35·k·(s+1) for β = `betaU k s` and k ≥ 1. 

### `stBetaU`

 What is used of β = `betaU k s`. 

---
{
  "module": "proof/sparsification/UniformInK/Top/FallBack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/FallBack.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/FallBack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Where k² exceeds a multiple of log n, k²·log₂ log₂(n+4)/(log₂(n+4))^α is bounded below, for α ≤ 1

`fallBack_rN_of`: `FallBack (SatK.rN 1 α)` for every α ≤ 1. Let ⌊log₂ n⌋ < B·k². Then L = log₂(n+4)
≤ ⌊log₂ n⌋ + 3 ≤ (B+4)·k². As log₂ L ≥ 1 and L^α ≤ L, the rate r(n) = log₂ L/L^α is at
least 1/L, so (B+4)·k²·r(n) ≥ 1. There the bound 2^{C·k²·n·r(n)} of the statement is at least 2ⁿ for
every C ≥ B + 4, and exhaustive counting is within it. 

### `logb_le`

 log₂(n+4) ≤ ⌊log₂ n⌋ + 3. 

### `inv_le_rN`

 The rate is at least 1/log₂(n+4). 

### `fallBack_rN_of`

 The rate log₂ log₂(n+4)/(log₂(n+4))^α, α ≤ 1, allows the fall-back to exhaustive counting. 

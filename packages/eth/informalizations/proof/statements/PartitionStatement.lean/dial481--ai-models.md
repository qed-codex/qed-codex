---
{
  "module": "proof/statements/PartitionStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PartitionStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PartitionStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Statements on the number of partitions (pure mathematics; definitions and statements only; imports Mathlib only) 

### `p`

 p(E), the number of partitions of E; p(0) = 1. 

### `cHR`

 π·√(2/3). 

### `kappa`

 κ = π·√(2/3)/ln 2. 

### `Bounds`

 κ·√E − B·log₂ E − C ≤ log₂ p(E) for E ≥ 1, and log₂ p(E) ≤ κ·√E + C for E ≥ 0. With B = 1 this
follows from the asymptotic formula of Hardy and Ramanujan. 

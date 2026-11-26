---
{
  "module": "proof/rates/ClauseBound/Part/Bounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Bounds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Bounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The two bounds on the number of partitions in logarithms to base 2

With κ = π·√(2/3)/ln 2 there are constants B and C with κ·√E − B·log₂ E − C ≤ log₂ p(E) for E ≥ 1
and log₂ p(E) ≤ κ·√E + C for all E.
Both follow by taking logarithms in p(E) ≤ exp(π·√(2E/3)) and in p(E) ≥ H·exp(π·√(2E/3))/E^B. The
asymptotic formula of Hardy and Ramanujan would give B = 1. 

### `logb_exp`

 log₂ e^x = x/ln 2. 

### `kappa_mul`

 κ·√E = π·√(2/3)·√E/ln 2. 

### `exists_bounds`

 There are B and C with κ·√E − B·log₂ E − C ≤ log₂ p(E) for E ≥ 1 and log₂ p(E) ≤ κ·√E + C for
all E. 

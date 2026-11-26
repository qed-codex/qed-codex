---
{
  "module": "proof/rates/ClauseBound/MainBoth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/MainBoth.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/MainBoth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Two rates of the bounds in n and in m are nonnegative

Two lemmas: the rate `SatK.rN 1 α n` = log₂ log₂(n+4)/(log₂(n+4))^α, of a bound in the number n of
variables, and the rate `SatM.rPow α m` = 1/(log₂(m+2))^α, of a bound in the number m of clauses,
are nonnegative for every real α. 

### `rN_nonneg`

 log₂ log₂(n+4)/(log₂(n+4))^α ≥ 0. 

### `rPow_nonneg`

 1/(log₂(m+2))^α ≥ 0. 

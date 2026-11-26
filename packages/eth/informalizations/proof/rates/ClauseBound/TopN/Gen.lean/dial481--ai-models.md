---
{
  "module": "proof/rates/ClauseBound/TopN/Gen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Gen.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Gen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Three elementary bounds on the logarithms of n + 4 and n + 2, for a natural number n

For every natural number n: 2 ≤ log₂(n+4), 1 ≤ log₂ log₂(n+4) and log₂(n+4) ≤ 2·log₂(n+2). 

### `two_le_log`

 2 ≤ log₂(n+4). 

### `one_le_loglog`

 1 ≤ log₂ log₂(n+4). 

### `log_four_le`

 log₂(n+4) ≤ 2·log₂(n+2). 

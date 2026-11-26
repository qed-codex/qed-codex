---
{
  "module": "proof/rates/ClauseBound/TopN/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Arithmetic for time bounds in the number n of variables

Inequalities of real arithmetic for bounds of the form C·2^(C·X) with X = n·r. `time_le'`: if L + 1
≤ a·2^(H·X) and E ≤ G·X, then q·(L + 2^E + 1)^q ≤ C·2^(C·X)
with C = q·(a+1)^q + q·(H + G). `log_le_mul`: if r ≥ 1/(c·(log₂(n+2))^c) with c ≥ 1 and n ≥ 1, then
log₂(n+2) ≤ c·D·(n·r) with D = 3·(c+1)!·2^(c+1). 

### `log_le_mul`

 log₂(n+2) ≤ c·D·(n·r), where D = 3·(c+1)!·2^(c+1), if r ≥ 1/(c·(log₂(n+2))^c) and n ≥ 1. 

### `time_le'`

 If L + 1 ≤ a·2^(H·X) and E ≤ G·X then q·(L + 2^E + 1)^q ≤ C·2^(C·X) with C = q·(a+1)^q + q·(H +
G). 

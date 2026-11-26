---
{
  "module": "proof/rates/ClauseBound/ParityChecks/MasterOL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/MasterOL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/MasterOL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A lower bound on the rate function (for the bound in n of Theorem A (c), second statement)

The rate function `SatK.rN 1 α n`, that is log₂ log₂(n+4)/(log₂(n+4))^α, is at least
1/(c·(log₂(n+2))^c) for α ≤ 1 and c ≥ 2 (`le_rN`).
With α = log₂(1/ρ) it is the rate of the bound in n of Theorem A (c) for a fixed k. 

### `le_rN`

 The function r is not too small: 1/(c·(log₂(n+2))^c) ≤ log₂ log₂(n+4)/(log₂(n+4))^α for α ≤ 1
and c ≥ 2. 

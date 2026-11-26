---
{
  "module": "proof/rates/ClauseBound/Inst/HalfEnd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfEnd.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfEnd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The parameter ρ = 1/√2 satisfies 1/2 ≤ ρ < 1

Theorem A of the paper turns pieces with parameters (ρ, c) (Definition 7, which asks for 1/2 ≤ ρ < 1)
into an algorithm for #k-SAT in time 2^{O(km/(log m)^α)} with α = log₂(1/ρ).
This file proves 1/2 ≤ 1/√2 and 1/√2 < 1, so that ρ = 1/√2, the ρ of Appendix B, meets this
condition. 

### `half_le`

 1/2 ≤ 1/√2. 

### `lt_one`

 1/√2 < 1. 

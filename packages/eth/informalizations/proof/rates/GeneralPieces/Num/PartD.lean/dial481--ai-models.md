---
{
  "module": "proof/rates/GeneralPieces/Num/PartD.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/PartD.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/PartD.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Part (d) of Theorem A

Part (d) says: one deterministic algorithm decides 3-SAT on n variables in time 2^{O(n/(log
n)^{α'/10})}, α' = log(1/ρ). Here it follows from a stronger theorem of this development, 3-SAT in
time
2^{O(n/(log n)^{3/19})} on one Turing machine, because α'/10 ≤ 1/10 ≤ 3/19. So it holds without any
pieces, and the route of the paper's proof (a sparsification that takes ε as an input, then part (c)
on every formula that it produces) is not followed. Besides part (d), the file proves 0 ≤ α' ≤ 1 for
1/2 ≤ ρ < 1, which gives α'/10 ≤ 1/10. 

### `alpha_mem`

 0 ≤ α' ≤ 1 for 1/2 ≤ ρ < 1, where α' = log(1/ρ). 

### `thmRunningTime_d`

 Part (d): one Turing machine decides 3-SAT on n variables within C·2^{C·n/(log₂(n+2))^{α'/10}}
steps. It is a consequence of the bound with the exponent 3/19, which is proved in this development
by another route and needs no pieces. 

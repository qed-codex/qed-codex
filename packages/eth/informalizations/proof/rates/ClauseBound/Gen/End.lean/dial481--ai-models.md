---
{
  "module": "proof/rates/ClauseBound/Gen/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Toward part (c) of Theorem A: the solver of the pieces is polynomial-time, and inequalities on the exponent

For part (c) of Theorem A (Appendix A), where pieces with parameters (ρ, c), given as
polynomial-time programs, give #k-SAT in time 2^{O(km/(log m)^{α'})}, α' = log₂(1/ρ), this file
proves: the solver
that a family of pieces gives is polynomial-time (`solverOf_poly`); 0 ≤ log₂(1/ρ) ≤ 1 for 1/2 ≤ ρ <
1; log₂(m+2) ≥ 1; and 1/(c·(log₂(m+2))^c) ≤ 1/(log₂(m+2))^α for 0 ≤ α ≤ 1 ≤ c. 

 ### The solver of the pieces is polynomial-time 

### `topK_eq`

 The number of nodes at the top of a schedule, without a case distinction on the list. 

### `topK_unary`

 The number of nodes at the top of a schedule is computed in unary. 

### `solverOf_poly`

 The solver that a family of pieces gives is polynomial-time, if the pieces are. 

 ### Inequalities on the exponent 

### `alpha_mem`

 0 ≤ log₂(1/ρ) ≤ 1 for 1/2 ≤ ρ < 1. 

### `one_le_log`

 log₂(m+2) ≥ 1. 

### `le_rPow`

 1/(c·(log₂(m+2))^c) ≤ 1/(log₂(m+2))^α for 0 ≤ α ≤ 1 ≤ c. 

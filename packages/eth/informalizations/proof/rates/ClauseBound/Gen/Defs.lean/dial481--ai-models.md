---
{
  "module": "proof/rates/ClauseBound/Gen/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The general recursion as a schedule: definitions and an interface statement

Square grids of side g_l = 2^{3l+x₀}·K_l, any pieces. The numbers K_l, g_l are those of
`LevelsStatement.lean`; the precision of the grouping at level l (Lemma 8) is D_l = 3·m·2^{l+4}, so
that
3·m/D_l = 2ζ_l. 

### `rep`

 n in unary. 

### `Par`

 Pieces as programs with parameters (ρ, c): the definition of the paper, with the running time
replaced by the exponent of the pad. 

### `step`

 The step from K_{l+1} = g_l² nodes to K_l nodes. 

### `sched`

 The steps from K_l nodes down to K₀ nodes. 

### `idx`

 The index of level l. 

 ### Pick.lean 

### `StPick`

 From a bound in unary: the largest l with K_l ≤ bound, and its index, in polynomial time. 

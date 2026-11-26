---
{
  "module": "proof/rates/ClauseBound/Gen/Seq.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Seq.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Seq.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The general recursion: K_l nodes at the index of level l, and K_l ≥ 2

This file holds two facts on the levels of the general recursion of Theorem A of the paper, stated
with the definitions of
`proof/rates/ClauseBound/Gen/Defs.lean` and `proof/rates/ClauseBound/Alg/Interfaces.lean`: the index
of level l is the schedule of the steps from K_l nodes down to K₀ nodes, so the solver has K_l nodes
at that index; and K_l ≥ 2 for x₀ ≥ 18.
The facts on K_l of part (a) of Theorem A are in `proof/rates/ClauseBound/Gen/PartA.lean`. 

### `topK_idx`

 The solver has K_l nodes at the index of level l. 

### `two_le_K`

 K_l ≥ 2. 

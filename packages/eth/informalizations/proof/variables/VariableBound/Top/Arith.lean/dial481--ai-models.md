---
{
  "module": "proof/variables/VariableBound/Top/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent of the pad: the statement `StArithD`

The proofs of the interface statements of proof/variables/VariableBound/Top/ArithDefs.lean are put
together, with those of proof/sparsification/UniformInK/Top/ArithDefs.lean that do not involve the
bounds of Step 3.
The bounds of Step 3, displays (68) and (69), enter as the hypothesis `Net.StBounds`. 

### `stArithD`

 Steps 4 and 5, the exponent: if the bounds of Step 3 hold (`Net.StBounds`), then for a
polynomial-time solver with a sequence of levels and 2^(−s(l)) ≤ e_l, 2^(s(l)) ≤ (2/e_l)^C there are
A and B, depending on neither k nor n:
for k ≥ 1 and n ≥ K^17 (K the number of nodes of the first level), with l the level picked for n and
s = s(l), the exponent of the plan, or n if there is none, is at most A·k²·n·e_l·(s+1), or ⌊log₂ n⌋
< B·k². 

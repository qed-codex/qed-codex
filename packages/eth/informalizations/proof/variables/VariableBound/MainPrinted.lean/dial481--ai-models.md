---
{
  "module": "proof/variables/VariableBound/MainPrinted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/MainPrinted.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/MainPrinted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemmas for the bound in n of Appendix D with Steps 1 to 4 as printed

This file holds lemmas of the Lean proof of the bound in n of Appendix D in which each sparse
formula is counted by Steps 1 to 4 as printed.
* `certCountDc`: the count of one sparse formula is polynomial-time in the pad.
* `expBDc`: the exponent `eBD` is at most `eD` and, if all variables occur and there is a clause, at
  most the exponent of the algorithm for the bound in m.
* `arithDc`: Steps 4 and 5, a bound on the exponent of a plan. 

### `certCountDc`

 The count of one sparse formula is polynomial-time in the pad, jointly in the width. 

### `expBDc`

 For k ≥ 1 and a k-CNF: the exponent `eBD` is at most `eD`, and, if all variables occur and there
is a clause, at most the exponent of the algorithm for the bound in m. 

### `arithDc`

 Steps 4 and 5: the exponent of a plan, or n if there is none, is at most A·k²·n·e_l·(s+1), or
⌊log₂ n⌋ < B·k²; under the hypotheses on the solver and on s(l) listed at `StArithD`. 

---
{
  "module": "proof/variables/VariableBound/Top/ArithPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithPlan.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent of a plan

Two interface statements are proved. `StPlanLeD`: the exponent of a plan, or else n, is at most n.
`StPlanNeedD`: it is at most `needD` if the three tests of the plan are passed and the solver is
polynomial-time.
The first bound needs nothing of the solver. The second uses that the solver's bounded computation
of its exponent gives the exponent, and gives a value whenever the
exponent is at most the bound n. 

### `stPlanLeD`

 The exponent of a plan, or else n, is at most n. 

### `stPlanNeedD`

 The exponent of a plan, or else n, is at most `needD` if the three tests are passed and the
solver is polynomial-time. 

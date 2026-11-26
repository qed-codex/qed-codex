---
{
  "module": "proof/variables/FixedWidthSteps/Hypothesis.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Hypothesis.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Hypothesis.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «Its hypothesis holds by (a) and (b)»

The levels of the recursion are the premise `PairsToBound.TheRecursionHasLevels`. What is added here
is the clause on the number of the proviso: by the last clause of `ChainOfInequalities`, a number
between 0.85ρ^ℓ and ρ^ℓ lies in [e_ℓ, 2e_ℓ]. 

### `hypothesisHoldsFrom`

 That the hypothesis holds, from the levels of the recursion and the chain of inequalities. 

---
{
  "module": "proof/variables/FixedWidthSteps/Small.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Small.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Small.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Finitely many n

For n ≥ 4 the exponent n·log log n/(log n)^α is positive, so every number is below 2^{C·n·log log
n/(log n)^α} for some C; for finitely many n take the largest of these C. 

### `lg_facts`

 For n ≥ 4: log n ≥ 2 and log log n ≥ 1. 

### `expVariables_pos`

 For n ≥ 4 the exponent is positive. 

### `timeVariables_mono`

 The bound grows with C. 

### `timeVariables_le`

 The bound is at most the power that it rounds down. 

### `exists_le_timeVariables`

 For one n ≥ 4, every number is within the bound for some C. 

### `smallCasesAreWithinTheBound`

 For fixed k and finitely many n, trying all assignments is within the bound. 

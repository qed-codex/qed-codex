---
{
  "module": "proof/machines/StepMachines/Math/SparsifyCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SparsifyCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SparsifyCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 A real-number estimate on a partial sum of binomial coefficients, proved with the binomial
theorem and `x + 1 ≤ exp x`:
for `0 < x ≤ 1` and `r ≤ D`, `x ^ r * ∑_{j ≤ r} C(D, j) ≤ exp (D * x)`. 

### `pow_mul_sum_choose_le_exp`

 For `0 < x ≤ 1` and `r ≤ D`: `x ^ r * ∑_{j ≤ r} C(D, j) ≤ exp (D * x)`. 

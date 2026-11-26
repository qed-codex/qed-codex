---
{
  "module": "proof/rates/ClauseBound/Rec/Few.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Few.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Few.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A partial sum of binomial coefficients

Two bounds on a partial sum of binomial coefficients. For 0 ≤ y ≤ 1 and n ≤ δ, y^n·Σ_{ν≤n} C(δ, ν) ≤
(1 + y)^δ (`pow_mul_sum_choose_le`); hence, for 1 ≤ n ≤ δ and y = n/δ,
Σ_{ν≤n} C(δ, ν) ≤ y^(−n)·(1 + y)^δ ≤ y^(−n)·exp(n) ≤ (3δ/n)^n (`sum_choose_le`). 

### `pow_mul_sum_choose_le`

 For 0 ≤ y ≤ 1: y^n·Σ_{ν≤n} C(δ, ν) ≤ (1 + y)^δ, provided n ≤ δ. 

### `sum_choose_le`

 For 1 ≤ n ≤ δ: Σ_{ν≤n} C(δ, ν) ≤ (3δ/n)^n. 

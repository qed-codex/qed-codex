---
{
  "module": "proof/rates/PaddedDescent/F/ArithTop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithTop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithTop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers at the top of the descent

A network on g nodes with at most Ub shared bits in all and size P is rebalanced to an instance on K
nodes. This file bounds from above the label length `lamG` of that
instance and the exponents of the enumerations which the rebalancing makes, as inequalities between
natural numbers. No programs occur here. 

### `lamG_mul_le`

 K³·lamG ≤ K³ + K·Ub + g·P. 

### `four_sq_mul_lamG_le`

 With Q = K²·lamG: 4·Q ≤ 4·K² + 4·Ub + X, if 4·g·P ≤ K·X. 

### `mul_div_le`

 The states of a class at the top: the exponent is at most X. 

### `size_le`

 The labels inside a class at the top: the exponent is at most X. 

### `mul_lamG_le`

 The index of a table at the top: the exponent is at most K + 2·X + r, if Ub ≤ K·X + r. 

### `inv_top_aux`

 The arithmetic of `inv_top` with plain variables (A = 8963^t, B = 10000^t, q = K²·lamG, v =
u·2^s·X). 

### `inv_top`

 The bound 8963^t·(K²·lamG) ≤ 10000^t·X + 8963^t·Z for the instance at the top of the descent: if
Ub ≤ u·n + r, n ≤ 2^s·X and t levels make up for the factor 2·u·2^s. 

---
{
  "module": "proof/sparsification/SparsificationLemma/Cal/Real.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Real.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Real.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Two inequalities between real numbers

This file proves `StSqrt` and `StYLe`.
`StSqrt`: log₂ x + 1 + 16/x ≤ √x for x ≥ 128. With s = √x ≥ 11 the tangent of the logarithm at 16
gives ln s ≤ 4·ln 2 + s/16 − 1, so ln x = 2·ln s ≤ 8·ln 2 + s/8 − 2, and this is at most
(s − 9/8)·ln 2 because ln 2 > 0.693. Finally 16/x ≤ 1/8.
`StYLe`: y ≤ ε for y = 32(k−1)²·log₂(32α)/(32α). With X = 32(k−1)²/ε and t = 32α we have y =
ε·X·log₂ t/t. The function ln t/t decreases for t ≥ e, so it is enough to look at t₀ = 2X·log₂ X,
where t₀ ≤ X² gives
ln t₀/t₀ ≤ 2·ln X/(2X·log₂ X) = ln 2/X. 

### `logb_le_sqrt_sub`

 log₂ x ≤ √x − 9/8 for x ≥ 128. 

### `stSqrt`

 log₂ x + 1 + 16/x ≤ √x for x ≥ 128. 

### `seven_le_logb`

 7 ≤ log₂ x for x ≥ 128. 

### `two_logb_le`

 2·log₂ x ≤ x for x ≥ 128. 

### `mul_logb_div_le`

 ε·X·log₂ t/t ≤ ε for X ≥ 128 and t ≥ 2X·log₂ X. 

### `stYLe`

 y ≤ ε whenever 32α ≥ 2x·log₂ x and x = 32(k−1)²/ε ≥ 128. 

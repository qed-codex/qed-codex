---
{
  "module": "proof/sparsification/SparsificationLemma/Cal/Alpha.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Alpha.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Alpha.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers x = 32(k−1)²/ε and α = ⌈2(k−1)²·ε⁻¹·⌈log₂ x⌉⌉

This file proves `StAlpha`, `StAlphaLe` and `StDegLe`, and that `logC` is ⌈log₂ x⌉.
For a rational x ≥ 1 the least natural number m with ⌈x⌉ ≤ 2^m is ⌈log₂ x⌉, because x ≤ 2^m, ⌈x⌉ ≤
2^m and log₂ x ≤ m say the same.
`StAlpha`: 2(k−1)²/ε = x/16, so x·⌈log₂ x⌉/16 ≤ α < x·⌈log₂ x⌉/16 + 1; and x ≥ 128 gives ⌈log₂ x⌉ ≥ 7.
`StAlphaLe`: the chain 32α ≤ 2x·⌈log₂ x⌉ + 32 ≤ 2·x^(3/2) ≤ 363·k³·ε^(−3/2) ≤ (8k/ε)³, in three
theorems: `alphaC_le_sqrt` has the first two links, `sqrt_xC_le` the third, `div_sqrt_le_cube` the
last. The second link is 2x·(log₂ x + 1 + 16/x) ≤ 2x·√x, by `StSqrt`.
We write x·√x for x^(3/2) and ε·√ε for ε^(3/2).
`StDegLe`: 2 + 4α·(32α)^(k−2) ≤ (32α)^(k−1) ≤ ((8k/ε)³)^(k−1) ≤ (8k/ε)^(3k). 

### `logb_le_clog`

 For a rational x > 0: log₂ x ≤ `Nat.clog 2 ⌈x⌉₊`. 

### `clog_lt_logb_add_one`

 For a rational x ≥ 1: `Nat.clog 2 ⌈x⌉₊` < log₂ x + 1. 

### `clog_eq_ceil_logb`

 For a rational x ≥ 1: `Nat.clog 2 ⌈x⌉₊` = ⌈log₂ x⌉. 

### `le_xC_of_two_le`

 x ≥ 32 for k ≥ 2 and ε ∈ (0,1]. 

### `le_xC`

 x ≥ 128 for k ≥ 3 and ε ∈ (0,1]. 

### `stLogC`

 `logC` is ⌈log₂ x⌉, for k ≥ 2 and ε ∈ (0,1]. 

### `stAlpha`

 What the sparsification uses of x and α: x ≥ 128, α ≥ 2, α ≥ k², 32α ≥ 2x·log₂ x, 32α ≤ 2x·⌈log₂
x⌉ + 32. 

### `xC_cast`

 x as a real number. 

### `alphaC_le_sqrt`

 32α ≤ 2x·⌈log₂ x⌉ + 32 ≤ 2·x^(3/2), written 2·x·√x. 

### `sqrt_xC_le`

 2·x^(3/2) ≤ 363·k³·ε^(−3/2), written with x·√x and ε·√ε. It holds because √32 ≤ 5.66 and
2·32·5.66 ≤ 363. 

### `div_sqrt_le_cube`

 363·k³·ε^(−3/2) ≤ (8k/ε)³ for ε ∈ (0,1], because ε³ ≤ ε·√ε and 363 ≤ 512. 

### `stAlphaLe`

 32α ≤ (8k/ε)³, for k ≥ 3 and ε ∈ (0,1]. 

### `stDegLe`

 2 + 4α·(32α)^(k−2) ≤ (8k/ε)^(3k), for k ≥ 3 and ε ∈ (0,1]. 

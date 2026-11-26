---
{
  "module": "proof/rates/ClauseBound/TopN/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Arithmetic lemmas in natural numbers: the seventeenth root, β, W and λ

Notation: K the number of nodes, Y = `K.size` the number of binary digits of K, s the precision, β =
`betaN k s`, b = β + 3, D = 2^β, W = `Wof k K s` = b²·D·Y.
* `root17_spec`: the integer part of the seventeenth root; `eq_replicate`: lists of units. `b_le_D`,
  `b_le_lin`, `k_le_beta`: bounds on β, among them b ≤ c_k·(s+1). `pow_le_n`: K^j ≤ n for j ≤ 17.
* `Wof_ge`: W dominates b·D, b²·Y, b², b·Y, Y, b, D and 1. `succ_le_two_pow`, `size_n_le`: if n <
  K^(17·C₀), then n has at most 17·C₀·Y binary digits.
* `two_g_div`, `lamS_mul_le`, `one_le_lamS`: 2g/K = 6K⁷ for g = 3K⁸, and bounds on the label length
  λ of the rebalanced instance. 

 ### The seventeenth root, and lists of units 

### `root17_spec`

 The length of `root17 m` is the integer part of the seventeenth root of m. 

### `eq_replicate`

 A list of units is determined by its length. 

 ### Natural numbers 

### `b_le_D`

 β + 3 ≤ 2^β. 

### `b_le_lin`

 β + 3 ≤ c_k·(s+1). 

### `k_le_beta`

 k ≤ β. 

### `pow_le_n`

 Powers of K up to the seventeenth are at most n. 

### `two_g_div`

 2g/K = 6K⁷. 

### `lamS_mul_le`

 K²·λ·K ≤ K³ + K·Ub + g·P for the label length λ of the rebalanced instance. 

### `one_le_lamS`

 1 ≤ λ. 

 ### The number W, and the binary digits of n 

### `Wof`

 W = b²·D·Y. 

### `Wof_ge`

 What is used of W: it dominates b·D, b²·Y, b·Y and 1. 

### `succ_le_two_pow`

 n + 1 ≤ 2^(17·C₀·Y). 

### `size_n_le`

 The number of binary digits of n is at most 17·C₀·Y. 

---
{
  "module": "proof/rates/ClauseBound/Alg/TopArith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/TopArith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/TopArith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Arithmetic for the exponent of the top level in m

A k-CNF with m clauses is turned into a network on g = 3K⁸ nodes and rebalanced to K nodes, where K =
K_l for the largest l with K_l⁹ ≤ m; then the clique solver
at level l is called. `needTop` is the exponent of a pad that suffices for all of this. This file
holds elementary inequalities on K and on the numbers of the top instance.

Among them:

* `root9 m` is the integer part of the ninth root of m (`root9_spec`);
* (log₂ K)ⁿ ≤ n!·2ⁿ·K (`logb_pow_le`), and the number of bits of K ≥ 2 is at most 2·log₂ K
  (`size_le_two_logb`);
* in natural numbers: g·P ≤ 5km, P·(2g/K + 1)·K ≤ 15km and K²·λ ≤ 8km for the numbers P and λ of the
  top instance (`g_mul_P_le`, `P_mul_le`, `sq_mul_lam_le`). 

 ### The ninth root 

### `lt_length_filter_iff`

 For a property that passes to smaller numbers, the number of b < n that have it is the first
number below n that does not have it. 

### `root9_spec`

 root9 m is the integer part of the ninth root of m. 

 ### Logarithms 

### `logb_le_of_le_pow`

 log₂ x ≤ n if x ≤ 2ⁿ. 

### `le_logb_of_pow_le`

 n ≤ log₂ x if 2ⁿ ≤ x. 

### `size_le_two_logb`

 The number of bits of K ≥ 2 is at most 2·log₂ K. 

### `logb_pow_le`

 (log₂ K)ⁿ ≤ n!·2ⁿ·K. 

 ### The numbers of the top instance 

### `g_mul_P_le`

 g·P ≤ 5km. 

### `two_g_div`

 2g/K = 6K⁷. 

### `P_mul_le`

 P·(2g/K + 1)·K ≤ 15km. 

### `cube_le`

 K³ ≤ km. 

### `sq_mul_lam_le`

 K²·λ ≤ 8km. 

### `one_le_lam`

 λ ≥ 1. 

### `one_le_B`

 The bound for the entries of the top instance is at least 1. 

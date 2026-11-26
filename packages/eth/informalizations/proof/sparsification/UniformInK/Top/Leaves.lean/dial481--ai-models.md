---
{
  "module": "proof/sparsification/UniformInK/Top/Leaves.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Leaves.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Leaves.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The number of leaves of the tree with the thresholds `thetaU τ`

`stLeavesU : StLeavesU`: for τ = 2^(4s+17), k ≥ 1 and s ≥ `s0U k`, the sum Σ_{j ≤ kn/τ} C(τ^(2k)·n,
j) is at most 2^(⌊n/2^s⌋+1). The estimate of the sum is
`WidthK.Thresholds.sum_choose_le_two_rpow`, which holds for every number L ≥ k in place of τ^(2k).
What is proved here is its hypothesis (k/τ)·log₂(e·τ·τ^(2k)) ≤ 1/2^s, which needs only k ≥ 1 and k²
≤ 2^s.
It is the analogue of `tauOf_works` in proof/rates/PaddedDescent/Choice.lean and of
`sum_choose_le_two_pow` in proof/rates/PaddedDescent/F/ArithWalk.lean. 

### `sq_le_of_s0U_le`

 k² ≤ 2^s for s ≥ s0U k. 

### `bsumU_tauOf`

 bsumU τ k = 2^(betaU k s) for τ = 2^(4s+17). 

### `three_mul_le`

 3·τ·bsumU τ k ≤ 2^(betaU k s + 4s + 19). 

### `mul_exponent_le`

 k·(betaU k s + 4s + 19)·2^s ≤ τ, if 1 ≤ k and k² ≤ 2^s: the left side is at most 4k²·(4s+17)·2^s
≤ 68·2^(3s). 

### `tauOf_worksU`

 (k/τ)·log₂(e·τ·bsumU τ k) ≤ 1/2^s for τ = 2^(4s+17), 1 ≤ k and s ≥ s0U k. 

### `le_bsumU`

 k ≤ bsumU τ k for τ = 2^(4s+17). 

### `stLeavesU`

 Σ_{j ≤ kn/τ} C(bsumU τ k · n, j) ≤ 2^(⌊n/2^s⌋+1) for τ = 2^(4s+17), k ≥ 1 and s ≥ s0U k. 

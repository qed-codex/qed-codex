---
{
  "module": "proof/sparsification/SparsifyWidthK/Thresholds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Thresholds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Thresholds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The thresholds of the sparsification of a k-CNF, and the number of leaves of its tree

The thresholds θ i and the bounds β i are defined in `SparsifyWidthK/Defs.lean` by one recursion
from a single number τ. This file proves the equations and
inequalities between them that the count of the steps of a path needs, the bound 2 + β 1 + … + β i ≤
τ^(2^(i+1)) for τ ≥ 4, the estimate
Σ_{j ≤ kn/τ} C(L·n, j) ≤ 2^(εn) for the number of leaves, and that for every k and every ε > 0 a
suitable τ exists. At the end these facts are given in
the form of the interface statements `StThr`, `StBetaSum`, `StLeafCount` and `StExistsTau` of
`SparsifyWidthK/Interfaces.lean`.
The estimate uses the lemma `pow_mul_sum_choose_le_exp` of `StepMachines/Math/SparsifyCount.lean`. 

 ### The defining equations

Below, θ i stands for `theta τ i`, β i for `beta τ i`, and `bsum τ i` is the sum 2 + β 1 + … + β i. 

### `theta_zero`

 θ 0 = 1. 

### `bsum_zero`

 The sum 2 + β 1 + … + β i is 2 for i = 0. 

### `theta_succ'`

 The recursion for θ as it is written in the definition. 

### `bsum_succ'`

 The recursion for the sum as it is written in the definition. 

### `beta_zero`

 β 0 = 0. 

### `beta_succ`

 β (i+1) = 2 · θ i · (2 + β 1 + … + β i). 

### `theta_succ`

 θ (i+1) = τ · β (i+1). 

### `bsum_succ`

 Each step of the recursion adds β (i+1) to the sum. 

### `bsum_eq`

 `bsum τ i` is indeed 2 + β 0 + β 1 + … + β i (and β 0 = 0). 

 ### Inequalities between the thresholds 

### `two_le_bsum`

 The sum is at least 2. 

### `one_le_theta`

 Every threshold is positive, if τ is. 

### `add_two_le_bsum`

 The sum grows by at least 1 with each step: i + 2 ≤ 2 + β 1 + … + β i. 

### `bsum_le`

 2 + β 1 + … + β i ≤ 2 · θ i. 

### `sq_mul_theta_le`

 τ² · θ i ≤ τ^(2^(i+1)) for τ ≥ 4: by the previous lemma the quantity τ² · θ i is at most squared
in each step. 

### `bsum_le_pow`

 2 + β 1 + … + β i ≤ τ^(2^(i+1)) for τ ≥ 4. 

 ### The number of leaves 

### `sum_choose_le_two_rpow`

 If (k/τ)·log₂(e·τ·L) ≤ ε, with k ≤ L and 1 ≤ τ, then Σ_{j ≤ kn/τ} C(L·n, j) ≤ 2^(εn). 

### `exists_tau`

 For every k, every ε > 0 and every τ₀ there is a number τ ≥ τ₀, τ ≥ 4, with (k/τ)·log₂(e·τ·(2 +
β 1 + … + β k)) ≤ ε.
The proof takes τ = m² with m ≥ 4·k·(2^(k+1)+1)/ε and uses log m ≤ m − 1. 

 ### The four interface statements 

### `stThr`

 The thresholds θ and the bounds β have the three properties that the count of the steps of a
path uses. 

### `stBetaSum`

 β 0 + … + β (k-1) ≤ 2 + β 1 + … + β k. 

### `stLeafCount`

 The number of leaves of the tree is at most 2^(εn), if (k/τ)·log₂(e·τ·(2 + β 1 + … + β k)) ≤ ε. 

### `stExistsTau`

 For every k and every ε > 0 there are arbitrarily large τ with (k/τ)·log₂(e·τ·(2 + β 1 + … + β
k)) ≤ ε. 

---
{
  "module": "proof/variables/VariableBound/Top/ArithNeed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithNeed.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithNeed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Steps 4 and 5: the exponent of the pad is at most (140·k·35·k + `ccD k C₀`·A₁ + 1)·n·e·(s+1)

`stNeedD : StNeedD`, from the statements on natural numbers `StUbD`, `StArgD`, `StLowerD` and
`UniformInK.StBetaU`, which are hypotheses here. The estimate between real numbers
`real_coreM` of proof/rates/ClauseBound/ParityChecks/ArithOL.lean, which speaks of real numbers
only, is used as it is. In the words of Step 4: the exponent is at most the sum of the terms of the
paper's cost display in Step 4 and of the exponents for the
profiles, the list of checks and the walk (`needD_le_sum`); the main term is e·U, with
e·140·k·n·(β+1) ≤ 140·k·35·k·n·e·(s+1) because β + 1 ≤ 35·k·(s+1) (one network costs 2^(O(e·k·n·log
Δ)) operations, and
log Δ = O(k·log(k/e)) of Step 5); all other terms together are at most (`ccD k C₀`·A₁ + 1)·n·e, if W
≤ A₁·K·e, where `ccD k C₀` = `ccD 0 C₀` + 140·k. Where the paper says that all these terms are
o(en), the bound here is
weaker, O(k·e·n), because of the part (K − 1)·λ, which that display of the paper does not have. 

### `lowerDR`

 The inequalities of `StLowerD` for β = `betaU k s`, between real numbers; for 1 ≤ β, k ≤ β, 2 ≤
K and K^17 ≤ n < K^(17·C₀). 

### `needD_le_sum`

 The exponent is at most the sum of its parts, if 2^β ≤ n + 1. 

### `real_finalD`

 The last step between real numbers: from Z ≤ e·(140·k·n·b) + cA·(n·e), b ≤ ck·q, R₃ ≤ n·e and N
≤ Z + R₃ to N ≤ (140·k·ck + cA + 1)·n·e·q; for e, n, k, cA ≥ 0 and q ≥ 1. 

### `needD_le`

 Steps 4 and 5: the exponent `needD` is at most (140·k·35·k + `ccD k C₀`·A₁ + 1)·n·e·(s+1), if W
≤ A₁·K·e; for k ≥ 1, 2 ≤ K, K^17 ≤ n < K^(17·C₀), 2^β ≤ n + 1, 0 < e ≤ 1, 2^(−s) ≤ e and a solver
with the bound `hrate` on its cost. 

### `stNeedD`

 Steps 4 and 5: the exponent `needD` is at most (140·k·35·k + `ccD k C₀`·A₁ + 1)·n·e·(s+1), if W
≤ A₁·K·e, under the hypotheses listed at `StNeedD`; from the statements on natural numbers. 

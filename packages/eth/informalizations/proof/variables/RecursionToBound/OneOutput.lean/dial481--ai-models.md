---
{
  "module": "proof/variables/RecursionToBound/OneOutput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/OneOutput.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/OneOutput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a), with sparsification as in Step 5: the cost of one output (Step 4 of Appendix D)

«Hence the number of satisfying assignments of Φ is computed in time 2^{O(ekn·log Δ)}» (Step 4 of
Appendix D), for the exponent `needAt` of one output with its own Δ.

The arithmetic of proof/variables/VariableBound/Top is stated for Δ a power of two, 2^β, and its
parts of lower order ask k ≤ β. An output's own Δ is any number from 2 on. So two powers of two are
used. With β₁ = ⌈log₂ Δ⌉ the main term, e·U, is bounded by display (68) at 2^β₁ ≥ Δ
(`VariableBound.StUbD`): U ≤ 140·k·n·(β₁+1) + 18·K^16, and β₁ + 1 ≤ 3·log Δ.
With β = max(β₁, k) all other parts are bounded at 2^β ≥ Δ (`VariableBound.StLowerD`,
`VariableBound.StArgD`): «All these are o(en)». Both steps use that the bounds grow with Δ
(`boundsGrowWithDelta`). The exponent of the solver itself need not grow with the label length; what
grows is the bound of the hypothesis of Theorem D (a) on it (the field `rate` of the
sequence of levels), and only that is used. Last, W = (β+3)²·2^β·(number of binary digits of K) ≤
A₁·K·e (`UniformInK.StMasterU`), because (2^β)⁶ ≤ K for large n (`UniformInK.StSixU`): 2^β ≤ (⌊log₂
n⌋+1)^(4kC₀+1), and k² ≤ √(log n).

`real_core` has the statement and proof of the estimate between real numbers
`ClauseBound.ParityChecks.ArithOL.real_coreM`, which is not public in its module. 

 ### Between real numbers 

### `real_core`

 The estimate of the exponent, between real numbers: the parts T1, T2, T3, R1, Rx of lower order
and the exponent nd of the solver; M is the main part of the bound on the total. 

 ### The parts of the exponent grow with Δ 

### `lamS_mono`

 The bound on the label length grows with the bounds on the total and on P. 

### `bitsS_mono`

 The bound on the length of the entries grows with the bound on P. 

### `size_nPrMax_le`

 The number of binary digits of the number of profiles: at most g·g·2 times that of the number of
objects, plus 1, g = 3K⁸. 

### `needAt_le_sum`

 The exponent for one output with Δ ≤ D is at most the sum of its parts, all but the exponent of
the solver taken at D. 

 ### The exponent for one output 

### `needAt_le`

 Step 4 for one output. Let 2 ≤ K, K^17 ≤ n < K^(17·C₀), Δ ≤ 2^β₁ with 1 ≤ β₁ ≤ β, k ≤ β, β + 3 ≤
2^β ≤ n + 1, 0 < e ≤ 1, W = `WofU β K` ≤ A₁·K·e, and let the solver have the bound of the hypothesis
of Theorem D (a) at the index i. Then the exponent for one output with this Δ is at most
e·140·k·n·(β₁+1) + `ccD k C₀`·A₁·n·e. 

 ### For large n the hypotheses hold 

### `add_three_le_two_pow`

 β + 3 ≤ 2^β for β ≥ 3. 

### `six_test`

 If (520200·C₀⁴)² ≤ ℓ and k⁴ ≤ ℓ, then 2·(102·C₀·(4kC₀+1))² ≤ ℓ, for C₀, k ≥ 1, because the left
side is at most 520200·C₀⁴·k² ≤ ℓ. 

### `clog_facts`

 2^⌈log₂ Δ⌉ ≤ 2Δ, 1 ≤ ⌈log₂ Δ⌉ and ⌈log₂ Δ⌉ + 1 ≤ 3·log Δ, for Δ ≥ 2. 

### `oneOutputCost`

 «Hence the number of satisfying assignments of Φ is computed in time 2^{O(ekn·log Δ)}» (Step 4
of Appendix D): for large n, the level ℓ of n, 3 ≤ k ≤ (log n)^(1/4) and 2 ≤ Δ ≤ (log n)^(4kC₀) the
exponent for one output with this Δ is at most A·e_ℓ·k·n·log Δ. 

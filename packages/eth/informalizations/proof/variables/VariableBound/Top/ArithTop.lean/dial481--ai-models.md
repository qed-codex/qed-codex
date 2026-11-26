---
{
  "module": "proof/variables/VariableBound/Top/ArithTop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithTop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithTop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent of the pad is O(k²·e·n·(s+1)) unless k² is larger than a multiple of log n

`stArithD_of`: `StArithD` from the interface statements of
proof/variables/VariableBound/Top/ArithDefs.lean and
proof/sparsification/UniformInK/Top/ArithDefs.lean.
Let a = `aU C C₀`, B = `BkD C C₀` and suppose B·k² ≤ ⌊log₂ n⌋. Then D = 2^β ≤ (⌊log₂ n⌋ + 1)^(a·k),
hence D⁶ ≤ K ≤ n. So the second and the third test of the plan are passed, and W ≤ A₁·K·e with A₁ =
`A1U C₀`.
If the first test is passed too, the exponent is at most `needD`, which is at most (140·35·k² +
`ccD k C₀`·A₁ + 1)·n·e·(s+1), where `ccD k C₀` ≤ (`ccD 0 C₀` + 140)·k. If it fails, then 2^s < 4k²
and the exponent is n ≤ 4k²·n·e.
The condition B·k² ≤ ⌊log₂ n⌋ takes the place of «k ≤ (log n)^(1/4)» and «n large» of Steps 5 and 6,
and follows from them once log₂ n is large enough; D⁶ ≤ K takes the place of Δ ≤ n^(1/(40·C₀)) of
Step 4. 

### `const_le`

 For k ≥ 1, the constant of `StNeedD` is at most a constant times k². 

### `of_BkD`

 From B·k² ≤ ℓ with B = `BkD C C₀`: the condition 2·(102·C₀·c)² ≤ ℓ of `UniformInK.StSixU` for c =
a·k, a = `aU C C₀`. 

### `test3`

 The third test of the plan, 29·⌈log₂(2Δ)⌉ + 19 ≤ n for Δ = 2^β, is passed if β + 3 ≤ 2^β and
(2^β)⁶ ≤ n. 

### `planAtD_le`

 The statement at one level: for k ≥ 1, a polynomial-time solver with K ≥ 2 nodes at the index i
and the bound need(λ, B) ≤ e·K²·λ + C₀·K²·log₂(K·(λ+B)), K^17 ≤ n < K^(17·C₀), 2^(−s) ≤ e ≤ 1,
1/(log₂ K)^C₀ ≤ e,
2^s ≤ (2/e)^C and B·k² ≤ ⌊log₂ n⌋, the exponent of the plan, or else n, is at most A·k²·n·e·(s+1),
with A = `AexpD C₀` and B = `BkD C C₀`; from the interface statements. 

### `stArithD_of`

 Steps 4 and 5, the exponent: with A = `AexpD C₀`, B = `BkD C C₀`, for k ≥ 1 and n ≥ K^17 (K the
number of nodes of the first level), l the level picked for n and s = s(l), the exponent of the
plan, or n if there is none,
is at most A·k²·n·e_l·(s+1), or ⌊log₂ n⌋ < B·k²; for a polynomial-time solver with a sequence of
levels and 2^(−s(l)) ≤ e_l, 2^(s(l)) ≤ (2/e_l)^C; from the interface statements. 

---
{
  "module": "proof/variables/VariableBound/Top/ArithDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Steps 4 and 5, the arithmetic of the exponent: constants and interface statements

The counterpart of proof/sparsification/UniformInK/Top/ArithDefs.lean. Notation as there: K the
number of nodes at the level picked for n, so that K^17 ≤ n < K^(17·C₀); g = 3K⁸; Y the number of
binary digits of K; β a natural number, later
`betaU k s`; b = β + 3, Δ = D = 2^β, W = b²·D·Y (`UniformInK.WofU`). The exponent of the padding
string (the number of operations, written as a string of ones; Appendix E), `needD`, is Lean's form
of display (70) of Step 4, with the profiles, the lists of checks and the walk of Step 5 added. Its
main term is
e·U with U ≤ 140·k·n·(β+1) + 18·K^16. «All these are o(en)» becomes: every other part, multiplied by
K, is at most a number times W·n (`StLowerD`). That number depends on C₀ only, except for the part
(K − 1)·λ, which
display (70) does not have; there it is 19 + 140·k + G. And W ≤ A₁·K·e (`UniformInK.StMasterU`, used
as it is).
What differs from that file: U, P are the bounds `UbD`, `PbD` of Step 3, known through
`Net.StBounds`; the tables have B = `BbD k n` = 14(k+1)n + 1 bits, which enter only under the
logarithm (`StArgD`); the plan has three tests.
`UniformInK.StMasterU` and the constants `aU`, `A1U` do not involve the bounds U, P and B of Step 3,
and are used as they are.
This file has definitions only. The statements `St…` are propositions; one file proves each of them. 

 ### Constants 

### `GD`

 The constant in g·P ≤ G·W·n. 

### `ccD`

 The sum of the constants of the parts of lower order. 

### `BkD`

 The constant of the alternative ⌊log₂ n⌋ < B·k². 

### `AexpD`

 The constant A of the bound A·k²·n·e·(s+1). 

 ### Natural numbers, for an arbitrary β 

### `StUbD`

 Display (68) in closed form, for Δ = 2^β with β ≥ 1 and n ≥ 1: `UbD k K n (2^β)`, the right side
of (68) with the logarithms rounded up, is at most 140·k·n·(β+1) + 18·K^16. This is the printed
«O(kn log Δ) + 2g²» with the
constant 140 (⌈log₂(2Δ)⌉ = β + 1 and 2g² = 18·K^16). 

### `StArgD`

 Step 4, «the numbers L and B' are polynomial in n», for k ≤ β, β + 3 ≤ 2^β ≤ n + 1, 2 ≤ K and
K^17 ≤ n < K^(17·C₀): K·(λ + B') ≤ 2^(5·17·C₀·Y + 16), where λ = `lamS` and B' = `bitsS` are this
formalization's bounds for the label
length and the entry length of the rebalanced instance. They stand for the printed L and B': λ =
⌊(K³ + K·U + g·P)/K³⌋ ≥ L, and B' = 6K⁷·P + (6K⁸ + 36K¹⁵)·B in place of ⌈2gP/K⌉ + g²·B. 

### `StLowerD`

 Step 4, «all these are o(en)», first half, for 1 ≤ β, k ≤ β, 2 ≤ K and K^17 ≤ n < K^(17·C₀): the
parts of lower order of the exponent, each multiplied by K, are at most a number times W·n. The
number depends on C₀ only, except for
the part (K − 1)·λ, where it is 19 + 140·k + G (G = `GD C₀`); display (70) has no such part. 

 ### The exponent 

### `StNeedD`

 Steps 4 and 5: the exponent `needD` of the padding string is at most (140·k·35·k + `ccD k C₀`·A₁ + 1)·n·e·(s+1),
if W ≤ A₁·K·e; for k ≥ 1, 2 ≤ K, K^17 ≤ n < K^(17·C₀), 2^β ≤ n + 1, 0 < e ≤ 1, 2^(−s) ≤ e and a
solver with the bound of display (57). 

### `StPlanNeedD`

 The exponent of a plan, or else n, is at most `needD` if the three tests are passed and the
solver is polynomial-time. 

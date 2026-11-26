---
{
  "module": "proof/rates/CountedRecursion/CountStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CountStep.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CountStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The count of one level

Proof of Theorem A (b): «So the total number of operations is at most |𝓘|^{|ℛ|}((K^g +
𝒯·2^{2N/K}τ)Ξ^{(c+4)C₁} + 2Ξ^{C₃}) + (2|𝓘| + 2)2^{cλ} + Ξ^{C₃} ≤ Ξ^{cg⁴/4+g+C₄}·𝒯·2^{2N/K+cλ} ≤
2^{e_{ℓ+1}N}·Ξ^{cg⁴/2+g+K²+C₄+(c+5)C₀K²}.»
The two inequalities in real variables are `GeneralPieces.Count.count_first` and `count_second`.
Here the costs of `RecursionDefs.lean` are brought to the form of the left side (`own_le`):
a query to the pieces costs 2^{cΛ} + 2 and not 2^{cΛ}, a query to the tables t ≥ 1, and a call 2
more than the bound; these go into three more factors Ξ. The bound for 𝒯 is the premise
`BoundBelow`; e_j ≥ 0 is taken from part (a) of the theorem, the premise `Levels.Gen.PartA`. C₄ = 3C +
c + 7. 

### `own_le_aux`

 The costs of one level, in real variables, in the form of the printed sum; Y stands for Ξ^C and
Z for Ξ³. 

### `own_le`

 The same with the powers of Ξ. X = Ξ, s = 2^{2N/K}, u = 2^{cΛ}, a the number of functions ι : ℛ
→ 𝓘, κ = K^g, T the bound for the level below (the premise `BoundBelow`), t the price of a query to
the tables. 

### `countStepFrom`

 `CountStepFrom`, with C₄ = 3C + c + 7. 

### `countStep`

 `CountStep`. 

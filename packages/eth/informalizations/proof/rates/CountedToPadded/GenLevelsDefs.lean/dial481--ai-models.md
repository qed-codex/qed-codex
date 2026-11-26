---
{
  "module": "proof/rates/CountedToPadded/GenLevelsDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/GenLevelsDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/GenLevelsDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «K_ℓ … can be computed from ℓ in time polynomial in K_ℓ», for the numbers K_ℓ of Theorem A

Definitions and two statements; nothing is proved here. The hypothesis of Theorem D (a) asks that
K_ℓ can be computed from ℓ in time polynomial in K_ℓ (`CliqueLevels.ComputesLevels`: a
polynomial-time function that gets ℓ and a bound b in unary and returns K_ℓ in unary if K_ℓ ≤ b, and
nothing otherwise). For the numbers of display (40),
K₀ = 2^{x₀}, g_ℓ = 2^{3ℓ+x₀}K_ℓ, K_{ℓ+1} = g_ℓ², this file names such a function. It makes ℓ rounds
on the pair (2^{3j+x₀}, K_j), in binary, and gives up as soon as K_j would exceed b; since the K_j
increase, it gives up if and only if K_ℓ > b. 

### `roundUnder`

 One round under the bound b: (2^{3j+x₀}, K_j) becomes (8·2^{3j+x₀}, (2^{3j+x₀}K_j)²) if the new
K is at most b; else nothing. 

### `levelsUnder`

 From (ℓ, b) in unary: K_ℓ in unary if K_ℓ ≤ b, else nothing. 

### `LevelsAreComputed`

 The numbers K_ℓ of display (40) are computed from ℓ in time polynomial in K_ℓ, by
`levelsUnder x₀`. 

### `SolvesGrowsWithTheConstant`

 `Solves` and `SolvesInFactor` only weaken when the constant C₀ grows (for K_ℓ ≥ 1). 

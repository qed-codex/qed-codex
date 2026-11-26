---
{
  "module": "proof/rates/CountedToPadded/GenLevels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/GenLevels.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/GenLevels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers K_ℓ of Theorem A are computed from ℓ in time polynomial in K_ℓ

* `fold_eq`: after ℓ rounds under the bound b the state is (2^{3ℓ+x₀}, K_ℓ) if K_ℓ ≤ b, and nothing
  otherwise. The K_ℓ do not decrease (`K_le_succ`), so a search that has given up stays right.
* `fold_le`: on every input the second number of the state is at most b, so it can be written in
  unary.
* `len_roundUnder_le`: a round makes the word of the state longer by at most 3b + 16 symbols, and b
  is at most the length of the input: the first number is multiplied by 8, the second is at most b.
* `levelsAreComputed`: the two together. `solvesGrowsWithTheConstant`: the bounds of `Solves` and
  `SolvesInFactor` grow with C₀. 

 ## What the program returns 

### `K_pos`

 K_ℓ ≥ 1. 

### `K_le_succ`

 K_ℓ ≤ K_{ℓ+1}. 

### `fold_eq`

 The state after ℓ rounds. 

### `roundUnder_le`

 After a round the second number is at most b. 

### `fold_le`

 On every input the second number of the state is at most b. 

 ## Polynomial time 

### `len_roundUnder_le`

 A round makes the word of the state longer by at most 3b + 16. 

### `fold_polyT`

 The rounds are computed in polynomial time. 

 ## The constant may grow 

### `factor_mono`

 The polynomial factor grows with the constant. 

### `bound_mono`

 The bound grows with the constant. 

### `levelsAreComputed`

 The numbers K_ℓ of Theorem A (K_0 = 2^{x₀}, K_{ℓ+1} = (2^{3ℓ+x₀} K_ℓ)^2) are computed from ℓ in
time polynomial in K_ℓ, by `levelsUnder x₀`. 

### `solvesGrowsWithTheConstant`

 `Solves` and `SolvesInFactor` only weaken when the constant C₀ grows. 

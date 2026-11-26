---
{
  "module": "proof/statements/LevelsStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/LevelsStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/LevelsStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The schedule of levels of Theorem A and part (a) of Theorem A (pure mathematics; definitions and statements only; imports Mathlib only) 

 ## The general recursion: K₀ = 2^{x₀}, e₀ = 1/2, ζ_ℓ = 2^{−ℓ−5}, g_ℓ = 2^{3ℓ+x₀}·K_ℓ, K_{ℓ+1} = g_ℓ², e_{ℓ+1} = (ρ + 3ζ_ℓ)·e_ℓ + 3/K_ℓ 

### `K`

 K_ℓ. 

### `g`

 g_ℓ. 

### `zeta`

 ζ_ℓ. 

### `e`

 e_ℓ. 

### `PartA`

 Part (a) of Theorem A, on the general recursion. 

### `PartA.case_ii`

 the condition of case (ii) of Lemma 8 at every level 

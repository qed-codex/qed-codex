---
{
  "module": "proof/networks/Eight/SecPseudocode_Levels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecPseudocode_Levels.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecPseudocode_Levels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The section «The algorithm in pseudocode» with ρ = 11/12: the upper estimate of the numbers e_ℓ and their limit

The counterpart of proof/networks/SingleBitPieces/SecPseudocode_Levels.lean for ρ = 11/12. The file
is named after that counterpart; in the paper this is Section 8. `Eight.Level.levelE`
(proof/networks/Eight/Level/Defs.lean) is e_ℓ of the display of Section 8, e₀ = 1/2, e_{ℓ+1} = (ρ +
2/K_ℓ)·e_ℓ + 2/K_ℓ, with ρ = 11/12 (`Eight.rho`); K_ℓ is `Paper.levelK`.
This file proves e_ℓ ≥ 0 (`levelE_nonneg`), the upper estimate e_ℓ ≤ 0.56·ρ^ℓ of Section 8
(`levelE_le`), e_ℓ → 0 (`levelE_tendsto`), and the form in which the limit is used (`exists_level`).
That (K_ℓ, e_ℓ) is achievable is not proved here.
The upper estimate is proved in the sharper form e_ℓ ≤ 0.56·ρ^ℓ − 3.8/K_ℓ, which goes through the
induction because ρ ≥ 7/8 and K_{ℓ+1} ≥ 19·K_ℓ.
From proof/networks/SingleBitPieces/SecPseudocode_Levels.lean only facts on K_ℓ are used, among them
`SingleBitPieces.SecPseudocode_Levels.levelK_pos` and `levelK_succ_ge`; they do not mention ρ. 

### `rho_pos`

 ρ = 11/12 is positive. 

### `rho_lt_one`

 ρ = 11/12 < 1. 

### `rho_ge`

 ρ = 11/12 ≥ 7/8. 

### `levelE_nonneg`

 e_ℓ is not negative. 

### `levelE_le_sub`

 The sharper form of the upper estimate: e_ℓ ≤ 0.56·ρ^ℓ − 3.8/K_ℓ. Not a sentence of the paper. 

### `levelE_le`

 Section 8: «precisely, unrolling … gives ½ρ^ℓ ≤ e_ℓ ≤ 0.56 ρ^ℓ», the second inequality, with ρ =
11/12. Same as in the paper. 

### `levelE_tendsto`

 Section 8: «e_ℓ → 0». Same as in the paper. 

### `exists_level`

 The form in which «e_ℓ → 0» is used for Theorem 2: for every η > 0 and every K₀ there is a level
ℓ with K_ℓ ≥ K₀ and e_ℓ ≤ η. Not a sentence of the paper; it follows from the limit and from ℓ <
K_ℓ. 

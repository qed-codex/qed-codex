---
{
  "module": "proof/threesat/Exits/Level.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Level.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Level.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proposition 3, «Hence e* = 0», and the levels of Section 8, on the algorithm for networks of this folder

Proposition 3: «If (K, e) is achievable and g = 3K⁸, then (g², e') is achievable for e' = (ρ + 2/K)e +
2/K. Hence e* = 0.» Section 8: «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every
ℓ, …».
This file proves four implications of proof/threesat/Exits/AlgDefs.lean, each from its hypotheses.
* `stLevelUpOf`: Proposition 3, first sentence, for the named algorithm `levelUp K E`, from Lemma 1
  for `Exits.netAlg` and its polynomial-time steps. What one level does with an algorithm for
  networks is generic in that algorithm: `Eight.ViaGrouping.levelAlgP_gridPsi_correct`,
  `levelAlgP_gridPsi_keeps` (proof/networks/Eight/ViaGrouping/LevelEnd.lean).
* `stLevelAchievableOf`: the first sentence as printed, from the form for the named algorithm.
* `stEStarOf`: «Hence e* = 0», by the last paragraph of the printed proof (`Eight.eStar_eq_zero_of`,
  proof/networks/Eight/SecLevel_EStar.lean).
* `stCliqueOf`: Clique(ℓ) has polynomial-time steps and meets the bound of «achievable» for (K_ℓ,
  e_ℓ): level 0 is brute force, and the step from ℓ to ℓ + 1 is the hypothesis at K = K_ℓ, e = e_ℓ. 

### `two_le_levelK`

 K_ℓ ≥ 2 (Section 8: «K₀ = 64 … K_{ℓ+1} = g_ℓ² = 9K_ℓ¹⁶»). 

### `zero_lt_levelG`

 g_ℓ ≥ 1 (Section 8: «g_ℓ = 3K_ℓ⁸»). 

### `stLevelUpOf`

 **Proposition 3, first sentence, for the named algorithm**: «If (K, e) is achievable and g =
3K⁸, then (g², e') is achievable for e' = (ρ + 2/K)e + 2/K.» From Lemma 1 for the algorithm of its
proof: «Apply Lemma 1 to the network with the smaller total.» g² is written 9K¹⁶. 

### `stLevelAchievableOf`

 **Proposition 3, first sentence**: «If (K, e) is achievable and g = 3K⁸, then (g², e') is
achievable for e' = (ρ + 2/K)e + 2/K.» From the form for the named algorithm. 

### `stEStarOf`

 **Proposition 3, second sentence**: «Hence e* = 0.» From the first sentence, by the last
paragraph of the printed proof. 

### `stCliqueOf`

 **Section 8**: «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every ℓ, …», for
Clique(ℓ). 

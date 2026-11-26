---
{
  "module": "proof/threesat/Printed/LevelSentences.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelSentences.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelSentences.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proposition 3 from the printed Definition 4

Proposition 3: «If (K, e) is achievable and g = 3K⁸, then (g², e') is achievable for e' = (ρ + 2/K)e +
2/K. Hence e* = 0.» «Achievable» is `Printed.Achievable`: a table query costs one operation.
The first sentence is `StLevelTied` (the bound, for the algorithm of the proof) together with
`StLevelPoly` (polynomial-time steps). The second sentence follows the last paragraph of the printed
proof sentence by sentence, as proof/networks/Eight/SecLevel_EStar.lean does for «achievable» as
defined in the namespace `Paper`.
Then Section 8: «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every ℓ», by
Clique(ℓ). The statements about the algorithm (`StLevelTied`, `StLevelPoly`, `StBrute`) are
hypotheses of the theorems `…_of` here; the facts on e* and «if (K, e) is achievable, so is (K, e₁)
for every e₁ ≥ e» are those of proof/threesat/Printed/Achievable.lean. 

### `levelProposition_of`

 **Proposition 3**, first sentence, from the two statements about the algorithm of its proof. 

### `eStar_le_of`

 «Let e > e*; then (K, e) is achievable for infinitely many K. Let e'' > ρe. For all large K we
have (ρ + 2/K)e + 2/K ≤ e'', so (9K¹⁶, e'') is achievable for infinitely many K, and therefore e* ≤
e''.» «Large» is K ≥ (2e + 2)/(e'' − ρe); 9K¹⁶ is written (3K⁸)². 

### `eStar_le_rho_mul_of`

 «Letting e'' → ρe and e → e* gives e* ≤ ρe*.» Here: for every η > 0, take e = e* + η/2 and e'' =
ρe + η/2, which is at most ρe* + η. 

### `eStarZero_of`

 **Proposition 3**, second sentence: e* = 0. «Since 0 ≤ e* ≤ 1/2 and ρ < 1, e* = 0.» (e* ≤ 1/2 is
not needed.) 

### `stEveryEta_of`

 The last sentence of the proof of Proposition 3: «That is, for every η > 0, (K, η) is achievable
for infinitely many K.» 

### `stClique_of`

 **Section 8: «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every ℓ»**, by
Clique(ℓ). 

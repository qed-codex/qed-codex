---
{
  "module": "proof/threesat/Printed/LevelFrom.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelFrom.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelFrom.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proposition 3 for `Printed.Achievable` (Definition 4 with a bound on the sizes of the states), with the hypotheses filled in

The files LevelNetworks, LevelCost, LevelPoly and LevelSentences of this folder take what other
files prove as hypotheses. Here these are filled in: the coding of the tables
(proof/threesat/Printed/Coding.lean), brute force and the facts on e* (Achievable.lean), Lemma 1 for
networks given by procedures (GroupingProcs.lean), polynomial-time steps of the machine of Lemma 1
(GroupingPoly.lean).
Lemma 1 for the algorithm of its proof (`StGroupingTied`) is the one hypothesis that is left in the
theorems `…_from`. 

### `stBothNetworks`

 **«Both networks satisfy Definition 2 with P = g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the
role of B, and with τ = poly(B + λ)».** 

### `stLevelPoly`

 The machine of Proposition 3 has polynomial-time steps, because the machine of Lemma 1 has
(`stGroupingPoly`). 

### `stLevelTied_from`

 Proposition 3, first sentence, for the algorithm of its proof, from Lemma 1 for the algorithm of
its proof. 

### `levelProposition_from`

 Proposition 3, first sentence. 

### `eStarZero_from`

 Proposition 3, second sentence. 

### `stEveryEta_from`

 «For every η > 0, (K, η) is achievable for infinitely many K.» 

### `stClique_from`

 «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every ℓ», by Clique(ℓ). 

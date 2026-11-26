---
{
  "module": "proof/maintheorem/MainRoute/GeneralInM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/GeneralInM.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/GeneralInM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Item (5) on every solver, and both bounds from one algorithm

The items of the route are numbered as in proof/maintheorem/MainRoute/Defs.lean.

* `e_le_rPow_of_sqrt`: at the level ℓ picked for m, «the largest ℓ with K_ℓ ≤ m^(1/9)», m <
  K_(ℓ+1)^9 ≤ K_ℓ^(9C₀), so log(m+2) ≤ (9C₀+1)·log K_ℓ; with e_ℓ ≤ a/√(log K_ℓ) this gives e_ℓ ≤
  (a·(9C₀+1)+1)/√(log(m+2)).
* `topM_of_sqrt`: `GeneralPieces.Tied.TopM` for the function for the bound in m (it and its exponent
  are polynomial-time, it is right, its exponent is O(k·m/√(log m)), and a machine computes it), for
  EVERY polynomial-time solver with a sequence of levels and e_ℓ ≤ a/√(log K_ℓ). Each ingredient is
  proved for any sequence of levels: `GeneralPieces.Top.topM_of_arith`, and the inequality that it
  asks for (the exponent is O(k·m·e_ℓ)), through the bound on the logarithm of the number of
  operations
  in the proof of Theorem A(c) (`GeneralPieces.TopDisplay.stTopArith2`). The network of the formula
  is rebalanced by case (i) of Lemma 8, as in the proof of Theorem A(c)
  (`GeneralPieces.partC_m_tied`).
* `meetsBoundInM_of_topM`: from three of these facts (right, exponent, machine), an ARBITRARY
  machine that computes the function with its exponent meets the bound in m.
* `boundInMOnEverySolver`, and `bothBounds_of`: `BothBoundsOnEverySolver` from it and
  `RouteOnEverySolver`. 

### `e_le_rPow_of_sqrt`

 At the level picked for m: if e_ℓ ≤ a/√(log K_ℓ) for all ℓ, then e_ℓ ≤
(a·(9C₀+1)+1)/√(log(m+2)), for every m. 

### `topM_of_sqrt`

 `GeneralPieces.Tied.TopM` for the function for the bound in m, for every polynomial-time solver
with a sequence of levels and e_ℓ ≤ a/√(log K_ℓ). 

### `meetsBoundInM_of_topM`

 From `GeneralPieces.Tied.TopM`: every machine that computes the function for the bound in m with
its exponent meets the bound in m. 

### `boundInMOnEverySolver`

 Item (5) for every solver: some machine computes the function for the bound in m on it, and
every machine that does meets the bound in m. 

### `bothBounds_of`

 Both bounds from one algorithm for cliques, from the chain for every solver and item (5) for
every solver. 

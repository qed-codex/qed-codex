---
{
  "module": "proof/variables/CountedInstance/Pairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/CountedInstance/Pairs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/CountedInstance/Pairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The clauses on numbers alone

For ρ = 1/√2, every x₀ ≥ 18 and every C₀ ≥ 10, from part (a) of Theorem A, proved here along its
proof in the paper (`GeneralPieces.PartA.thmRunningTime_a`):

* K_ℓ ≥ 2, K_ℓ < K_(ℓ+1) ≤ K_ℓ^{10} ≤ K_ℓ^{C₀}, (log K_ℓ)^{−C₀} ≤ 1/log K_ℓ ≤ e_ℓ ≤ 1
  (`GeneralPieces.PartAUse`);
* K_ℓ is computed by the named program (`CliqueLevels.levelsAreComputed`);
* the rational number `GeneralPieces.Between.num` ℓ / `GeneralPieces.Between.den` ℓ, computed from
  ℓ, which serves as the number in [e_ℓ, 2e_ℓ] of the hypothesis of Theorem D (a), lies between 0.85·ρ^ℓ
  and ρ^ℓ (`GeneralPieces.Between.between_half`), and every such number lies in [e_ℓ, 2e_ℓ]
  (`GeneralPieces.Asymptotic.between`);
* e_ℓ ≤ 0.85·√(3x₀+6)/√(log K_ℓ) (`PairsToBound.thetaOfThePairs`) ≤ (3x₀+6)/√(log K_ℓ). 

### `thePairsMeetTheClauses`

 The clauses of the hypothesis of Theorem D (a) that speak of numbers alone, for the pairs (K_ℓ,
e_ℓ) at ρ = 1/√2. 

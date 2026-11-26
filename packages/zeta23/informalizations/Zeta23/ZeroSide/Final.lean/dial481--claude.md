---
{
  "module": "Zeta23/ZeroSide/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ZeroSide/Final.lean — prop:block with the analytic inputs discharged.

Zeta23/ZeroSide.lean proves §4's block structure / prop:block with three analytic facts as explicit
hypotheses (PhiHatConj, PhiHatReal, PoissonSq) and positivity of L and aL². Here they are supplied
from Zeta23.Hypotheses.GzGp (phiHat_conj, phiHat_ofReal), Zeta23.Taper (Params.half_le_a) and
Zeta23.Poisson (Params.hasSum_phiHatR_sq = lem:poisson), leaving only the standing assumptions
(hP : P.Valid) and (hwL : 8 * P.w ≤ P.L T) [eq:wrange]; and the `∀ᶠ T` form that
thmA_abstract consumes (hwL holds eventually since L = λ log(T/2π) → ∞).
-/
```

### `phiHatConj`

 From Zeta23.GzGp.phiHat_conj (uses only that φ is real and even). 

### `phiHatReal`

 From Zeta23.GzGp.phiHat_ofReal. 

### `blockInputs_of_hwL`

 prop:block + [eq:Ncount] packaged for Assembly at height T, under the standing assumptions only. 

### `tendsto_L_atTop`

 L = λ·log(T/2π) → ∞. 

### `blockInputs`

 **The input `thmA_abstract` consumes**: eventually in T, prop:block holds. 

### `eventually_blockInputs`

 Alias of `blockInputs` in the shape used by Main.lean. 

 ### The individual statements with hypotheses discharged (convenience re-exports) 

### `prop_block_i_posIndex`

 **[prop:block] (i)** "n₊(Ã) ≤ s₁ + s₂ + p". 

### `prop_block_i_rank`

 **[prop:block] (i)** "rank(Ã) ≤ s₁ + s₂ + 2p = #𝒵(I')". 

### `prop_block_ii_decomp`

 **[prop:block] (ii)** "Â = P + Q" (Â := A/(aL²) [eq:hatunits] = P.hat T (Z.Az P T)). 

### `prop_block_ii_P_posSemidef`

 **[prop:block] (ii)** "P ⪰ 0". 

### `prop_block_ii_rank_P`

 **[prop:block] (ii)** "rank P ≤ s₁ + s₂". 

### `prop_block_ii_trace_P`

 **[prop:block] (ii)** "tr P ≤ N_on(I')" (by lem:poisson). 

### `prop_block_ii_posIndex_Q`

 **[prop:block] (ii)** "n₊(Q) ≤ p" (by lem:inertia). 

---
{
  "module": "Zeta23/RvM/LocalCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/LocalCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/LocalCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/LocalCount.lean

H-RvM's local count for Mathlib's ζ:  N(t, t+1] ≤ A₀ log(|t| + 3) for all real t
(= Zeta23.RiemannVonMangoldt.local_count at Z := zetaZeroConfig; [Tit86, Thm 9.2]).

Route (never evaluating ζ left of σ = 0.19, so no Stirling is needed):
 * count only zeros with β ≥ 1/2 and double (Zeta23.ZeroConfig.N_le_two_mul_half, Zeta23/RvM/Halving.lean,
   via the ρ ↦ 1−ρ̄ symmetry);
 * Jensen-type zero count on a disc: the ported PNT+ `ZerosBound` (Zeta23/FromPNTPlus/StrongPNTPrefix.lean,
   Apache-2.0) applied to g(w) := ζ(c₀ + 1.9 w)/ζ(c₀), c₀ := 2 + (t+½)i, r = 0.84, R = 0.95:
   the β ≥ 1/2 part of the window lies in ‖w‖ ≤ 0.84 (1.5² + 0.5² ≤ (1.9·0.84)²), the big disc stays in
   σ ≥ 0.195 and at distance ≥ 1 from the pole for |t| ≥ 4;
 * ζ-growth ‖ζ(s)‖ ≤ C(|Im s|+3)^A on σ ≥ 0.15, ‖s−1‖ ≥ 1 and ‖ζ(2+it)‖ ≥ 1/3
   (Zeta23.RvM.zeta_growth_right / zeta_lower_bound_two, Zeta23/RvM/ZetaGrowth.lean);
 * |t| < 4 by the finite constant N(−4, 5].
-/
```

### `riemannZeta_zeros_finite_of_isCompact`

 zeros of ζ in any compact set are finite (none accumulate, none near the pole). 

### `gfun`

 the rescaled function g(z) := ζ(s₀ + c z) · u. 

### `analyticOrderNatAt_gfun`

 order transport: the order of g at w is the multiplicity of ζ at s₀ + c w. 

### `norm_sub_center_le`

 ‖z‖ ≤ |Re z| + |Im z| packaged for the window geometry: a point ρ with 0 < Re ρ < 1 and
t < Im ρ ≤ t + 1 lies within distance 3 of 2 + it. 

### `NhalfR`

 zeros with β ≥ 1/2 in the window (t, t+1], with multiplicity, as a real number. 

### `half_count_large`

 the β ≥ 1/2 half-window count is ≪ log(|t|+3) for |t| ≥ 4 (disc argument). 

### `count_small`

 small heights: N(t,t+1] ≤ N(−4,5] for |t| ≤ 4. 

### `zeta_local_zero_count`

 **H-RvM local count for ζ** ([Tit86, Thm 9.2]): ∃ A₀ ≥ 1, ∀ t ∈ ℝ, N(t, t+1] ≤ A₀ log(|t| + 3),
zeros counted with multiplicity (analytic order of Mathlib's riemannZeta), two-sided in t. 

### `zetaZeroConfig_local_count`

 The same, in H-RvM's vocabulary (Z.N at Z := zetaZeroConfig). 

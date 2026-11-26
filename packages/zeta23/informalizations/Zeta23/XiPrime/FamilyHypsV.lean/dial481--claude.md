---
{
  "module": "Zeta23/XiPrime/FamilyHypsV.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/FamilyHypsV.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/FamilyHypsV.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/FamilyHypsV.lean — the explicit formula's window-regularity class FamilyHyps
(ExplicitFormula.lean §7) for the PROFILED families T ↦ P.atV v T (φ_v = √(v(u/L))·φ), any
WindowProfile v (the flat family and the C³ ramp calculus are in Zeta23/XiPrime/FamilyHyps.lean,
consumed here).

  theorem familyHyps_atV {P : Params} (hP : P.Valid) (hlam : P.lam < 1) {v : ℝ → ℝ} (hv : WindowProfile v) :
      FamilyHyps (P.atV v)

ROUTE.  v > 0 on [−½, ½] and v continuous ⇒ v ≥ m > 0 on [−½−η, ½+η] (compactness: IsCompact.exists_isMinOn +
IsCompact.exists_cthickening_subset_open).  With a smooth cut-off χ (ContDiffBump, = 1 on |s| ≤ ½+η/2, = 0 off
|s| < ½+η) put ṽ := χ·v + (1−χ)·m ≥ m and h̃ := √ṽ: GLOBALLY C³, = √v on |s| ≤ ½+η/2, with |h̃^{(i)}| ≤ H (i ≤ 3).
Then φ_v = (h̃(·/L))·φ AS FUNCTIONS (where φ ≠ 0 we have |u/L| < ½; elsewhere both sides vanish), so φ_v is C³ and
Leibniz + iteratedDeriv_comp_const_mul (|(h̃(·/L))^{(i)}| ≤ H·L^{−i}) + the ramp bounds ‖φ^{(k)}‖₁ ≤ 2B
(k ≥ 1) and ∫|φ| ≤ L give ‖φ_v^{(j)}‖₁ ≤ 2^j·(2B+1)·H ≤ 8(2B+1)H, uniformly in T (L ≥ 1, w ≥ 1).
-/
```

 ## §1. A globally C³ square root of the profile 

### `exists_margin`

 v ≥ m > 0 on a closed η-neighbourhood of [−½, ½]. 

### `exists_smooth_sqrt`

 **a globally C³ square root of v near [−½, ½]** with uniformly bounded derivatives of order ≤ 3. 

 ## §2. φ_v as (h̃(·/L))·φ, and the L¹ size of its derivatives 

### `gfac`

 the smooth factor in the u-variable: u ↦ h̃(u/L). 

### `phiV_eq_mul`

 **φ_v = (h̃(·/L))·φ as functions** (h̃ = √v on |s| ≤ ½+η where v > 0; φ = 0 off [−L/2, L/2]). 

### `integral_abs_iteratedDeriv_mul_le`

 **‖(h̃(·/L)·φ)^{(k)}‖_{L¹} ≤ 8(2B+1)H** for 1 ≤ k ≤ 3 (L ≥ 1, w ≥ 1, 2w ≤ L), and integrability. 

 ## §3. FamilyHyps for the profiled families 

### `_root_.Zeta23.XiPrime.familyHyps_atV`

 **FamilyHyps for T ↦ P.atV v T**, every valid P with λ < 1 and every WindowProfile v. 

### `_root_.Zeta23.XiPrime.familyHyps_atV_quartic`

 the quartic instance: the 0.86864 / 0.93432 ξ′ window family. 

---
{
  "module": "Zeta23/XiPrime/Hardy/EFContour/Analytic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour/Analytic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour/Analytic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFContour/Analytic.lean — analytic data for the W explicit-formula contour INCLUDING THE REAL AXIS.

Hardy/Basic.lean proves everything about χ, L₂, W at points with Im s ≠ 0.  The contour
[1−c, c] × [−R, R] (1 < c ≤ 5/4) crosses the real axis, so here we redo the analytic facts on the vertical strip
−2 < Re s < 3 minus the two genuine singular points 0 and 1, using ONE device: G := (Γℝ)⁻¹ = π^{s/2}/Γ(s/2) is
ENTIRE (Mathlib's differentiable_one_div_Gamma), Γℝ = G⁻¹ literally, and Γℝ s ≠ 0 ↔ s is not a pole of Γℝ
(Mathlib's junk value at the poles is 0 and Γℝ has no genuine zeros).  Hence
  * Γℝ analytic at s ⇔ Γℝ s ≠ 0;  χ = Γℝ(1−·)·G analytic where Γℝ(1−s) ≠ 0, nonzero where moreover Γℝ s ≠ 0;
    L₂ = −½χ′/χ and W = ζ′ + L₂ζ analytic on {−2 < Re < 3} \ {0, 1};
  * G has a SIMPLE zero at 0 (G(s) = s·G(s+2)/(2π), from Gammaℝ_add_two), so G∘(1−·) has a simple zero at 1,
    s·(G′/G)(s) → 1 at 0, and therefore  s·L₂(s) → −½ (s → 0),  (s−1)·L₂(s) → ½ (s → 1);
  * with Mathlib's tendsto_riemannZeta_sub_one_div (ζ(s) − 1/(s−1) → γ) and a removable singularity:
    (s−1)²ζ′(s) → −1, whence the POLE DATA of W:  s·W(s) → ¼ (s → 0),  (s−1)²·W(s) → −½ (s → 1);
  * Wreg := s(s−1)²·W(s), filled in with ¼ at 0 and −½ at 1, is analytic on {−2 < Re < 3}, nonzero at 0, 1,
    and has the zeros and orders of W elsewhere.
-/
```

 ### §1. G := (Γℝ)⁻¹ is entire; Γℝ is analytic exactly where it is nonzero 

### `invGammaℝ`

 G(s) := (Γℝ s)⁻¹. 

### `differentiable_invGammaℝ`

 G is entire. 

### `analyticAt_Gammaℝ`

 Γℝ is analytic at every point where it is nonzero (= every non-pole). 

### `Gammaℝ_ne_zero_of_re`

 Γℝ s ≠ 0 unless s ∈ {0, −2, −4, …}; in particular on −2 < Re s, s ≠ 0. 

### `Gammaℝ_one_sub_ne_zero_of_re`

 Γℝ (1 − s) ≠ 0 on Re s < 3, s ≠ 1. 

### `logDeriv_Gammaℝ_eq_neg`

 logDeriv Γℝ = −logDeriv G where Γℝ ≠ 0. 

 ### §2. The simple zero of G at 0 

### `invGammaℝ_eq_mul`

 G(s) = s · G(s+2)/(2π) for every s (at s = 0 both sides vanish). 

### `invGammaℝCof`

 the cofactor h(s) := G(s+2)/(2π), entire with h(0) = ½. 

### `analyticOrderAt_invGammaℝ_zero`

 G has a simple zero at 0. 

### `analyticOrderAt_invGammaℝ_one_sub_one`

 G ∘ (1 − ·) has a simple zero at 1. 

### `tendsto_mul_logDeriv_invGammaℝ_zero`

 **s·(G′/G)(s) → 1 as s → 0.** 

 ### §3. χ, L₂ and W on the strip off {0, 1} 

### `chiFE_analyticAt'`

 χ is analytic wherever Γℝ(1−s) ≠ 0 (in particular at 0, where it has a simple zero). 

### `logDeriv_chiFE_eq`

 logDeriv χ = logDeriv (Γℝ∘(1−·)) + logDeriv G wherever both factors are nonzero. 

### `logDeriv_Gammaℝ_one_sub_eq`

 logDeriv (Γℝ∘(1−·)) = −logDeriv (G∘(1−·)) wherever Γℝ(1−s) ≠ 0. 

### `stripReg`

 the working region: the vertical strip −2 < Re s < 3 minus {0, 1}. 

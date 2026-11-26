---
{
  "module": "Zeta23/Taper/Decay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Decay.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Decay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — Taper/Decay.lean.  Two sections, `GBounds` and `Psi`.
Names and statements here are used by the umbrella Zeta23/Taper.lean (and the Params layer)
and by downstream files.
Canonical text: the paper, §2.2 [subsec:family].  See Zeta23/Taper.lean header for conventions:
generic parameters (ϱ : ℝ → ℝ) (L w : ℝ); paper's side condition is 1 ≤ w ≤ L/8 [eq:wrange];
each lemma carries the minimal hypothesis it needs.
-/
```

 ### [eq:gbounds]: "`(L − 2w − |y|)₊ ≤ g(y) ≤ A_φ(y) ≤ (L − |y|)₊`" 

 Helpers on the autocorrelation `(v ⋆ v)(y) := ∫ v(u) v(u+y) du` [eq:PhigA] of a real function:
evenness (translation invariance of Lebesgue measure), the interval-overlap length
`|[−M,M] ∩ ([−M,M] − y)| = (2M − |y|)₊`, the two comparison bounds, vanishing for `|y| ≥ 2M`,
and continuity in `y` (parametric integral over the compact support). 

### `volume_Icc_inter_shift`

 `|[−M, M] ∩ ([−M, M] − y)| = max (2M − |y|) 0`. 

### `autocorr_le_of_support`

 Upper comparison: `0 ≤ v ≤ 1` and `v = 0` off `(−M, M)` ⟹ `(v⋆v)(y) ≤ (2M − |y|)₊`. 

### `le_autocorr_of_plateau`

 Lower comparison: `0 ≤ v`, `v = 1` on `[−M, M]`, integrand integrable ⟹ `(2M − |y|)₊ ≤ (v⋆v)(y)`. 

### `autocorr_eq_zero_of_support`

 `v = 0` off `(−M, M)` and `|y| ≥ 2M` ⟹ `(v⋆v)(y) = 0` (the supports of `v` and `v(·+y)` are disjoint). 

### `autocorr_continuous_of_support`

 Continuity of `y ↦ (v⋆v)(y)` for continuous `v` vanishing off `(−M, M)`. 

 The taper instances: `A_φ = φ ⋆ φ` (support `[−L/2, L/2]`, `0 ≤ φ ≤ 1`) and `g = φ² ⋆ φ²`
(plateau `φ² = 1` on `[−L/2+w, L/2−w]`). 

### `Aphi_even`

 "`g` and `A_φ` are even". 

### `g_eq_zero`

 `g(y) = 0` for `|y| ≥ L` (so `Σ_n a_n² g(log n)` runs over `n ≤ X = e^L` only). 

### `Aphi_eq_zero`

 "(and `A_φ(L) = 0`)" [prop:trace, P-part]; more generally `A_φ(y) = 0` for `|y| ≥ L`. 

 ### [eq:psidef]: "`max(|φ̂(r)|, |Φ(r)|) ≤ ψ(r) := min(L, 2/|r|, c_ϱ/(w r²))`"
We give the three bounds separately (division-free) and then the `ψ` form. 

 #### Helpers: first-order [eq:hfbound], and the ℂ-valued φ² 

### `norm_paperFT_mul_le`

 [eq:hfbound], first order (one integration by parts): supp f ⊆ [−Λ, Λ], f ∈ C_c¹ ⇒
‖h_f(z)‖ · ‖z‖ ≤ e^{|Im z| Λ} ‖f'‖₁. (Companion of Zeta23.norm_paperFT_mul_sq_le.) 

### `phiSqC_contDiff`

 The ℂ-valued φ² used in Φ := (φ²)^ is C² with support in [−L/2, L/2]. 

### `integral_phi_sq_le`

 ∫ φ² ≤ L. 

### `abs_le_psi_of_bounds`

 [eq:psidef] abstractly: the three bounds `|F| ≤ L`, `|F|·|r| ≤ 2`, `|F|·r² ≤ c_ϱ/w` give `|F| ≤ ψ`. 

 #### Measurability / integrability of ψ 

### `psi_le_rpow_neg_two`

 For r > 0: ψ(r) ≤ (c_ϱ/w) · r^{−2} (rpow form). 

### `plateauMaj`

 The common integrable plateau majorant: `a` on [−1,1] and `b·|r|⁻²` outside (ψ: a = L, b = c_ϱ/w;
r²-moments: a = 4, b = C²).  ∫ = 2a + 2b. 

### `psiMaj`

 The integrable majorant of ψ: L on [−1,1] and (c_ϱ/w)|r|⁻² outside. 

### `continuous_paperFT_ofReal`

 φ̂_ℝ is continuous (paperFT of an integrable function, at real arguments; dominated
convergence with the bound ‖φ‖). Auxiliary version for this file; Zeta23/Taper/Fourier.lean
(downstream) carries phiHatR_continuous. 

 ### [eq:psiints].  We record upper bounds — every downstream citation of [eq:psiints] in §5 is
"≪ log L" or "≤ 8L".  (Paper: "a direct computation (split at |r| = 2/L and |r| = c_ϱ/2w; note
c_ϱ L/4w ≥ 1 by [eq:wrange]) gives Ψ₀ = 4 + 2 log(c_ϱ L/4w), ∫ψ²|r| = 8 + 8 log(c_ϱ L/4w),
∫ψ² ≤ 8L".) 

### `psiints_consts`

 Constants for [eq:psiints]: A := 2/L ≤ B := c_ϱ/(2w) ("note c_ϱ L/4w ≥ 1 by
[eq:wrange]"), B/A = c_ϱ L/(4w). 

### `indicator_psi_le`

 On (0, ∞), ψ is dominated by the three-piece majorant L·1_{(0,A]} + (2/r)·1_{(A,B]} +
(c_ϱ/w) r⁻²·1_{(B,∞)} (in fact with equality; ≤ is all we use). 

### `integral_psi_Ioi_le`

 [eq:psiints]: Ψ₀ := ∫₀^∞ ψ(r) dr ≤ 4 + 2 log(c_ϱ L/(4w)) (paper: "="). 

### `integral_psi_sq_mul_abs_le`

 [eq:psiints]: ∫_ℝ ψ(r)²|r| dr ≤ 8 + 8 log(c_ϱ L/(4w)) (paper: "="): split (0,2/L],
(2/L, c/2w], (c/2w, ∞): ∫₀^∞ ψ² r ≤ L²(2/L)²/2 + 4 log(cL/4w) + (c/w)²/(2(c/2w)²) = 2 + 4 log + 2. 

### `integral_psi_sq_le`

 [eq:psiints]: "∫_ℝ ψ² ≤ 8L". Uses only ψ ≤ min(L, 2/|r|):
∫ = 2∫₀^∞ ≤ 2(∫₀^{2/L} L² + ∫_{2/L}^∞ 4r⁻²) = 2(2L+2L). 

 #### Generic moment bounds from |F| ≤ ψ-type information 

### `integral_sq_mul_abs_le_of_le_psi`

 If |F| ≤ ψ pointwise then ∫ F²|r| ≤ ∫ ψ²|r| ≤ 8 + 8 log(c_ϱ L/4w). 

### `momMaj`

 The integrable majorant for the r²-moments: 4 on [−1,1] and C²|r|⁻² outside. 

### `sq_mul_sq_le_momMaj`

 Pointwise: |F(r)|·|r| ≤ 2 and |F(r)|·r² ≤ C give F(r)² r² ≤ momMaj C r. 

### `integral_phiHatR_sq_mul_abs_le`

 Consequence packaged for [prop:trace]/[prop:mumu]: ∫ φ̂(r)² |r| dr ≤ 8 + 8 log(c_ϱ L/4w). 

### `integrable_phiHatR_sq_mul_sq`

 Used for [prop:trace] (μ/Π tails): `φ̂(r)² r²` is integrable … 

### `integral_phiHatR_sq_mul_sq_le`

 … and `∫ φ̂(r)² r² dr ≤ 8 + 2 (c_ϱ/w)²` (from [eq:psidef]: `φ̂² r² ≤ 4` on `|r| ≤ 1`,
`≤ (c_ϱ/w)² r⁻²` on `|r| > 1`). 

### `integrable_PhiR_sq_mul_sq`

 Φ analogue (used for [prop:mumu]): `Φ(x)² x²` integrable … 

### `integral_PhiR_sq_mul_sq_le`

 … and `∫ Φ(x)² x² dx ≤ 8 + 2 (c_ϱ/w)²` (same ψ route as for φ̂). 

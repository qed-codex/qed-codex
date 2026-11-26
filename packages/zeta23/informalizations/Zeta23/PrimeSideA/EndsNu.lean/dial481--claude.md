---
{
  "module": "Zeta23/PrimeSideA/EndsNu.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsNu.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsNu.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — [lem:ends], the two one-dimensional ν-weighted ψ estimates feeding the 𝓔₂ bound
(§5.3 of the paper).  Consumed by Zeta23/PrimeSideA/EndsE2.lean.

* N1 `nu_weight_bound` (§5.3: "In the second factor, the range |τ'−τ_k| ≤ 2T has |τ'| ≤ 4T and
  contributes at most 2Ψ₀B; on |τ'−τ_k| =: r > 2T we have |τ'| ≤ 2r, |ν_X(τ')| ≤ B + log(r/T) and
  ψ(r) ≤ c_ϱ r⁻², contributing ≪ B/T. So the second factor is ≤ 3Ψ₀B uniformly in k."):
      ∫_ℝ ψ(τ−a) |ν_X(τ)| dτ ≤ (2Ψ + 5c_ϱ)·B   for a ∈ I = [T,2T],  Ψ := 4 + 2 log(c_ϱL/4w) ≥ Ψ₀.
  Route (constants only differ): |ν_X(τ)| ≤ B + log⁺(|τ|/4T) ≤ B + 2√(|τ|/4T) ≤ B + 2 + 2√(|τ−a|/4T)
  for |a| ≤ 2T, so the integral is ≤ (B+2)∫ψ + T^{-1/2}∫ψ(r)√|r| dr ≤ (B+2)·2Ψ + 2L + 4c_ϱ/w.
* N2 `nu_grid_bound` (§5.3: "The sum over k of the first factor equals ∫_{τ∉I}|ν_X(τ)|σ(τ)dτ with
  σ(τ) := Σ_{k<d} ψ(τ−τ_k) … Hence ∫_{τ∉I}|ν_X|σ ≪ BLl"):
      ∫_{ℝ∖I} |ν_X(τ)| σ(τ) dτ ≤ CN2(c_ϱ)·B·L·l.
Here ψ = `psiA cϱ p` [eq:psidef], B = `B` = l + 4√X and `NuBound p` = [eq:Bdef]
(discharged by nuX_abs_le), all from Zeta23/PrimeSideA/EndsCore.lean.
-/
```

### `CN2`

 The constant of N2 (depends on c_ϱ only; explicit, value immaterial). 

### `integral_psiA_mul_sqrt_le`

 ∫_ℝ ψ(r)√|r| dr ≤ 2L + 4c_ϱ/w  (ψ ≤ L on |r| ≤ 1, ψ(r)√r ≤ (c_ϱ/w) r^{−3/2} on r > 1). 

### `nu_weight_bound_of_L_le_two_B`

 **N1, master form** (§5.3, "the second factor is ≤ 3Ψ₀B uniformly in k"): for a ∈ [T,2T] and any level
`B` with `L ≤ 2B`, `4 ≤ B`,   ∫_ℝ ψ(τ−a)|ν(τ)| dτ ≤ (2(4 + 2 log(c_ϱL/4w)) + 7c_ϱ)·B.
(The two paper regimes are the corollaries `nu_weight_bound` (B ≥ l ≥ L/2) and `nu_weight_bound_L` (B ≥ L).) 

### `nu_weight_bound`

 **N1** (§5.3, "the second factor is ≤ 3Ψ₀B uniformly in k"): for a ∈ [T,2T],
  ∫_ℝ ψ(τ−a)|ν_X(τ)| dτ ≤ (2(4 + 2 log(c_ϱL/4w)) + 7c_ϱ)·B   (paper regime B ≥ l, L ≤ 2l). 

### `nu_weight_bound_L`

 **N1, L-intrinsic form** (no bandwidth cap; the absorbing hypothesis is `L ≤ B`). 

 ### N2: reduction to the half-line and the majorant 

### `setIntegral_Iio_comp_sub_left`

 change of variables Δ = T − τ on (−∞, T). 

### `setIntegral_Ioi_comp_sub_right`

 change of variables Δ = τ − c on (c, ∞). 

### `Sgrid`

 σ reduced to the half-line: S(Δ) := Σ_{j<d} ψ(Δ + jh)  (§5.3). 

### `Sgrid_le_near`

 near range (§5.3): S(Δ) ≤ ψ(Δ) + h⁻¹∫_Δ^∞ ψ. 

### `Sgrid_le_far`

 far range (§5.3): S(Δ) ≤ d ψ(Δ)  (ψ antitone). 

### `sigma_eq_left`

 σ(τ) = S(T−τ) for τ ≤ T;  σ(τ) ≤ S(τ−2T) for τ ≥ 2T. 

### `Mnear`

 The half-line majorants (§5.3).  Near: Δ ≤ 2T, |ν| ≤ B and
S(Δ) ≤ ψ(Δ) + (L/2π)min(Ψ', c/(wΔ));  far: Δ > 2T, |ν| ≤ B + 2√(Δ/T) and S(Δ) ≤ d c/(wΔ²). 

### `Sgrid_mul_le_Mnear`

 the product S(Δ)·(ν-bound) against the majorant, near range. 

### `Sgrid_mul_le_Mfar`

 the product S(Δ)·(ν-bound) against the majorant, far range. 

### `dom_left`

 pointwise domination, left of I:  σ(τ)|ν(τ)| ≤ M(T−τ) for τ < T. 

### `dom_right`

 pointwise domination, right of I:  σ(τ)|ν(τ)| ≤ M(τ−2T) for τ > 2T. 

 ### N2: integrating the majorant 

### `Mfar_eq_rpow`

 rpow form of the far majorant on Δ > 0. 

### `integral_Mnear_le`

 near integral (§5.3): ∫_0^{2T} Mnear ≤ B[Ψ' + (L/2π)(Ψ' + (c/w) log 2T)],  Ψ' = ∫_0^∞ ψ. 

### `integral_Mfar_le`

 far integral (§5.3): ∫_{2T}^∞ Mfar ≤ (d/T)(c/w)(B/2 + 4). 

### `integrableOn_sigma_mul_abs_nuX`

 integrability of N2's integrand on ℝ ∖ I. 

### `log_two_mul_T_le`

 log(2T) = log(4π) + l ≤ l + 12. 

### `nu_grid_bound_raw`

 **N2, raw form** (§5.3): the common core of `nu_grid_bound` / `nu_grid_bound_L` — the majorant
integrated on both half-lines, before the polynomial endgame:
  ∫_{τ∉I}|ν|σ ≤ 2·(B·(2 + 2L + (25/2)c_ϱL + c_ϱL²/2 + c_ϱLl) + L·c_ϱ·B),   any level B ≥ 8. 

### `nu_grid_bound`

 **N2** (§5.3, "∫_{τ∉I}|ν_X|σ ≪ BLl", σ(τ) := Σ_{k<d} ψ(τ−τ_k))  (paper regime B ≥ l, L ≤ 2l). 

### `nu_grid_bound_L`

 **N2, L-intrinsic form**: ∫_{τ∉I}|ν|σ ≤ CN2·B·L·(L + l)  (l = log(T/2π) carries the
genuine log T from the window geometry; no bandwidth cap, absorbing hypothesis `L ≤ B`). 

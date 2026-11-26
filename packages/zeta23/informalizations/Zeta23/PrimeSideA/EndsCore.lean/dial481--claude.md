---
{
  "module": "Zeta23/PrimeSideA/EndsCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsCore.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — prime side, [lem:ends] "End effects" (§5, §5.3 of the paper), with [eq:Kdef],
[eq:trG2int], [eq:Kbounds].

TARGET (consumed by thm:traces):
  theorem lem_ends (hΓ : GammaFacts) (hcheb : ChebyshevMertens) (hlam : 0 < lam ∧ lam ≤ 1) :
    ∃ C : ℝ, EventuallyAt cϱ lam (fun p F =>
      |trGt2A p F - MtotalA p F| ≤ C * (p.L * p.l * Real.log p.l * (p.l ^ 2 + p.X)))

PAPER (§5.3, verbatim): "For T ≥ T₀,  tr G̃² = 𝓜 + O(L l log l (l² + X)),
  𝓜 := ∬_{I×I} Φ(τ−τ')² ν_X(τ) ν_X(τ') dτ dτ'."

ROUTE (paper's, §5.3, with two simplifications that only change absolute constants):
* [eq:trG2int]  L² tr G̃² = Σ_{k,l<d} G_{kl}² = ∬_{ℝ²} K(τ,τ')² ν(τ)ν(τ') dτdτ',
  K(τ,τ') := Σ_{0≤k<d} φ̂(τ−τ_k)φ̂(τ'−τ_k) [eq:Kdef]  — here a product of two integrals and a
  FINITE sum, so no Fubini beyond ∫(f)·∫(g) = ∬ f⊗g.
* K_∞ := Σ_{k∈ℤ} φ̂(τ−τ_k)φ̂(τ'−τ_k) = L Φ(τ−τ') by [lem:poisson] (LocalHyps.poisson), so
  ∬_{I×I} K_∞² νν' = L² 𝓜, and  L²(tr G̃² − 𝓜)·L² … precisely:
  Σ G² − L²𝓜·… = 𝓔₁ + 𝓔₂,  𝓔₁ := ∬_{I×I}(K² − K_∞²)νν',  𝓔₂ := ∬_{ℝ²∖I×I} K²νν'.
* [eq:Kbounds]  |K|, |K_∞| ≤ L² (paper: aL²; a ≤ 1);  |K_out| = |K_∞ − K| handled by the
  weighted AM–GM  |Σ_{k∉[0,d)} a_k b_k| ≤ ½(s ρ(τ) + ρ(τ')/s), ρ(τ) := Σ_{k∉[0,d)} φ̂(τ−τ_k)²
  = aL² − Σ_{k<d} φ̂(τ−τ_k)² (Poisson diagonal — a FINITE expression), with s := g(τ')/g(τ),
  g := (1 + dist(·,∂I))⁻².  This replaces the paper's (∫_I ψ_k)²-sum (§5.3) and gives
  |𝓔₁| ≤ 2L²B²(∫_I ρ/g)(∫_I g) ≪ L²B²·L·l ≤ L³B² l log l  — within the lemma's error (the paper
  gets L³B² log L here; the slack l is free since 𝓔₂ is the dominant term anyway).
* 𝓔₂ exactly as the paper (§5.3): |𝓔₂| ≤ 2L² Σ_{k<d}(∫_{I^c}ψ_k|ν|)(∫_ℝ ψ_k|ν|),
  second factor ≤ 3Ψ₀B, Σ_k first factor = ∫_{I^c}|ν|σ ≪ BLl via the grid bound
  σ(τ) ≤ ψ(Δ) + h⁻¹∫_Δ^∞ψ, σ ≤ d ψ(Δ); for the far range we use log⁺x ≤ 2√x instead of
  integrating logarithms (constants only).
* [eq:Bdef] |ν_X(τ)| ≤ B + log⁺(|τ|/4T), B = l + 4√X: Zeta23/PiFacts.lean
  (from H-Γ + H-cheb); B² ≤ 2l² + 32X.
All constants C may depend on c_ϱ and λ (PrimeSideA convention); T₀ likewise.

FILE LAYOUT:
  EndsCore.lean (this file) — defs, continuity/integrability, [eq:trG2int],
     decomposition, ψ toolkit, [eq:Kbounds] pointwise;
  EndsE1.lean — calE1_bound;   EndsE2.lean (1-D estimates N1/N2 in EndsNu.lean,
     weights in EndsWeighted.lean) — calE2_bound;
  Ends.lean — assembly lem_ends' / lem_ends (proved from the two bounds).
-/
```

 The ψ majorant `psiA cϱ p r = min(L, 2/|r|, c_ϱ/(w r²))` [eq:psidef] and the [eq:psiints]
facts (psi_integrable, psi_sq_integrable, integral_psi_Ioi_le, integral_psi_sq_le, phiHat_le_psi,
Phi_le_psi) are in Zeta23/PrimeSideA (`LocalHyps`). 

### `NuBound`

 [eq:Bdef] pointwise bound on ν_X (Zeta23/PiFacts.lean `nuX_abs_le`):
"`|ν_X(τ)| ≤ B + log⁺(|τ|/4T)` (τ ∈ ℝ), `|ν_X(τ)| ≤ B` (|τ| ≤ 4T), `B := l + 4√X`" for T ≥ T₀. 

### `Bconst`

 `B := l + 4√X` [eq:Bdef]. 

 ν-GENERIC LAYER (for Theorem E): every object below that involves the density is
stated for an ABSTRACT `ν : ℝ → ℝ` (hypotheses: `Continuous ν` and `NuBound p B ν` for a free
`B ≥ 0`); ζ is the instantiation `ν := Zeta23.nuX p.X`, `B := Bconst p` (bridges by `rfl`). 

### `GentryNu`

 `G_{kl}` for an abstract density ν (`GentryA p F k l = GentryNu (Zeta23.nuX p.X) p F k l`, rfl). 

### `MtotalNu`

 `𝓜` for an abstract density (`MtotalA p F = MtotalNu (Zeta23.nuX p.X) p F`, rfl). 

 ## [eq:Kdef] 

### `Kfun`

 `K(τ,τ') := Σ_{0≤k<d} φ̂(τ−τ_k) φ̂(τ'−τ_k)` [eq:Kdef]. 

### `Kinf`

 `K_∞(τ,τ') = L Φ(τ−τ')` (the value of `Σ_{k∈ℤ}`, [lem:poisson]). 

### `rho`

 `ρ(τ) := aL² − Σ_{k<d} φ̂(τ−τ_k)²`  (`= Σ_{k∉[0,d)} φ̂(τ−τ_k)²` by the Poisson diagonal). 

 All double integrals below are integrals over `ℝ × ℝ` w.r.t. `volume` (= `volume.prod
volume`), restricted to `I ×ˢ I` or its complement where indicated — the same spelling as
`Mform` in Zeta23/PrimeSideA/Defs.lean. 

### `sqI`

 the square `I × I`, `I = [T,2T]`. 

### `trG2integrand`

 the integrand of [eq:trG2int]: `K(τ,τ')² ν(τ) ν(τ')`. 

### `KinfIntegrand`

 the integrand `K_∞(τ,τ')² ν(τ) ν(τ')` (`= L² Φ(τ−τ')² νν'`). 

### `calE1`

 `𝓔₁ := ∬_{I×I} (K² − K_∞²) ν ν'` (§5.3). 

### `calE2`

 `𝓔₂ := ∬_{(I×I)ᶜ} K² ν ν'` (§5.3). 

 ## [eq:trG2int] and the decomposition 

### `nuX_continuous`

 ν_X is continuous (μ smooth by H-Γ, Π_X by hypothesis, P_X a trigonometric polynomial). 

 ### Integrability ("the interchange being justified by absolute convergence", §5.3) 

### `abs_phiHat_mul_one_add_sq_le`

 `|φ̂(r)|(1 + r²) ≤ L + c_ϱ/w` (from [eq:psidef]). 

### `one_add_sq_le_shift`

 shift inequality `1 + τ² ≤ 2(1 + a²)(1 + (τ − a)²)`. 

### `abs_phiHat_shift_le`

 `|φ̂(τ − a)| ≤ 2(L + c/w)(1 + a²)/(1 + τ²)`. 

### `max_log_zero_le`

 `log⁺ x ≤ x` for `x ≥ 0`. 

### `abs_nuX_le_linear`

 crude global form of [eq:Bdef]: `|ν_X(τ)| ≤ B + |τ|` (for `T ≥ 1/4`). 

### `gkl`

 the one-variable pieces `g_{kl}(τ) := φ̂(τ−τ_k) φ̂(τ−τ_l) ν_X(τ)` of `G_{kl} = ∫ g_{kl}`. 

### `abs_gkl_le`

 domination `|g_{kl}(τ)| ≤ C_{kl} (1 + τ²)⁻¹`. 

### `GentryNu_eq`

 `G_{kl} = ∫ g_{kl}`. 

### `sum_gkl_mul_gkl`

 pointwise: `Σ_{k,l<d} g_{kl}(τ) g_{kl}(τ') = K(τ,τ')² ν(τ)ν(τ')`. 

### `trG2integrand_integrable`

 The heart of "the interchange being justified by absolute convergence" (§5.3):
`K(τ,τ')² ν(τ)ν(τ')` is integrable on `ℝ²`. 

### `eq_trG2int`

 **[eq:trG2int]** (§5.3): `Σ_{k,l<d} G_{kl}² = ∬_{ℝ²} K(τ,τ')² ν_X(τ)ν_X(τ') dτdτ'`
("the interchange being justified by absolute convergence"). 

### `integral_Kinf_sq`

 `∬_{I×I} K_∞² νν' = L² 𝓜` (§5.3 "note …"). 

### `decomp`

 The decomposition  `Σ_{k,l<d} G_{kl}² − L²𝓜 = 𝓔₁ + 𝓔₂`. 

 ## ψ toolkit  (generic facts about `psiA cϱ p` = min(L, 2/|r|, c/(w r²)) [eq:psidef]).
Statements are consumed by EndsE1/EndsE2. 

### `psiA_antitoneOn`

 ψ is antitone on [0, ∞). 

### `integral_psiA_eq_two_mul`

 ∫_ℝ ψ = 2 ∫_{(0,∞)} ψ (ψ even). 

### `setIntegral_psiA_Ioi_le_div`

 tail: ∫_{(Δ,∞)} ψ ≤ c_ϱ/(w Δ) for Δ > 0 (from ψ(r) ≤ c/(w r²)). 

### `setIntegral_psiA_Ioi_mono`

 tail monotonicity: ∫_{(Δ,∞)} ψ ≤ ∫_{(0,∞)} ψ for Δ ≥ 0. 

### `sum_grid_le_of_antitoneOn`

 Generic: for f ≥ 0 antitone on [0,∞) and integrable on (Δ,∞), Δ ≥ 0, h > 0:
Σ_{j<n} f(Δ + j h) ≤ f(Δ) + h⁻¹ ∫_{(Δ,∞)} f  (j = 0 term + antitone comparison on each cell
[Δ+jh, Δ+(j+1)h], cells summed by intervalIntegral.sum_integral_adjacent_intervals). 

### `sum_psiA_grid_le`

 grid sum vs integral (ψ antitone): Σ_{j<n} ψ(Δ + j h) ≤ ψ(Δ) + h⁻¹ ∫_{(Δ,∞)} ψ. 

### `psiA_sq_antitoneOn`

 ψ² is antitone on [0,∞) (ψ ≥ 0 antitone). 

### `sum_psiA_sq_grid_le`

 same for ψ²: Σ_{j<n} ψ(Δ + j h)² ≤ ψ(Δ)² + h⁻¹ ∫_{(Δ,∞)} ψ². 

### `setIntegral_psiA_sq_Ioi_le_div`

 tail for ψ²: ∫_{(Δ,∞)} ψ² ≤ (c_ϱ/w)²/(3Δ³) for Δ > 0. 

### `setIntegral_psiA_sq_Ioi_le`

 ∫_{(Δ,∞)} ψ² ≤ ∫_ℝ ψ² ≤ 8L. 

### `abs_phiHat_le_psiA`

 `|φ̂(r)| ≤ ψ(r)` [eq:psidef] (LocalHyps field). 

### `integral_psiA_le`

 `2Ψ₀ := ∫_ℝ ψ ≤ 2(4 + 2 log(c_ϱ L/4w))` [eq:psiints]. 

 ## [eq:Kbounds] pointwise (§5.3) 

### `rho_nonneg`

 Poisson diagonal, finite part: `Σ_{k<d} φ̂(τ−τ_k)² ≤ aL²`, i.e. `ρ(τ) ≥ 0`. 

### `hasSum_rho`

 `ρ(τ) = Σ_{k∉[0,d)} φ̂(τ−τ_k)²` as a `HasSum` over the complement of `range d` in ℤ
(from LocalHyps.poisson τ τ and Phi_zero). 

### `abs_Kfun_le`

 **[eq:Kbounds]** first part: `|K(τ,τ')| ≤ aL² ≤ L²` (Cauchy–Schwarz + Poisson diagonal). 

### `abs_Kinf_le`

 `|K_∞(τ,τ')| = L|Φ(τ−τ')| ≤ L² ` (LocalHyps.Phi_le_L). 

### `abs_Kfun_le_sum_psiA`

 **[eq:Kbounds]** via ψ: `|K(τ,τ')| ≤ Σ_{k<d} ψ(τ−τ_k) ψ(τ'−τ_k)`. 

 ### K_out pointwise (weighted AM–GM), for 𝓔₁ 

### `sum_Ico_int_eq_sum_fin`

 general reindexing `Σ_{k ∈ Ico 0 d} f k = Σ_{k : Fin d} f k` for `f : ℤ → ℝ`. 

### `hasSum_Kout`

 `K_out = K_∞ − K` as a HasSum over `k ∉ [0,d)` (from LocalHyps.poisson). 

### `abs_mul_le_weighted`

 termwise weighted AM–GM: `|a b| ≤ (s a² + b²/s)/2` for `s > 0`. 

### `abs_Kinf_sub_Kfun_le`

 **Pointwise bound for K_out** (weighted AM–GM): for every `s > 0`,
`|K_∞(τ,τ') − K(τ,τ')| ≤ (s ρ(τ) + ρ(τ')/s)/2`. 

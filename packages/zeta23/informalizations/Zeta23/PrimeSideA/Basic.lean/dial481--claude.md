---
{
  "module": "Zeta23/PrimeSideA/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization of
  "More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
-/
```


# Prime side, part A — paper §5 [sec:prime]:  [prop:trace], [lem:ends], [eq:Msplit], [prop:mumu], [prop:cross]

Seam with `PrimeSideB.lean` ([prop:PP], [thm:traces]): see the header of
`Zeta23/PrimeSideA/Defs.lean`.  Everything here is ζ-free: the zeros never
appear in §5 ("In this section the zeros play no role", §5); `N(T,2T)` enters [prop:trace]
only through [eq:muints] + [eq:RvM], which we take as hypotheses on an abstract real `N`.

## Shape of the results
All error terms are explicit inequalities, uniform in `T`:
  `∃ C, EventuallyAt cϱ lam (fun p F => |lhs p F − main p F| ≤ C * err p)`
where `EventuallyAt cϱ lam P` means: there is `T₀` such that `P p F` holds for every parameter set
`p` with `p.lam = lam`, `T₀ ≤ p.T` and every taper datum `F` satisfying `LocalHyps cϱ p F`.
So `C` and `T₀` may depend on `c_ϱ`, on the constants inside H-Γ/H-cheb, and on `λ` — the paper
has `C` depending on ϱ only and `T₀ = T₀(λ)` (§5.5); ours is the (weaker, sufficient at fixed λ)
reading.  This is a deviation from the paper.

## Hypotheses consumed (all proved elsewhere in the repository; none is a Lean axiom)
* `Zeta23.GammaFacts` (H-Γ [eq:mufacts]+[eq:muints]) and `Zeta23.ChebyshevMertens` (H-cheb
  [lem:cheb]) — Zeta23/Hypotheses.lean, verbatim (fields of `PaperInputs`).
* `LocalHyps cϱ p F` — taper/test-family facts [eq:psidef], [eq:abdef], [eq:gbounds], [eq:Phi2FT],
                      `∫φ̂² = 2πaL`, `Φ(0) = aL`, `∫Φ² = 2πbL`;
                      [lem:poisson] (★); [eq:PiPfacts] for Π_X;
                      parameter regime [eq:wrange], `0<λ≤1`.


 ## Hypothesis packages

H-Γ and H-cheb are Zeta23/Hypotheses.lean's `Zeta23.GammaFacts` and `Zeta23.ChebyshevMertens` (about the
concrete `Zeta23.mu` and Λ-sums), taken verbatim.  The taper/test-family facts are packaged here: 

### `psiA`

 ψ(r) := min(L, 2/|r|, c_ϱ/(w r²)) [eq:psidef], with the r = 0 guard
(= `Zeta23.Params.psi` / `Taper.psi'` by `rfl` under the bridge).  Majorant for both `φ̂` and `Φ`. 

### `LocalHyps`

 The facts about the test family at parameters `p` used in §5, each tagged with
its paper label; `cϱ` is the profile constant `c_ϱ = 4‖ϱ'‖_∞ + 4‖ϱ''‖₁ ≥ 4` of [eq:phinorms]
(= `Zeta23.Params.crho`).  These facts are supplied by Taper.lean / Poisson.lean and
PiFacts.lean: this structure is instantiated elsewhere in the repository (a theorem
`LocalHyps P.crho ⟨T, P.lam, P.w⟩ ⟨P.phiHatR T, P.PhiR T, P.Aphi T, P.g T, P.a T, P.b T⟩` for
valid `P` and large `T`), not assumed. 

### `LocalHyps.four_le_cϱ`

 [eq:phinorms] `c_ϱ ≥ 4`. 

### `LocalHyps.lam_pos`

 `0 < λ ≤ 1` [Notation]. 

### `LocalHyps.one_le_w`

 [eq:wrange] `1 ≤ w ≤ L/8` (forces `L ≥ 8`). 

### `LocalHyps.one_le_l`

 "T is large": `l ≥ 1`, i.e. `T ≥ 2πe`. 

### `LocalHyps.phiHat_cont`

 φ̂ real-analytic facts: continuity; evenness (φ even) [§2.2 "φ̂ and Φ are real, even, entire"]. 

### `LocalHyps.phiHat_le_L`

 [eq:psidef] `|φ̂(r)| ≤ ψ(r) := min(L, 2/|r|, c_ϱ/(w r²))`, split into three division-free bounds. 

### `LocalHyps.phiHat_sq_integrable`

 Integrability consequences of [eq:psidef] (`φ̂² ≤ ψ² ≤ min(L², c_ϱ²/(w²r⁴))`), and
  [eq:psiints] in the packaged form `∫ φ̂(r)²|r| dr ≤ ∫ ψ²|r| = 8 + 8 log(c_ϱL/4w)` (§2.2, used at
  §5.2 "∫ φ̂(r)²|r| dr ≪ log L"). 

### `LocalHyps.phiHat_sq_mul_sq_integrable`

 also from [eq:psidef]: `φ̂(r)²r² ≤ min(4, (c_ϱ/w)²/r²)`, so `∫ φ̂(r)² r² dr ≤ 8 + 2(c_ϱ/w)²`
  (used for the `|r| > τ_k/2` tails at §5.2 in place of the paper's sharper r⁻⁴ bound). 

### `LocalHyps.phiHat_sq_integral`

 `∫ φ̂(r)² dr = 2π ∫ φ² = 2π a L` [prop:trace proof, §5.2; Plancherel in the paper's
  convention `∫ f ḡ = (2π)⁻¹ ∫ f̂ conj ĝ` + eq:abdef]. 

### `LocalHyps.phiHat_sq_fourier`

 `φ̂² = Â_φ` on ℝ [§2.2] + Fourier inversion, in the real form used at §5.2:
  `∫ φ̂(r)² cos(ry) dr = 2π A_φ(y)` (`φ̂²` even, `A_φ` even, continuous, supported in `[−L,L]`). 

### `LocalHyps.g_lower`

 [eq:gbounds] `(L−2w−|y|)₊ ≤ g(y) ≤ A_φ(y) ≤ (L−|y|)₊`. 

### `LocalHyps.Phi_contDiff`

 Φ facts: `Φ` is C¹ (indeed entire), even [§2.2]. 

### `LocalHyps.Phi_le_L`

 [eq:psidef] `|Φ(r)| ≤ ψ(r)`, three division-free bounds. 

### `LocalHyps.Phi_sq_integrable`

 Integrability consequences of [eq:psidef] for Φ, and [eq:psiints] packaged as
  `∫ Φ(x)²|x| dx ≤ 8 + 8 log(c_ϱL/4w)` (§5.4 "∫Φ(x)²|x|dx ≪ log L (by (eq:psidef), (eq:psiints))"). 

### `LocalHyps.Phi_sq_mul_sq_integrable`

 second moment of `Φ²` (same [eq:psidef] path as the `φ̂` version; needed against the
  `10r²/t` term of `mu_increment_bound` in [prop:mumu]). 

### `LocalHyps.Phi_zero`

 `Φ(0) = aL` [§2.2]. 

### `LocalHyps.Phi_sq_integral`

 `∫_ℝ Φ² = 2π g(0) = 2π b L` [§2.2]. 

### `LocalHyps.Phi_sq_fourier`

 [eq:Phi2FT] `∫_ℝ Φ(x)² e^{ixy} dx = 2π g(y)` (§5.4), real form (`Φ²`, `g` even). 

### `LocalHyps.poisson`

 [lem:poisson] (★) `Σ_{k∈ℤ} φ̂(τ−τ_k) φ̂(τ'−τ_k) = L Φ(τ−τ')` (§2.2). 

### `LocalHyps.b_lower`

 [eq:abdef] `1 − 2w/L ≤ b ≤ a ≤ 1`. 

### `LocalHyps.psi_integrable`

 [eq:psidef] in majorant form, with the [eq:psiints] integrals (`Ψ₀ = 4 + 2log(c_ϱL/4w)`,
  `∫ψ² ≤ 8L`) — fields match `Zeta23.Params.psi'_integrable / psi'_sq_integrable /
  integral_psi'_Ioi_le / integral_psi'_sq_le` in Zeta23/Taper.lean (consumed by [lem:ends]). 

### `LocalHyps.phiHat_le_psi`

 `|φ̂| ≤ ψ` and `|Φ| ≤ ψ` [eq:psidef] in the majorant form used by [lem:ends]. 

### `LocalHyps.PiX_cont`

 Π_X is continuous and [eq:PiPfacts] `|Π_X(τ)| ≤ 3√X/(1+|τ|)` (§2.1), for the concrete
  `Zeta23.PiX X` [eq:Pidef] — via `PiX_bound` (holds for all `X ≥ 1`) and `PiX_continuous`. 

### `EventuallyAt`

 "For `T ≥ T₀`, uniformly": `P p F` holds for every parameter set `p` at bandwidth ratio `lam`
with `T₀ ≤ p.T` and every functional datum `F` satisfying the local hypotheses. 

 ### Bilinearity and symmetry of 𝓜[·,·] (§5.4: "a symmetric bilinear form (Φ² is even)") 

### `Mform_comm`

 Symmetry `𝓜[u,v] = 𝓜[v,u]`: swap `(τ,τ') ↦ (τ',τ)` on the square and use that `Φ` is even. 

### `Mform_trinomial`

 The trinomial expansion behind [eq:Msplit]. 

 ### The "insert sup bounds" estimate for 𝓜[·,·]  (§5.4) 

### `setIntegral_sq_shift_le`

 `∫_S Φ(x−y)² dy ≤ ∫_ℝ Φ²` (translation invariance and `Φ² ≥ 0`); this is
`sup_τ ∫_I Φ(τ−τ')² dτ' ≤ 2πbL` of §5.4. 

### `abs_Mform_le`

 **Sup-bound for 𝓜** [prop:cross proof, §5.4: "the remaining three bounds follow by inserting
these sup bounds into the definition of 𝓜[·,·] (an integral over a region of τ'-length T)"]:
if `|u| ≤ B_u` and `|v| ≤ B_v` on `I = [T,2T]` then `|𝓜[u,v]| ≤ B_u B_v · T · ∫_ℝ Φ²`. 

 ### The large-T regime: elementary consequences of the hypotheses 

### `Setting.le_l_of_T`

 `l ≥ l₀` once `T ≥ 2π e^{l₀}`. 

### `Setting.twopi_le_T`

 `T ≥ 2π` (in particular `T ≥ 1`, `T > 0`) once `T ≥ 2π e^{l₀}` with `l₀ ≥ 0`. 

### `Setting.le_X_of_T`

 `X ≥ x₀` once `T ≥ 2π exp(|x₀|/λ)` (`X = (T/2π)^λ → ∞`; this is the "T ≥ T₀(λ)" of §5). 

### `LocalHyps.integral_Phi_sq_le`

 `∫Φ² = 2πbL ≤ 2πL`. 

### `LocalHyps.PiX_le_on_I`

 [eq:PiPfacts] on `I`: `|Π_X| ≤ 3√X/T` (§5.2, §5.4). 

 ### Window-generic core of the taper hypotheses (paper §7.1 [subsec:MT])

"Nothing in Sections 4–5 used that φ is flat-topped" — except the [eq:gbounds] plateau lower
bound and the [eq:abdef] lower bound on b.  LocalHypsCore is LocalHyps minus exactly those two
facts, with the window-generic replacements g_nonneg and b_ge_half (both hold for the
Montgomery–Taylor window of [thm:D], which does not satisfy LocalHyps).  Surviving field names
are identical to LocalHyps'.  The window-generic §5 results can be re-typed over this
structure; the structure itself is purely additive. 

### `LocalHypsCore.four_le_cϱ`

 [eq:phinorms] `c_ϱ ≥ 4`. 

### `LocalHypsCore.lam_pos`

 `0 < λ ≤ 1` [Notation]. 

### `LocalHypsCore.one_le_w`

 [eq:wrange] `1 ≤ w ≤ L/8` (forces `L ≥ 8`). 

### `LocalHypsCore.one_le_l`

 "T is large": `l ≥ 1`, i.e. `T ≥ 2πe`. 

### `LocalHypsCore.phiHat_cont`

 φ̂ real-analytic facts: continuity; evenness (φ even) [§2.2 "φ̂ and Φ are real, even, entire"]. 

### `LocalHypsCore.phiHat_le_L`

 [eq:psidef] `|φ̂(r)| ≤ ψ(r) := min(L, 2/|r|, c_ϱ/(w r²))`, split into three division-free bounds. 

### `LocalHypsCore.phiHat_sq_integrable`

 Integrability consequences of [eq:psidef] (`φ̂² ≤ ψ² ≤ min(L², c_ϱ²/(w²r⁴))`), and
  [eq:psiints] in the packaged form `∫ φ̂(r)²|r| dr ≤ ∫ ψ²|r| = 8 + 8 log(c_ϱL/4w)` (§2.2, used at
  §5.2 "∫ φ̂(r)²|r| dr ≪ log L"). 

### `LocalHypsCore.phiHat_sq_mul_sq_integrable`

 also from [eq:psidef]: `φ̂(r)²r² ≤ min(4, (c_ϱ/w)²/r²)`, so `∫ φ̂(r)² r² dr ≤ 8 + 2(c_ϱ/w)²`
  (used for the `|r| > τ_k/2` tails at §5.2 in place of the paper's sharper r⁻⁴ bound). 

### `LocalHypsCore.phiHat_sq_integral`

 `∫ φ̂(r)² dr = 2π ∫ φ² = 2π a L` [prop:trace proof, §5.2; Plancherel in the paper's
  convention `∫ f ḡ = (2π)⁻¹ ∫ f̂ conj ĝ` + eq:abdef]. 

### `LocalHypsCore.phiHat_sq_fourier`

 `φ̂² = Â_φ` on ℝ [§2.2] + Fourier inversion, in the real form used at §5.2:
  `∫ φ̂(r)² cos(ry) dr = 2π A_φ(y)` (`φ̂²` even, `A_φ` even, continuous, supported in `[−L,L]`). 

### `LocalHypsCore.g_nonneg`

 window-generic remnant of [eq:gbounds]: `g ≥ 0` and `g ≤ A_φ ≤ (L−|y|)₊`
  (the flat-top plateau lower bound `(L−2w−|y|)₊ ≤ g` is NOT here — see §7.1). 

### `LocalHypsCore.Phi_contDiff`

 Φ facts: `Φ` is C¹ (indeed entire), even [§2.2]. 

### `LocalHypsCore.Phi_le_L`

 [eq:psidef] `|Φ(r)| ≤ ψ(r)`, three division-free bounds. 

### `LocalHypsCore.Phi_sq_integrable`

 Integrability consequences of [eq:psidef] for Φ, and [eq:psiints] packaged as
  `∫ Φ(x)²|x| dx ≤ 8 + 8 log(c_ϱL/4w)` (§5.4 "∫Φ(x)²|x|dx ≪ log L (by (eq:psidef), (eq:psiints))"). 

### `LocalHypsCore.Phi_sq_mul_sq_integrable`

 second moment of `Φ²` (same [eq:psidef] path as the `φ̂` version; needed against the
  `10r²/t` term of `mu_increment_bound` in [prop:mumu]). 

### `LocalHypsCore.Phi_zero`

 `Φ(0) = aL` [§2.2]. 

### `LocalHypsCore.Phi_sq_integral`

 `∫_ℝ Φ² = 2π g(0) = 2π b L` [§2.2]. 

### `LocalHypsCore.Phi_sq_fourier`

 [eq:Phi2FT] `∫_ℝ Φ(x)² e^{ixy} dx = 2π g(y)` (§5.4), real form (`Φ²`, `g` even). 

### `LocalHypsCore.poisson`

 [lem:poisson] (★) `Σ_{k∈ℤ} φ̂(τ−τ_k) φ̂(τ'−τ_k) = L Φ(τ−τ')` (§2.2). 

### `LocalHypsCore.b_ge_half`

 window-generic remnant of [eq:abdef]: `1/2 ≤ b ≤ a ≤ 1` (the flat-top `1 − 2w/L ≤ b`
  is NOT here; 1/2 suffices for every positivity/division use and holds for the
  Montgomery–Taylor window). 

### `LocalHypsCore.psi_integrable`

 [eq:psidef] in majorant form, with the [eq:psiints] integrals (`Ψ₀ = 4 + 2log(c_ϱL/4w)`,
  `∫ψ² ≤ 8L`) — fields match `Zeta23.Params.psi'_integrable / psi'_sq_integrable /
  integral_psi'_Ioi_le / integral_psi'_sq_le` in Zeta23/Taper.lean (consumed by [lem:ends]). 

### `LocalHypsCore.phiHat_le_psi`

 `|φ̂| ≤ ψ` and `|Φ| ≤ ψ` [eq:psidef] in the majorant form used by [lem:ends]. 

### `LocalHypsCore.PiX_cont`

 Π_X is continuous and [eq:PiPfacts] `|Π_X(τ)| ≤ 3√X/(1+|τ|)` (§2.1), for the concrete
  `Zeta23.PiX X` [eq:Pidef] — see `PiX_bound` (holds for all `X ≥ 1`) and `PiX_continuous`. 

### `LocalHyps.toCore`

 every flat-top taper datum satisfies the window-generic core:
b ≥ 1 − 2w/L ≥ 3/4 ≥ 1/2 ([eq:abdef] + [eq:wrange]), g ≥ 0 (plateau bound). 

### `EventuallyAtCore`

 "uniformly for T ≥ T₀", Core-quantified: stronger than EventuallyAt
(fewer hypotheses on F). 

 Core copies of the LocalHyps helper lemmas (same names under the Core namespace). 

### `LocalHypsCoreW`

 Window-generic taper facts without the bandwidth cap λ ≤ 1 — the family regime is
λ = L/l ∈ (1, 2) (family window L = log(qT/2π), so L > l).
This regime goes beyond the paper: §5's statements all assume λ ≤ 1; nothing Core-typed is
re-typed here — this is a purely additive split: fields = LocalHypsCore's minus lam_le_one, and
LocalHypsCore.toCoreW below.  Consumed only by the family-average statements. 

### `LocalHypsCoreW.four_le_cϱ`

 [eq:phinorms] `c_ϱ ≥ 4`. 

### `LocalHypsCoreW.lam_pos`

 `0 < λ` [Notation] (no upper cap here). 

### `LocalHypsCoreW.one_le_w`

 [eq:wrange] `1 ≤ w ≤ L/8` (forces `L ≥ 8`). 

### `LocalHypsCoreW.one_le_l`

 "T is large": `l ≥ 1`, i.e. `T ≥ 2πe`. 

### `LocalHypsCoreW.phiHat_cont`

 φ̂ real-analytic facts: continuity; evenness (φ even) [§2.2 "φ̂ and Φ are real, even, entire"]. 

### `LocalHypsCoreW.phiHat_le_L`

 [eq:psidef] `|φ̂(r)| ≤ ψ(r) := min(L, 2/|r|, c_ϱ/(w r²))`, split into three division-free bounds. 

### `LocalHypsCoreW.phiHat_sq_integrable`

 Integrability consequences of [eq:psidef] (`φ̂² ≤ ψ² ≤ min(L², c_ϱ²/(w²r⁴))`), and
  [eq:psiints] in the packaged form `∫ φ̂(r)²|r| dr ≤ ∫ ψ²|r| = 8 + 8 log(c_ϱL/4w)` (§2.2, used at
  §5.2 "∫ φ̂(r)²|r| dr ≪ log L"). 

### `LocalHypsCoreW.phiHat_sq_mul_sq_integrable`

 also from [eq:psidef]: `φ̂(r)²r² ≤ min(4, (c_ϱ/w)²/r²)`, so `∫ φ̂(r)² r² dr ≤ 8 + 2(c_ϱ/w)²`
  (used for the `|r| > τ_k/2` tails at §5.2 in place of the paper's sharper r⁻⁴ bound). 

### `LocalHypsCoreW.phiHat_sq_integral`

 `∫ φ̂(r)² dr = 2π ∫ φ² = 2π a L` [prop:trace proof, §5.2; Plancherel in the paper's
  convention `∫ f ḡ = (2π)⁻¹ ∫ f̂ conj ĝ` + eq:abdef]. 

### `LocalHypsCoreW.phiHat_sq_fourier`

 `φ̂² = Â_φ` on ℝ [§2.2] + Fourier inversion, in the real form used at §5.2:
  `∫ φ̂(r)² cos(ry) dr = 2π A_φ(y)` (`φ̂²` even, `A_φ` even, continuous, supported in `[−L,L]`). 

### `LocalHypsCoreW.g_nonneg`

 window-generic remnant of [eq:gbounds]: `g ≥ 0` and `g ≤ A_φ ≤ (L−|y|)₊`
  (the flat-top plateau lower bound `(L−2w−|y|)₊ ≤ g` is NOT here — see §7.1). 

### `LocalHypsCoreW.Phi_contDiff`

 Φ facts: `Φ` is C¹ (indeed entire), even [§2.2]. 

### `LocalHypsCoreW.Phi_le_L`

 [eq:psidef] `|Φ(r)| ≤ ψ(r)`, three division-free bounds. 

### `LocalHypsCoreW.Phi_sq_integrable`

 Integrability consequences of [eq:psidef] for Φ, and [eq:psiints] packaged as
  `∫ Φ(x)²|x| dx ≤ 8 + 8 log(c_ϱL/4w)` (§5.4 "∫Φ(x)²|x|dx ≪ log L (by (eq:psidef), (eq:psiints))"). 

### `LocalHypsCoreW.Phi_sq_mul_sq_integrable`

 second moment of `Φ²` (same [eq:psidef] path as the `φ̂` version; needed against the
  `10r²/t` term of `mu_increment_bound` in [prop:mumu]). 

### `LocalHypsCoreW.Phi_zero`

 `Φ(0) = aL` [§2.2]. 

### `LocalHypsCoreW.Phi_sq_integral`

 `∫_ℝ Φ² = 2π g(0) = 2π b L` [§2.2]. 

### `LocalHypsCoreW.Phi_sq_fourier`

 [eq:Phi2FT] `∫_ℝ Φ(x)² e^{ixy} dx = 2π g(y)` (§5.4), real form (`Φ²`, `g` even). 

### `LocalHypsCoreW.poisson`

 [lem:poisson] (★) `Σ_{k∈ℤ} φ̂(τ−τ_k) φ̂(τ'−τ_k) = L Φ(τ−τ')` (§2.2). 

### `LocalHypsCoreW.b_ge_half`

 window-generic remnant of [eq:abdef]: `1/2 ≤ b ≤ a ≤ 1` (the flat-top `1 − 2w/L ≤ b`
  is NOT here; 1/2 suffices for every positivity/division use and holds for the
  Montgomery–Taylor window). 

### `LocalHypsCoreW.psi_integrable`

 [eq:psidef] in majorant form, with the [eq:psiints] integrals (`Ψ₀ = 4 + 2log(c_ϱL/4w)`,
  `∫ψ² ≤ 8L`) — fields match `Zeta23.Params.psi'_integrable / psi'_sq_integrable /
  integral_psi'_Ioi_le / integral_psi'_sq_le` in Zeta23/Taper.lean (consumed by [lem:ends]). 

### `LocalHypsCoreW.phiHat_le_psi`

 `|φ̂| ≤ ψ` and `|Φ| ≤ ψ` [eq:psidef] in the majorant form used by [lem:ends]. 

### `LocalHypsCoreW.PiX_cont`

 Π_X is continuous and [eq:PiPfacts] `|Π_X(τ)| ≤ 3√X/(1+|τ|)` (§2.1), for the concrete
  `Zeta23.PiX X` [eq:Pidef] — see `PiX_bound` (holds for all `X ≥ 1`) / `PiX_continuous`. 

### `LocalHypsCore.toCoreW`

 every flat-top taper datum satisfies the window-generic core:
b ≥ 1 − 2w/L ≥ 3/4 ≥ 1/2 ([eq:abdef] + [eq:wrange]), g ≥ 0 (plateau bound). 

### `PX_abs_le`

 H-cheb [eq:cheb1] ⇒ `|P_X(τ)| ≤ (1/π) Σ_{n≤X} Λ(n)/√n ≤ (3/π)√X ≤ √X` for `X ≥ x₀`
([eq:PiPfacts] second half, §2.1; used as `|P_X| ≤ √X` at §5.4). 

### `mu_abs_le_l`

 H-Γ [eq:mufacts] ⇒ for `T ≥ T₀`: `|μ(τ)| ≤ l` on `I = [T,2T]` (the paper's `0 < μ ≤ l on I`,
§5.4; only the two-sided bound is needed). 

 ### Elementary lemmas for [prop:trace] 

### `two_sin_mul_sum_cos`

 Telescoping identity behind the Dirichlet-kernel bound (§5.2):
`2 sin(θ/2) Σ_{k<d} cos(α + kθ) = sin(α + dθ − θ/2) − sin(α − θ/2)`. 

### `abs_sin_mul_abs_sum_cos_le`

 §5.2 `|Σ_{k<d} e^{ikhy}| ≤ |sin(hy/2)|⁻¹`, in the division-free real form
`|sin(θ/2)| · |Σ_{k<d} cos(α + kθ)| ≤ 1`. 

### `two_min_div_le_sin`

 Jordan's inequality on `[0, π]`: for `0 ≤ y ≤ L`, `sin(πy/L) ≥ 2 min(y, L−y)/L` (§5.2:
`|sin(πy/L)|⁻¹ ≤ L/(2 min(y, L−y))`). 

### `Aphi_mul_sum_cos_le`

 The P-part pointwise bound of [prop:trace] (§5.2): for `y ≥ log 2`,
`A_φ(y) |Σ_{k<d} cos(τ_k y)| ≤ L²/(2 log 2)`  (using `τ_k = T + kh`, `h = 2π/L`,
`0 ≤ A_φ(y) ≤ (L−y)₊` [eq:gbounds], the Dirichlet-kernel bound and Jordan's inequality;
for `y ≥ L` the left side vanishes). 

### `riemann_sum_monotone`

 Unit-step Riemann sums of a monotone function (Mathlib) rescaled to step `h` and combined:
for `μ` monotone and `≥ 0` on `[T−h, ∞)`, `0 < h ≤ T`, `d = ⌊T/h⌋` (§5.2:
`h Σ_{k=0}^{d−1} μ(τ_k) = ∫_T^{2T} μ + O(h μ(2T))`, `recall T < T + dh ≤ 2T < T + (d+1)h`). 

 ### Analytic lemmas for [prop:trace]: growth and increments of μ, decay of Π_X 

### `mu_linear_bound`

 From H-Γ [eq:mufacts]: a crude global bound `|μ(τ)| ≤ M + |τ|` (used only to control the
`|r| > τ_k/2` tails, §5.2 "|μ(τ_k+r) − μ(τ_k)| ≪ l + log(2+|r|)"). 

### `mu_increment_bound`

 From H-Γ [eq:mufacts] `μ' ≪ |τ|⁻¹` + the crude bound: for `t ≥ 2` and all `r`,
`|μ(t+r) − μ(t)| ≤ (K|r| + 10r²)/t`.  (§5.2: `≪ |r|/T` for `|r| ≤ τ_k/2` by the mean value
theorem; for `|r| > τ_k/2` we use `2|r|/t > 1` to absorb the crude bound into the `r²/t` term.) 

### `PiX_shift_bound`

 [eq:PiPfacts] shifted (§5.2: `|Π_X(τ)| ≤ 6√X/T for |τ−τ_k| ≤ T/2`, and the tail absorbed via
`(2|r|/t)² > 1`): for `t ≥ 2` and all `r`, `|Π_X(t+r)| ≤ 6√X/t + 12√X r²/t²`. 

### `integral_phiHat_sq_mul_sin`

 `∫ φ̂(r)² sin(ry) dr = 0` (odd integrand; `φ̂` even). 

### `integral_phiHat_sq_mul_cos_shift`

 §5.2: `∫ φ̂(τ−τ_k)² cos(τy) dτ = 2π A_φ(y) cos(τ_k y)`, after the substitution `τ = t + r`:
`∫ φ̂(r)² cos((t+r)y) dr = 2π A_φ(y) cos(ty)` (from `φ̂² = Â_φ` + inversion, field `phiHat_sq_fourier`). 

### `P_part_eq`

 **P-part of [prop:trace] at one grid point** (§5.2):
`G^P_kk = ∫ φ̂(r)² P_X(τ_k+r) dr = −2 Σ_{n≤X} a_n A_φ(y_n) cos(τ_k y_n)`. 

### `mu_part_bound`

 **μ-part of [prop:trace] at one grid point** (§5.2: `G^μ_kk = 2πaL μ(τ_k) + O(log L/T)`):
for `t ≥ 2`, `|∫ φ̂(r)² μ(t+r) dr − 2πaL·μ(t)| ≤ (K ∫φ̂²|r| + 10 ∫φ̂²r²)/t`, with `K` from
`mu_increment_bound`. 

### `Pi_part_bound`

 **Π-part of [prop:trace] at one grid point** (§5.2: `|G^Π_kk| ≤ 6√X·2πaL/T + O(√X T⁻³)`):
for `t ≥ 2`, `|∫ φ̂(r)² Π_X(t+r) dr| ≤ (6√X/t)·2πaL + (12√X/t²)·∫φ̂²r²`. 

### `Pi_part_integrable`

 Integrability of `φ̂(r)² Π_X(t+r)` (bounded × integrable). 

### `P_part_integrable`

 Integrability of `φ̂(r)² P_X(t+r)` (bounded × integrable). 

### `mu_part_integrable`

 Integrability of `φ̂(r)² μ(t+r)` for `t > 0` (`|μ| ≤ M + |τ|` and `∫φ̂²|r| < ∞`). 

### `GentryA_diag_eq`

 **Decomposition of a diagonal entry** (§5.2: `G_kk = ∫ φ̂(τ−τ_k)² ν_X(τ)dτ =: G^μ_kk +
G^Π_kk + G^P_kk according to (eq:nudef)`), after translating `τ = τ_k + r`. 

### `mu_nonneg_eventually`

 H-Γ ⇒ `μ ≥ 0` far out (Stirling): `∃ τ₀ ≥ 0, μ ≥ 0 on [τ₀, ∞)` (the paper's "μ is positive …
on [T−h, 2T]", §5.2). 

### `sum_P_part_bound`

 **Sum of the P-parts** (§5.2): `|Σ_{k<d} G^P_kk| ≤ (L²/log 2) Σ_{n≤X} a_n`. 

### `Setting.d_le`

 The grid: `τ_k ∈ [T, 2T]` for `0 ≤ k < d` (§2.2 "τ_0,…,τ_{d−1} ∈ [T,2T)"), and `d ≤ LT/2π`. 

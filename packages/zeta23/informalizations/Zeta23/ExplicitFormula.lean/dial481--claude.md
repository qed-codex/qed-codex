---
{
  "module": "Zeta23/ExplicitFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ExplicitFormula.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ExplicitFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ExplicitFormula.lean  —  the explicit formula, normalisations (paper App. A [app:EF]).

The *normalisation chain*: the passage from a literature-verbatim explicit formula to the paper's
density ν_X = μ + Π_X + P_X [eq:mudef]–[eq:nudef], with every 2π and every sign:

  * `EF.literatureRHS` / `EF_lit` : the right-hand side of [eq:EFstd] (App. A, first display), i.e. the
    Weil explicit formula in the form the paper quotes from [IK04, Thm 5.12] / [Wei52] / [Bom00],
    for a single test function k ∈ C_c²(ℝ) with h(z) := ∫ k(u) e^{izu} du;
  * `EF.prop_EF_of_lit` : [eq:EFstd] for k := f ⋆ g̃  ⟹  [eq:EF]  W(f,g) = ∫ h_f(τ) conj(h_g(τ)) ν_X(τ) dτ,
    X = e^L, for f, g ∈ C_c²(ℝ) supported in [−L/2, L/2]  — exactly App. A's three identifications
    (Gamma term, prime term, pole term) plus h_{f⋆g̃}(z) = h_f(z)·conj(h_g(conj z)).

The truth of [eq:EFstd] itself (contour integration of
h((s-1/2)/i)·ξ'/ξ(s)) is the hypothesis `EF_lit`, stated for the zero configuration
abstractly.

CONVENTIONS (paper [Notation]).  Paper Fourier transform:
    f̂(τ) = h_f(τ) := ∫_ℝ f(u) e^{iτu} du,   inversion  f(u) = (1/2π) ∫_ℝ h_f(r) e^{-iru} dr.
Mathlib: 𝓕 f w = ∫ v, exp(-2πi v w) • f v.  Dictionary (proved below, `paperFT_ofReal_eq_fourier`):
    h_f(τ) = 𝓕 f (-τ/(2π)).
-/
```

 ### App. A objects owned by this file 

### `tilde`

 App. A: `g̃(u) := conj (g(−u))`. 

### `weilTest`

 App. A: the Weil test function `k := f ⋆ g̃`, i.e. `k(x) = ∫ f(t) g̃(x − t) dt`
(Mathlib convolution w.r.t. Lebesgue measure and the ℝ-bilinear map `ContinuousLinearMap.mul ℝ ℂ`). 

 ## The literature form [eq:EFstd] 

### `gammaBracket`

 The Gamma-factor bracket in [eq:EFstd]: `Re Γ'/Γ(1/4 + ir/2) − log π`
( = Γ_ℝ'/Γ_ℝ(1/2+ir) + Γ_ℝ'/Γ_ℝ(1/2−ir), Γ_ℝ(s) = π^{-s/2}Γ(s/2); equals 2π μ(r) by [eq:mudef]).
Γ'/Γ is spelled `Complex.digamma` (= logDeriv Gamma), identically to `Zeta23.mu` in Defs.lean. 

### `literatureRHS`

 Right-hand side of [eq:EFstd] (App. A, first display), VERBATIM:
`h(i/2) + h(−i/2) − Σ_{n≥1} Λ(n) n^{-1/2} (k(log n) + k(−log n)) + (1/2π) ∫_ℝ h(r) [Re Γ'/Γ(1/4 + ir/2) − log π] dr`
with `h := paperFT k`.  The n-sum is written over all `n : ℕ` (Λ(0) = Λ(1) = 0); for compactly supported k it
has finite support. 

### `EF_lit`

 **H-EF, literature form** ([eq:EFstd]; [IK04, Thm 5.12] specialised to ζ / [Wei52] / [Bom00]):
for every `k ∈ C_c²(ℝ)` with `h(z) := ∫ k(u)e^{izu}du`,
`Σ_ρ m_ρ h(γ_ρ) = literatureRHS k`, the zero sum converging absolutely (paper: "here absolutely
convergent since h(r) ≪_k (1+|r|)^{-2} on |Im r| ≤ 1/2").  It is a hypothesis
(structure field in Hypotheses.lean), never a Lean axiom. 

### `EF_paper`

 **H-EF, paper form** ([prop:EF], [eq:EF]): for `f, g ∈ C_c²(ℝ)` with supports in `[−L/2, L/2]`,
`W(f,g) = ∫_ℝ h_f(τ) conj(h_g(τ)) ν_X(τ) dτ`, `X = e^L`. 

 ## ℂ-specialised integral helpers

(In this toolchain `rw [← integral_const_mul]` fails to key-match on ℂ-valued integrals because the
RCLike-generic lemma elaborates `Mul ℂ`/`NormedAddCommGroup ℂ` through a different instance path than
a goal written with `*`; restating the lemmas at ℂ (proved by `exact`) makes `rw` usable.) 

 ## Dictionary with Mathlib's Fourier transform 

### `paperFT_ofReal_eq_fourier`

 `h_k(τ) = 𝓕 k (−τ/(2π))` for real τ. 

### `integrable_paperFT_ofReal`

 `h_k` is integrable on the real line when `𝓕 k` is (dictionary + linear substitution). 

### `paper_inversion`

 Paper inversion `k(u) = (1/2π) ∫ h(r) e^{−iru} dr` (App. A, "so that …"), from Mathlib's
`Continuous.fourierInv_fourier_eq` and the substitution `v = −r/(2π)`. 

 ## The test function k = f ⋆ g̃ 

### `paperFT_weilTest`

 App. A: `h_{f⋆g̃}(z) = h_f(z) · conj(h_g(conj z))` for all complex z. 

### `tsupport_weilTest_subset`

 App. A: `supp k ⊆ [−L, L]` when `supp f, supp g ⊆ [−L/2, L/2]`. 

 ## App. A: the three identifications 

### `gamma_term`

 *Gamma term*: `(1/2π) ∫ h(r)[Re Γ'/Γ(1/4+ir/2) − log π] dr = ∫ h μ` — definitional ([eq:mudef]). 

### `hasCompactSupport_of_tsupport_subset`

 Compact support from a support bound. 

### `integrable_paperFT_mul_cexp`

 `h(r) e^{-irw}` is integrable in r when h is. 

### `integrable_paperFT_mul_cos`

 `h(r) cos(r y)` is integrable in r when h is. 

### `k_add_k_neg`

 App. A, *prime term*, first step: `k(y) + k(−y) = (1/2π)∫ h(τ)(e^{−iτy}+e^{iτy})dτ = (1/π) ∫ h(τ) cos(τy) dτ`. 

### `prime_summand_eq_zero`

 App. A, *prime term*, support step: `k(±log n) = 0` for `n > X = e^L`; and the n = 0 term
vanishes since Λ(0) = 0.  Hence the n-sum in [eq:EFstd] is the finite sum over `0 < n ≤ ⌊X⌋`. 

### `prime_term`

 *Prime term*: for k continuous with `supp k ⊆ [−L, L]` and h integrable on ℝ,
`−Σ_{n≥1} Λ(n)n^{-1/2}(k(log n)+k(−log n)) = ∫ h P_X`, `X = e^L`
(uses inversion: `k(y)+k(−y) = (1/π)∫ h(τ)cos(τy)dτ`, and `k(±log n) = 0` for `n > X`). 

 ### Pole term: inversion + Fubini, and the two explicit integrals 

### `integrable_inversion_kernel`

 Joint integrability of `(u,τ) ↦ h(τ) e^{−iτu} E(u)` for integrable h (on ℝ) and E. 

### `integral_k_mul_weight`

 App. A, "inserting `k(u) = (1/2π)∫ h(τ)e^{−iτu}dτ` and interchanging (all integrals absolutely
convergent)": for an integrable weight E,  `∫ k(u)E(u)du = (1/2π) ∫ h(τ) (∫ E(u)e^{−iτu}du) dτ`. 

### `integrable_paperFT_mul_weightFT`

 The τ-integrand produced by `integral_k_mul_weight` is integrable (Fubini). 

### `integrable_exp_neg_abs_half_mul`

 Integrability of `u ↦ e^{−|u|/2} e^{−iτu}` on ℝ (two half-lines). 

### `integral_exp_neg_abs_half`

 App. A: `∫_ℝ e^{−|u|/2} e^{−iτu} du = (1/4 + τ²)^{−1}`. 

### `EL`

 The truncated growing weight `E_L(u) := 1_{[−L,L]}(u) e^{|u|/2}`. 

### `exp_cpow`

 `X^s = e^{Ls}` for `X = e^L`. 

### `integral_EL_mul`

 App. A: `∫_{−L}^{L} e^{|u|/2}e^{−iτu}du = 2Re∫_0^L e^{us̄}du = 2Re((X^s−1)/s)`, `s = 1/2+iτ`,
`X = e^L`. 

### `pole_term`

 *Pole term*: for k continuous with `supp k ⊆ [−L, L]` and h integrable on ℝ,
`h(i/2) + h(−i/2) = ∫ h Π_X`, `X = e^L`
(uses `∫_ℝ e^{−|u|/2}e^{−iτu}du = (1/4+τ²)^{-1}` and `∫_{−L}^{L} e^{|u|/2}e^{−iτu}du = 2Re((X^s−1)/s)`). 

 ### Integrability of the three densities against h (from the computations above) 

### `integrable_paperFT_mul_nuX`

 `h·ν_X` is integrable, given that `h·μ` is (μ grows like log|τ|, so this last fact needs the
decay [eq:hfbound] of h and the Stirling bound [eq:mufacts]; it is supplied by the caller). 

 ## Adding up 

### `literatureRHS_eq_integral_nu`

 App. A, "Adding the three identifications gives (eq:EF)": the literature right-hand side equals
`∫ h ν_X`, `X = e^L`, for k ∈ C_c(ℝ) with `supp k ⊆ [−L, L]`, `𝓕 k` integrable and `h·μ` integrable. 

 ## [prop:EF] from the literature form 

### `prop_EF_of_lit`

 **Main theorem.**  [eq:EFstd] (hypothesis `EF_lit`) ⟹ [eq:EF] for the pair (f,g):
`W(f,g) = ∫ h_f(τ) conj(h_g(τ)) ν_X(τ) dτ`, `X = e^L`.
Side hypotheses `hFk`, `hμ` are the two integrability facts App. A uses silently
("all integrals absolutely convergent") for k = f ⋆ g̃; both follow from [eq:hfbound] and [eq:mufacts]. 

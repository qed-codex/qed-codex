---
{
  "module": "Zeta23/Poisson.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Poisson.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Poisson.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
[lem:poisson] "Poisson summation for the Gabor system", the paper §2.2:

  "For all τ, τ' ∈ ℝ,
     K_∞(τ,τ') := Σ_{k∈ℤ} φ̂(τ−τ_k) φ̂(τ'−τ_k) = L·Φ(τ−τ'),   in particular   Σ_{k∈ℤ} φ̂(τ−τ_k)² = aL²."

Here τ_k := T + k h, h := 2π/L [eq:fk], Φ := (φ²)^ [eq:PhigA], a := L⁻¹∫φ² [eq:abdef], and
φ̂(s) = ∫ φ(u) e^{isu} du is the paper's Fourier convention (`Zeta23.paperFT`).  Only the
real-argument identity is proved (that is all [prop:block](ii) uses; the complex continuation
mentioned in [rem:pairblock] is not used by the proof).

Proof route (the paper's, rearranged so that Fourier inversion is not needed): with
  G(ξ) := L · ∫ φ(u) φ(Lξ−u) e^{i(τu + τ'(Lξ−u) − TLξ)} du      (= L e^{−iTLξ}(φ_τ ∗ φ_{τ'})(Lξ)),
G is continuous with support in [−1,1] and G(k) = 0 for k ∈ ℤ∖{0} (because φ(u) = 0 for
|u| ≥ L/2), G(0) = L ∫ φ(u)φ(−u)e^{i(τ−τ')u} du = L Φ(τ−τ') (φ even), and a Fubini computation
gives 𝓕G(w) = φ̂(τ−τ_w) φ̂(τ'−τ_w) for Mathlib's 𝓕 and every real w (τ_w := T + w·2π/L).
Mathlib's Poisson summation `Real.tsum_eq_tsum_fourier_of_rpow_decay_of_summable`
(Σ_k G(k) = Σ_n 𝓕G(n)) then gives the claim; summability of n ↦ φ̂(τ−τ_n)φ̂(τ'−τ_n) comes from
the decay |φ̂(r)| ≪ (1+r²)⁻¹, i.e. [eq:hfbound]/[eq:psidef].
-/
```

 #### A decay-to-`IsBigO` lemma 

### `isBigO_of_decay`

 If `‖g w‖ · (1 + (c − w h)²) ≤ C` for all real `w` (`h ≠ 0`) then `g = O(|w|⁻²)` on
`cocompact ℝ`. 

 #### The auxiliary function `G` 

### `gInt`

 Integrand of `G`: `(ξ,u) ↦ L φ(u) φ(Lξ−u) e^{i(τu + τ'(Lξ−u) − TLξ)}`. 

### `Gaux`

 `G(ξ) := L ∫ φ(u) φ(Lξ−u) e^{i(τu + τ'(Lξ−u) − TLξ)} du` (see module docstring). 

### `Gaux_continuous`

 `G` is continuous. 

### `Gaux_eq_zero`

 `G(ξ) = 0` for `|ξ| ≥ 1`. 

### `Gaux_zero`

 `G(0) = L · (φ²)^(τ − τ')` (uses φ even). 

### `cexp_bookkeeping`

 The exponent bookkeeping: for `L ≠ 0`,
`e^{i(τu + τ'(Lξ−u) − TLξ)} · e^{−2πiξw} = e^{iαu} · e^{iβ(Lξ−u)}` with
`α = τ − (T + w·2π/L)`, `β = τ' − (T + w·2π/L)`. 

### `fourier_Gaux`

 Fubini computation: `𝓕G(w) = φ̂(τ − τ_w) φ̂(τ' − τ_w)`, `τ_w = T + w·2π/L`. 

 #### The abstract identity 

### `hasSum_paperFT_mul_paperFT`

 Core identity [lem:poisson], complex form, for an abstract window: `φ : ℝ → ℝ` continuous,
even, vanishing for `|u| ≥ L/2` (`L > 0`), with `|φ̂(s)|(1+s²)` bounded on ℝ.
For all real `T, τ, τ'`:  `Σ_{k∈ℤ} φ̂(τ−τ_k) φ̂(τ'−τ_k) = L · (φ²)^(τ−τ')`, `τ_k = T + k·2π/L`,
as a `HasSum`. 

### `phiHat_decay`

 Decay input for Poisson: `|φ̂(s)|(1 + s²) ≤ L + C₁` on ℝ (from [eq:hfbound] at `y = 0`). 

### `hasSum_phiHatR_mul`

 [lem:poisson], general form, real-valued:
`Σ_{k∈ℤ} φ̂(τ−τ_k) φ̂(τ'−τ_k) = L Φ(τ−τ')` with `τ_k = T + k·(2π/L)`. 

### `hasSum_phiHatR_sq`

 [lem:poisson], "in particular": `Σ_{k∈ℤ} φ̂(γ−τ_k)² = a L²` for every real `γ`. 

### `hasSum_phiHatR_mul`

 [lem:poisson] for the paper's data: for all real τ, τ',
`HasSum (k ↦ φ̂(τ − τ_k) φ̂(τ' − τ_k)) (L Φ(τ − τ'))`, `τ_k = P.tau T k = T + k·(2π/L)`. 

### `hasSum_phiHatR_sq`

 [lem:poisson] "in particular": `HasSum (k ↦ φ̂(γ − τ_k)²) (a L²)` for every real γ. 

---
{
  "module": "Zeta23/Taper/Fourier.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Fourier.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Fourier.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — Taper/Fourier.lean  (Fourier-side facts about the taper).
Canonical text: the paper, §2.2 [subsec:family]:
  "Thus φ̂ and Φ are real, even, entire; φ̂(0) ≤ L, Φ(0) = aL; φ̂² = Â_φ and Φ² = ĝ on ℝ;
   ∫_ℝ Φ² = 2π g(0) = 2π bL; g and A_φ are even".
Conventions: generic parameters (ϱ : ℝ → ℝ) (L w : ℝ); paper's
side condition is 1 ≤ w ≤ L/8 [eq:wrange]; each lemma carries the minimal hypothesis it needs.
The decay needed for integrability is taken directly
from Zeta23/Poisson/PaperFT.lean (norm_paperFT_le, norm_paperFT_mul_sq_le).

MATHLIB INVENTORY, what this file leans on:
* dictionary  Zeta23.paperFT_ofReal_eq_fourier : paperFT f s = 𝓕 f (-s/(2π))  (PaperFT.lean);
* convolution theorem  Real.fourier_mul_convolution_eq  (Mathlib/Analysis/Fourier/Convolution.lean)
  for integrable + continuous f₁ f₂ : ℝ → ℂ, 𝓕 (f₁ ⋆[mul ℂ ℂ] f₂) = 𝓕 f₁ · 𝓕 f₂ — the paper's
  autocorrelation (v ⋆ v)(y) = ∫ v(u) v(u+y) du coincides with Mathlib's convolution for EVEN v;
* Fourier inversion  MeasureTheory.Integrable.fourierInv_fourier_eq  (Mathlib/Analysis/Fourier/
  Inversion.lean): f, 𝓕 f integrable, f continuous at v ⇒ 𝓕⁻ (𝓕 f) v = f v.  "Plancherel"
  ∫ φ̂² = 2π ∫ φ² is obtained as inversion of Â_φ = φ̂² at 0 (no L² theory needed);
* smoothness  Real.contDiff_fourier  (Mathlib/Analysis/Fourier/FourierTransformDeriv.lean);
* integrable_inv_one_add_sq  (dominating function (1+r²)⁻¹ for the decay |φ̂(r)| ≤ min(C₀, C₂/r²)).
-/
```

 ### ℂ-specialized restatements of RCLike-generic integral lemmas
(same workaround as `integral_const_mul_C` in PaperFT.lean: `rw` with the
RCLike-stated lemma can fail to unify the `NormedAddCommGroup ℂ` instance path). 

 ## Generic facts about the paper-convention transform `h_v(z) = ∫ v(u) e^{izu} du` of a REAL
function `v`.  Everything in the [eq:PhigA] sentence is an instance of these with `v = φ` or `v = φ²`. 

### `conj_paperFT_ofReal`

 For real `v`: `conj h_v(z) = h_v(−conj z)`. 

### `paperFT_neg_of_even`

 For even `v`: `h_v(−z) = h_v(z)` (all complex `z`). 

### `paperFT_ofReal_eq_re`

 For real even `v` and real `r`, `h_v(r)` is real. 

### `contDiff_paperFT_ofReal`

 `h_v` restricted to ℝ is smooth when `v` is continuous with compact support
(via the dictionary to Mathlib's `𝓕` and `Real.contDiff_fourier`). Stated for complex-valued `f`. 

### `integrable_of_abs_mul_one_add_sq_le`

 A continuous `h : ℝ → ℝ` with `|h r| (1 + r²) ≤ K` is integrable (dominated by `K/(1+r²)`). 

### `integrable_re_paperFT_sq_and`

 Integrability of `(Re h_f)²` and `(Re h_f)² |r|` on ℝ for `f ∈ C_c²`, from the decay
[eq:hfbound]: `|h_f(r)| ≤ ‖f‖₁` and `|h_f(r)| r² ≤ ‖f''‖₁` (Zeta23.norm_paperFT_le / norm_paperFT_mul_sq_le). 

 ### The paper's autocorrelation `(v ⋆ v)(y) := ∫ v(u) v(u+y) du` [eq:PhigA] versus Mathlib's convolution 

### `autocorr_neg`

 `v ⋆ v` is even (no hypothesis on `v`: substitute `u ↦ u − y`). 

### `ofReal_autocorr_eq_convolution`

 For EVEN real `v`, the complexified autocorrelation is Mathlib's convolution `v_ℂ ⋆ v_ℂ`:
`∫ v(u)v(u+y) du = ∫ v(t) v(y−t) dt` (substitute `u = −t`, use `v(−t) = v(t)`). 

### `paperFT_autocorr`

 `(v ⋆ v)^ = (v̂)²` on ℝ for even real continuous compactly supported `v` — the paper's
"`(f∗g)^ = f̂ ĝ`" [Notation] through the dictionary and `Real.fourier_mul_convolution_eq`. 

 ## Fourier inversion in the paper's convention, cosine form 

### `integral_mul_cos_of_paperFT_eq`

 If `A : ℝ → ℝ` is continuous and integrable and `h_A(r) = G(r)` (`r ∈ ℝ`) with `G` real and
integrable, then `∫ G(r) cos(ry) dr = 2π A(y)`.  (Inversion `A = 𝓕⁻ 𝓕 A`, the substitution
`r = −2πξ`, and real parts; the sine part drops because `A` is real.)  This is the form in which
the paper uses "Fourier inversion" for `A_φ` [prop:trace, P-part] and `g` [eq:Phi2FT]. 

 ## "`φ̂` and `Φ` are real, even, entire; …" (facts stated after [eq:PhigA]) 

 #### auxiliary packaging of φ and φ² as inputs to the generic lemmas 

### `phiC_supp`

 alias of `Strip.phiC_support`. 

 #### real / even / conjugation symmetry (hypothesis-free: only "φ real and even" is used) 

### `phiHat_ofReal`

 `φ̂` real on ℝ: `φ̂(r) = ↑(Re φ̂(r))` for real `r` (φ even and real). 

### `phiHat_conj`

 "since `φ̂` is real on ℝ we have `conj φ̂(z̄) = φ̂(z)`" [text after eq:fk], stated as
`φ̂(conj z) = conj (φ̂ z)`. 

 #### continuity / differentiability on ℝ ("entire" is more than any consumer needs) 

### `PhiR_contDiff_one`

 `Φ` is `C¹` on ℝ (indeed entire; C¹ is what [prop:cross] differentiates). 

 #### values at 0 

### `paperFT_ofReal_zero`

 `h_f(0) = ∫ f` for a real `f` (cast to ℂ). 

### `phiHatR_zero_le`

 "`φ̂(0) ≤ L`". 

### `PhiR_zero`

 "`Φ(0) = aL`". 

 #### "`φ̂² = Â_φ` and `Φ² = ĝ` on ℝ" — convolution theorem 

### `phiHatR_sq_eq`

 "`φ̂² = (A_φ)^` on ℝ". 

### `PhiR_sq_eq`

 "`Φ² = ĝ` on ℝ". 

 #### integrability of `φ̂², φ̂²|r|, Φ², Φ²|r|` (decay [eq:hfbound] via PaperFT.lean) 

 #### Plancherel / inversion identities 

### `integral_phiHatR_sq_mul_cos`

 Fourier inversion of `φ̂² = (A_φ)^` in cosine form: `∫ φ̂(r)² cos(ry) dr = 2π A_φ(y)`
(used at [prop:trace] P-part: "∫φ̂(τ−τ_k)²cos(τy)dτ = 2πA_φ(y)cos(τ_k y)"). 

### `integral_PhiR_sq_mul_cos`

 [eq:Phi2FT]: "`∫_ℝ Φ(x)² e^{ixy} dx = 2π g(y)` (`y ∈ ℝ`)", in cosine form (`Φ²` is even
and real, so the sine part vanishes). 

### `integral_phiHatR_sq`

 `∫ φ̂(r)² dr = 2π ∫ φ² = 2π a L` (Plancherel; [prop:trace] μ-part, "∫φ̂(r)²dr = 2π∫φ² = 2πaL").
Obtained as the `y = 0` case of the inversion formula, with `A_φ(0) = ∫φ² = aL`. 

### `integral_PhiR_sq`

 "`∫_ℝ Φ² = 2π g(0) = 2π b L`". 

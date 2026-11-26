---
{
  "module": "Zeta23/ThmE/EFLitChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/EFLitChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/EFLitChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/EFLitChi.lean — the literature-form explicit formula for L(s,χ)
(primitive χ mod q > 1) and its bridge to ExplicitFormulaPaperChi.

The paper does not display the χ-EF ([thm:E] proof (i),
§8.2, says only "the derivation of Appendix A applies to [IK04, Theorem 5.12] for
L(s,χ)"); literatureRHSchi below is a transcription of IK04-Thm-5.12-for-L(s,χ), with
the χ/conj(χ) leg assignment forced by the paper's ν-side display P_{X,χ} (§8.2).

Conventions: h := paperFT k (h(z) = ∫k(u)e^{izu}du); κ = (1−χ(−1))/2; no pole terms (Λ(s,χ)
entire for primitive χ, q > 1); coefficients c n = (coeff χ) n (the character values ℕ → ℂ).
-/
```

### `literatureRHSchi`

 Right-hand side of the literature explicit formula for L(s,χ), primitive χ mod q > 1
(IK04 Thm 5.12 specialised; transcription — see file header):
  −Σ_{n≥1} (Λ(n)/√n)(c(n) k(log n) + conj(c(n)) k(−log n))
    + (1/2π)∫_ℝ h(r)·[Re ψ(1/4 + κ/2 + ir/2) + log(q/π)] dr. 

### `EF_lit_chi`

 **H-EF(χ), literature form**: for every k ∈ C_c²(ℝ), the zero sum converges absolutely and
  Σ_ρ m_ρ h(γ_ρ) = literatureRHSchi. 

### `integrable_paperFT_mul_sin`

 Twisted prime term (mirror of Zeta23.EF.prime_term): the c-twisted prime sum equals
∫ h·P_{X,χ} — transcription target: P_{X,χ} = −π⁻¹ Re Σ_{n≤X} Λ(n)χ(n)n^{−1/2−iτ} (§8.2);
Re-unfolding via PXc_eq_sum_cos_sin (Hypotheses.lean) assigns c(n) to the e^{−iτ log n} leg. 

### `ck_add_conj_k_neg`

 Twisted inversion pairing: cc * k(y) + conj(cc) * k(-y) equals (1/pi) times the integral of
h(tau) * (Re cc * cos(tau y) + Im cc * sin(tau y)). 

### `prime_summand_chi_eq_zero`

 Support step, twisted: the summand vanishes for n outside (0, floor(e^L)]. 

### `gamma_term_chi`

 κ-shifted archimedean term (mirror of Zeta23.EF.gamma_term): pointwise-rearrangement of the
bracket into μ_χ (muq's definition is (1/2π)(log(q/π) + Re ψ(1/4+κ/2+iτ/2))). 

### `integrable_paperFT_mul_PXc`

 Integrability of h·P_{X,χ} (finite twisted cos/sin sum; no Chebyshev input needed). 

### `literatureRHSchi_eq_integral_nu`

 Mirror of Zeta23.EF.literatureRHS_eq_integral_nu — NO pole term for q > 1. 

### `abs_muq_le_of_gammaFactsChi`

 From H-Gamma(chi): |mu_chi(tau)| <= K2 (1+|tau|)^(1/2) for all tau (continuity on [-1,1];
Stirling with log(q|tau|/2pi) and log x <= 2 x^(1/2) for |tau| >= 1). 

### `integrable_paperFT_mul_muq`

 k in C_c^2 and H-Gamma(chi) imply h_k times mu_chi is integrable. 

### `explicitFormulaPaperChi_of_lit`

 **Bridge** (App-A-for-χ, mirror of Zeta23.EF.explicitFormulaPaper_of_lit): the literature form
plus the χ-Γ facts give the paper form H-EF(χ).  [Proof: transplant of the ζ-case chain with
ν_{X,χ} = μ_χ + P_{X,χ}; side-integrabilities via the Bridge.lean toolkit (norm_paperFT bounds,
abs_mu-type from GammaFactsChi.stirling) + PXc continuity/boundedness (PXc_abs_le).] 

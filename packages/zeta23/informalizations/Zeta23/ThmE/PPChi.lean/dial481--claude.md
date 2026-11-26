---
{
  "module": "Zeta23/ThmE/PPChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/PPChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/PPChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization of the paper
"More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
-/
```


# [prop:PP] for L(s,chi)

[thm:E] proof (iii) (§8.2): "the coefficients a_n acquire unimodular factors chi(n)n^{i.}, which
leave the diagonal D unchanged (|chi(n)|^2 = 1) and enter Lemma lem:MV and all other bounds only
through |a_n|".  This file proves that sentence for [prop:PP]:

* prop_PP_chi:  |M[P_{X,c}, P_{X,c}] − (T/pi)·sumA2gCoprime| ≤ C·L²X, over EventuallyAtCore
  (window-generic: no flat-top plateau fact used); hypotheses H-cheb + H-MV + CoeffUnimodular
  (unimodularity used EXACTLY once: the diagonal main term a_n²·normSq(c n)).
* sumA2gCoprime_upper (over EventuallyAtCore) and sumA2gCoprime_lower (over the FULL EventuallyAt:
  the lower g-sandwich needs LocalHyps.g_lower, which LocalHypsCore deliberately lacks — the
  Montgomery–Taylor window case supplies its own analogue), from H-cheb-coprime.

Route (magnitude/phase): write c n = r_n·exp(i·phi_n),
r_n := norm (c n), phi_n := arg (c n), so P_{X,c}(tau) = −(1/pi)·Sum_n a_n·r_n·cos(tau·log n − phi_n)
— ONE family of phase-shifted cosines.  The PPKernel pair decomposition generalizes by a single
phase parameter (Jker already carries an arbitrary constant): AminusPh/AplusPh below.  On the
diagonal the phase difference vanishes and AminusPh = Aminus, giving the zeta diagonal with weight
r_n²; the off-diagonal [lem:MV] application takes x_n with norm x_n ≤ a_n ("only through |a_n|");
the O2 bound is phase-free.


### `sumA2gCoprime`

 Sum_{n ≤ X, (n,q)=1} Lambda(n)²/n · g(log n) — the [prop:PP] main-term sum for L(s,chi)
(index set = ChebyshevMertensCoprime's). 

### `sum_w_eq_sumA2gCoprime`

 The weighted diagonal sum equals the coprime sum, for unimodular coefficients. 

### `AminusPh`

 A⁻ with phases. 

### `AplusPh`

 A⁺ with phases. 

### `AminusPh_self`

 Equal phases: AminusPh = Aminus (the diagonal case). 

### `continuous_Jker_offset_ph`

 Continuity of the phased Jker integrand in x (mirror of continuous_Jker_offset). 

### `inner_cos_cos_ph`

 Product-to-sum with phases on the sheared window (mirror of inner_cos_cos). 

### `Mform_cos_cos_ph`

 [eq:MPP] per pair with phases: for T ≥ 0,
M[cos(·y − φ), cos(·y' − φ')] = ½ A⁻_ph + ½ A⁺_ph. 

### `abs_AplusPh_le`

 O₂-type bound, phase-free (mirror of abs_Aplus_le): for 0 < y + y',
|A⁺_ph(y,y',φ,φ')| ≤ (2/(y+y'))·∫Φ². 

### `sub_mul_AminusPh_eq`

 O₁-type exact evaluation with phases (mirror of sub_mul_Aminus_eq): for θ := y − y' ≠ 0, T ≥ 0,
ψ := φ − φ':
θ·A⁻_ph(y,y',φ,φ') = [sin(θ2T−ψ)C⁻(y) + cos(θ2T−ψ)S⁻(y) − (sin(θT−ψ)C⁻(y') + cos(θT−ψ)S⁻(y'))]
                   + [sin(θ2T−ψ)C⁺(y') + cos(θ2T−ψ)S⁺(y') − (sin(θT−ψ)C⁺(y) + cos(θT−ψ)S⁺(y))]. 

 ## The magnitude/phase form of P_{X,c} 

### `cpow_neg_half_sub_I_mul`

 n^(−1/2 − iτ) = (√n)⁻¹·e^{−i·τ·log n} for n ≥ 1. 

### `PXc_eq_sum`

 The magnitude/phase form:  P_{X,c}(τ) = −(1/π) Σ_n a_n·‖c n‖·cos(τ·log n − arg(c n)). 

 ## H-MV with phases 

### `MV_real_ph`

 Mirror of MV_real with a per-index phase: for real weights u, v and phases φv,
both trig sums Σ_{n≠m} u_n v_m·trig(cc(y_n−y_m) − (φv_n − φv_m))/(y_n−y_m) obey the H-MV bound. 

### `MV_size_le₂`

 Size bound with weights on BOTH slots: |w₁| ≤ 1, |w₂| ≤ W ⟹ the MV bound ≤ 2CW·ΣΛ²,
in both slot orders. 

 ## The decomposition 𝓜[P_{X,c}, P_{X,c}] = 𝒟 + 𝒪₁ + 𝒪₂, weighted and phased 

### `Mform_PXc_PXc`

 [eq:MPP] for P_{X,c} (mirror of Mform_PX_PX): with weights a_k‖c k‖ and phases arg(c k). 

 ## The three estimates, weighted and phased 

### `diag_estimate_chi`

 𝒟 for P_{X,c} (mirror of diag_estimate; weight ‖c n‖² ≤ 1 rides along). 

### `O2_estimate_chi`

 𝒪₂ for P_{X,c} (mirror of O2_estimate; weights ≤ 1, phase-free bound). 

 ## 𝒪₁ for P_{X,c} 

### `O1_bound_chi`

 𝒪₁ for P_{X,c} (mirror of O1_bound; weights a_k‖c k‖ ≤ a_k, phases arg(c k) ride into
MV_real_ph): |Σ_{n≠m} w_n w_m A⁻_ph| ≤ 16·C·(∫Φ²)·ΣΛ². 

 ## The coprime g-sandwich (§5.4 with [eq:cheb2] restricted to (n,q)=1) 

### `sumA2gCoprime_upper`

 Upper half, over the window-generic Core layer (uses only g ≤ A_φ ≤ (L−|y|)₊). 

### `sumA2gCoprime_lower`

 Lower half, over the FULL taper layer (needs the flat-top bound g_lower, absent from Core). 

 ## Assembly: [prop:PP] for L(s,chi) 

### `prop_PP_chi_uniform`

 **prop_PP_chi, q-uniform form** (hybrid range, [rem:otherL](i)): the same constant and
threshold for every modulus and unimodular coefficient sequence — the ∃ C T₀ sit outside (q, c).
(The constant does not depend on (q, c); unimodularity enters only through the norm bound and the
diagonal identity.  `prop_PP_chi` below is the (q, c)-specialisation of this theorem.) 

### `prop_PP_chi`

 **[prop:PP] for L(s,chi)** ([thm:E] (iii)): under H-cheb + H-MV + CoeffUnimodular,
|𝓜[P_{X,c},P_{X,c}] − (T/π)·Σ_{n≤X,(n,q)=1}Λ(n)²/n·g(log n)| ≤ C·L²X for T ≥ T₀, over the
window-generic Core taper layer.
Proof: the q-uniform form `prop_PP_chi_uniform` above, specialised to (q, c) — the constant and
threshold do not depend on them. 

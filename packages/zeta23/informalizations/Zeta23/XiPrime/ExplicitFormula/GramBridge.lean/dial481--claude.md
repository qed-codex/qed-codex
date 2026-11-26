---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/GramBridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/GramBridge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/GramBridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/GramBridge.lean — Gram-matrix bridge lemmas for the xiEF assembly.

Bookkeeping between the Defs-level objects of the statement XiEF — Z.Gz (zero side), P.Gentry /
P.GentryC / P.Gentry1 (prime-side entries) — and the analytic objects the explicit formula produces:
tsums of H = WeilEF.Hfn over {ρ | ξ′ ρ = 0} and integrals ∫ ĥ(τ)·density(τ) dτ, for the Weil test function
of the pair (f_k, f_l),  kfun P T k l := weilTest (P.fk T k) (P.fk T l)  (the single definition, in
Zeta23/XiPrime/ExplicitFormula.lean; the family version is kfun (Pf T) T k l).
ζ model: Zeta23/Hypotheses/GzGp.lean (Gz_eq_W, EFrhs_eq_Gp, paperFT_fk, phiHat_conj, phiHat_ofReal).

  (S1) Gsummand_eq_mult_Hfn, Gz_eq_tsum_xi, summable_Gsummand_of
  (S2) literatureRHS_pairTest_eq_Gentry
  (S3) paperFT_pairTest, paperFT_pairTest_ofReal, GentryC_eq_of_nuc, Gentry1_eq
  (S4) tau_mem, tauStar_mem
Standing per-T hypotheses (as in GzGp): hφC2 : ContDiff ℝ 2 (fun u => (P.phi T u : ℂ)),
hφsupp : tsupport (P.phi T) ⊆ Icc (−L/2) (L/2), hL : 0 < P.L T.
-/
```

 ### regularity of f_k and of the pair test function 

 ### (S3a) ĥ of the pair test function 

### `paperFT_pairTest`

 ĥ_{f_k ⋆ f̃_l}(z) = φ̂(z − τ_k)·φ̂(z − τ_l). 

### `paperFT_pairTest_ofReal`

 on the real line ĥ is the REAL number φ̂_ℝ(τ − τ_k)·φ̂_ℝ(τ − τ_l). 

 ### (S1) zero side: Gsummand / Gz as m_ρ · H(ρ) 

### `Gsummand_eq_mult_Hfn`

 Z.Gsummand P T k l ρ = m_ρ · H_{f_k ⋆ f̃_l}(ρ)   (H k s = paperFT k ((s − 1/2)/I) = ĥ(γ_ρ), rfl). 

### `Gz_eq_tsum_xi`

 the zero-side Gram entry as a tsum over the zeros of ξ′ weighted by xiDerivMult. 

### `summable_Gsummand_of`

 absolute convergence of the zero-side entry, transported from the ξ′-indexed sum. 

 ### (S2) prime side with ζ's coefficients: literatureRHS = Gentry 

### `integrable_paperFT_pairTest_mul_nuX`

 ĥ·ν_X is integrable on ℝ for the pair test function (X = e^L = P.X T). 

### `literatureRHS_pairTest_eq_Gentry`

 **(S2)**  literatureRHS (f_k ⋆ f̃_l) = G_{kl} (= ∫ φ̂_ℝ(τ−τ_k) φ̂_ℝ(τ−τ_l) ν_X(τ) dτ, X = e^L). 

 ### (S3b) prime side with general coefficients: GentryC / Gentry1 versus Gentry 

### `GentryC_eq_of_nuc`

 If the density with coefficients c splits as ν_c(X) = ν_X + P_{cJ}(X) pointwise and ĥ·P_{cJ} is
integrable, then  M^c_{kl} = G_{kl} + ∫ ĥ(τ) P_{cJ}(X; τ) dτ  (as complex numbers). 

### `Gentry1_eq`

 **Gentry1 = Gentry + J-term**: the entry-dependent main term of [XF′ Thm 4.2] splits as the ζ entry
plus ∫ ĥ·P_{cJ}, given the density decomposition nuc X (xiCoeff L⋆) = nuX X + Pc X cJ. 

 ### (S4) the grid points lie in [T, 2T] 

### `tau_mem`

 T ≤ τ_k ≤ 2T for 0 ≤ k < d  (τ_k = T + k·2π/L, d = ⌊LT/2π⌋). 

### `tauStar_mem`

 T ≤ τ⋆_{kl} ≤ 2T. 

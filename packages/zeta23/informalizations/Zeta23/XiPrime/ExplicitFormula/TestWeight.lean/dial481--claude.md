---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/TestWeight.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/TestWeight.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/TestWeight.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/TestWeight.lean — TEST-WEIGHT ESTIMATES for the ξ′ explicit formula.

Canonical text: [XF′] §3 (Lemma 3.1) and §4 (Thm 4.2 proof (b),(c)).
Consumer: EntryError.lean (the entry error 𝓔_{kl} of (EF4)).

WHAT IS HERE.  For a height family `Pf : ℝ → Params` with `hPf : FamilyHyps Pf` (ExplicitFormula.lean §7)
put P := Pf T, φ := P.phi T, L := P.L T, X := P.X T = e^L, τ_k := P.tau T k, and the Weil test function
    kfun P T k l := Zeta23.EF.weilTest (P.fk T k) (P.fk T l)      (k l : ℤ),
so that  paperFT (kfun P T k l) z = φ̂(z − τ_k) · φ̂(z − τ_l)  for ALL complex z (paperFT_kfun; this is
[XF′ Lemma 3.1] "Φ(s) = φ̂(t−ic−τ_k) φ̂(t−ic−τ_l)"), and H := Zeta23.WeilEF.Hfn (kfun …) is the weight of
the zero-side summand.  We prove, with constants depending only on hPf (never on T, k, l, t):
 (W5) the Cauchy-convolution lemma  ∫ dt/((1+(t−a)²)(1+(t−b)²)) ≤ 32π/(4+(a−b)²), its integrability, and
      the far-region bound  ∫_{|t−a| ≥ R} (same) ≤ π/R²;
 (W0) kfun ∈ C_c², tsupport ⊆ [−L, L] (also for u ↦ kfun(−u)); 0 < L, 1 ≤ L eventually;
 (W1) ‖H(5/4+it)‖ ≤ C X^{3/4} L² / ((1+(t−τ_k)²)(1+(t−τ_l)²));
 (W2) (|t−τ_k|+|t−τ_l|) ‖H(5/4+it)‖ ≤ C X^{3/4} L / ((1+(t−τ_k)²)(1+(t−τ_l)²))   (uses φ′, φ‴);
 (W3) the same two for the mirrored weight u ↦ kfun(−u), with τ ↦ −τ;
 (W4) on ℝ: paperFT kfun τ = φ̂_ℝ(τ−τ_k) φ̂_ℝ(τ−τ_l) (real), integrable, ∫‖·‖ ≤ C L²/(1+(τ_k−τ_l)²);
 (W6) ∫‖H‖ and ∫(1+|t−τ⋆|)‖H‖ ≤ C X^{3/4} L²/(1+(τ_k−τ_l)²), and the far-region bound
      ∫_{|t−τ⋆| ≥ 3τ⋆/4} ‖H‖ ≤ C X^{3/4} L²/T² when T ≤ τ_k, τ_l ≤ 2T (true for 0 ≤ k,l < d: tau_mem_Icc);
      same for the mirrored weight around −τ⋆.
ORGANISATION.  §A generic real analysis (W5).  §B paperFT helpers.  §C `WindowAt P T C`: the window
facts FamilyHyps gives at ONE good height (plus 1 ≤ L, 1 ≤ T), and `FamilyHyps.windowAt : ∃ C T₁, …`.
§D–§H: every estimate at a fixed height under `WindowAt`, with an EXPLICIT constant (a polynomial in C)
— these are the uniform statements; §I re-packages each in the "∃ C T₁, ∀ T ≥ T₁, ∀ k l" form.
A consumer needing ONE (C, T₁) for several items should use §C + the §D–§H lemmas directly.
The line is Re s = 5/4, written `(5/4 : ℂ) + t * I`.
-/
```

 ## §A. Generic real analysis: the Cauchy convolution lemma (W5) 

### `integrable_inv_one_add_sq_sub`

 the Cauchy kernel 1/(1+(t−a)²) is integrable. 

### `cauchyConv_pointwise`

 pointwise: 1/((1+(t−a)²)(1+(t−b)²)) ≤ 4/(4+(a−b)²) · (1/(1+(t−a)²) + 1/(1+(t−b)²)). 

### `cauchyConv_integrable`

 (W5a) integrability of the product of two Cauchy kernels. 

### `cauchyConv_integral_le`

 (W5b) ∫ dt/((1+(t−a)²)(1+(t−b)²)) ≤ 32π/(4+(a−b)²)  (we even get 8π). 

### `cauchyConv`

 **(W5)** the Cauchy convolution lemma, packaged (integrability and bound together). 

### `cauchyConv_integral_le'`

 the same bound with the friendlier denominator 1 + (a−b)². 

### `cauchyConv_far`

 **(W5, far region)**: for R > 0,  ∫_{|t−a| ≥ R} dt/((1+(t−a)²)(1+(t−b)²)) ≤ π/R². 

 ## §B. paperFT helpers 

### `norm_paperFT_mul_le`

 [eq:hfbound], first order: supp f ⊆ [−Λ, Λ], f ∈ C_c¹ ⇒ ‖h_f(z)‖·‖z‖ ≤ e^{|Im z|Λ}‖f′‖₁.
(Same statement and proof as Zeta23.Taper.norm_paperFT_mul_le.) 

### `norm_paperFT_mul_cube_le`

 [eq:hfbound], third order: f ∈ C_c³ ⇒ ‖h_f(z)‖·‖z‖³ ≤ e^{|Im z|Λ}‖f‴‖₁ (three integrations by parts). 

### `paperFT_comp_neg`

 paperFT of u ↦ k(−u) is paperFT k reflected. 

### `Hfn_five_four`

 H(5/4 + it) = h_k(t − 3i/4). 

### `Hfn_five_four_ofReal`

 bridge for consumers who spell the line point with a real 5/4: `((5/4:ℝ):ℂ) + t*I`. 

### `Hfn_five_four_neg`

 the mirrored weight on the line: H_{k∘neg}(5/4 + it) = h_k(−t + 3i/4). 

 ## §C. The window at one good height 

### `WindowAt`

 What `FamilyHyps` gives at ONE height T ≥ T₁ (plus 1 ≤ L, 1 ≤ T), with a single constant C ≥ 1
bounding ‖φ′‖₁, ‖φ″‖₁, ‖φ‴‖₁.  Every estimate of §§D–H is proved under this hypothesis with an explicit
constant; `FamilyHyps.windowAt` produces it eventually in T. 

### `_root_.Zeta23.XiPrime.FamilyHyps.windowAt`

 `FamilyHyps` ⇒ the window facts hold at every large height, with one constant. 

 ### §D. φ as a complex function, and the two per-factor bounds 

### `integral_norm_phiC_le`

 ‖φ‖₁ ≤ L (|φ| ≤ 1 on its support [−L/2, L/2]). 

### `phiHat_bound`

 **per-factor bound (size)**: ‖φ̂(z)‖ (1 + (Re z)²) ≤ (1+C) e^{|Im z| L/2} L
(zeroth-order [eq:hfbound] with ‖φ‖₁ ≤ L, plus second-order with ‖φ″‖₁ ≤ C and (Re z)² ≤ ‖z‖², L ≥ 1). 

### `phiHat_moment_bound`

 **per-factor bound (first moment)**: ‖z‖ ‖φ̂(z)‖ (1 + (Re z)²) ≤ 2C e^{|Im z| L/2}
(first- and third-order [eq:hfbound]: ‖φ′‖₁, ‖φ‴‖₁ ≤ C). 

### `exp_mul_exp_eq_X_rpow`

 X^{3/8} · X^{3/8} = X^{3/4}, X = e^L. 

### `factor_le`

 the factor on the line Im z = −3/4:  ‖φ̂(x − 3i/4)‖ ≤ (1+C) X^{3/8} L/(1+x²). 

### `mfactor_le`

 the factor on the mirrored line:  ‖φ̂(−x + 3i/4)‖ ≤ (1+C) X^{3/8} L/(1+x²). 

### `rfactor_le`

 the factor on the real line (no exponential): ‖φ̂(x)‖ ≤ (1+C) L/(1+x²). 

 ## §E. The Weil test function k = f_k ⋆ f̃_l and its transform 

### `kfun_contDiff`

 (W0) k ∈ C². 

### `kfun_hasCompactSupport`

 (W0) k has compact support. 

### `kfun_tsupport`

 (W0) tsupport k ⊆ [−L, L]. 

### `kfun_neg_contDiff`

 (W0, mirrored) u ↦ k(−u) ∈ C². 

### `paperFT_kfun`

 **[XF′ Lemma 3.1]**  h_k(z) = φ̂(z − τ_k) · φ̂(z − τ_l)  for all complex z
(h_{f⋆g̃}(z) = h_f(z)·conj h_g(z̄), h_{f_k}(z) = φ̂(z − τ_k), and conj φ̂(z̄) = φ̂(z) as φ is real and even). 

### `Hfn_kfun`

 the weight on the line Re s = 5/4:  H(5/4+it) = φ̂((t−τ_k) − 3i/4) · φ̂((t−τ_l) − 3i/4). 

### `Hfn_kfun_neg`

 the mirrored weight on the line:  H_{k∘neg}(5/4+it) = φ̂(−(t+τ_k) + 3i/4) · φ̂(−(t+τ_l) + 3i/4). 

 ## §F. (W1)–(W3): pointwise bounds on the line Re s = 5/4 

### `norm_Hfn_kfun_le`

 **(W1)** ‖H(5/4+it)‖ ≤ (1+C)² X^{3/4} L² / ((1+(t−τ_k)²)(1+(t−τ_l)²)). 

### `moment_norm_Hfn_kfun_le`

 **(W2)** (|t−τ_k| + |t−τ_l|) ‖H(5/4+it)‖ ≤ 4C(1+C) X^{3/4} L / ((1+(t−τ_k)²)(1+(t−τ_l)²)). 

### `norm_Hfn_kfun_neg_le`

 **(W3, size)** the mirrored weight: ‖H_{k∘neg}(5/4+it)‖ ≤ (1+C)² X^{3/4} L² / ((1+(t+τ_k)²)(1+(t+τ_l)²)). 

### `moment_norm_Hfn_kfun_neg_le`

 **(W3, first moment)** (|t+τ_k| + |t+τ_l|) ‖H_{k∘neg}(5/4+it)‖ ≤ 4C(1+C) X^{3/4} L / (…). 

 ## §G. (W4): the transform on the real line 

### `paperFT_kfun_ofReal`

 **(W4)** on ℝ the transform is the real number φ̂_ℝ(τ−τ_k) φ̂_ℝ(τ−τ_l). 

### `integrable_paperFT_kfun_ofReal`

 **(W4)** h_k is integrable on ℝ. 

### `integral_norm_paperFT_kfun_ofReal_le`

 **(W4)** ∫‖h_k‖ ≤ 32π (1+C)² L² / (1 + (τ_k − τ_l)²). 

 ## §H. (W6): integrated consequences on the line Re s = 5/4 

### `integrable_Hfn_kfun`

 (W6) t ↦ H(5/4+it) is integrable. 

### `integral_norm_Hfn_kfun_le`

 **(W6a)** ∫‖H(5/4+it)‖dt ≤ 32π(1+C)² X^{3/4} L² / (1+(τ_k−τ_l)²). 

### `integral_norm_Hfn_kfun_neg_le`

 **(W6a, mirrored)** ∫‖H_{k∘neg}(5/4+it)‖dt ≤ 32π(1+C)² X^{3/4} L² / (1+(τ_k−τ_l)²). 

### `weighted_norm_Hfn_kfun_le`

 **(W6b, pointwise)** (1+|t−τ⋆|)‖H(5/4+it)‖ ≤ (1+C)(1+3C) X^{3/4} L² / ((1+(t−τ_k)²)(1+(t−τ_l)²)). 

### `weighted_norm_Hfn_kfun_neg_le`

 **(W6b, pointwise, mirrored)** (1+|t+τ⋆|)‖H_{k∘neg}(5/4+it)‖ ≤ (1+C)(1+3C) X^{3/4} L² / (…). 

### `integral_weighted_norm_Hfn_kfun_le`

 **(W6b)** ∫(1+|t−τ⋆|)‖H(5/4+it)‖dt ≤ 32π(1+C)(1+3C) X^{3/4} L² / (1+(τ_k−τ_l)²). 

### `integral_weighted_norm_Hfn_kfun_neg_le`

 **(W6b, mirrored)** ∫(1+|t+τ⋆|)‖H_{k∘neg}(5/4+it)‖dt ≤ 32π(1+C)(1+3C) X^{3/4} L² / (1+(τ_k−τ_l)²). 

 ### far region: |t − τ⋆| ≥ 3τ⋆/4  (τ⋆ = (τ_k+τ_l)/2, T ≤ τ_k, τ_l ≤ 2T) 

### `tau_mem_Icc`

 for 0 ≤ k < d:  T ≤ τ_k ≤ 2T  (τ_k = T + k·2π/L, d = ⌊LT/2π⌋). 

### `setIntegral_far_norm_Hfn_kfun_le`

 **(W6c)** far from the bump:  ∫_{|t−τ⋆| ≥ 3τ⋆/4} ‖H(5/4+it)‖ dt ≤ 16π (1+C)² X^{3/4} L² / T²,
for T ≤ τ_k, τ_l ≤ 2T (tau_mem_Icc). 

### `setIntegral_far_norm_Hfn_kfun_neg_le`

 **(W6c, mirrored)** ∫_{|t+τ⋆| ≥ 3τ⋆/4} ‖H_{k∘neg}(5/4+it)‖ dt ≤ 16π (1+C)² X^{3/4} L² / T². 

 ## §I. The "∃ C T₁, ∀ T ≥ T₁, ∀ k l" packaging (constants depend only on hPf)

Each item below is a one-line corollary of `FamilyHyps.windowAt` and the fixed-height lemma of §§E–H named
in its proof. 

### `testWeight_regular`

 **(W0)** regularity and support of the weight and its mirror; 0 < L, 1 ≤ L eventually. 

### `testWeight_paperFT`

 **[XF′ Lemma 3.1]** for the family: h_k(z) = φ̂(z−τ_k) φ̂(z−τ_l), all complex z, eventually in T. 

### `testWeight_norm_le`

 **(W1)** size on the line Re s = 5/4. 

### `testWeight_moment_norm_le`

 **(W2)** first moment on the line Re s = 5/4. 

### `testWeight_neg_norm_le`

 **(W3)** the mirrored weight u ↦ k(−u): the same two bounds with τ ↦ −τ (written t + τ). 

### `testWeight_real_line`

 **(W4)** on the real line: real-valued product formula, integrable, ∫‖·‖ ≤ C L²/(1+(τ_k−τ_l)²). 

### `testWeight_integrals`

 **(W6)** for the family: integrability, ∫‖H‖, ∫(1+|t−τ⋆|)‖H‖ ≤ C X^{3/4}L²/(1+Δ²), and the far tail
≤ C X^{3/4} L²/T² (for T ≤ τ_k, τ_l ≤ 2T); plus the same four for the mirrored weight around −τ⋆. 

### `testWeight_tau_mem_Icc`

 (W6, indices) for a Fin d index the hypothesis T ≤ τ_k ≤ 2T of the far-tail bound holds eventually. 

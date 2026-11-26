---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/Expansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/Expansion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/Expansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/Expansion.lean — the logarithmic derivative of ξ′ on the line Re s = 5/4.
 [XF′ §2]:
 * E := ξ′/ξ = L − A  (Lfn + ζ′/ζ;  A = −ζ′/ζ = LSeries Λ,  B := −A′ = LSeries (Λ·log));
 * Lemma 2.1:  ξ″/ξ′ = E + E′/E,  E′ = L′ + B;
 * FREEZING in closed form: replacing L by a constant Λ⋆ and L′ by 0 in E′/E = (L′+B)/(L−A) gives
   B/(Λ⋆ − A) ( = Σ_j Λ⋆^{−(j+1)} B A^j = Σ_N C_J(N;Λ⋆) N^{−s}, see LSeries_xiCoeffJ ),
   with the EXACT identity  (L′+B)/(L−A) − B/(Λ⋆−A) = L′/(L−A) + B(Λ⋆−L)/((L−A)(Λ⋆−A))
   and hence  ‖·‖ ≤ ‖L′‖/(‖L‖−A₀) + B₀‖L−Λ⋆‖/((‖L‖−A₀)(‖Λ⋆‖−A₀))  (no series on this side);
 * line estimates at σ = 5/4:  ‖A‖ ≤ A₀, ‖B‖ ≤ B₀,  Re L(5/4+it) ≥ ½log|t| − C,
   ‖L′(5/4+it)‖ ≤ C/|t|,  ‖L(5/4+it) − L⋆(τ)‖ ≤ C(|t−τ|+1)/min(t,τ)  (Stirling: GammaFacts).
-/
```

 ## 1. E, A, B 

### `Efn`

 E := ξ′/ξ = L + ζ′/ζ (meaningful on Re s > 1, where ζ ≠ 0). 

### `Afn`

 A := Σ Λ(n) n^{−s} = −ζ′/ζ. 

### `Bfn`

 B := Σ Λ(n) log n · n^{−s} = −A′. 

### `isOpen_one_lt_re`

 the open half-plane Re s > 1. 

### `abscissa_vonMangoldt_le_one`

 abscissa of absolute convergence of Λ is ≤ 1. 

### `logMul_vonMangoldt`

 the B-coefficients are logMul of the A-coefficients. 

### `summable_Bfn`

 B is absolutely summable on Re s > 1. 

### `differentiableAt_Lfn`

 L is differentiable on Re s > 0 away from 0 and 1 (here: Re s > 1). 

### `hasDerivAt_logDeriv_zeta`

 logDeriv ζ is differentiable on Re s > 1 with derivative B (= −A′). 

### `xiDeriv_eq_xi_mul_Efn`

 ξ′ = ξ · E on Re s > 1 (Seam.xiDeriv_eq_xi_mul). 

### `Efn_ne_zero`

 E(s) ≠ 0 wherever ξ′(s) ≠ 0 (Re s > 1). 

### `logDeriv_xiDeriv_eq_Efn`

 **[XF′ Lemma 2.1]**  ξ″/ξ′ = E + E′/E on Re s > 1 wherever ξ′ ≠ 0. 

 ## 2. Freezing, in closed form (pure algebra) 

### `freeze_identity`

 the exact freezing identity. 

### `freeze_bound`

 **the freezing bound**: for ‖A‖ ≤ A₀ < min(‖L‖, ‖Λ⋆‖) and ‖B‖ ≤ B₀,
‖(L′+B)/(L−A) − B/(Λ⋆−A)‖ ≤ ‖L′‖/(‖L‖−A₀) + B₀‖L−Λ⋆‖/((‖L‖−A₀)(‖Λ⋆‖−A₀)). 

### `deriv_Efn_div_Efn_eq`

 E′/E in the (L′+B)/(L−A) form, on Re s > 1. 

 ## 3. Uniform bounds for A and B on the line Re s = 5/4 

 ## 4. L on the line Re s = 5/4 (Stirling via Zeta23.GammaFacts) 

### `norm_log_w_sub_le`

 the complex logarithm near the positive imaginary axis:
‖log(5/8 + i t/2) − (log(t/2) + iπ/2)‖ ≤ 4/t for t ≥ 2. 

### `norm_Lfn_sub_Lstar_self_le`

 **one-point Stirling for L**: ‖L(5/4+it) − L⋆(t)‖ ≤ 8/t for t ≥ 2,
L⋆(t) = ½log(t/2π) + iπ/4 (Defs.Lstar). 

### `log_sub_log_le_of_le`

 ordered case of |log t − log τ| ≤ |t − τ| / min t τ. 

### `norm_Lstar_sub_Lstar_le`

 ‖L⋆(t) − L⋆(τ)‖ = ½|log t − log τ| ≤ |t−τ|/(2 min t τ). 

### `norm_Lfn_sub_Lstar_le`

 **L against a frozen L⋆(τ)**: ‖L(5/4+it) − L⋆(τ)‖ ≤ (|t−τ| + 16)/(2 min t τ) for t, τ ≥ 2. 

### `norm_Lstar_ge`

 ‖L⋆(τ)‖ ≥ ½ log(τ/2π). 

### `norm_Lfn_ge`

 ‖L(5/4+it)‖ ≥ ½ log(t/2π) − 8/t for t ≥ 2. 

 ## 5. L′ on the line, conjugation symmetry, and the uniform bound for E′/E 

### `LfnD`

 the digamma form of L (the right side of Seam.Lfn_eq_digamma), for differentiation. 

### `norm_deriv_digamma_le`

 ‖ψ′(w)‖ ≤ 1/Im(w)² + 2/|Im w| for Re w > 0, |Im w| ≥ 1/2 (trigamma series + Zeta23.StirlingVert). 

### `norm_deriv_Lfn_le`

 **L′ on the line**: ‖L′(5/4+it)‖ ≤ 3/|t| for |t| ≥ 2. 

 ## 6. Conjugation symmetry on the line 

### `derivE_div_E_eq`

 E′/E = ξ″/ξ′ − E (Lemma 2.1 rearranged). 

### `LSeries_real_conj`

 an L-series with REAL coefficients is conjugation-equivariant. 

### `frozen_conj`

 the frozen object B/(Λ⋆ − A) is conjugation-equivariant in (Λ⋆, s). 

 ## G. The generic line layer: archimedean line data (c, Λ, Λ⋆)  [XF′ §2 / §9.1 in one statement]

Everything the explicit formulas need on a line Re s = c about E := Λ + ζ′/ζ (ξ′: Λ = L, E = ξ′/ξ; W: Λ = L₂,
E = E₂ = W/ζ) follows from five Stirling-type facts about Λ and the frozen-parameter map Λ⋆ = Lpar, packaged as
ArchLineData, plus the single per-object input  hE : ∀ t, E(c+it) ≠ 0.  Instances: §7 below (Λ = Lfn, Lpar = Lstar,
c = 5/4) and Hardy/EFExpansion.lean (Λ = L2, Lpar = L2star, 9/8 ≤ c ≤ 5/4). 

### `EofL`

 E_Λ := Λ + ζ′/ζ. (Efn = EofL Lfn and E2fn = EofL L2, by rfl.) 

### `ArchLineData`

 **archimedean line data** for (c, Λ, Λ⋆). 

### `norm_Afn_le_at`

 A is bounded on Re s = c > 1. 

### `norm_Bfn_le_at`

 B is bounded on Re s = c > 1. 

### `analyticAt_logDeriv_zeta`

 ζ′/ζ is analytic on Re s > 1. 

### `ArchLineData.continuous_E_line`

 continuity along the line of E, E′, and of E′/E where E ≠ 0. 

### `ArchLineData.E_conj`

 conjugation symmetry of E off the real axis on Re s > 1. 

### `ArchLineData.derivE_conj`

 the derivative inherits the conjugation symmetry (E analytic on the open set {Re > 1, Im ≠ 0}). 

### `ArchLineData.derivE_div_E_uniform`

 **the uniform bound for E′/E on the line**, given E ≠ 0 there. 

### `ArchLineData.freeze_on_line`

 **the freezing estimate on the line**: for T ≥ T₀, τ ≥ T, t ≥ T/4,
‖E′/E(c+it) − B(c+it)/(Λ⋆(τ) − A(c+it))‖ ≤ C (|t − τ| + 1)/(T log T). 

### `ArchLineData.frozen_uniform`

 the frozen object B/(Λ⋆(τ) − A(c+it)) is uniformly small on the line: ‖B/(Λ⋆(τ) − A(c+it))‖ ≤ 4B₀/log T. 

### `ArchLineData.norm_E_line`

 ‖E(c+it)‖ ≤ M log(2+|t|). 

### `ArchLineData.norm_E_add_dE_line`

 ‖(E + E′/E)(c+it)‖ ≤ M log(2+|t|), given E ≠ 0 on the line. 

 ## 7. The ξ′ instance: (c, Λ, Λ⋆) = (5/4, L, L⋆); the uniform bound for E′/E under (F2) and the freezing estimate 

### `Lfn_conj`

 L(conj z) = conj L(z) (everywhere; Γℝ and 1/s, 1/(s−1) are real on ℝ). 

### `norm_Lfn_line54`

 ‖L(5/4+it)‖ ≤ M log(2+|t|) for all t. 

### `archLineData_Lfn`

 **the archimedean line data for ξ′**: (c, Λ, Λ⋆) = (5/4, L, L⋆). 

### `continuous_derivE_div_E_line`

 continuity of t ↦ E′/E(5/4+it) given ξ′ ≠ 0 on the line. 

### `derivE_div_E_uniform`

 **uniform bound for E′/E on Re s = 5/4 under (F2)** — instance of ArchLineData.derivE_div_E_uniform. 

### `freeze_on_line`

 **the freezing estimate on the line** [XF′ Lemma 2.4, at σ = 5/4] — instance of ArchLineData.freeze_on_line:
there are C, T₀ such that for T ≥ T₀, τ ≥ T and t ≥ T/4,
‖E′/E(5/4+it) − B(5/4+it)/(L⋆(τ) − A(5/4+it))‖ ≤ C (|t − τ| + 1)/(T log T). 

### `frozen_uniform`

 the frozen object is uniformly small on the line — instance of `ArchLineData.frozen_uniform`. 

---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/ZeroFree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/ZeroFree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/ZeroFree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/ZeroFree.lean — (F2): every zero of ξ′ lies in the open critical strip.

TARGETS (interface: Zeta23/XiPrime/ExplicitFormula.lean §2):
  re_logDeriv_xi_pos            : 1 ≤ Re s → 0 < Re ξ′/ξ(s)
  xiDeriv_ne_zero_of_one_le_re  : 1 ≤ Re s → ξ′(s) ≠ 0
  xiDeriv_ne_zero_of_re_nonpos  : Re s ≤ 0 → ξ′(s) ≠ 0
  xiDerivZerosInStrip_holds     : XiDerivZerosInStrip
all four in namespace Zeta23.XiPrime; every auxiliary statement lives in Zeta23.XiPrime.ZeroFree.

ROUTE (Hadamard-free; no product formula for ξ is used).  Fix s with ξ(s) ≠ 0, put s′ := reflect s
= 1 − s̄ and the weight  wt s w := 1/(s − w) − 1/(s′ − w)  (two simple poles, O(|w|⁻²) at ∞).
(1) Weighted argument principle with a MEROMORPHIC weight (generic, on top of
    Zeta23.Analytic.residueTheorem_finset): (1/2πi)∮ g·f′/f = Σ_{zeros ρ} ord_ρ(f) g(ρ) + Σ_{poles q of g} r_q f′/f(q).
(2) Applied to f = ξ (entire; zeros = nontrivial zeros of ζ with the same order) and g = wt s on the
    SQUARE [1 − R, R] × [−R, R] at a good height R = R_j of Zeta23.WeilEF.good_heights:
      (1/2πi)∮ = Σ_{|γ_ρ|<R} m_ρ wt s ρ − ξ′/ξ(s) + ξ′/ξ(s′).
(3) The whole border integral → 0 as j → ∞: on the border |wt s| ≤ 4|s − s′|/R² while
    |ξ′/ξ| ≤ C(log²(j+10) + log(2+R)) (good heights + Γℝ′/Γℝ growth in the strip; Stirling for ψ and
    |ζ′/ζ| bounded to the right of 3/2; the functional equation ξ′/ξ(1−w) = −ξ′/ξ(w) to the left),
    and the perimeter is 8R − 2: total O(log²j / j).  [Growing the square kills the vertical sides
    directly, so no full-line integrals are needed, as opposed to sending R → ∞ at fixed width and
    then the width → ∞.]
    The finite zero sums → the tsum over Zeta23.zetaZeroConfig (|wt s ρ| ≤ C_s/(1+|γ_ρ|²) and
    Zeta23.WeilEF.zero_sum_inv_sq).  Hence  ξ′/ξ(s) − ξ′/ξ(s′) = Σ'_ρ m_ρ wt s ρ.
(4) Symmetry: ξ′/ξ(s′) = −conj ξ′/ξ(s), so the left side is 2 Re ξ′/ξ(s); and
    Re wt s ρ = Re 1/(s−ρ) + Re 1/(s − reflect ρ), so reindexing by the involution ρ ↦ reflect ρ of the
    zero set gives  Re ξ′/ξ(s) = Σ'_ρ m_ρ (σ − β)/|s − ρ|²  (re_logDeriv_xi_eq_tsum).
(5) For σ ≥ 1 every term is > 0 (β < 1) and a zero exists (Riemann–von Mangoldt), so Re ξ′/ξ(s) > 0 and
    ξ′(s) = ξ(s)·ξ′/ξ(s) ≠ 0; σ ≤ 0 follows from ξ′(1−s) = −ξ′(s) (Seam.xiDeriv_one_sub).
-/
```

 ## §A. Generic residue calculus: a meromorphic weight against f′/f; an ML bound 

### `isBigO_mul_logDeriv_near_zero`

 Near a zero ρ of finite order of an analytic f, with a weight g analytic at ρ:
g·f′/f − ord_ρ(f)·g(ρ)/(· − ρ) is bounded on a punctured neighbourhood of ρ. 

### `isBigO_mul_near_weightPole`

 Near a simple pole q of the weight g (principal part r/(· − q)), with F differentiable at q:
g·F − r·F(q)/(· − q) is bounded on a punctured neighbourhood of q. 

### `rectangleIntegral'_mul_logDeriv_weightPoles`

 **Weighted argument principle with a meromorphic weight.**  f analytic on a neighbourhood of
every point of the closed rectangle and nonvanishing on its border, Z its (finite) zero set there;
g analytic on the rectangle off a finite set Q of interior points, disjoint from Z, with principal
part r q/(· − q) at q ∈ Q.  Then
(1/2πi)∮ g·f′/f = Σ_{ρ∈Z} ord_ρ(f)·g(ρ) + Σ_{q∈Q} r q·(f′/f)(q). 

### `norm_rectangleIntegral_le`

 **ML bound** for a rectangle integral: ‖∮ f‖ ≤ (sup_border ‖f‖) · (perimeter). 

 ## §B. Facts about ξ: zeros, orders, symmetries of ξ′/ξ 

### `xi_eq_zero_iff`

 The zeros of ξ are exactly the nontrivial zeros of ζ (ξ(0) = ξ(1) = 1/2; off {0,1},
ξ = s(s−1)/2·Λ and the zeros of Λ are the nontrivial zeros of ζ). 

### `analyticOrderNatAt_xi`

 At a nontrivial zero, ord(ξ) = ord(Λ) = ord(ζ) = zeroMult. 

### `logDeriv_xi_one_sub`

 ξ′/ξ(1 − s) = −ξ′/ξ(s). 

### `logDeriv_xi_conj`

 ξ′/ξ(s̄) = conj ξ′/ξ(s). 

### `xi_reflect`

 ξ(1 − s̄) = conj ξ(s). 

### `logDeriv_xi_reflect`

 ξ′/ξ(1 − s̄) = −conj ξ′/ξ(s). 

 ## §C. Growth of ξ′/ξ on the contour 

### `differentiableAt_digamma`

 ψ is differentiable (in particular continuous) on the open right half-plane
(Γ analytic and nonvanishing there; as in Zeta23.WeilEF.digamma_growth_strip). 

### `digamma_add_nat`

 iterated functional equation: ψ(z + n) = ψ(z) + Σ_{k<n} 1/(z + k)  (Re z > 0). 

### `norm_digamma_le`

 ψ grows logarithmically on Re z ≥ 1/2: Stirling (Zeta23.StirlingVert.digamma_stirling) for
|Im z| ≥ 1/2; for |Im z| < 1/2 shift z back into the compact box [1/2,3/2] × [−1/2,1/2] with the
functional equation and bound the harmonic-type sum by 2(1 + log n). 

### `norm_logDeriv_Gammaℝ_le_far`

 ‖Γℝ′/Γℝ(w)‖ ≤ C log(2 + |w|) for Re w ≥ 1. 

### `norm_logDeriv_zeta_le_far`

 ‖ζ′/ζ(w)‖ ≤ Σ Λ(n) n^{−3/2} for Re w ≥ 3/2. 

### `norm_logDeriv_xi_le_far`

 ‖ξ′/ξ(w)‖ ≤ C log(2 + |w|) for Re w ≥ 3/2  (ξ′/ξ = Γℝ′/Γℝ + 1/w + 1/(w−1) + ζ′/ζ). 

### `norm_logDeriv_xi_le_goodHeight`

 On the horizontal segments Im w = ±R, −1/2 ≤ Re w ≤ 3/2 of a good height R (ζ ≠ 0 and
‖ζ′/ζ‖ ≤ L on Im = ±R, 1/2 ≤ Re ≤ 2): ‖ξ′/ξ(w)‖ ≤ C (L + log(2 + R)). 

### `zc`

 lower-left corner of the square contour [1 − R, R] × [−R, R]. 

### `wc`

 upper-right corner of the square contour [1 − R, R] × [−R, R]. 

### `norm_logDeriv_xi_le_border`

 ‖ξ′/ξ‖ ≤ C (L + log(2 + R)) on the whole border of the square at a good height R ≥ 2. 

### `wt`

 the weight: wt s w = 1/(s − w) − 1/(s′ − w), s′ = reflect s = 1 − s̄. 

### `norm_wt_le_border`

 on the border of the square, |wt s| ≤ 4|s − s′|/R² once R ≥ 2|s| + 4. 

 ## §D. The square identity at a good height 

### `square_identity`

 **Square identity.**  ξ(s) ≠ 0, Re s ≠ 1/2, R ≥ |s| + 2 with ζ ≠ 0 on Im = ±R, 1/2 ≤ Re ≤ 2:
(1/2πi)∮_{∂([1−R,R]×[−R,R])} wt s · ξ′/ξ = Σ_{|Im ρ| < R} m_ρ wt s ρ − ξ′/ξ(s) + ξ′/ξ(reflect s).
(ζ ≠ 0 on Re ∈ [1/2, 2] of the lines Im = ±R keeps ALL zeros of ξ off those lines: a zero ρ with
Re ρ < 1/2 would give the zero 1 − ρ with Re ∈ (1/2, 1) on the mirrored line —
Zeta23.WeilEF.completedZeta_ne_zero_on_horizontals.) 

 ## §E. Limits along the good heights 

### `tendsto_rectangleIntegral`

 the border integral tends to 0 along the good heights. 

### `exists_normSq_sub_ge`

 a point off the zero set is at distance ≫_s (1 + |γ_ρ|²)^{1/2} from every zero ρ. 

### `norm_wt_le_zero`

 |wt s ρ| ≤ C_s/(1 + |γ_ρ|²) on the zero set. 

### `summable_mult_mul`

 Σ_ρ m_ρ φ(ρ) converges absolutely whenever |φ(ρ)| ≤ C/(1 + |γ_ρ|²) on the zeros. 

### `zero_sum_limit_gen`

 the finite zero sums over {|Im ρ| < R_j} converge to the tsum (generic form of
Zeta23.WeilEF.zero_sum_limit). 

### `logDeriv_xi_sub_reflect`

 **ξ′/ξ(s) − ξ′/ξ(1 − s̄) = Σ'_ρ m_ρ [1/(s−ρ) − 1/(1 − s̄ − ρ)]**  (ξ(s) ≠ 0; the tsum converges
absolutely by summable_wt hxi). 

 ## §F. Real parts: the partial-fraction formula for Re ξ′/ξ, and positivity 

### `reflectEquiv`

 the involution ρ ↦ 1 − ρ̄ of the zero set. 

### `re_logDeriv_xi_eq_tsum`

 **Re ξ′/ξ(s) = Σ'_ρ m_ρ (σ − β)/|s − ρ|²** over the distinct nontrivial zeros ρ = β + iγ of ζ
weighted by their multiplicity, for every s with ξ(s) ≠ 0 — inside the strip too.  The tsum is a
genuine sum, not Lean's junk value 0: summable_re_one_div hxi proves absolute convergence. 

### `exists_isNontrivialZero`

 ζ has a nontrivial zero (Riemann–von Mangoldt: N(T,2T) ≫ T log T). 

### `re_logDeriv_xi_pos`

 **Re ξ′/ξ(s) > 0 for Re s ≥ 1.** 

### `xiDerivZerosInStrip_holds`

 **(F2), unconditionally**: every zero of ξ′ lies in the open critical strip. 

---
{
  "module": "Zeta23/XiPrime/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
The theorems of the ξ′ development, with full types written out.
See Zeta23/XiPrime/Statement.lean for every definition and named proposition used below.

Each theorem's binder list is its list of assumptions.
  • xiDeriv_simple_on_line / _cumulative / headlineFlat_unconditional — no hypotheses.  The flat-window ξ′
    theorem at the Gevrey taper profile ϱ₂ (Zeta23.Taper.rhoTwo).
  • xiDeriv_simple_on_line_flat (any C³ taper profile ϱ; binder hϱ only, conclusion ϱ-free), _flat_std
    (ϱ := smoothTransition, no binders), xiDeriv_fixedLamBounds (every λ ∈ (0,1)), _limitForm (the literal
    λ → 1⁻ sentence) — all unconditional.
  • xiDeriv_simple_on_line_quartic_std (0.86864 / 0.93432, the near-optimal quartic window) — no
    hypotheses; _quartic for any C³ taper (binder hϱ only).
  • hardyW_simple_on_line (Z′: simple real stationary points of Hardy's Z, 0.85838 / 0.92919 of the zeros of
    W = ζ′ + L₂ζ) — no hypotheses; hardyW_simple_on_line_flat for any C³ taper (binder hϱ only).
Proved in this tree:
  (F2) all zeros of ξ′ lie in 0 < Re s < 1 — xiDerivZerosInStrip_holds (Re ξ′/ξ > 0 on Re s ≥ 1
       without the Hadamard product, via the partial fraction of ξ′/ξ over zeta zeros);  (F1) the seam —
  xiDerivSeam_of_strip;  (F3) Riemann–von Mangoldt + local count for ξ′ — xiDeriv_riemannVonMangoldt;
  (E1) the ξ′ explicit formula with frozen coefficients, entrywise — xiEF (with the Gram bridge and TestWeight);
  (C1) (H1)–(H3) for b_N = C(N; L_T) incl. the diagonal law with density D₁ — xiCoeffFamily_hyps (with MainTerm);
  (C2) the coefficient re-expansion — xiReexpansion;  the certified constants certFlat / certQuartic;  the
  quartic-window zero side + admissibility;  the two moments of the fixed-coefficient prime-side
  matrix incl. prop:PP for general coefficients (PP.lean);  the two-trace transfer;
  H-Γ (Zeta23.gammaFacts) and Montgomery–Vaughan (Zeta23.MV.mv_hilbert).

Prior art.  For "simple and on the critical line", unconditionally, the ξ′
constants 0.8584 (flat) / 0.8686 (quartic) exceed the best previous value 0.79874 (Conrey's method,
J. reine angew. Math. 399 (1989), with θ = 4/7, building on J. Number Theory 16 (1983) and, for simple zeros of the
derivatives, J. Number Theory 17 (1983) 71–75; the value is the one recorded in
Farmer, Electron. J. Combin. 2 (1995) and quoted in Farmer–Gonek, arXiv:0803.0425 = Farmer–Gonek–Lee,
J. London Math. Soc. (2) 90 (2014)); they equal Farmer–Gonek–Lee's RH-conditional value with RH removed.  They do not exceed the best known on-line-only proportion (multiplicity
allowed): X. Wu, Quart. J. Math. 66 (2015) 759–771 (arXiv:1206.3737) has 0.86957.
Z′ simple-and-real: Hall 2004:
"Z′ has not been studied directly"; Rolle from PRZZ gives ≈ 0.417.  RH-conditional comparators:
0.8825 simple / 0.9412 distinct (Chirre–Gonçalves–de Laat 2020).  For ξ^{(k)} in short windows (not the dyadic windows of
this file) cf. I. S. Rezvyakova, "Zeros of the derivatives of the Riemann ξ-function", Izv. Math. 69 (2005) 539–605 (proportion
of zeros of ξ^{(k)} on the line > 1 − (3/5)k⁻²) and "On simple zeros of derivatives of the Riemann ξ-function", Izv. Math.
70 (2006) 265–276 (simple zeros of ξ^{(k)} on the line in windows U = T(log(T/2π))^{−10}: proportion ≥ 1 − (e²+2)/(16k²),
uniformly for k ≤ log log T/(2 log log log T)); at k = 1 these are 0.4 and 0.413, below the long-window constants above.

ϱ is the taper profile of the test window (any TaperProfile; the tree's stdProfile = Real.smoothTransition
is supplied in the *_std corollaries so that no profile variable remains).
-/
```

### `xiDerivZeros₀`

 **The zeros of ξ′, all of them, with multiplicity — hypothesis-free.**  Both (F2) := xiDerivZerosInStrip_holds
and (F1) := xiDerivSeam_of_strip are theorems, so the configuration of
Statement.xiDerivZeros takes no arguments.  carrier = {ρ | ξ′ ρ = 0}, mult = analytic order (rfl). 

### `xiDerivZeros₀_rvm`

 (F3) for ξ′, hypothesis-free: Riemann–von Mangoldt + local count. 

### `xiEF_flat`

 **The ξ′ explicit formula for the flat family, ANY C³ taper profile, every λ ∈ (0,1)** — xiEF with
(F2) := xiDerivZerosInStrip_holds, the seam := xiDerivSeam_of_strip, and the window-regularity class FamilyHyps :=
familyHyps_flat (Zeta23/XiPrime/FamilyHyps.lean). 

### `xiDeriv_simple_on_line_flat`

 **[XF′ Thm 8.2] — ξ′, flat window, dyadic heights, certified ε-free decimals.**
There is T₀ such that for every T ≥ T₀:
  0.85838 · N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T)  — at least 85.838 % of the zeros ρ₁ of ξ′ with T < Im ρ₁ ≤ 2T,
      counted with multiplicity and with no condition on Re ρ₁, are simple and satisfy Re ρ₁ = 1/2;
  0.92919 · N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T) — at least 92.919 % of them are distinct.
No hypotheses beyond "ϱ is a C³ taper profile" (the test-function family's shape parameter; the conclusion does not
mention ϱ).  See xiDeriv_simple_on_line / _flat_std below for binder-free instances. 

### `headlineFlat`

 the same sentence, as the Prop HeadlineFlat stated in Statement.lean (rfl repackaging). 

### `xiDeriv_simple_on_line_flat_cumulative`

 **[XF′ Thm 8.2] — ξ′, flat window, cumulative heights (0,T].**  There is T₀ such that for every T ≥ T₀:
  0.85838 · N_{ξ′}(0,T) ≤ N⁰ˢ_{ξ′}(0,T)   and   0.92919 · N_{ξ′}(0,T) ≤ N_{d,ξ′}(0,T)
(i.e. liminf N⁰ˢ_{ξ′}(T)/N_{ξ′}(T) ≥ 0.85838).  From the dyadic form by dyadic summation (Zeta23.Assembly.dyadic),
using only interval-additivity of the three counts and N_{ξ′}(0,T) → ∞ (from (F3)).  Same conditions. 

 ### The same with the tree's concrete profile ϱ := stdProfile (= Real.smoothTransition), so that the
type mentions no profile variable. 

### `xiDeriv_simple_on_line_flat_std`

 Unconditional (ϱ := stdProfile = Real.smoothTransition). 

### `xiDeriv_simple_on_line_flat_cumulative_std`

 Unconditional, cumulative. 

 ## The hypothesis-free theorem

At the Gevrey taper profile ϱ₂ := Zeta23.Taper.rhoTwo (the C^∞ profile with certified derivative bounds,
Zeta23/Taper/Gevrey.lean) the window-regularity class FamilyHyps of the explicit formula holds for the flat family
(FamilyFlat.familyHyps_flat_gevrey), so xiEF_xiDerivZeros discharges the last binder. 

### `xiEF_flat_rhoTwo`

 The explicit formula for ξ′ for the flat family at ϱ₂, every λ ∈ (0,1) — a theorem: `xiEF`
with (F2) := `xiDerivZerosInStrip_holds`, the seam := `xiDerivSeam_of_strip`,
FamilyHyps := `familyHyps_flat_gevrey`. 

### `xiDeriv_simple_on_line`

 **[XF′ Thm 8.2] for ξ′ — unconditional, no hypotheses.**  There is T₀ such that for every T ≥ T₀:
  0.85838 · N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T)   and   0.92919 · N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T),
where N_{ξ′}(T,2T) is the number of zeros ρ₁ of ξ′ (ξ = Riemann's xi-function, Defs.xi, identified with Mathlib's
completedRiemannZeta by Statement.xi_eq) with T < Im ρ₁ ≤ 2T counted with multiplicity and with no condition
on Re ρ₁, N⁰ˢ_{ξ′} counts those that are simple with Re ρ₁ = 1/2, and N_{d,ξ′} the distinct ones.  I.e. at
least 85.838 % of the zeros of ξ′ are simple and on the critical line, and at least 92.919 % are distinct. 

### `xiDeriv_simple_on_line_cumulative`

 **cumulative form, unconditional:** 0.85838·N_{ξ′}(0,T) ≤ N⁰ˢ_{ξ′}(0,T) and 0.92919·N_{ξ′}(0,T) ≤ N_{d,ξ′}(0,T)
for all large T (liminf_{T→∞} N⁰ˢ_{ξ′}(T)/N_{ξ′}(T) ≥ 0.85838). 

### `xiDeriv_fixedLamBounds`

 **[XF′ Thm 8.2] at every fixed λ ∈ (0,1), flat window — unconditional:** for every ε > 0 and all large T,
(2 − κ₁(λ) − ε)·N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T) and (3/2 − κ₁(λ)/2 − ε)·N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T), κ₁(λ) := kappaXi λ vFlat
= 1/c_λ(flat; D₁) with the full series D₁ (Statement.FixedLamBounds). 

### `xiDeriv_simple_on_line_limitForm`

 **[XF′ Thm 8.2], the literal λ → 1⁻ form, flat window — unconditional:** for every ε > 0 and all large T,
(2 − κ₁(1) − ε)·N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T) and (3/2 − κ₁(1)/2 − ε)·N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T), where
κ₁(1) = kappaXi 1 vFlat = 1/λ + 2∫₀¹(1−r)D₁(λr)dr at λ = 1 ([XF′]: 2 − κ₁(1) = 0.858383…).  From the fixed-λ form by
continuity of λ ↦ κ₁(λ) on (0,1] (continuousOn_kappaXi_vFlat + eps_form_of_continuousOn). 

### `zerosIn_finite`

 Non-vacuity companions.  The counted sets are finite — so Ncount (a finsum) and N0simple/Ndist (ncard's) are
honest cardinalities, not Lean's junk value 0 for infinite sets — and the denominator N_{ξ′}(T,2T) → ∞. 

### `headlineFlat_unconditional`

 the Props stated in Statement.lean, unconditionally. 

 ## The same proportions against the zeta zero count N(T,2T)  ([XF′ (F3)]: N_{ξ′}(T) = N(T) + O(log T))

Both configurations obey Riemann–von Mangoldt with the same main term (T/2π)ℓ₁ (ξ′: xiDerivZeros₀_rvm; ζ:
Zeta23.RvM.riemannVonMangoldt Zeta23.gammaFacts), so N_{ξ′}(T,2T) ≥ (1−δ)N_ζ(T,2T) eventually for every δ > 0, and the strict
certificate margin absorbs the δ.  N_ζ = Zeta23.Ncount = the nontrivial zeros of Mathlib's riemannZeta in T < Im ≤ 2T
with multiplicity (Zeta23/Statement.lean). 

### `eventually_zetaCount_le_Ncount`

 N_{ξ′}(T,2T) ≥ (1 − δ)·N_ζ(T,2T) eventually, every δ > 0. 

### `xiDeriv_simple_vs_zetaCount`

 **vs. N_ζ — unconditional:** there is T₀ such that for every T ≥ T₀,
  0.85838 · N_ζ(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T)   and   0.92919 · N_ζ(T,2T) ≤ N_{d,ξ′}(T,2T),
N_ζ(T,2T) = Zeta23.Ncount T (2T) = # nontrivial zeros of ζ with T < Im ≤ 2T, with multiplicity.  ("At least 85.838 % of
N(T,2T)": that many simple critical-line zeros of ξ′ at height in (T,2T].) 

 ## The quartic window  v(s) = 1 − (7/100)(2s)² − (51/200)(2s)⁴  [XF′ Thm 8.2, optimal-window line]

Same binder list as the flat case: the extra input (the zero-side facts for the height family
Pf := (paramsOf ϱ λ).atV vQuartic — Assembly.WindowZeroSide) is proved as windowZeroSide_atV
(XiPrime/QuarticWindow/ZeroSide.lean), and the quartic prime-side inputs are Inputs.coeffMoments_quartic_xi /
Inputs.traceTransfer_quartic. 

### `xiEF_atV`

 **The ξ′ explicit formula for the window family P.atV v, any C³ taper and any admissible profile v,
every λ ∈ (0,1)** — xiEF with FamilyHyps := familyHyps_atV (Zeta23/XiPrime/FamilyHypsV.lean). 

### `xiDeriv_simple_on_line_quartic`

 **[XF′ Thm 8.2] — ξ′, quartic window, dyadic heights, certified ε-free decimals.**
There is T₀ such that for every T ≥ T₀:
  0.86864 · N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T)   (≥ 86.864 % simple and on Re s = 1/2),
  0.93432 · N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T)  (≥ 93.432 % distinct).
No hypotheses beyond "ϱ is a C³ taper profile" (conclusion ϱ-free); see xiDeriv_simple_on_line_quartic_std for the
binder-free instance. 

### `xiDeriv_simple_on_line_quartic_cumulative`

 **[XF′ Thm 8.2] — ξ′, quartic window, cumulative heights (0,T]:**
0.86864·N_{ξ′}(0,T) ≤ N⁰ˢ_{ξ′}(0,T) and 0.93432·N_{ξ′}(0,T) ≤ N_{d,ξ′}(0,T) for all large T.  Same conditions. 

### `xiDeriv_simple_on_line_quartic_std`

 **[XF′ Thm 8.2], quartic (near-optimal) window — unconditional, no hypotheses:** for all large T,
0.86864·N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T) and 0.93432·N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T) — at least 86.864 % of the zeros of ξ′ are
simple and on the critical line, at least 93.432 % are distinct. 

 ## Z′ — the stationary points of Hardy's function  [XF′ §9, Thm 9.4]

W := ζ′ + L₂ζ (Defs.hardyW) is the Mathlib-honest meromorphic function with Z′(t) = i e^{iϑ(t)} W(½+it)
[XF′ (Z3)], so "t ∈ (T,2T], Z′(t) = 0 ≠ Z″(t)" is "½+it is a simple zero of W" and NcountW counts all non-real
zeros of W in the height window.  The W headline is assembled by the same spine at Z := the zeros of W with
|Im| ≥ t_W.  Inputs, all proved in this tree: (Z6)(iii) — there is t_W > 0 above which every zero of W lies in
the open strip — wZerosInStrip_holds (reflection-symmetry positivity Σ_{|γ|≤T} m_ρ(1−β_ρ) = N_T/2 beats
Re L₋ = O(1/t²); no Littlewood gap theorem, no zero-free region); the W seam wSeam_of_strip; the
zero-side family facts (windowZeroSide_flat); the prime side for wCoeffFamily (wCoeffFamily_hyps + the ξ′ prime
side; same density D₁ ⇒ same κ₁ ⇒ the same certificate certFlat).  (Z7) H-RvM + local count for W —
riemannVonMangoldt_W.  The W two-trace transfer wTraceTransfer_of with wReexpansion
(Inputs.traceTransfer_flat_w).  The W explicit formula WEF (StatementW.lean) for the flat family
(wEF_flat below), so the W headlines carry no hypothesis beyond the taper binder hϱ. 

### `wStripHeight`

 the height t_W > 0 above which all zeros of W are in the open critical strip (from wZerosInStrip_holds). 

### `wSeam_wStripHeight`

 The W seam facts at `t_W`, obtained as a theorem via `wSeam_of_strip`. 

### `wZeros₀`

 **The zeros of W with |Im| ≥ t_W, all of them, with multiplicity — hypothesis-free configuration.** 

### `wZeros₀_rvm`

 (Z7) for W, hypothesis-free: Riemann–von Mangoldt + local count for the zeros of W above t_W. 

### `wEF_flat`

 **The W explicit formula for the flat family, any C³ taper, every λ ∈ (0,1)** — the W explicit formula wEF
(assembled from EFExpansion, EFContour, the test-weight / Gram-bridge / low-zero facts and the pole + L-series facts) instantiated at
(Z6) := wZerosInStrip_holds, seam := wSeam_of_strip, (Z7) := riemannVonMangoldt_W, FamilyHyps := familyHyps_flat. 

### `hardyW_simple_on_line_flat`

 **[XF′ Thm 9.4] — Z′, flat window:** there is T₀ such that for every T ≥ T₀,
  0.85838 · N_W(T,2T) ≤ #{ρ : W(ρ) = 0 simple, Re ρ = 1/2, T < Im ρ ≤ 2T}  (= #{t ∈ (T,2T] : Z′(t) = 0 ≠ Z″(t)}),
  0.92919 · N_W(T,2T) ≤ N_{d,W}(T,2T),
where N_W counts all zeros of W with T < Im ≤ 2T with multiplicity.  No hypotheses beyond "ϱ is a C³ taper profile"
(conclusion ϱ-free); hardyW_simple_on_line below is the binder-free instance. 

### `hardyW_simple_on_line`

 **[XF′ Thm 9.4] — simple stationary points of Hardy's Z-function — unconditional, no hypotheses.**
There is T₀ such that for every T ≥ T₀:
  0.85838 · N_W(T,2T) ≤ N⁰ˢ_W(T,2T)   and   0.92919 · N_W(T,2T) ≤ N_{d,W}(T,2T),
where W := ζ′ + L₂ζ = ζ′ − ½(χ′/χ)ζ (Defs.hardyW; Z′(t) = i e^{iϑ(t)} W(½+it) [XF′ (Z3)]), N_W(T,2T) counts all zeros of W with
T < Im ≤ 2T with multiplicity (NcountW), N⁰ˢ_W those that are simple with Re = 1/2 — equivalently the t ∈ (T,2T] with
Z′(t) = 0 ≠ Z″(t) — and N_{d,W} the distinct ones.  So at least 85.838 % of the zeros of W (of "𝒵′") at height in (T,2T]
are simple and on the critical line, i.e. are simple real stationary points of Hardy's Z. 

 ### Z′ with the quartic window  [XF′ Thm 9.4 "resp. 86.86 % (optimal window)"] 

### `wEF_atV`

 the W explicit formula for the profiled family P.atV v, any C³ taper, any admissible profile. 

### `hardyW_simple_on_line_quartic`

 **[XF′ Thm 9.4], quartic window — any C³ taper:** 0.86864·N_W(T,2T) ≤ N⁰ˢ_W(T,2T) and 0.93432·N_W ≤ N_{d,W}, large T. 

### `hardyW_simple_on_line_quartic_std`

 **[XF′ Thm 9.4], quartic window — unconditional, no hypotheses:** at least 86.864 % of the zeros of W at height in
(T,2T] are simple real stationary points of Hardy's Z, at least 93.432 % are distinct. 

 ## Z′ literally: simple real stationary points of Hardy's Z-function  [XF′ (Z3) + Thm 9.4]

Zeta23/XiPrime/Hardy/ZFunction.lean defines Hardy's Z branch-free: sline t := 1/2 + t·I, Gfun t := Γℝ(sline t),
ephase t := Gfun t / ‖Gfun t‖ (= e^{iϑ(t)} — no arg/log branch), ZC t := ephase t · ζ(sline t), hardyZ t := (ZC t).re, and proves
ZC is real, HasDerivAt ZC (I · ephase t · hardyW (sline t)) t for t ≠ 0 [(Z3)], hence Z′(t) = 0 ↔ W(½+it) = 0 and then
Z″(t) ≠ 0 ↔ the zero is simple, and ncard_simpleStationaryZ : for 0 < T,
  #{t ∈ (T,2T] | Z′(t) = 0 ∧ Z″(t) ≠ 0} = N0simpleW T (2T). 

### `hardyZ_simple_stationary_points`

 **Simple real stationary points of Hardy's Z — unconditional, no hypotheses** ([XF′ Thm 9.4], flat window):
there is T₀ such that for every T ≥ T₀,
  0.85838 · N_W(T,2T) ≤ #{t ∈ (T,2T] : Z′(t) = 0 and Z″(t) ≠ 0},
N_W(T,2T) = NcountW T (2T) = the number of zeros of W = ζ′ − ½(χ′/χ)ζ with T < Im ≤ 2T, counted with multiplicity
(= N(T,2T) + O(log T), the zeta zero count, by Hardy.Count), Z = hardyZ Hardy's Z-function (ZFunction.lean). 

### `hardyZ_simple_stationary_points_quartic`

 the same with the quartic window: **0.86864 · N_W(T,2T) ≤ #{t ∈ (T,2T] : Z′(t) = 0 ≠ Z″(t)}**, unconditionally. 

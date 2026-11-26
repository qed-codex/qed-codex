---
{
  "module": "Zeta23/XiPrime/Statement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Statement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Statement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Statement.lean — the interface of the ξ′ / Z′ development.

REFERENCES.  Throughout Zeta23/XiPrime, "[XF′ §n]" cites the accompanying write-up on the zeros of ξ′ and of
Hardy's Z′ (section and theorem numbers refer to it).

Definitions and named propositions only.  Layout:
  §1  sanity anchors for ξ: ξ entire, ξ(1−s) = ξ(s), ξ = ½s(s−1)Λ off {0,1}.
  §2  the two classical propositions about the zeros of ξ′, stated here as named Props —
      XiDerivZerosInStrip (F2); the seam facts XiDerivSeam (F1, local finiteness) — and the
      ZeroConfig instance xiDerivZeros built from them.
  §3  the T-indexed coefficient interface CoeffFamily / CoeffFamily.Hyps ([XF′ §11 (H1)–(H3)]:
      coefficients b_N = C(N; L_T) depend on T, constants are T-uniform).
  §4  the interface propositions:
        XiEF               [XF′ Thm 4.2]  entrywise explicit formula, fixed coefficients;
        XiTraceTransfer    [XF′ Lemma 5.1 + 6.1] matrix-level two-trace transfer Ĝ¹ ↔ M̂ᵀ;
        CoeffMoments       [XF′ Thm 8.1 / §11]  two moments of M̂ᵀ for a CoeffFamily;
        xiCoeffFamily.Hyps [XF′ Lemma 7.1] the ξ′ coefficients satisfy (H1)–(H3), D = D₁;
        CertFlat / CertQuartic [XF′ Thm 8.2 "Certified constants"].
  §5  the headline sentences as Props (ξ′), with the ε-free certified decimals.
  §6  the Z′ (Hardy) layer: hypotheses + headline Props  [XF′ §9].
-/
```

 ## §1. Sanity anchors for ξ 

### `xi_differentiable`

 ξ is entire. 

### `xi_eq`

 ξ(s) = ½ s(s−1)·Λ(s) for s ∉ {0,1}  (Λ = completedRiemannZeta = π^{-s/2}Γ(s/2)ζ(s)); this pins the
signs in Mathlib's completedRiemannZeta_eq (Λ = Λ₀ − 1/s − 1/(1−s)). 

### `xi_one_sub`

 the functional equation ξ(1−s) = ξ(s). 

### `xiDeriv_differentiable`

 ξ′ is entire (derivative of an entire function: analytic ⇒ derivative analytic). 

### `XiZerosAreZetaZeros`

 In the open strip, the zeros of ξ are exactly the nontrivial zeros of ζ (sanity; s(s−1)/2 ≠ 0 and
Γℝ(s) ≠ 0 there).  Stated here as a Prop. 

 ## §2. The zeros of ξ′ as an abstract ZeroConfig  [XF′ (F1)–(F3)] 

### `XiDerivZerosInStrip`

 **(F2)** [XF′ §1]: "all zeros of ξ′ lie in 0 < Re s < 1" (Re ξ′/ξ(s) = Σ_ρ Re 1/(s−ρ) > 0 for Re s ≥ 1
by the Hadamard product for ξ, all of whose zeros have 0 < β < 1; then ξ′(1−s) = −ξ′(s)).  Source: Conrey,
J. Number Theory 16 (1983) §2; Levinson–Montgomery, Acta Math. 133 (1974).  Proved in this tree:
theorem xiDerivZerosInStrip_holds (XiPrime/ExplicitFormula/ZeroFree.lean, from Re ξ′/ξ > 0 on Re s ≥ 1).  Consumed by: ZeroConfig.strip
(hence prop:tail's X^{1/2} and W-summability) and by XiEF (every zero inside the contour
[1−σ₁, σ₁] × [−tₙ, tₙ] of [XF′ Prop 4.1] is a member of the configuration). 

### `XiDerivSeam`

 **Seam facts for ξ′** (the analogue of Zeta23.ZetaSeam): classical facts, proved in
XiPrime/Seam.lean.  one_le_mult: ξ′ is entire and not identically zero
(ξ′(2) ≠ 0, or ξ has zeros) so the analytic order at a zero is finite and ≥ 1.  reflect/mult_reflect
[XF′ (F1)]: from ξ′(1−s) = −ξ′(s) and conj ξ′(conj s) = ξ′(s) (differentiate xi_one_sub; Λ₀ real on ℝ), at
the level of analyticOrderAt.  finite_window: zeros of an entire function ≢ 0 are isolated, and the zeros
of ξ′ are confined to a bounded vertical strip |Re s − ½| ≤ R₀ (for Re s ≥ R₀+½: Re L(s) > A(Re s) ≥ |A(s)|,
the cheap half of (F2); then (F1)) — so each height window meets a compact set. 

### `xiDerivZeros`

 The zeros of ξ′ with their multiplicities as an Zeta23.ZeroConfig: carrier := {ρ | ξ′ ρ = 0} EXACTLY
(all zeros), mult := xiDerivMult EXACTLY.  Takes (F2) and the seam facts as arguments; every downstream
theorem therefore displays them in its type until XiPrime/Final.lean supplies the theorems. 

### `XiDerivRvM`

 **(F3)** [XF′ §1]: "N_{ξ′}(T) = N(T) + O(log T);  N_{ξ′}(t+1) − N_{ξ′}(t) ≪ log(t+3)" (Conrey 1983 §2, or:
argument principle for ξ′/ξ = L − A on Re s = 2, where Re(L − A) > 0; Jensen for the local count), rendered
as the tree's RiemannVonMangoldt structure for the ξ′ configuration:  |N_{ξ′}(T,2T) − (T/2π)ℓ₁| ≤ C log T
and N_{ξ′}(t,t+1) ≤ A₀ log(|t|+3) (two-sided, as in Zeta23.RiemannVonMangoldt).  Proved in this tree:
theorem xiDeriv_riemannVonMangoldt (XiPrime/ZeroCount.lean); kept as a named Prop for the interface. 

 ## §3. The T-indexed coefficient interface  [XF′ §11 (H1)–(H3)] 

### `CoeffFamily`

 A coefficient FAMILY: for each height T a finitely-used sequence c^{(T)} : ℕ → ℂ, and ONE continuous
diagonal density D on [0,1].  (ξ′: c^{(T)}_N = C(N; L_T), D = D₁;  Z′: c^{(T)}_N = C(N; ½ l(T)), D = D₁;
ζ: c ≡ −Λ, D(s) = s.) 

### `CoeffFamily.c`

 T ↦ (N ↦ c_N^{(T)}) 

### `CoeffFamily.D`

 the diagonal density: Σ_{N≤e^y} |c_N|²/N ~ l² ∫₀^{y/l} D 

### `CoeffFamily.Hyps`

 **(H1)–(H3)** for a coefficient family, with T-UNIFORM constants (every ∃C is outside ∀T).  Ranges:
x ∈ [2, e^{l(T)}] = [2, T/2π] covers every x ≤ X = e^{λl} ≤ e^{l} used downstream (λ ≤ 1) and is as far as
Lemma 7.1(iii)-type majorants reach (beyond e^{l} the partial sums of C(N;L_T) grow like x^{1+c/l});
y ∈ [0, l(T)] covers y ≤ L = λl.  Sums over N ∈ Finset.Ioc 0 ⌊x⌋₊ (tree convention).  [XF′ §11]:
(H1) Σ_{N≤x}|c_N|N^{-1/2} ≤ C√x·l, (H2) Σ_{N≤x}|c_N|² ≤ C x l², (H3) Σ_{N≤e^y}|c_N|²/N = l²∫₀^{y/l}D + o(l²)
uniformly in y ≤ l (ε-form, no rate).  The (C3) = cheb1c analogue is NOT carried, as it is not
consumed downstream. 

### `CoeffFamily.Hyps.c_one`

 c₁ = 0: the N = 1 frequency log 1 = 0 does not oscillate (its 𝓜[μ,P_c] term would be of size
  T·l·L·‖c 1‖); true for C(1;Λ⋆) = 0. 

### `CoeffFamily.Hyps.D_cont`

 D is continuous on ℝ (the Abel step differentiates y ↦ l²∫₀^{y/l} D
  two-sidedly at every y ∈ [0, L], including y = 0; D₁ is entire so this costs the producer nothing). 

### `xiCoeffFamily`

 the ξ′ coefficient family: b_N^{(T)} := C(N; L_T), L_T = ½l + iπ/4, density D₁  [XF′ §6–7]. 

### `wCoeffFamily`

 the Z′ coefficient family: C(N; ½ l) (REAL parameter, no phase), same density D₁  [XF′ §9.3(ii)]. 

### `D1Summable`

 Sanity obligation for the tsum inside Defs.D1 (junk-zero guard): the series defining D₁ converges
for every real s (factorial decay). 

 ## §4. The interface propositions (one per component)

Conventions.  Pf : ℝ → Params is a HEIGHT-INDEXED parameter family ("the window at height T is
(Pf T).phi T"): for the flat window Pf := fun _ => P; for a profile v, Pf := P.atV v (Defs).  Every
constant is quantified BEFORE T (uniform in the family).  Z : ZeroConfig is abstract in the Props and is
instantiated at xiDerivZeros hF2 hs (resp. wZeros) by Assembly. 

### `XiEF`

 **XiEF — the explicit formula for ξ′, entrywise, with fixed coefficients**  [XF′ Thm 4.2].
For all large T and all 0 ≤ k,l < d:  the zero-side Gram entry
G¹_{kl} = Σ_{ρ₁} m_{ρ₁} φ̂(γ_{ρ₁}−τ_k) φ̂(γ_{ρ₁}−τ_l)  (= Z.Gz, an absolutely convergent sum — asserted)
equals the entry-dependent main term  M_{kl} = ∫ φ̂(τ−τ_k)φ̂(τ−τ_l)[μ + Π_X + P¹_X(τ; L⋆^{kl})]dτ
(= (Pf T).Gentry1, Defs) up to  |𝓔_{kl}| ≤ C · T^{−δ} · (min(1, |τ_k − τ_l|⁻²) + 1/T)  for some δ > 0.
Shape notes: (i) [XF′ Thm 4.2] displays X^{1/2}L²l/T·min(1,Δ⁻²);
the Lean proof runs the contour on the FIXED line Re s = 5/4 (verbatim reuse of the Zeta23/WeilEF line
lemmas, all stated for 1 < c ≤ 3/2) rather than σ₁ = 1+3/l, giving X^{3/4}L²l/T = O(T^{−δ}),
δ = (1 − 3λ/4)/2 > 0 for every fixed λ ≤ 1 — a POWER SAVING is all Lemma 5.1 consumes (|tr Ê| ≤ dCT^{−δ}/(aL²)
= o(N), ‖Ê‖_F² ≤ C′T^{−2δ}(dL + d²/T²)/(aL²)² = o(N), with d ≍ TL, N ≍ Tl, a ≍ 1); (ii) min(1, Δ⁻²) is written
1 / max 1 Δ² so that Δ = 0 gives 1, not Lean's 0⁻¹ = 0; (iii) the "+ 1/T" floor is the Δ-independent term
of the proof's "Collecting (a)–(f)" line, which the displayed bound omits — it costs consumers
nothing.  T ^ (-δ) is Real.rpow (T > 0 eventually). 

### `XiTraceTransfer`

 **XiTraceTransfer — entry errors and entry-dependence are invisible in the two traces**
[XF′ Lemma 5.1 + Lemma 6.1] (consumes XiEF, the PP upper bound for the coefficient
families e_r of [XF′ §6], and Lemma 7.1(iii)).  In hat units (M ↦ M/(aL²)), with Mᵀ := the prime-side
matrix for the FIXED coefficients c^{(T)} = C(·; L_T) ((Pf T).GpC T (F.c T), Defs), for every δ > 0
eventually:  |tr Ĝ¹ − tr M̂ᵀ| ≤ δ·N(T,2T)  and  ‖Ĝ¹‖_F² ≤ (1+δ)‖M̂ᵀ‖_F² + δ·N(T,2T).
(The second line packages ‖𝓔̂‖_F = o(√N) and ‖M̂‖_F² = ‖M̂ᵀ‖_F²(1+O(1/l)); only the upper bound is
consumed by the certificate.) 

### `CoeffMoments`

 **CoeffMoments — the two moments of the fixed-coefficient prime-side matrix**  [XF′ Thm 8.1 for Mᵀ;
§11 "coefficient-generalised prime side"].  For every δ > 0 eventually:
(1−δ)N ≤ tr M̂ᵀ ≤ (1+δ)N  and  ‖M̂ᵀ‖_F² ≤ (κ + δ)·N,  N = N(T,2T) of Z (enters only through H-RvM for Z:
the prime side computes T ℓ₁/2π-type main terms).  The producer `coeffMoments_of_traces` has the shape
CoeffFamily.Hyps F → RiemannVonMangoldt Z → GammaFacts → MVHilbert C_MV → P.Valid → P.lam < 1 →
(window realisation, per profile: ∃ c T₀, ∀ T ≥ T₀, ThmD.AdmWindow ((Pf T).phi T) (P.L T) P.w c
∧ 1/2 ≤ AdmWindow.bv …) → (∀ T, (Pf T).lam = P.lam ∧ (Pf T).w = P.w) →
Tendsto (fun T => ThmD.cRatio (P.lam1 T) ((Pf T).a T) ((Pf T).b T) (J_T T)) atTop (𝓝 c∞) → 0 < c∞ →
CoeffMoments Z Pf F c∞⁻¹,  with J_T T := 2/(P.L T)³ · l T · ∫ y in 0..P.L T, (F.D (y / l T) · (Pf T).g T y);
Assembly plugs c∞ = cWin F.D P.lam v via `tendsto_cRatio_cWin`.  The intermediate
TracesBoundsXi lives in XiPrime/PrimeSide/Interface.lean. 

### `GzMoments`

 **GzMoments — the seam consumed by the certificate** (Assembly composes XiEF + XiTraceTransfer +
CoeffMoments into this; it is literally the pair (htrace, hfrob) of Zeta23.Assembly.count_certificate /
count_certificate_c3 with κ in place of Zeta23.kfun λ):  (1−δ)N ≤ tr Ĝ¹  and  ‖Ĝ¹‖_F² ≤ (κ+δ)N  eventually. 

### `WindowProfile`

 admissible window profiles v on [−1/2, 1/2] (realised as φ_v = √(v(u/L))·φ, Defs.phiV): even, C³,
strictly positive on the closed interval (so √v is C³ there), bounded by 1.  vFlat and vQuartic qualify. 

### `CertFlat`

 **CertFlat — the certified constant, flat window**  [XF′ Thm 8.2 "Certified constants":
1/c ≤ 100905635384/88388425125 + ε₉ ≤ 1.1416163 at λ = 1, so 2 − 1/c ≥ 0.8583837, 3/2 − 1/(2c) ≥ 0.9291918]
(proved in Certificate.lean).  Stated in the exact form the ε-free headline consumes: SOME
λ ∈ [1/2, 1) at which the fixed-λ bounds already beat the decimals STRICTLY (proof: exact rational value of
κ with D1trunc K, K ≥ 9, at λ = 1; D₁ ≤ D1trunc K + ε_K on [0,1] on the correct side; strict at λ = 1; then
continuity of λ ↦ κ₁(λ,v) on [1/2,1]).  κ₁ here is Defs.kappaXi with the FULL series D₁.  DECIMALS: the
interface carries FIVE (leaving ≥ 10⁻⁶ slack so that no certificate route can miss the stated Prop by 10⁻⁷);
the sharp six/seven-digit rational bounds are proved as separately named theorems anyone may quote. 

### `CertQuartic`

 **CertQuartic** — same for v(s) = 1 − (7/100)(2s)² − (51/200)(2s)⁴:
1/c ≤ 277244140547469154168336/245053976636191319722125 + ε₉ ≤ 1.1313598, so ≥ 0.8686402 / 0.9343201. 

 ## §5. The headline sentences for ξ′  [XF′ Thm 8.2]

Assembly route (XiPrime/Assembly.lean): for Z := xiDerivZeros hF2 hs, v admissible, λ ∈ (0,1):
XiEF Z Pf ∧ XiTraceTransfer Z Pf xiCoeffFamily ∧ CoeffMoments Z Pf xiCoeffFamily κ ⟹ GzMoments Z Pf κ'
for every κ' > κ ⟹ (zero side: the tree's TailInputs/BlockInputs for Pf T at height T, generic in Z and in
the Params value, + Zeta23.Assembly.count_certificate (c = 2) / count_certificate_c3 (c = 3), verbatim)
⟹ FixedLamBounds; then CertFlat/CertQuartic give the ε-free decimals.  The λ → 1⁻ "limit form" with
κ₁(1, v) needs only continuity of λ ↦ κ₁(λ,v) on (0,1] ([XF′ Remark 7.2]) and is stated separately. 

### `FixedLamBounds`

 [XF′ Thm 8.2] at fixed λ ∈ (0,1) and window v:  for every ε > 0 and all large T,
(2 − κ₁(λ,v) − ε)·N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T)   and   (3/2 − κ₁(λ,v)/2 − ε)·N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T). 

### `HeadlineFlat`

 **Headline (flat window), ε-free certified form.**  There is T₀ such that for all T ≥ T₀:
  0.85838 · N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T)     — at least 85.838% of the zeros of ξ′ with T < Im ≤ 2T,
                                                counted with multiplicity, are SIMPLE and ON Re s = 1/2;
  0.92919 · N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T)     — at least 92.919% are DISTINCT.
([XF′]'s certified values are 0.858383… / 0.929191…; five decimals frozen here, see CertFlat.) 

### `HeadlineQuartic`

 **Headline (quartic window), ε-free certified form:**  0.86864·N_{ξ′}(T,2T) ≤ N⁰ˢ_{ξ′}(T,2T) and
0.93432·N_{ξ′}(T,2T) ≤ N_{d,ξ′}(T,2T) for all large T  ([XF′]: 0.868640… / 0.934320…). 

### `HeadlineCumulative`

 cumulative form (liminf over (0,T]):  c·N_{ξ′}(0,T) ≤ N⁰ˢ_{ξ′}(0,T) for large T, c = 0.85838 resp.
0.86864 — from the dyadic form by Zeta23.Assembly.dyadic, given H-RvM for ξ′ (N_{ξ′}(0,T) → ∞). 

 The theorems of XiPrime/Final.lean state these headlines with their full types written out, e.g.

  theorem xiDeriv_simple_on_line_flat : ∃ T₀, ∀ T ≥ T₀,
      (0.85838 : ℝ) * Ncount T (2*T) ≤ N0simple T (2*T) ∧ (0.92919 : ℝ) * Ncount T (2*T) ≤ Ndist T (2*T)

with (F2) (XiDerivZerosInStrip), the seam facts (XiDerivSeam) and XiDerivRvM instantiated by the theorems
that prove them, so no such hypothesis appears in the published statements. 

 ## §6. The Z′ layer (Hardy's function)  [XF′ §9] — same architecture

Statement discipline: everything is about the Mathlib-honest meromorphic function
W := ζ′ + L₂ζ = ζ′ − ½(χ′/χ)ζ (Defs.hardyW); Hardy's Z(t) = e^{iϑ(t)}ζ(½+it) and Z′(t) = i e^{iϑ(t)} W(½+it)
[XF′ (Z3)] are a REMARK (a Z built from arg/log branches is not something Lean's deriv treats honestly).
So "t ∈ (T,2T] with Z′(t) = 0 ≠ Z″(t)" is rendered as "½+it is a simple zero of W", which (Z3) shows is the
same set with the same multiplicities. 

### `WZerosInStrip`

 **(Z6)(iii)+(i)+(Z2)** [XF′ §9.1]: every zero of W with |Im ρ| ≥ t₀ lies in 0 < Re ρ < 1 (Littlewood's gap
theorem + de la Vallée Poussin on 1 ≤ σ ≤ 2; Stirling for σ ≥ 2; the functional equation W(s) = −χ(s)W(1−s)
for σ ≤ 0).  Kept as a named Prop; proved in this tree for some t₀ > 0: wZerosInStrip_holds
(XiPrime/Hardy/ZeroFree.lean), with the W seam then given by wSeam_of_strip (XiPrime/Hardy/Seam.lean). 

### `WSeam`

 seam facts for W at heights |Im| ≥ t₀ (analogue of XiDerivSeam; [XF′ (Z2), (Z7)]). 

### `wZeros`

 the zeros of W at height |Im| ≥ t₀ as a ZeroConfig (carrier EXCLUDES the real zeros/poles and the
finitely many low zeros; for T ≥ t₀ its window counts are NcountW etc. — lemma below). 

### `wZeros_window`

 for windows above t₀ the configuration's window is ALL zeros of W there. 

### `wPoleWeight`

 the W coefficient density has pole weight 2: Assembly uses Defs.nucZ / a GpC-analogue with 2·Π_X;
[XF′ §9.3(i)] "doubling Π_X multiplies negligible bounds by 2 or 4" — the CoeffMoments conclusion is
unchanged, so the W prime side is CoeffMoments for wCoeffFamily verbatim, with the Π-part lemmas carrying a
weight parameter.  (Interface note only; no new Prop.) 

### `HeadlineW`

 **Headline for Z′ (flat / quartic), ε-free** [XF′ Thm 9.4]: for all large T,
c·N_W(T,2T) ≤ #{simple zeros of W on Re s = 1/2 with T < Im ≤ 2T} (= #{t ∈ (T,2T]: Z′(t)=0≠Z″(t)}),
cd·N_W(T,2T) ≤ N_{d,W}(T,2T); and N_W(T,2T) = N(T,2T) + O(log T) [XF′ (Z7)] converts the denominator to
the zeta count Zeta23.Ncount if desired (stated separately in Final.lean). 

---
{
  "module": "Zeta23/Hypotheses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Hypotheses.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Hypotheses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Hypotheses.lean — the hypothesis ("axiom") boundary.

Canonical text: the paper.

PRINCIPLE: the fields of PaperInputs are PUBLISHED, CLASSICAL inputs,
stated in the paper's own form with the paper's equation labels. Everything the paper itself derives
(lem:poisson, prop:block, prop:tail, [eq:PiPfacts], [eq:Bdef], prop:trace, thm:traces, §6, taper facts
[eq:phinorms]–[eq:psiints], …) is a proof obligation and must NOT be added here. There are NO Lean
axiom declarations anywhere in this project: hypotheses are fields of the Prop-valued structure
PaperInputs, which every headline theorem takes as an explicit argument, so #print axioms stays at
{propext, Classical.choice, Quot.sound} and the trust boundary is exactly this file.

Every field below: docstring = paper label + verbatim paper statement + literature source + any
deviation in shape (∃-constant form unless the constant is load-bearing).
-/
```

 ## H-EF — Weil's explicit formula in the paper's spectral form  [prop:EF], [eq:EF], [eq:Wdef] 

### `ExplicitFormulaPaper`

 **H-EF** [prop:EF]/[eq:EF], verbatim: "Let f,g ∈ C_c²(ℝ) with supp f, supp g ⊂ [−L/2, L/2]. Then
    W(f,g) = ∫_ℝ h_f(τ) conj(h_g(τ)) ν_X(τ) dτ,   X = e^L."
where [eq:Wdef] "W(f,g) := Σ_ρ m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ)) … converges absolutely; here and below
Σ_ρ runs over the distinct nontrivial zeros (of either sign of γ) and the multiplicity is written
explicitly", h_f = paperFT f, and ν_X = μ + Π_X + P_X is Zeta23.nuX [eq:mudef]–[eq:nudef].
Source: Weil 1952 via [IK04, Theorem 5.12]; the paper's Appendix A [app:EF] derives this exact
normalisation from the literature form [eq:EFstd]. Zeta23/ExplicitFormula.lean proves
(literature form) → ExplicitFormulaPaper.
Shape notes: (i) quantified over every L > 0 (so X = e^L > 1 as the paper requires); (ii) the support
hypothesis is carried explicitly (without it the statement is false); (iii) the
absolute convergence of W and of the right-hand integral ("all integrals absolutely convergent",
App. A) are asserted as part of the package, since Lean's tsum/integral of a non-convergent
expression is 0; (iv) C_c² is rendered as ContDiff ℝ 2 + tsupport ⊆ [−L/2, L/2] (compact). 

 ## H-RvM — Riemann–von Mangoldt + local zero count  [eq:RvM], [prop:tail] first line 

### `RiemannVonMangoldt`

 **H-RvM**.
* main [eq:RvM], verbatim: "By the Riemann–von Mangoldt formula, with l := log(T/2π),
  N(T,2T) = (T/2π)(l + 2 log 2 − 1) + O(log T)."  (ell1 T = l T + 2 log 2 − 1.) Source: [Tit86, Thm 9.4].
* local_count [prop:tail]: "Let A₀ ≥ 1 be an absolute constant such that N(t+1) − N(t) ≤ A₀ log(t+3)
  for all t ≥ 0" — "classical [Tit86, Theorem 9.2]".
  Deviation (deliberate): stated two-sided, for all real t with
  log(|t|+3), i.e. also for windows of negative ordinate. The paper's proof of prop:tail bounds the
  zeros with γ ≤ 0 using the γ ↦ −γ symmetry of the zero set, which it states in [subsec:weil] but
  which is not a field of ZeroConfig; the two-sided local count is an equally classical consequence
  of [Tit86, 9.2] + that symmetry and removes the extra seam obligation. 

 ## H-cheb — Chebyshev–Mertens  [lem:cheb], [eq:cheb1], [eq:cheb2] 

### `ChebyshevMertens`

 **H-cheb** [lem:cheb], verbatim: "For x ≥ 2,
  Σ_{n≤x} Λ(n) ≪ x,  Σ_{n≤x} Λ(n)/√n ≤ 3√x (x ≥ x₀),  Σ_{n≤x} Λ(n)/(√n log n) ≪ √x/log x,
  Σ_{n≤x} Λ(n)² ≪ x log x,                                                          [eq:cheb1]
  Σ_{n≤x} Λ(n)²/n = (log x)²/2 + O(log x),  Σ_{n≤x} Λ(n)²/n (log x − log n) = (log x)³/6 + O((log x)²).
                                                                                    [eq:cheb2]"
Source: [MV07, §2.2] (Chebyshev, Mertens; partial summation). Sums are over n ∈ Finset.Ioc 0 ⌊x⌋₊
(Mathlib's Chebyshev.psi indexing); Λ = ArithmeticFunction.vonMangoldt; the n = 1 terms vanish
(Λ 1 = 0; in cheb1c Lean reads 0/0 as 0). Each ≪ / O(·) is an ∃ C; cheb1b keeps the paper's
literal constant 3 with threshold x₀. Zeta23/Chebyshev.lean proves these fields. 

 ## H-MV — Montgomery–Vaughan weighted Hilbert inequality  [lem:MV] 

### `MVHilbert`

 The weighted ("generalised") Hilbert inequality with constant C [lem:MV], verbatim:
"Let λ_1,…,λ_R be distinct real numbers, δ_r := min_{s≠r} |λ_r − λ_s|, and x_r, z_r ∈ ℂ. Then
  |Σ_{r≠s} x_r conj(z_s)/(λ_r − λ_s)| ≤ (3π/2) (Σ_r |x_r|²/δ_r)^{1/2} (Σ_r |z_r|²/δ_r)^{1/2}."
Source: [MV74, Theorem 2] for z = x (the paper citation); the bilinear form is derived in the paper by a
3-line operator-norm argument. "Any absolute constant in place of 3π/2 would suffice below."
Shape notes: index set = any Fintype ι with DecidableEq; distinctness = injectivity of freq; instead
of δ_r := min_{s≠r}|λ_r−λ_s| (undefined for R = 1) we allow ANY admissible weights 0 < δ_r ≤
|λ_r − λ_s| (s ≠ r) — equivalent to the paper's statement since the right side is antitone in δ.
The bilinear (x,z) form is assumed directly (it is what prop:PP/prop:cross consume). 

 ## H-Γ — Stirling-type facts for μ  [eq:mufacts], [eq:muints] 

### `GammaFacts`

 **H-Γ** [eq:mufacts], verbatim: "μ is even, smooth, increasing in |τ|, μ ≥ μ(0) > −1,
  μ(τ) = (1/2π) log(|τ|/2π) + O(τ⁻²),  μ'(τ) ≪ |τ|⁻¹  (|τ| ≥ 1)"
("(eq:mufacts) is Stirling's formula and Re Γ'/Γ(σ+it) = −γ_E + Σ_{n≥0}(1/(n+1) − (n+σ)/((n+σ)²+t²))"),
and the pure-Γ halves of [eq:muints]:
  "∫_T^{2T} μ(τ) dτ = Tℓ₁/(2π) + O(1/T)",   "∫_T^{2T} μ(τ)² dτ = (Tℓ₁²/4π²)(1 + O(l⁻²))".
(The remaining clause of [eq:muints], "= N(T,2T) + O(l)", is [eq:RvM] and is NOT restated here.)
Source: Stirling for Γ'/Γ (e.g. [MV07, App. C]). This structure only STATES the facts; they are
proved in Zeta23/GammaFacts/Complete.lean (`gammaFacts : GammaFacts`, via the digamma series and a
vertical-line Stirling estimate in Zeta23/GammaFacts/*). "increasing" is rendered as MonotoneOn on [0,∞)
(nondecreasing), which is all prop:trace's Riemann-sum comparison uses. 

 ## The bundle 

### `PaperInputs`

 The published analytic inputs of the paper ([thm:A]: "besides these it uses only Weil's explicit
formula, Stirling's formula for Γ'/Γ, the Riemann–von Mangoldt formula (eq:RvM) and the bound
N(t+1)−N(t) ≪ log(t+3)" + "Chebyshev–Mertens estimates … and the Montgomery–Vaughan generalised
Hilbert inequality"), stated for an abstract zero configuration Z. Every headline theorem takes
(H : PaperInputs Z) explicitly. 

### `PaperInputs.EF`

 H-EF  [prop:EF]/[eq:EF] 

### `PaperInputs.RvM`

 H-RvM [eq:RvM] + local count [prop:tail] 

### `PaperInputs.cheb`

 H-cheb [lem:cheb] 

### `PaperInputs.MV`

 H-MV [lem:MV], ∃ absolute constant 

### `PaperInputs.Gamma`

 H-Γ [eq:mufacts] + Γ-halves of [eq:muints] 

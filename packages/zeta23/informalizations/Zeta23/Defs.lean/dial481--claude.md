---
{
  "module": "Zeta23/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Defs.lean — fixed data of the paper.

Reference text: the paper "More than two thirds of the zeros of the Riemann zeta function lie on
the critical line". Bracketed labels [eq:foo] below are the paper's own labels.

Design (ζ-free abstract layer): nothing in this file mentions
riemannZeta. The zeros enter only through the abstract structure ZeroConfig
("every locally finite multiset of points in the strip 0<β<1 that is invariant under ρ ↦ 1−ρ̄",
paper end of §4). Only Zeta23/Statement.lean instantiates ZeroConfig from Mathlib's ζ.
-/
```

 ## 0. Fourier convention dictionary  [Notation], [subsec:weil]

Paper: "Fourier transforms are f̂(τ) := ∫_ℝ f(u) e^{iτu} du, so that ∫ f ḡ = (1/2π) ∫ f̂ conj(ĝ)
and (f∗g)^ = f̂ ĝ."  and  "For f ∈ C_c²(ℝ) put h_f(z) := f̂(z) = ∫ f(u) e^{izu} du, an entire
function".  Mathlib's Real.fourierIntegral 𝓕 is ∫ f(v) e^{−2πi v ξ} dv, so for real τ:
    paperFT f τ = 𝓕 f (−τ / (2π)).
All paper-side statements use paperFT; conversion to 𝓕 happens only inside proofs. 

### `paperFT`

 Paper Fourier transform / h_f :  paperFT f z = ∫ u, f u * exp (I * z * u)  for complex z
([Notation]; [subsec:weil] "h_f(z) := f̂(z) = ∫ f(u)e^{izu} du"). 

 ## 1. Scalars depending on T only  [Notation], [eq:RvM], [eq:Fdef] 

### `l`

 l := log(T/2π)  [Notation]. 

### `ell1`

 ℓ₁ := l + 2 log 2 − 1, "so that N(T,2T) = Tℓ₁/2π + O(l)"  [Notation]. 

### `Hfun`

 H(λ) := 2 − 1/λ − λ/3  [eq:Fdef]; H(1) = 2/3. 

### `Ffun`

 F(λ) := λ / (1 + λ²/3)  [eq:Fdef]; F(1) = 3/4. 

### `D0`

 D₀ := T^{1/2}  [eq:D0]. 

### `Iwin`

 I := [T, 2T]  [Notation]. 

### `Iprime`

 I' := (T − D₀, 2T + D₀]  [eq:D0]. 

 ## 2. The densities μ, Π_X, P_X, ν_X  [eq:mudef]–[eq:nudef]

Paper, verbatim: "Define, for τ ∈ ℝ and X = e^L > 1, s := 1/2 + iτ,
  μ(τ)   := (1/2π) Re Γ'/Γ(1/4 + iτ/2) − (log π)/(2π),                      [eq:mudef]
  Π_X(τ) := 1/(2π(1/4+τ²)) + (1/π) Re (X^s − 1)/s,                           [eq:Pidef]
  P_X(τ) := −(1/π) Σ_{n≤X} Λ(n)/√n · cos(τ log n),                           [eq:Pdef]
  ν_X    := μ + Π_X + P_X."                                                   [eq:nudef]


### `mu`

 μ(τ) := (1/2π)·Re (Γ'/Γ)(1/4 + iτ/2) − log π /(2π)   [eq:mudef].
Complex.digamma = logDeriv Gamma = Γ'/Γ (Mathlib Gamma/Digamma.lean). 

### `PiX`

 Π_X(τ) := 1/(2π(1/4+τ²)) + (1/π)·Re((X^s − 1)/s),  s = 1/2 + iτ  [eq:Pidef]
("the terms h_k(±i/2) coming from the pole of ζ … rewritten as the density Π_X"). 

### `PX`

 P_X(τ) := −(1/π) Σ_{n ≤ X} Λ(n) n^{−1/2} cos(τ log n)  [eq:Pdef]. Sum over n ∈ Finset.Ioc 0 ⌊X⌋₊
(same indexing as Mathlib's Chebyshev.psi; Λ vanishes off prime powers; the n = 1 term is 0). 

### `nuX`

 ν_X := μ + Π_X + P_X  [eq:nudef]. 

 ## 3. Abstract zero configurations  [Results], [subsec:weil], §4 closing paragraph 

### `gammaOf`

 γ_ρ := (ρ − 1/2)/i = γ − i(β − 1/2), "so that ρ = 1/2 + iγ_ρ, |Im γ_ρ| < 1/2, and γ_ρ ∈ ℝ iff
β = 1/2"  [Notation]. 

### `reflect`

 The reflection ρ ↦ 1 − ρ̄ (same ordinate γ, mirrored β)  [subsec:weil]. 

### `ZeroConfig`

 An abstract zero configuration: a set (carrier) of DISTINCT points ρ = β+iγ in the closed
strip 0 ≤ β ≤ 1 (the instances built from the zeros of ζ and of L(s,χ) lie in the open strip) with
multiplicities mult ρ ≥ 1, locally finite in the ordinate, and
invariant under ρ ↦ 1−ρ̄ with equal multiplicity. Paper §4 (after prop:zeroside), verbatim:
"Inequalities (eq:zeroside) hold for every locally finite multiset of points in the strip 0<β<1
that is invariant under ρ ↦ 1−ρ̄ and satisfies N(t+1)−N(t) ≪ log(t+3); they contain no
arithmetic."  [subsec:weil]: "The multiset {(γ_ρ,m_ρ)} is invariant under γ ↦ γ̄ (i.e. ρ ↦ 1−ρ̄;
multiplicities agree …)".  The quantitative local count N(t+1)−N(t) ≤ A₀ log(t+3) is not part of
this structure; it is a field of PaperInputs (H-RvM) in Zeta23/Hypotheses.lean.
Distinct points (the set) and multiplicities (the function) are deliberately separate objects. 

### `ZeroConfig.carrier`

 the set 𝒵 of distinct zeros 

### `ZeroConfig.mult`

 multiplicity m_ρ (value irrelevant off carrier) 

### `ZeroConfig.finite_window`

 local finiteness in the ordinate: finitely many zeros with T₁ < γ ≤ T₂ 

### `window`

 {ρ ∈ 𝒵 : T₁ < γ ≤ T₂}, γ = Im ρ (positive-ordinate window convention of [Results]; NOT |γ|). 

### `onLine`

 on-line points: β = 1/2. 

### `simple`

 simple points: m_ρ = 1. 

### `N`

 N(T₁,T₂) := #{ρ : T₁ < γ ≤ T₂} counted WITH multiplicity  [Results]. 

### `Nd`

 N_d(T₁,T₂) := same, each distinct point counted once  [Results]. 

### `N0`

 N₀(T₁,T₂) := zeros on the critical line with T₁ < γ ≤ T₂, WITH multiplicity  [Results]. 

### `N0star`

 N₀*(T₁,T₂) := zeros on the critical line with T₁ < γ ≤ T₂, WITHOUT multiplicity  [Results]. 

### `N0s`

 N₀ˢ(T₁,T₂) := #{ρ : T₁ < γ ≤ T₂, β = 1/2, m_ρ = 1}  [Results]. 

### `Ns`

 Nˢ(T₁,T₂) := number of simple zeros (any β) with T₁ < γ ≤ T₂  [Results]. 

### `Wsummand`

 Summand of Weil's form: m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ))  [eq:Wdef]. 

### `W`

 W(f,g) := Σ_ρ m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ)), "Σ_ρ runs over the DISTINCT nontrivial zeros (of
either sign of γ) and the multiplicity is written explicitly"  [eq:Wdef]. As a tsum over the
subtype of carrier; absolute convergence is part of hypothesis H-EF. 

 ## 4. The test family  [subsec:family] 

### `TaperProfile`

 "Fix once and for all a nondecreasing function ϱ ∈ C³(ℝ) with ϱ = 0 on (−∞,0] and ϱ = 1 on
[1,∞)"  [subsec:family]. 

### `Params`

 Fixed (T-independent) parameters: the profile ϱ, the exponent λ (lam; X = (T/2π)^λ), and the
ramp width w ([eq:wrange]: 1 ≤ w ≤ L/8; §6 takes w := 1). T is always a separate argument. 

### `Params.Valid`

 Standing assumptions on the fixed parameters: ϱ a taper profile, 0 < λ ≤ 1, w ≥ 1.
(The upper bound w ≤ L/8 of [eq:wrange] depends on T and is stated where used.) 

### `L`

 L := λ·l  [Notation]. 

### `X`

 X := e^L = (T/2π)^λ  [Notation]. 

### `lam1`

 λ₁ := L/ℓ₁ = λ + O(1/l)  [Notation], [eq:ratio]. Not the same as λ. 

### `hgrid`

 grid step h := 2π/L  [eq:fk]. 

### `d`

 d := ⌊T/h⌋ = ⌊LT/2π⌋  [eq:fk]. 

### `tau`

 τ_k := T + k h (k ∈ ℤ)  [eq:fk]. 

### `phi`

 the taper φ(u) := ϱ((L/2 − |u|)/w)  [eq:phidef]; supp φ = [−L/2, L/2] exactly. 

### `a`

 a := L⁻¹ ∫ φ²  [eq:abdef]. 

### `b`

 b := L⁻¹ ∫ φ⁴  [eq:abdef]. 

### `phiHat`

 φ̂(z) for complex z (paper convention, = h_φ(z)). 

### `phiHatR`

 φ̂ on the real line as a real number ("φ̂ and Φ are real, even, entire"); = Re of phiHat.
That the imaginary part vanishes is proved in Taper.lean, not assumed. 

### `Phi`

 Φ := (φ²)^  [eq:PhigA], complex argument. 

### `PhiR`

 Φ on the real line as a real number; Φ(0) = aL. 

### `autocorr`

 (v ⋆ v)(y) := ∫ v(u) v(u+y) du  [eq:PhigA]. 

### `g`

 g := φ² ⋆ φ²  [eq:PhigA]; Φ² = ĝ on ℝ, g(0) = bL. 

### `Aphi`

 A_φ := φ ⋆ φ  [eq:PhigA]; φ̂² = (A_φ)^. 

### `crho`

 c_ϱ := 4‖ϱ'‖_∞ + 4‖ϱ''‖₁ (≥ 4)  [eq:phinorms]. 

### `psi`

 ψ(r) := min(L, 2/|r|, c_ϱ/(w r²))  [eq:psidef]; at r = 0 the paper's value is L (2/0 = ∞), which
Lean's 2/0 = 0 would get wrong, hence the explicit case. 

### `fk`

 f_k(u) := φ(u) e^{−iτ_k u}  [eq:fk]; h_{f_k}(z) = φ̂(z − τ_k). 

### `calE`

 ℰ_T := w/L + (l² + X) log l /(T l) + T^{λ/2 − 1}  [thm:traces]. 

 ### The prime-side matrix (second expression in [eq:Gdef]) 

### `Gentry`

 G_{kl} via the PRIME side: ∫_ℝ φ̂(τ−τ_k) φ̂(τ−τ_l) ν_X(τ) dτ, X = e^L  [eq:Gdef, 2nd expression],
for arbitrary integer indices k, l. Real-valued. 

### `Gp`

 The d×d prime-side matrix G = (G_{kl})_{0≤k,l<d} as a complex matrix (entries are real;
complex so that RHLinalg's RCLike lemmas and the zero-side matrix share one type). 

### `trGtilde`

 tr G̃ as the real number L⁻¹ Σ_{k<d} G_{kk} (what §5 computes)  [prop:trace]. 

### `trGtildeSq`

 tr G̃² = Σ_{k,l<d} G̃_{kl}² (= ‖G̃‖_F², G real symmetric)  [sec:prime intro]. 

### `tilde`

 scaling to tilde units M ↦ M/L  [eq:Gdef], [eq:AE]  (G̃, Ã, Ẽ). 

### `hat`

 scaling to hat units M ↦ M/(aL²)  [eq:hatunits]  (Ĝ, Â, Ê). Not to be mixed with tilde
units. 

 ### The zero-side matrices  [eq:Gdef] first expression, [eq:AE], §4 Block structure 

### `Gsummand`

 zero-side summand m_ρ φ̂(γ_ρ − τ_k) φ̂(γ_ρ − τ_l). 

### `Gz`

 G_{kl} := W(f_k,f_l) = Σ_ρ m_ρ φ̂(γ_ρ−τ_k) φ̂(γ_ρ−τ_l)  [eq:Gdef, 1st expression] (zero side;
tsum over all distinct zeros). H-EF gives Z.Gz P T = P.Gp T. 

### `ZIprime`

 𝒵(I') := distinct zeros with ordinate γ ∈ I' = (T−D₀, 2T+D₀]  [§4 Block structure]. 

### `Az`

 A_{kl} := Σ_{ρ : γ ∈ I'} m_ρ φ̂(γ_ρ−τ_k) φ̂(γ_ρ−τ_l)  [eq:AE] (a FINITE sum, finsum). 

### `Ez`

 E := G − A  [eq:AE] (the tail: zeros with γ ∉ I', INCLUDING negative ordinates). 

### `S1`

 𝒮₁: β = 1/2 and m_ρ = 1, within 𝒵(I'). s₁ := #𝒮₁  [§4 Block structure]. 

### `S2`

 𝒮₂: β = 1/2 and m_ρ ≥ 2, within 𝒵(I'). s₂ := #𝒮₂. 

### `offLine`

 off-line points of 𝒵(I') (β ≠ 1/2); 𝒫 = unordered pairs {ρ, 1−ρ̄} of these, #offLine = 2p. 

### `s1`

 s₁ := #𝒮₁. 

### `s2`

 s₂ := #𝒮₂. 

### `p`

 p := number of unordered off-line pairs {ρ,1−ρ̄} in 𝒵(I'); #offLine = 2p. 

### `NIprime`

 N(I') := N(T−D₀, 2T+D₀)  [eq:Ncount]. 

### `NonIprime`

 N_on(I') := Σ_{ρ ∈ 𝒮₁ ∪ 𝒮₂} m_ρ  [§4]. 

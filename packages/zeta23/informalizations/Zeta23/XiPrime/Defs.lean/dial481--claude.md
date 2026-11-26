---
{
  "module": "Zeta23/XiPrime/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 ## 1. Riemann's ξ and its derivative, against Mathlib  [XF′ §0]

Mathlib: completedRiemannZeta s = Λ(s) = π^{-s/2} Γ(s/2) ζ(s) (poles at 0, 1), and the entire
completedRiemannZeta₀ = Λ₀ with Λ(s) = Λ₀(s) − 1/s − 1/(1−s) (completedRiemannZeta_eq).  Riemann's
ξ(s) := ½ s(s−1) Λ(s) = ½ s(s−1) Λ₀(s) + ½, entire by construction.  The body below is verbatim that
of Zeta23.WeilEF.xi, so XiPrime.xi = WeilEF.xi holds by rfl. 

### `xi`

 ξ(s) := s(s−1)/2 · Λ₀(s) + 1/2  (= ½ s(s−1) π^{-s/2} Γ(s/2) ζ(s) for s ∉ {0,1}; entire). 

### `xiDeriv`

 ξ′ := the complex derivative of ξ (an entire function; [XF′ §0] writes F := (ξ′)′/ξ′). 

### `IsXiDerivZero`

 ρ₁ is a zero of ξ′:  ξ′(ρ₁) = 0 — all zeros, no real-part condition (the
denominator of every headline proportion counts every zero of ξ′ in the height window, exactly as
[XF′ Thm 8.2] does).  The classical fact (F2) of [XF′ §1], "all zeros of ξ′ lie in 0 < Re s < 1"
(Re ξ′/ξ = Σ_ρ Re 1/(s−ρ) > 0 for Re s ≥ 1 via the Hadamard product for ξ, then ξ′(1−s) = −ξ′(s);
Conrey, J. Number Theory 16 (1983) §2), is not built into this predicate: it is the named proposition
XiPrime.XiDerivZerosInStrip of Statement.lean. 

### `xiDerivMult`

 m_{ρ₁} := multiplicity of ρ₁ as a zero of ξ′ = analytic order of ξ′ at ρ₁ (ℕ∞ → ℕ via toNat; as for
Zeta23.zeroMult, 1 ≤ xiDerivMult ρ encodes "ξ′ not locally ≡ 0 at ρ AND ξ′(ρ) = 0"). 

### `zerosIn`

 {ρ₁ : ξ′(ρ₁) = 0, T₁ < Im ρ₁ ≤ T₂}  (ALL zeros in the height window; positive ordinates, NOT |Im|). 

### `Ncount`

 N_{ξ′}(T₁,T₂) := number of zeros of ξ′ with T₁ < Im ≤ T₂ (any real part), COUNTED WITH MULTIPLICITY
([XF′ (F3)]: N_{ξ′}(T) = N(T) + O(log T)).  This is the DENOMINATOR of every headline proportion. 

### `Ndist`

 N_{d,ξ′}(T₁,T₂) := number of DISTINCT zeros of ξ′ with T₁ < Im ≤ T₂ (any real part). 

### `N0simple`

 N^{s}_{0,ξ′}(T₁,T₂) := #{ρ₁ : T₁ < Im ρ₁ ≤ T₂, Re ρ₁ = 1/2, m_{ρ₁} = 1}: SIMPLE zeros of ξ′ ON the
critical line (each such point counted once — it is simple).  Numerator of [XF′ Thm 8.2, first line]. 

### `N0`

 N_{0,ξ′}(T₁,T₂) := zeros of ξ′ on the critical line, with multiplicity (for the trivial chain only). 

 ## 2. The coefficient system C(N; Λ⋆)  [XF′ Def. 2.3]

[XF′ Def 2.3], verbatim: "C(N;Λ⋆) := −Λ(N) + Σ_{j=0}^{Ω(N)−1} Λ⋆^{−(j+1)} [(Λ·log) ∗ Λ^{∗j}](N)",
where ∗ is Dirichlet convolution, Λ^{∗0} = δ, Ω(N) = number of prime factors with multiplicity (the
j-sum is genuinely finite: Λ^{∗j} is supported on N with Ω(N) ≥ j, so (Λ log) ∗ Λ^{∗j} needs Ω(N) ≥ j+1).
Lean: Λ = ArithmeticFunction.vonMangoldt (ℝ-valued), log = ArithmeticFunction.log, pointwise product =
pmul, Dirichlet convolution = the ring multiplication of ArithmeticFunction ℝ, so Λ ^ j is the j-fold
DIRICHLET power (Λ ^ 0 = 1 = δ), Ω = ArithmeticFunction.cardFactors.  Λ⋆ is a COMPLEX parameter
([XF′] uses Λ⋆ = L⋆ = ½ log(τ⋆/2π) + iπ/4 for ξ′ and the REAL value ½ log(τ⋆/2π) for Z′). 

### `lamLogConv`

 the real arithmetic function (Λ·log) ∗ Λ^{∗j}. 

### `xiCoeff`

 C(N; Λ⋆) ∈ ℂ  [XF′ Def 2.3].  (For Λ⋆ = 0 Lean reads 0⁻¹ = 0; irrelevant, |Λ⋆| > A(σ₁) always.) 

### `LT`

 L_T := ½ l + iπ/4,  l = log(T/2π)  [XF′ §6]: the frozen parameter ("b_N := C(N; L_T)"). 

### `Lstar`

 L⋆(τ⋆) := ½ log(τ⋆/2π) + iπ/4  [XF′ Def 2.3 / Thm 4.2]: the entry-dependent frozen parameter,
τ⋆ = ½(τ_k + τ_l). 

### `L2star`

 L_{2⋆}(τ⋆) := ½ log(τ⋆/2π) ∈ ℝ  [XF′ Thm 9.2]: the Z′ frozen parameter (no phase). 

 ## 3. Prime-side densities with general complex coefficients  [XF′ Thm 4.2, §6] 

### `Pc`

 P_c(X; τ) := (1/π) Re Σ_{N ≤ X} c_N N^{−1/2−iτ}
            = (1/π) Σ_{N ≤ X} (Re c_N · cos(τ log N) + Im c_N · sin(τ log N)) / √N
for an arbitrary coefficient sequence c : ℕ → ℂ (the real-part form of [XF′ Thm 4.2]; for
c = −Λ this is the paper's P_X = Zeta23.PX, for c = Λ·χ it is ThmE's twisted density).  Indexing
Finset.Ioc 0 ⌊X⌋₊ as Zeta23.PX. 

### `P1X`

 P^{(1)}_X(τ; Λ⋆) := P_c(X; τ) with c = C(·; Λ⋆)  [XF′ Thm 4.2]. 

### `nucW`

 ν_{c,ϖ}(X) := μ + ϖ·Π_X + P_c(X): density with general coefficients c and POLE WEIGHT ϖ (so that ξ′ and
Z′ are one prime-side theorem).  ξ′: ϖ = 1 [XF′ Thm 4.2(a)];  Z′: ϖ = 2 [Thm 9.2(a)]. 

### `nuc`

 ν_c(X) := μ + Π_X + P_c(X)  (pole weight 1; the ξ′ density). 

### `nucZ`

 ν^{𝒵}_c(X) := μ + 2·Π_X + P_c(X)  (pole weight 2; the Z′ density). 

### `GentryCW`

 M^{c,ϖ}_{kl} := ∫_ℝ φ̂(τ−τ_k) φ̂(τ−τ_l) ν_{c,ϖ}(X;τ) dτ, X = e^L: the prime-side Gram entry for FIXED
coefficients c and pole weight ϖ.  The integrand is parenthesised as ONE product (binder-swallow guard). 

### `GentryC`

 M^{c}_{kl} := the pole-weight-1 (ξ′) entry  ([XF′ §6] "M^T" is c = C(·;L_T); Zeta23.Params.Gentry is
c = −Λ up to nuc 1 = nuX by rfl-unfolding). 

### `GpC`

 the d×d matrix (M^{c}_{kl})_{0≤k,l<d} as a complex matrix (entries real), same typing as P.Gp. 

### `tauStar`

 τ⋆_{kl} := ½(τ_k + τ_l). 

### `Gentry1`

 M_{kl} := ∫ φ̂(τ−τ_k) φ̂(τ−τ_l) [μ + Π_X + P^{(1)}_X(τ; L⋆^{kl})] dτ — the ENTRY-DEPENDENT main term
of [XF′ Thm 4.2] (coefficients frozen at L⋆ = L⋆(τ⋆_{kl})). 

### `Gp1`

 the d×d matrix M of entry-dependent main terms. 

 ## 4. The diagonal density D₁ and the window functional  [XF′ Lemma 7.1, Thm 8.1] 

### `D1coeff`

 d_k := 2·4^k (k−1)!/(2k)!  (k ≥ 1), the coefficient of s^{2k+1} in D₁; d₁ = 4, d₂ = 4/3, d₃ = 16/45, …
Stated for the shifted index: D1coeff k = d_{k+1} = 2·4^{k+1}·k!/(2k+2)!. 

### `D1`

 D₁(s) := s − 4s² + Σ_{k≥1} d_k s^{2k+1}  [XF′ Lemma 7.1]  (= Σ_k D_{1,k}: D_{1,1} = s(2s−1)²,
D_{1,k} = 4^k(k−1)!/(k(2k−1)!) s^{2k+1} for k ≥ 2; Farmer–Gonek's F₁ minus its T^{-2α} log T term).
The series has infinite radius of convergence (tsum form). 

### `D1trunc`

 truncation of D₁ keeping k ≤ K (K ≥ 1 terms of the series), a polynomial; the certificate works with
D1trunc 9 and the tail bound ε₉ ≤ 3.43·10⁻⁷ on [0,1]  [XF′ Thm 8.2 "Certified constants"]. 

### `vConv`

 (v⋆v)(r) := ∫_{−1/2}^{1/2−r} v(s)·v(s+r) ds — the autocorrelation of the profile on the unit window, for
lags 0 ≤ r ≤ 1 (both s and s+r range over [−1/2,1/2]; = L⁻¹·(autocorrelation of the sharp window
u ↦ v(u/L)·1_{[−L/2,L/2]} at lag rL)).  ONE parenthesised product.  (This is the form the prime side's
J_T converges to with no Fubini step.) 

### `jWin`

 𝒥_D(λ; v) := 2 ∫₀¹ D(λr)·(v⋆v)(r) dr   [XF′ Thm 8.1, proof: "J_{D₁} = (2/λ)∫₀¹(v⋆v)(r)D₁(λr)dr
= (1/λ)∬_{[−1/2,1/2]²} D₁(λ|s−s′|)v(s)v(s′) ds ds′" — we take the FIRST displayed form as the definition;
λ·𝒥_D = λ²·J_D].  ζ check: D(s) = s, v ≡ 1: vConv 1 r = 1 − r, jWin = 2λ∫₀¹ r(1−r)dr = λ/3. 

### `cWin`

 The generalised window functional  c_λ(v; D) := λ(∫v)² / (∫v² + λ·𝒥_D(λ;v)),  ∫ over [−1/2, 1/2]
[XF′ Thm 8.1: c^{(1)}_λ(v) = c_λ(v; D₁) = λ(∫v)²/(∫v² + λ∬D₁(λ|s−s′|)vv′)].  For D(s) = s this equals
Zeta23.ThmD.cFun (λ²∬|s−s′|vv′). 

### `kappaXi`

 κ₁(λ, v) := 1/c_λ(v; D₁) — the ξ′ second-moment constant ("‖Ĝ^{(1)}‖_F² = κ₁ N (1+o(1))").
For the flat window v ≡ 1 (vConv 1 r = 1 − r): κ₁(λ,1) = 1/λ + 2∫₀¹(1−r)D₁(λr)dr (ζ analogue, D(s) = s:
1/λ + λ/3 = Zeta23.kfun). 

### `vFlat`

 the flat window profile v ≡ 1 on [−1/2,1/2] (realised by the tree's ramp taper P.phi, φ² = v(u/L)
up to the width-w ramps). 

### `vQuartic`

 the explicit quartic window v(s) = 1 − (7/100)(2s)² − (51/200)(2s)⁴  [XF′ Thm 8.2 "Certified
constants"]: positive on [−1/2,1/2] (min 27/40 at s = ±1/2), even, polynomial; it saturates the
numerically optimal window to 10⁻⁶. 

### `_root_.Zeta23.Params.phiV`

 the window with profile v realised on the tree's taper: φ_v(u) := √(v(u/L)) · φ(u), so that
φ_v² = v(u/L)·φ² (ThmD's phiD pattern with cos(√2λ·) ↦ v).  max 0 guards the sqrt off [−L/2,L/2]. 

### `_root_.Zeta23.Params.atV`

 the per-height parameter set realising φ_v at height T (ThmD's Params.atD trick, Zeta23/ThmD/ParamsD.lean:
(P.atV v T).phi T = P.phiV v T, while λ, w, L, X, d, τ_k, … are P's, definitionally). 

 ## 5. Hardy-side objects for the Z′ theorem  [XF′ §9.0] 

### `chiFE`

 χ(s) := Λ(1−s)/Λ(s)·(Γ-part) — concretely the factor with ζ(s) = χ(s) ζ(1−s); we take the Mathlib-native
form χ := Gammaℝ(1−s)/Gammaℝ(s) (Gammaℝ s = π^{-s/2}Γ(s/2)), meromorphic. 

### `L2`

 L₂(s) := −½ χ′/χ (s)  [XF′ §9.0]  (= ½(L(s)+L(1−s)); real on Re s = 1/2, = ϑ′(t) there). 

### `hardyW`

 W(s) := ζ′(s) − ½ (χ′/χ)(s) ζ(s) = ζ′(s) + L₂(s) ζ(s)  [XF′ §9.0]; meromorphic on ℂ (poles at 0, 1,
3, 5, …), real on ℝ, and  Z′(t) = i e^{iϑ(t)} W(½+it)  [XF′ (Z3)], so the zeros of W on Re s = 1/2 are
exactly the stationary points of Hardy's Z, with multiplicity. 

### `IsWZero`

 ρ is a non-real zero of W:  W ρ = 0 ∧ Im ρ ≠ 0 — no real-part condition (as for ξ′).
W is meromorphic with poles only on ℝ (at 0, 1, 3, 5, …) and has infinitely many real zeros [XF′ (Z6)];
"Im ρ ≠ 0" removes both (at a pole Mathlib's deriv/values are junk and analyticOrderAt = 0, so poles must
not be admitted as "zeros"), and the height window T < Im ρ ≤ 2T, T > 0, never sees them anyway.  The
classical fact (Z6)(iii) "every zero of W with |Im| ≥ t₀ lies in 0 < Re < 1" (Littlewood's gap theorem +
de la Vallée Poussin) is the named proposition XiPrime.WZerosInStrip of Statement.lean. 

### `wMult`

 multiplicity of a zero of W := analytic order of W (W is analytic off its real poles). 

### `zerosInW`

 zeros of W with T₁ < Im ≤ T₂ (any real part; non-real automatically when T₁ ≥ 0). 

### `NcountW`

 N_W(T₁,T₂), with multiplicity  [XF′ (Z7)]: = N(T₁,T₂) + O(log T₂). 

### `NdistW`

 N_{d,W}(T₁,T₂): distinct zeros of W with T₁ < Im ≤ T₂. 

### `N0simpleW`

 #{ρ : T₁ < Im ρ ≤ T₂, Re ρ = 1/2, W(ρ) = 0 simple} = #{t ∈ (T₁,T₂] : Z′(t) = 0 ≠ Z″(t)}  [XF′ (Z3)]. 

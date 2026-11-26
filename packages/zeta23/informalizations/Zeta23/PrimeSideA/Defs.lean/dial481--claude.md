---
{
  "module": "Zeta23/PrimeSideA/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — prime side (paper §5 [sec:prime]) — ABSTRACT LAYER & SHARED DEFINITIONS
for PrimeSideA.lean / PrimeSideB.lean.

Bracketed labels and section numbers (§5.2, …) are as in the paper
"More than two thirds of the zeros of the Riemann zeta function lie on the critical line".

SEAM between PrimeSideA.lean and PrimeSideB.lean:
  * The seam object is the symmetric bilinear form
        𝓜[u₁,u₂] := ∬_{I×I} Φ(τ−τ')² u₁(τ) u₂(τ') dτ dτ',   I = [T,2T]          (§5.4)
    spelled here LITERALLY as `Mform Φ T u₁ u₂` below, and 𝓜 := 𝓜[ν_X,ν_X] = `MtotalA`.
  * PrimeSideA.lean : [prop:trace] tr G̃ = aL·N(T,2T)+O(L√X);
      [eq:trG2int]+[eq:Kbounds]+[lem:ends] tr G̃² = 𝓜 + O(L·l·log l·(l²+X));
      [eq:Msplit] (6-term expansion of 𝓜); [prop:mumu]; [prop:cross] (four bounds).
  * PrimeSideB.lean : [prop:PP] incl. 𝒟/𝒪₁/𝒪₂ and the g-sandwich via H-cheb [eq:cheb2];
      [thm:traces] = [eq:tr1],[eq:tr2],[eq:ratio] assembling A's five results + prop:PP + H-Γ [eq:muints] + H-RvM.
  * Error-term shape everywhere: ∃ C T₀ (allowed to depend on the profile constants and on λ),
      ∀ T ≥ T₀, |lhs − main| ≤ C·(error expression).  No filters / IsBigO until the final liminf wrapper.

ABSTRACT LAYER.  §5 is a computation about the functions φ̂, Φ, μ, Π_X, P_X on the REAL line
using only a short list of facts about them ([eq:psidef], [eq:abdef], [eq:gbounds], [eq:Phi2FT],
[lem:poisson], [eq:mufacts], [eq:PiPfacts], [lem:cheb]).  We therefore prove §5 for ABSTRACT data
(`Setting` = the scalars T, λ, w;  `LocalFun` = the taper data φ̂, Φ, A_φ, g, a, b) subject
to exactly those facts (hypothesis structures in PrimeSideA.lean), and a thin bridge
(Zeta23/PrimeSideA/Bridge.lean) instantiates it with the
concrete objects of Zeta23/Defs.lean: `Zeta23.Params.phiHatR`, `.PhiR`, `.a`, `.b`, `.g`, `.Aphi`,
so that `trGtA` below becomes `Zeta23.Params.trGtilde` etc.  Names in this
layer carry a trailing `A` (abstract) where they would otherwise clash with Zeta23/Defs.lean.
The closed-form, ζ-free objects `Zeta23.l`, `Zeta23.ell1`, `Zeta23.mu` [eq:mudef], `Zeta23.PiX` [eq:Pidef],
`Zeta23.PX` [eq:Pdef], `Zeta23.nuX` [eq:nudef] are used DIRECTLY from Zeta23/Defs.lean, and the analytic
inputs H-Γ / H-cheb are Zeta23/Hypotheses.lean's `GammaFacts` / `ChebyshevMertens` verbatim, so the
statements here are literally about the official objects of Zeta23/Defs.lean; only the taper enters
abstractly.

The prime side is ζ-free: N(T,2T) enters only as an abstract real together
with [eq:RvM].

FOURIER CONVENTION: paper f̂(τ) := ∫ f(u) e^{iτu} du (§1.4) = `Zeta23.paperFT`.  On
this side we only meet φ̂ and Φ := (φ²)^ on ℝ, where they are real and even; we carry them as
functions ℝ → ℝ (= `phiHatR`, `PhiR` of Defs.lean).
-/
```

 ## Scalars of the abstract setting  [§1 Notation, §1.4; eq:wrange; eq:fk] 

### `Setting`

 The free scalar parameters: height `T`, bandwidth ratio `λ` (`0<λ≤1`), ramp width `w`
([eq:wrange] `1 ≤ w ≤ L/8`; §6 takes `w = 1`).  (Zeta23/Defs.lean's `Params` = (ϱ, λ, w) with `T`
separate; the bridge is `fun (P : Zeta23.Params) T => ⟨T, P.lam, P.w⟩` and then `L, X, d, tau, h`
below agree with `P.L T, P.X T, P.d T, P.tau T, P.hgrid T` by `rfl`.) 

### `l`

 `l := log(T/2π)` [Notation] — this IS `Zeta23.l p.T`. 

### `ell1`

 `ℓ₁ := l + 2 log 2 − 1` [Notation] — this IS `Zeta23.ell1 p.T`.  NOTE ℓ₁ ≠ l. 

### `L`

 `L := λ l` [Notation] (same body as `Zeta23.Params.L`). 

### `X`

 `X := e^L = (T/2π)^λ` [Notation] (same body as `Zeta23.Params.X`). 

### `h`

 Grid spacing `h := 2π/L` [§2.2] (= `Zeta23.Params.hgrid`). 

### `d`

 `d := ⌊T/h⌋ = ⌊LT/2π⌋` [§2.2] (= `Zeta23.Params.d`). 

### `tau`

 Grid points `τ_k := T + k h  (k ∈ ℤ)` [eq:fk] (= `Zeta23.Params.tau`). 

### `I`

 The window `I := [T, 2T]` [Notation] (= `Zeta23.Iwin p.T`). 

 ## The prime-power sum: notation of §5 for `Zeta23.PX` [eq:Pdef, §2.1] 

### `acoef`

 `a_n := Λ(n) n^{-1/2}` [Notation, §1.4]. 

### `ycoef`

 `y_n := log n` [Notation, §1.4]. 

### `primeRange`

 The index set "prime powers `n ≤ X`": all `0 < n ≤ ⌊X⌋` weighted by Λ (zero off prime powers);
spelled `Finset.Ioc 0 ⌊X⌋₊` as in Zeta23/Defs.lean's `PX` and Mathlib's `Chebyshev.psi`. 

### `PX_eq`

 `Zeta23.PX` in the `a_n, y_n` notation of §5: `P_X(τ) = −(1/π) Σ_{n≤X} a_n cos(τ y_n)`. 

 ## Abstract functional data

In the concrete instantiation `phiHat, Phi, Aphi, g, a, b` are Zeta23/Defs.lean's `P.phiHatR T`,
`P.PhiR T`, `P.Aphi T`, `P.g T`, `P.a T`, `P.b T` ([eq:phidef], [eq:abdef], [eq:PhigA]). 

### `LocalFun`

 The T-dependent taper data [eq:PhigA, eq:abdef] (abstract; see the bridge). 

### `LocalFun.phiHat`

 `φ̂` restricted to ℝ (real-valued: φ is real and even) [§2.2]. 

### `LocalFun.Phi`

 `Φ := (φ²)^` restricted to ℝ (real, even, entire) [eq:PhigA]. 

### `LocalFun.Aphi`

 `A_φ := φ ⋆ φ`, `(v⋆v)(y) := ∫ v(u)v(u+y)du` [eq:PhigA]. 

### `LocalFun.g`

 `g := φ² ⋆ φ²` [eq:PhigA]. 

### `LocalFun.a`

 `a := L⁻¹ ∫ φ²` [eq:abdef]. 

### `LocalFun.b`

 `b := L⁻¹ ∫ φ⁴` [eq:abdef]. 

### `GentryA`

 The prime-side matrix entry (second expression in [eq:Gdef], §2.2):
`G_{kl} = ∫_ℝ φ̂(τ−τ_k) φ̂(τ−τ_l) ν_X(τ) dτ`, with `ν_X = Zeta23.nuX X` [eq:nudef] CONCRETE
(same shape as `Zeta23.Params.Gentry`, which is the case `F.phiHat := P.phiHatR T`). 

### `GtildeA`

 `G̃ := G/L` as a `d × d` real matrix, indices `0 ≤ k,l < d` [eq:Gdef]. 

### `trGtA`

 `tr G̃ = L⁻¹ Σ_{k<d} G_{kk}` [§5.2 "L tr G̃ = Σ_{k<d} G_kk"] (same shape as
`Zeta23.Params.trGtilde`: `L⁻¹ * Σ_{k : Fin d}`). 

### `trGt2A`

 `tr G̃² = Σ_{k,l<d} G̃_{kl}² = L⁻² Σ_{k,l<d} G_{kl}²` [§5; eq:trG2int] (same shape as
`Zeta23.Params.trGtildeSq`). 

 ## The seam: the bilinear form 𝓜[·,·]  [§5 "Evaluation of 𝓜", §5.4] 

### `Mform`

 `𝓜[u₁,u₂] := ∬_{I×I} Φ(τ−τ')² u₁(τ) u₂(τ') dτ dτ'`, `I = [T,2T]` (§5.4).
This literal spelling is shared between PrimeSideA.lean and PrimeSideB.lean. 

### `MtotalA`

 `𝓜 := ∬_{I×I} Φ(τ−τ')² ν_X(τ) ν_X(τ') dτ dτ'` [lem:ends statement, §5.3]. 

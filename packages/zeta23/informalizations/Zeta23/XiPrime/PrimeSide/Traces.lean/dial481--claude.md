---
{
  "module": "Zeta23/XiPrime/PrimeSide/Traces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Traces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Traces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/Traces.lean — ξ′ component, generalised-coefficient prime side: the output package
TracesBoundsXi and the ABSTRACT assembly FactsXi → TracesBoundsXi.

Mirror of Zeta23/ThmD/Traces.lean (DataD/FactsD → TracesBoundsD, the window-general [thm:traces])
with three changes, all forced by what XiPrime/Coeff.lean can deliver:
 * the §5 remainders carry the CRUDE coefficient majorants (Lemma 7.1(iii), Remark 7.2):
   prop_trace O(L√X·l), lem_ends O(L·l³·log l·(1+X)), prop_PP O(L·l²·X), cross_muP O(L·l²·√X),
   cross_PPi O(L·X·l) — each larger than the ζ shape by a power of l, each still o(main) at fixed
   λ < 1 because it sits behind X/T or √X/T;
 * the partial-summation field sumJ is in ε-form (the diagonal law Lemma 7.1(i) is
   "+ o(l²)"): Σ_N |c_N|²/N·g(log N) = (L³/2)·J_T + o(l²·L);
 * consequently the conclusions are Asymptotics.IsEquivalent statements (rate-free), proved with
   Mathlib's ~[atTop] algebra (mul/div/pow) instead of explicit-constant pointwise lemmas.
Everything here is about abstract real functions of T; no integrals, no coefficients.
-/
```

 ## The moment functional and the output package 

### `JD`

 The window × density moment `J_T := (2/L³) · l · ∫_0^L D(y/l) g(y) dy`
(for `D(s) = s` this is ThmD's `J_T = (2/L³) ∫_0^L g(y) y dy` of [eq:abJ]; its T-limit for the window with
profile `v` is `jWin D λ v / λ`, XiPrime/Window.lean). 

### `mainTr2Xi`

 the second-trace main term `(TL/2π)(b ℓ₁² + L² J)` ([eq:ratio-general]; [XF′] Thm 8.1's `‖G̃‖²_F`). 

### `TracesBoundsXi`

 **The ξ′ trace package** (mirror of `Zeta23.ThmD.TracesBoundsD` in rate-free form).  `aT, bT` are the
taper moments `L⁻¹∫φ², L⁻¹∫φ⁴`, `JT` the moment `JD D g_T (P.L T) (l T)`, `trG, trG2` the two prime-side
traces of `M̃ᵀ = Mᵀ/L`, and `Ncnt` any count with `Ncnt = T ℓ₁/2π + O(l)` (ξ′: N_{ξ′}(T,2T)). 

### `TracesBoundsXi.tr1'`

 [eq:tr1]': `tr G̃ ~ a L N` — [XF′] Thm 8.1 `tr Ĝ = N(1 + o(1))`. 

### `TracesBoundsXi.tr2`

 [eq:tr2]: `tr G̃² ~ (TL/2π)(b ℓ₁² + L² J_T)` — [XF′] Thm 8.1's `‖Ĝ‖²_F = (N/c)(1 + o(1))` before
  normalisation. 

### `TracesBoundsXi.ratio`

 [eq:ratio-general]: `(tr G̃)²/tr G̃² ~ cRatio(λ₁; a, b, J_T) · N`. 

### `TracesBoundsXi.frhat`

 hat-units second moment: `tr G̃²/(aL)² ~ cRatio(λ₁; a, b, J_T)⁻¹ · N` (`= ‖M̂ᵀ‖²_F`). 

 ## Little-o glue 

### `isLittleO_of_le_mul`

 domination by a vanishing multiple gives little-o: |g| ≤ E·h eventually with E → 0. 

### `evBound_isLittleO_of_le_mul`

 an EvBound whose majorant is dominated by a vanishing multiple of h is little-o of h. 

### `eventually_abs_sub_le_of_isEquivalent`

 two-sided δ-form of an asymptotic equivalence with an eventually nonnegative right side. 

 ## The scalar rates 

### `tendsto_l_sq_mul_X_div`

 `l² X / T → 0` for `0 < λ < 1` (the one place `λ < 1` strictly is used: `X = (T/2π)^λ`). 

### `tendsto_rpow_half_lam_sub_one`

 `T^{λ/2 − 1} → 0` (λ < 2). 

### `tendsto_inv_l_sq`

 `1/l² → 0`. 

### `tendsto_inv_T`

 `1/T → 0` along atTop (named for uniformity). 

 ## Data and hypotheses of the abstract assembly 

### `DataXi`

 the abstract real functions of T entering the ξ′ two-trace computation (mirror of
`PrimeSide.Data` + ThmD's `JT`; the pole weight `cΠ` is absorbed into the Π-cross data). 

### `DataXi.aT`

 `a := L⁻¹ ∫ φ²` 

### `DataXi.bT`

 `b := L⁻¹ ∫ φ⁴` 

### `DataXi.JT`

 `J_T := (2/L³)·l·∫_0^L D(y/l) g(y) dy` 

### `DataXi.trG`

 `tr M̃ᵀ` 

### `DataXi.trG2`

 `tr (M̃ᵀ)²` 

### `DataXi.Ncnt`

 the count `N` (any, with `N = Tℓ₁/2π + O(l)`) 

### `DataXi.Mtot`

 `𝓜 = 𝓜[ν, ν]` 

### `DataXi.Mmumu`

 `𝓜[μ, μ]` 

### `DataXi.MPP`

 `𝓜[P_c, P_c]` 

### `DataXi.MmuP`

 `𝓜[μ, P_c]` 

### `DataXi.MmuPi`

 `cΠ·𝓜[μ, Π_X]` 

### `DataXi.MPPi`

 `cΠ·𝓜[P_c, Π_X]` 

### `DataXi.MPiPi`

 `cΠ²·𝓜[Π_X, Π_X]` 

### `DataXi.intMu2`

 `∫_T^{2T} μ²` 

### `DataXi.sumB2g`

 the diagonal `Σ_{N≤X} |c_N|²/N · g(log N)` 

### `Rxi`

 the lem_ends-scale remainder `R_T := L·l³·log l·(1 + X)` that absorbs every first-form error. 

### `Mstar`

 the comparison scale of the second trace: `M⋆ := T·L·l²` (`≤ 4π · mainTr2Xi`). 

### `FactsXi`

 **Hypotheses of the ξ′ two-trace assembly** = the §5 sub-results for the density
`ν = μ + cΠ·Π_X + P_c` with the crude coefficient majorants, + H-Γ's [eq:muints], + H-RvM-type count,
+ the window ranges.  Mirror of `ThmD.FactsD` (see the file header for the three changes). 

### `FactsXi.ab_range`

 window ranges [eq:abJ]: `1/2 ≤ b ≤ a ≤ 1`, `0 ≤ J_T` eventually. 

### `FactsXi.rvm`

 H-RvM-type: `N = T ℓ₁/2π + O(l)`. 

### `FactsXi.muints2`

 [eq:muints]: `∫_T^{2T} μ² = (Tℓ₁²/4π²)(1 + O(l⁻²))`. 

### `FactsXi.prop_trace`

 [prop:trace] for ν: `tr G̃ = a L N + O(L √X · l)`. 

### `FactsXi.lem_ends`

 [lem:ends] for ν (via lem_ends_nu with `B ≍ l(1+√X)`): `tr G̃² = 𝓜 + O(L l³ log l (1+X))`. 

### `FactsXi.Msplit`

 [eq:Msplit]: the bilinear expansion of `𝓜[ν,ν]`, `ν = μ + cΠ·Π_X + P_c`. 

### `FactsXi.prop_mumu`

 [prop:mumu] (coefficient-free, verbatim): `𝓜[μ,μ] = 2π b L ∫_T^{2T} μ² + O(l² log L)`. 

### `FactsXi.prop_PP`

 [prop:PP] for P_c: `𝓜[P_c,P_c] = (T/π) Σ |c_N|²/N g(log N) + O(L l² X)`. 

### `FactsXi.sumJ`

 partial summation from the ε-form diagonal law: `Σ |c_N|²/N g(log N) = (L³/2) J_T + o(l² L)`. 

### `FactsXi.cross_muP`

 [prop:cross] for ν: `𝓜[μ,P_c] ≪ L l² √X`. 

### `FactsXi.cross_muPi`

 `cΠ·𝓜[μ,Π_X] ≪ l L √X` 

### `FactsXi.cross_PPi`

 `cΠ·𝓜[P_c,Π_X] ≪ L X l` 

### `FactsXi.cross_PiPi`

 `cΠ²·𝓜[Π_X,Π_X] ≪ L X / T` 

 ## Two exact identities 

### `ratio_identity`

 the exact identity behind [eq:ratio-general]:
`(aLN)²/M₂ = cRatio(L/ℓ; a,b,J)·N · (N / (Tℓ/2π))`, valid when `T, L, ℓ, b + λ₁²J` are nonzero. 

### `frhat_identity`

 the exact identity behind the hat-units second moment:
`M₂/(aL)² = cRatio(L/ℓ; a,b,J)⁻¹ · (Tℓ/2π)`. 

 ## The assembly 

### `isEquivalent_Ncnt`

 `N ~ T ℓ₁ / 2π`. 

### `tr1'`

 **[eq:tr1]'**: `tr G̃ ~ a L N`. 

### `tr2_first`

 the first form of [eq:tr2]: all §5 remainders collected into `O(R_T)`. 

### `Mstar_le`

 `M⋆ ≤ 4π · (TL/2π)(bℓ₁² + L²J)` and positivity of the main term, eventually. 

### `tr2`

 **[eq:tr2]**: `tr G̃² ~ (TL/2π)(b ℓ₁² + L² J_T)`. 

### `ratio`

 **[eq:ratio-general]**: `(tr G̃)²/tr G̃² ~ cRatio(λ₁; a, b, J_T) · N`. 

### `frhat`

 **hat-units second moment**: `tr G̃²/(aL)² ~ cRatio(λ₁; a, b, J_T)⁻¹ · N`. 

### `tracesBoundsXi_of_factsXi`

 **The ξ′ two-trace package, assembled** (statement declared in Interface.lean). 

 ## From the trace package to the δ-form hat-unit moments (the shape of `CoeffMoments`)

With `tr M̂ᵀ = tr G̃/(aL)` and `‖M̂ᵀ‖²_F = tr G̃²/(aL)²`, and the window limit `cRatio(λ₁; a_T, b_T, J_T) → c∞ > 0`
(XiPrime/Window.lean), the package gives: for every δ > 0, eventually
`(1−δ)N ≤ tr G̃/(aL) ≤ (1+δ)N` and `tr G̃²/(aL)² ≤ (c∞⁻¹ + δ) N`. 

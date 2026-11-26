---
{
  "module": "Zeta23/PrimeSideB.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization of the paper
"More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
-/
```


# Prime side, part B: [prop:PP] and the assembly of Theorem [thm:traces]

Paper §5 ("The prime side: magnitude"), subsections "Evaluation of 𝓜" and "Summary".

Contents
* §0 glue between the explicit-constant interface shape `EvBound` and Mathlib's `IsBigO`.
* §1 `Zeta23.PaperParams`: elementary facts about the scalar parameters `l, ℓ₁, L, X, λ₁, 𝓔_T`
  of `Defs.lean` (growth, positivity, `𝓔_T → 0`).  Pure real analysis, no hypotheses.
* §2 `Zeta23.PrimeSide.Facts` / `Zeta23.PrimeSide.tracesBounds_of_facts`: the proof of [thm:traces]
  ([eq:tr1], [eq:tr2], [eq:ratio], second forms) from the five sub-results of §5 + [eq:muints] (H-Γ)
  + [eq:RvM] (H-RvM) + [eq:abdef] (Taper), all taken as hypotheses on abstract real functions of `T`.
  This is where the paper's constants `ℓ₁² + L²/3` and `F(λ₁)` are checked.
* §3 [prop:PP]: `𝓜[P_X,P_X] = (T/π) Σ_{n≤X} Λ(n)²/n · g(log n) + O(L² X)` and the sandwich
  `(L−2w)³/6 + O(L²) ≤ Σ a_n² g(y_n) ≤ L³/6 + O(L²)` — over the concrete definitions of `Defs.lean`
  and `Mform`.


 ## §0.  Explicit-constant ↔ `IsBigO` glue 

### `of_isBigO`

 From `IsBigO` back to the explicit form, when the majorant is eventually nonnegative. 

### `mono_right'`

 Weaken the majorant up to a constant: if `g ≤ c·g'` eventually then `EvBound f g → EvBound f g'`. 

### `of_eventually_le`

 An eventual pointwise bound with an explicit constant gives an `EvBound`. 

### `of_abs_le`

 Change `f` up to eventual pointwise domination. 

### `majorant_nonneg`

 The majorant of an `EvBound` is eventually nonnegative. 

 ## §1.  The scalar parameters of `Defs.lean` 

### `two_log_two_sub_one_pos`

 `2 log 2 − 1 > 0`, so `ℓ₁ > l`. 

### `X_eq_rpow`

 `X = (T/2π)^λ` for `T > 0`. 

### `L_le_l`

 `L ≤ l` when `λ ≤ 1` and `l ≥ 0`. 

### `sqrt_X_eq`

 `√X = (T/2π)^{λ/2}`. 

### `sqrt_X_le_rpow`

 `√X ≤ T^{λ/2}` for `T > 0` (as `T/2π ≤ T`). 

### `eventually_X_le_T`

 `X ≤ T` eventually (`λ ≤ 1`). 

### `calE_summands_nonneg`

 each of the three summands of `𝓔_T` is eventually nonnegative 

### `calE_ge_w_div_L`

 `𝓔_T ≥ w / L` for `T` large. 

### `calE_ge_rpow`

 `𝓔_T ≥ T^{λ/2-1}` for `T` large. 

### `calE_ge_mid`

 `𝓔_T ≥ (l²+X) log l /(T l)` for `T` large. 

### `calE_tendsto_zero`

 `𝓔_T → 0` as `T → ∞`, for every fixed `0 < λ ≤ 1` and `w` (the paper [thm:traces]:
  "`𝓔_T ≪_λ w/L + T^{λ−1} log l` (λ<1), `𝓔_T ≪ w/L + log l / l` (λ=1)"; and `L = λ l → ∞`). 

 ## §2.  Assembly of Theorem [thm:traces] from the §5 sub-results

All quantities are real functions of `T` at fixed `P = (ϱ, λ, w)`.  The hypotheses below are exactly
the conclusions of [prop:trace], [lem:ends], [eq:Msplit], [prop:mumu], [prop:PP], [prop:cross]
(the paper §5), [eq:muints] (from H-Γ), [eq:RvM] (H-RvM) and [eq:abdef] (Taper), each in the
explicit-constant form `EvBound`. 

### `Data`

 The real-valued functions of `T` entering [thm:traces].  Docstrings give the paper object. 

### `Data.aT`

 `a := L⁻¹ ∫ φ²` [eq:abdef] 

### `Data.bT`

 `b := L⁻¹ ∫ φ⁴` [eq:abdef] 

### `Data.trG`

 `tr G̃` (prime-side expression, [eq:Gdef] second form, divided by `L`) 

### `Data.trG2`

 `tr G̃² = Σ_{k,l<d} G̃_{kl}²` 

### `Data.Ncnt`

 `N(T,2T)` 

### `Data.Mtot`

 `𝓜 := ∬_{I×I} Φ(τ−τ')² ν_X(τ) ν_X(τ') dτ dτ'` [lem:ends] 

### `Data.Mmumu`

 `𝓜[μ,μ]` 

### `Data.MPP`

 `𝓜[P_X,P_X]` 

### `Data.MmuP`

 `𝓜[μ,P_X]` 

### `Data.MmuPi`

 `𝓜[μ,Π_X]` 

### `Data.MPPi`

 `𝓜[P_X,Π_X]` 

### `Data.MPiPi`

 `𝓜[Π_X,Π_X]` 

### `Data.intMu2`

 `∫_T^{2T} μ(τ)² dτ` 

### `Data.sumL2g`

 `Σ_{n ≤ X} Λ(n)²/n · g(log n) = Σ_n a_n² g(y_n)` 

### `Facts`

 Hypotheses of the [thm:traces] assembly = conclusions of the §5 sub-results and of the
classical inputs, on the abstract data `D`.  Paper labels in each field's docstring. 

### `Facts.abdef`

 [eq:abdef]: `1 − 2w/L ≤ b ≤ a ≤ 1` (for `T` large, so that `w ≤ L/8`). 

### `Facts.rvm`

 [eq:RvM] (H-RvM): `N(T,2T) = T ℓ₁/2π + O(l)`. 

### `Facts.muints2`

 [eq:muints], second formula (from H-Γ): `∫_T^{2T} μ² = (T ℓ₁²/4π²)(1 + O(l⁻²))`. 

### `Facts.prop_trace`

 [prop:trace]: `tr G̃ = a L N(T,2T) + O(L √X)`. 

### `Facts.lem_ends`

 [lem:ends]: `tr G̃² = 𝓜 + O(L l log l (l² + X))`. 

### `Facts.Msplit`

 [eq:Msplit]: bilinear expansion of `𝓜 = 𝓜[ν_X, ν_X]`, `ν_X = μ + Π_X + P_X`. 

### `Facts.prop_mumu`

 [prop:mumu], first form: `𝓜[μ,μ] = 2π b L ∫_T^{2T} μ² + O(l² log L)`. 

### `Facts.prop_PP`

 [prop:PP] (this file, §3), first form:
    `𝓜[P_X,P_X] = (T/π) Σ_{n≤X} Λ(n)²/n g(log n) + O(L² X)`. 

### `Facts.sum_lower`

 [prop:PP] (this file, §3), sandwich lower half: `Σ a_n² g(y_n) ≥ (L−2w)³/6 − O(L²)`. 

### `Facts.sum_upper`

 sandwich upper half: `Σ a_n² g(y_n) ≤ L³/6 + O(L²)`. 

### `Facts.cross_muP`

 [prop:cross]: `𝓜[μ,P_X] ≪ l √X`. 

### `Facts.cross_muPi`

 [prop:cross]: `𝓜[μ,Π_X] ≪ l L √X`. 

### `Facts.cross_PPi`

 [prop:cross]: `𝓜[P_X,Π_X] ≪ L X`. 

### `Facts.cross_PiPi`

 [prop:cross]: `𝓜[Π_X,Π_X] ≪ L X / T`. 

 ### The assembly 

### `tr1`

 [eq:tr1], first equality — this is [prop:trace] verbatim. 

### `Ncnt_lower`

 From [eq:RvM]: eventually `T l /(4π) ≤ N(T,2T)` (and hence `N > 0`). 

### `T_le_Ncnt`

 eventually `T ≤ 4π N(T,2T)`. 

### `tr1'`

 [eq:tr1], second equality: `tr G̃ = L N(T,2T)(1 + O(𝓔_T))`.
  Paper: from `1 − 2w/L ≤ a ≤ 1`, `L N ≫ L T l` and `√X ≤ T^{λ/2}`. 

### `regime`

 The common regime `T ≥ 1, l ≥ 1, log l ≥ 1, L ≥ 1, X ≥ 1, L ≤ l, X ≤ T` (eventually). 

### `tr2_first`

 [eq:tr2], first form:
  `tr G̃² = 2π b L ∫_T^{2T} μ² + (T/π) Σ Λ(n)²/n g(log n) + O(L l log l (l²+X))`. 

### `tr2_pointwise`

 The pointwise inequality behind [eq:tr2] (second form), with every quantity a real variable:
all analytic content is in the hypotheses, and the constants `ℓ₁² + L²/3` are checked here. 

### `tr2`

 [eq:tr2], second form: `tr G̃² = (T L/2π)(ℓ₁² + L²/3)(1 + O(𝓔_T))`. 

### `ratio_pointwise`

 The pointwise inequality behind [eq:ratio], every quantity a real variable.  Here
`Φ₀ := F(L/ℓ)·N` and the identity `F(λ₁) N · (TL/2π)(ℓ² + L²/3) = L² N · Tℓ/2π` is where the
paper's `F(λ₁)`, `λ₁ = L/ℓ₁`, is checked. 

### `ratio`

 [eq:ratio]: `(tr G̃)²/tr G̃² = F(λ₁) N(T,2T)(1 + O(𝓔_T))`, `λ₁ = L/ℓ₁`. 

### `tracesBounds_of_facts`

 **Theorem [thm:traces]** (§5 of the paper, "Summary"), assembled: the content
`TracesBounds` holds for the data `D` under `Facts D`. 

 ## §3.  [prop:PP]

Statement over `Mform` and `Defs.lean`'s `PX, PhiR, g`,
via the 𝒟 / 𝒪₁ / 𝒪₂ decomposition [eq:MPP]. 

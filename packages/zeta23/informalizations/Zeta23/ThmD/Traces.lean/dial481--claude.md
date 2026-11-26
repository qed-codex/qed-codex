---
{
  "module": "Zeta23/ThmD/Traces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Traces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Traces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/Traces.lean — window-general traces assembly.
[eq:ratio-general]: the window-general [thm:traces] assembly.  Mirrors Zeta23/PrimeSideB.lean's
Data/Facts → TracesBounds pipeline with TWO changes (paper §7.1):
 * the [eq:gbounds] sandwich fields (sum_lower/sum_upper, forcing Σa_n²g ≈ L³/6 i.e. J = 1/3)
   are replaced by the moment field sumJ : Σ_{n≤X} a_n² g(y_n) = (L³/2)·J_T + O(L²)
   (discharged for the concrete window by ThmD/PP.lean sumA2g_close + Window.lean jD_close);
 * b is kept symbolic (no b_lower ≈ 1); only 1/2 ≤ b ≤ a ≤ 1 is carried (true for the
   Montgomery–Taylor window: b* = 1/2 + sin(2ϑ)/(4ϑ) > 1/2, minus O(w/L)).
Conclusion: TracesBoundsD (Zeta23/ThmD/AssemblyD.lean) with ratio constant
cRatio λ₁ a b J = λ₁a²/(b + λ₁²J).
-/
```

### `DataD`

 the abstract data of the D-assembly: PrimeSideB's Data plus the window moment J_T
([eq:abJ]: J := (2/L³)∫_0^L g(y)·y dy). 

### `DataD.JT`

 J := (2/L³) ∫_0^L g(y) y dy [eq:abJ]. 

### `FactsD`

 Hypotheses of the window-general [thm:traces] assembly (paper §7.1 "Propositions 5.1–5.5 hold
verbatim" + the partial-summation step).  All fields except ab_range and sumJ are verbatim copies
of Zeta23.PrimeSide.Facts (window-generic); see that structure for the paper labels. 

### `FactsD.ab_range`

 window-general [eq:abJ] ranges: 1/2 ≤ b ≤ a ≤ 1 and 0 ≤ J ≤ 1 eventually. 

### `FactsD.sumJ`

 the §7.1 partial-summation step in place of the sandwich:
  Σ_{n≤X} a_n² g(y_n) = (L³/2)·J_T + O(L²). 

### `tr2D_pointwise`

 The pointwise inequality behind the D-version of [eq:tr2] ([eq:ratio-general] main term):
with the window moments b, J symbolic and the partial-summation input |S − L³J/2| ≤ Cs·L²
in place of the flat-top sandwich, |G2 − (TL/2π)(bℓ² + L²J)| ≤ C·E·(TL/2π)(bℓ² + L²J).
Simpler than PrimeSide.tr2_pointwise: no (b−1)-collapse is needed since b stays in the main term. 

### `eventually_const_mul_le_half`

 from `f → 0`: eventually `C * f T ≤ 1/2` (used for the `Cᵢ·𝓔_T ≤ 1/2` side conditions of
`ratioD_pointwise`, here and in ThmDE.Traces). 

### `ratioD_pointwise`

 The pointwise inequality behind [eq:ratio-general], every quantity a real variable; the
identity cRatio(L/ℓ; a, b, J)·N · (TL/2π)(bℓ² + L²J) = (aL)²N · Tℓ/2π is where the
window-general constant is checked (mirrors PrimeSide.ratio_pointwise; a stays on tr G̃). 

### `tr1'D`

 the D-form of [eq:tr1]': tr G̃ = a L N (1 + O(𝓔)) — a STAYS (no collapse to 1). 

### `mainTr2D`

 the D main term: (TL/2π)(b ℓ₁² + L² J) [eq:ratio-general]. 

### `tr2_firstD`

 the D-form of [eq:tr2], first form (verbatim mirror of PrimeSide.tr2_first over FactsD). 

### `tr2D`

 the D-form of [eq:tr2], second form: tr G̃² = (TL/2π)(bℓ₁² + L²J)(1 + O(𝓔_T)). 

### `ratioD`

 the D-form of [eq:ratio]: (tr G̃)²/tr G̃² = cRatio(λ₁; a, b, J)·N·(1 + O(𝓔_T)). 

### `frhatD_pointwise`

 pointwise form of the hat-units Frobenius bound: the positive part of
G2/(aL)² − (1/cRatio)N is ≤ (4πA + 2C₂)·E·((1/cRatio)N). 

### `frhatD`

 the frhat field: the D-form hat-units second-moment upper bound. 

### `tracesBoundsD_of_factsD`

 **[eq:ratio-general] assembly**: the D-interface traces bounds with ratio constant
cRatio λ₁ a b J. The body mirrors Zeta23.PrimeSide.tracesBounds_of_facts with b, J
symbolic. 

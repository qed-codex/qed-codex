---
{
  "module": "Zeta23/ThmDE/Traces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Traces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Traces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmDE/Traces.lean — [eq:ratio-general] for L(s,χ):
the window-general [thm:traces] assembly of Zeta23/ThmD/Traces.lean (moments b, J symbolic; the
[eq:gbounds] sandwich replaced by the §7.1 partial-summation field sumJ) with the Dirichlet-
character changes of Zeta23/ThmE/TracesChi.lean ([thm:E] proof (iii)): ℓ₁ ↦ ℓ_{1,χ}, three-term
[eq:Msplit] (no pole terms), Σ_{(n,q)=1}.  The pointwise real inequalities tr2D_pointwise /
ratioD_pointwise / frhatD_pointwise (Zeta23/ThmD/Traces.lean) are reused VERBATIM with ℓ := ℓ_{1,χ}
(they take the density-log as a free real ≥ l).  Output: Zeta23.ThmDE.TracesBoundsDChi.
-/
```

### `DataDChi`

 the data of the χ-D assembly: TracesChi's DataChi plus the window moment J_T [eq:abJ]. 

### `DataDChi.JT`

 J := (2/L³) ∫_0^L g(y) y dy [eq:abJ]. 

### `FactsDChi`

 Hypotheses of the window-general χ-[thm:traces] assembly: ThmE.FactsChi with the sandwich
fields (sum_lower/sum_upper) replaced by sumJ and abdef by ab_range (as in ThmD.FactsD). 

### `FactsDChi.ab_range`

 window-general [eq:abJ] ranges: 1/2 ≤ b ≤ a ≤ 1 and 0 ≤ J ≤ 1 eventually. 

### `FactsDChi.sumJ`

 the §7.1 partial-summation step for the coprime sum:
  Σ_{n≤X,(n,q)=1} a_n² g(y_n) = (L³/2)·J_T + O_q(L²). 

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

### `frhatD`

 the frhat field: the D-form hat-units second-moment upper bound. 

### `tracesBoundsDChi_of_factsDChi`

 **[eq:ratio-general] for L(s,χ), assembled.** 

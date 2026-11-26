---
{
  "module": "Zeta23/XiPrime/Hardy/EFContour/Poles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour/Poles.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour/Poles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
The pole data of W at 0 and 1 and the regularised Wreg := s(s−1)²·W.

  s·L₂(s) → −½ (s→0),  (s−1)·L₂(s) → ½ (s→1),  (s−1)²ζ′(s) → −1,  s·W(s) → ¼,  (s−1)²·W(s) → −½;
  Wreg := update (update (s ↦ s(s−1)²W(s)) 0 ¼) 1 (−½) is analytic on −2 < Re s < 3 (removable singularities),
  agrees with s(s−1)²W(s) off {0,1}, has W's zeros and orders there, and logDeriv Wreg = logDeriv(s(s−1)²) + W′/W.
-/
```

 ### helpers: nonvanishing of Γℝ near 0 and 1, punctured maps 

### `tendsto_one_sub_nhdsWithin`

 s ↦ 1 − s maps 𝓝[≠] 1 to 𝓝[≠] 0. 

### `continuousAt_logDeriv`

 logDeriv of an analytic nonvanishing function is continuous. 

 ### §4. Pole limits 

### `zetaReg`

 the regular part of ζ at 1 in Mathlib's normalisation: F := ζ − (Γℝ)⁻¹/(s−1) is differentiable AT 1
(HurwitzZeta.differentiableAt_hurwitzZetaEven_sub_one_div) and near 1. 

### `riemannZeta_eq_zetaReg_add`

 ζ = zetaReg + G/(·−1) as FUNCTIONS (G = (Γℝ)⁻¹; both sides junk-equal at 1 and at the poles of Γℝ). 

 ### §5. The regularised Wreg 

### `polarPoly`

 p(s) := s(s−1)², the polar polynomial of W on the strip. 

### `Wreg`

 Wreg := s(s−1)²·W(s) with the removable singularities at 0, 1 filled in (values ¼, −½). 

### `Wreg_eventuallyEq`

 off {0,1}, Wreg agrees with p·W on a neighbourhood. 

### `Wreg_analyticAt`

 Wreg is analytic on the strip −2 < Re s < 3 (including at 0 and 1). 

### `Wreg_eq_zero_iff`

 off {0,1} (inside the strip) Wreg vanishes exactly where W does … 

### `analyticOrderAt_Wreg`

 … with the same analytic order. 

### `logDeriv_Wreg`

 logDeriv Wreg = logDeriv p + W′/W off {0,1} where W ≠ 0. 

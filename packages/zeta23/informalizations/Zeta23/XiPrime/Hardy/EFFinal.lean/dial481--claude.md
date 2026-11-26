---
{
  "module": "Zeta23/XiPrime/Hardy/EFFinal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFFinal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFFinal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFFinal.lean — the W explicit formula WEF, instantiated.
  theorem wEF (hZ : WZerosInStrip t₀) (hs : WSeam t₀) (hR : RiemannVonMangoldt (wZeros hZ hs))
      (Pf : ℝ → Params) (hPf : FamilyHyps Pf) : WEF (wZeros hZ hs) Pf
from EFMain.wEF_of with LineFactsW ← Hardy/EFExpansion (e2LineFacts', freezeFactsW', norm_FZ_line),
ContourFactsW ← Hardy/EFContour (w_full_line_identity + lminus_line_identity),
CoeffFactsC ← Coeff/LSeries.LSeries_xiCoeffJ_of_gt_one at σ₀ = 9/8.
-/
```

### `lineFactsW`

 `LineFactsW` derived from the EF expansion. 

### `contourFactsW`

 `ContourFactsW` assembled from Hardy/EFContour.lean (`w_full_line_identity`, `lminus_line_identity`). 

### `coeffFactsC`

 `CoeffFactsC` from `LSeries_xiCoeffJ_of_gt_one` at σ₀ = 9/8. 

### `wEF`

 **WEF** [XF′ Thm 9.2]: the explicit formula for W = ζ′ + L₂ζ (i.e. for Z′), entrywise, frozen coefficients at
the REAL parameter L_{2⋆}(τ⋆), pole weight 2, error C·T^{−δ}·(1/max(1,(τ_k−τ_l)²) + 1/T). 

---
{
  "module": "Zeta23/WeilEF/Contour.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Contour.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Contour.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/Contour.lean — The main contour: rectangle identity for H·Λ'/Λ,
horizontal vanishing along good heights, and the R → ∞ full-line identity.
Consumes: Zeta23.Analytic.rectangleIntegral'_mul_logDeriv_of_poles,
Zeta23.WeilEF.GoodHeights, differentiable_paperFT,
XiLogDeriv zeros/poles data, Mathlib completedRiemannZeta_residue_one /
completedHurwitzZetaEven_residue_zero.
-/
```

### `rectangle_identity`

 **Rectangle identity** at a zero-free height R: the weighted argument principle for
H·Λ'/Λ over [1−c, c] × [−R, R]: (1/2πi)∮ = Σ_{|γ_ρ| < R} m_ρ H(ρ) − H(0) − H(1)
(Λ's poles at 0 and 1 are simple with residues 1 and... sign handled by the −m·g(p) pole terms
with m = 1 at both). 

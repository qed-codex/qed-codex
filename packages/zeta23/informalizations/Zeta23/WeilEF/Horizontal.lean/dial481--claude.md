---
{
  "module": "Zeta23/WeilEF/Horizontal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Horizontal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Horizontal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/Horizontal.lean — the horizontal sides of the explicit-formula rectangle vanish along
good heights (a sub-piece of `full_line_identity`).

For `s = x ± iR_j`, `x ∈ [1−c, c] ⊂ [−1/2, 3/2]`:  `‖H(s)‖ ≤ C_H/(1+R_j²)` (`norm_Hfn_le`), and
`‖Λ'/Λ(s)‖ ≤ K·log²(j+10)`: for `re s ≥ 1/2` split `Λ'/Λ = Γℝ'/Γℝ + ζ'/ζ` (`logDeriv_completedZeta`),
bound `ζ'/ζ` by the good-height hypothesis and `Γℝ'/Γℝ = −log π/2 + ψ(s/2)/2` by
`digamma_growth_strip`; for `re s < 1/2` reflect with `Λ'/Λ(s) = −Λ'/Λ(1−s)`
(`logDeriv_completedZeta_one_sub`), `1−s` lying on the opposite good horizontal.  Hence
`‖HIntegral‖ ≤ (2c−1)·C_H·K·log²(j+10)/(1+R_j²) → 0`.
-/
```

### `horizontal_vanish`

 **Horizontal sides vanish** (interface for `full_line_identity`). 

---
{
  "module": "Zeta23/XiPrime/Hardy/Seam.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Seam.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Seam.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/Seam.lean — the SEAM facts for W := ζ′ − ½(χ′/χ)ζ (W zero side).

Discharges `WSeam t₀` (Zeta23/XiPrime/Statement.lean §6) given t₀ > 0 and WZerosInStrip t₀:
  theorem wSeam_of_strip (ht₀ : 0 < t₀) (hZ : WZerosInStrip t₀) : WSeam t₀
(the strip hypothesis is used ONLY for finite_window; one_le_mult / reflect_zero / mult_reflect hold for every
non-real zero: Hardy/Basic.lean's functional equation + Schwarz reflection, and W ≢ 0 on each half-plane by the
explicit points 2 ± it₁ of Hardy/TwoLine.lean).
-/
```

### `instContinuousSMulRealComplex`

 In this import closure typeclass search does not find `ContinuousSMul ℝ ℂ` on its own; the convexity lemmas below need it, so the instance is supplied explicitly. 

 ### W ≢ 0 near any non-real point 

### `one_le_wMult_iff`

 1 ≤ m_ρ ↔ W(ρ) = 0, for non-real ρ. 

 ### finiteness of height windows (uses the strip hypothesis) 

### `finite_upper`

 zeros of W with |Im| ≥ t₀ inside a compact height range are finite (in the half-strip [0,2] × [a,b], a ≥ t₀ > 0,
or its mirror image). 

 ### the seam 

### `wSeam_of_strip`

 **The W seam**, given t₀ > 0 and the strip hypothesis (used only for finite_window). 

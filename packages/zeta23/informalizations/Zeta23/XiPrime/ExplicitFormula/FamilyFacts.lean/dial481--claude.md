---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/FamilyFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/FamilyFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/FamilyFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/FamilyFacts.lean — per-height facts of a FamilyHyps height-family, packaged, and the
power/log absorption used in the final (EF4) bound.
-/
```

### `FamilyHyps.perT`

 **Per-height facts of a FamilyHyps family.**  For T ≥ T₁: λ fixed in (0,1); L = λ·l(T) with
1 ≤ L ≤ log T (so 0 < L); X = e^L with X^{3/4} ≤ T^{3λ/4}; the window φ_T is C² as a complex-valued function
and supported in [−L/2, L/2]; and (the C) it is even, |φ| ≤ 1, ‖φ^{(j)}‖₁ ≤ C for j = 1,2,3. 

### `log_le_const_mul_rpow`

 log T ≤ (1/ε)·T^ε for T ≥ 0 (Mathlib's Real.log_le_rpow_div, repackaged). 

### `pow_log_absorb`

 **Power/log absorption.**  With δ := (1 − 3λ/4)/2 > 0 (λ < 1):
  T^{3λ/4}·log²T·A/(T·log T) ≤ C·T^{−δ}   and   T^{3λ/4}·log²T·A/T² ≤ C·T^{−δ}/T   for T ≥ 2. 

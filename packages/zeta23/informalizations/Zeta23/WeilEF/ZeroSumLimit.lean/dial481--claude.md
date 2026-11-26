---
{
  "module": "Zeta23/WeilEF/ZeroSumLimit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/ZeroSumLimit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/ZeroSumLimit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/ZeroSumLimit.lean — consumed by Zeta23/WeilEF/FullLine.lean (full_line_identity).

The zero-side limit: along heights R_j ∈ [j+7, j+8] the finite sums Σ_{|γ_ρ| < R_j} m_ρ H(ρ)
(the zero term of rectangle_identity, Zeta23/WeilEF/Contour.lean) converge to the absolutely
convergent tsum over all nontrivial zeros (EF_zero_sum_summable,
Zeta23/WeilEF/ZeroSummability.lean), since the windows {|Im ρ| < R_j} increase and exhaust the carrier.
-/
```

### `zero_sum_limit`

 **Zero-sum limit.** The truncated zero sums over `|Im ρ| < R_j` converge to the full
tsum over all nontrivial zeros. 

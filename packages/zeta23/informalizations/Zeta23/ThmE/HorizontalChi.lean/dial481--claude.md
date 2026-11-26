---
{
  "module": "Zeta23/ThmE/HorizontalChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/HorizontalChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/HorizontalChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/HorizontalChi.lean — the horizontal sides of the explicit-formula rectangle for L(s,χ)
vanish along good heights.  The analogue for L(s,χ) of Zeta23/WeilEF/Horizontal.lean: ‖H‖ ≤ C_H/(1+R²) (norm_Hfn_le);
for re s ∈ [1/2, 3/2]: Λ'/Λ_sym = L'/L + (arch)' /arch (logDeriv_completedLSym_split, exists_parity,
norm_logDeriv_archChi_le); for re s < 1/2 reflect with logDeriv_completedLSym_one_sub_conj
(s ↦ 1 − conj s keeps the imaginary part); then length × sup and log²(q(j+10))/(1+(j+7)²) → 0.
-/
```

### `horizontal_vanish_chi`

 **Horizontal sides vanish, χ-version** (used in `full_line_identity_chi`). 

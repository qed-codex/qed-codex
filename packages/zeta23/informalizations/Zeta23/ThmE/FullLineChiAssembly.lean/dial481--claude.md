---
{
  "module": "Zeta23/ThmE/FullLineChiAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FullLineChiAssembly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FullLineChiAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/FullLineChiAssembly.lean — the R → ∞ assembly of `full_line_identity_chi`
(two-character statement) from: rectangle_identity_chi (ContourChi; no pole terms),
good_heights_chi (FullLineChi), horizontal_vanish_chi (HorizontalChi),
verticals_eq_chi + zero_sum_limit_chi (FullLineChiFold), and the χ majorant pack
(FullLineChiProof).  Template: Zeta23/WeilEF/FullLineAssembly.lean.
-/
```

 ## Good heights, re-indexed (R_j ∈ [j+7, j+8]) 

 ## Λ(·,χ) ≠ 0 on the horizontal sides (left half by the functional equation + conjugation:
Λ_sym(s,χ) = W(χ)·conj Λ_sym(1 − conj s, χ), and 1 − conj s has re = 1 − re s > 1/2, SAME im) 

 ## The full-line integrand is integrable 

 ## The assembly 

### `full_line_identity_chi'`

 **Full-line identity for L(s,χ)** (two-character form). 

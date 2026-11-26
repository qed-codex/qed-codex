---
{
  "module": "Zeta23/ThmE/FullLineChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FullLineChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FullLineChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/FullLineChi.lean — statements for the χ-EF endgame: good heights for L(s,χ)
and zero-sum summability.
All ζ-side templates are named in each docstring; the f-generic machinery
(vertical_line_shift, norm_Hfn_le, exists_far_point, FoldChi, LGrowth) is proved
elsewhere in the repository.
-/
```

### `isNontrivialZeroL_of_mem_closedBall`

 a zero of L(·,χ) (χ ≠ 1) in the closed ball of radius r < 2 about 2 + t i is a nontrivial zero. 

### `sum_mult_six_windows_L`

 a finite set of nontrivial zeros with ordinates in (a, a+6] has total multiplicity
≤ 6 A₀ log(|a|+9) (six unit windows of the local count). 

### `card_le_sum_mult_L`

 card ≤ total multiplicity (each nontrivial zero has multiplicity ≥ 1). 

### `good_heights_chi`

 Good heights for L(s,χ) (template: Zeta23.WeilEF.good_heights; gap-selection via
exists_far_point + localCountChi; the L'/L bound via L_logDeriv_partial_fraction's count
conjunct, both ±R as in the ζ-case). 

### `EF_zero_sum_summable_chi`

 Zero-sum summability for L(s,χ) (template: Zeta23.WeilEF.EF_zero_sum_summable via the
local count; with good_heights_chi). 

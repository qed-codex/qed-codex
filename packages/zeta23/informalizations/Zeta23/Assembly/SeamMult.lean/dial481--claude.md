---
{
  "module": "Zeta23/Assembly/SeamMult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly/SeamMult.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly/SeamMult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Assembly/SeamMult.lean — seams A for the multiplicity-aware rank–trace variants.  Decorates `hatAz_mult2/3` (Zeta23/ZeroSide/Mult.lean) with the
seamA pattern: Â → Ĝ = Â + Ê (tail perturbation, c-generic) and I′ → (T,2T] windows.  Conclusions:
  seamA_mult2 : 4trĜ − ‖Ĝ‖² − 2N − 3·NII − B(4 + 2√‖Ĝ‖² + B) ≤ N₀ˢ(T,2T)      [c = 2]
  seamA_mult3 : 6trĜ − ‖Ĝ‖² − 3N − 5·NII − B(6 + 2√‖Ĝ‖² + B) ≤ 2·N_d(T,2T)   [c = 3]
feeding Assembly/Certificate's count_certificate (c=2) and count_certificate_c3.
-/
```

### `ctr_sub_frobSq_perturb`

 c-generic version of `four_tr_sub_frobSq_perturb`. 

### `seamA_mult2`

 **Seam A, multiplicity-aware, c = 2**: the seamA shape with conclusion N₀ˢ. 

### `seamA_mult3`

 **Seam A, multiplicity-aware, c = 3**: 6trĜ − ‖Ĝ‖² − 3N − 5NII − B(6+2√+B) ≤ 2·N_d. 

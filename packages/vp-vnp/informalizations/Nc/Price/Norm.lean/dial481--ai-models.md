---
{
  "module": "Nc/Price/Norm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Norm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Norm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Norms of loads

For the proof of Theorem thm:laws (`Paper/Laws.lean`): the norms ‖n‖² = Σ n_e²/α e of loads, and, if
Σ_e α e·w(e)² ≤ Σ_ν β ν·w(ν)², a new load of norm ≤ (1+η)·S·R that costs at least as much as S times an old load of
norm ≤ R.


### `nrm`

 The norm of a load: √(Σ n_e²/α e). 

### `sum_mul_le_nrm`

 Cauchy–Schwarz. 

### `Loads`

 Natural loads of bounded norm: a finite set. 

### `exists_load`

 One price: if Σα·w² ≤ Σβ·w′² and ‖n‖ ≤ R, then for S large (S·η·R ≥ ‖1‖) there is a natural
load x with ‖x‖ ≤ (1+η)·S·R and Σ S·n·w ≤ Σ x·w′. 

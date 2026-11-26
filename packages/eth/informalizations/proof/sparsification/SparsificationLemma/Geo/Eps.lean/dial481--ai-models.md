---
{
  "module": "proof/sparsification/SparsificationLemma/Geo/Eps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/Eps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/Eps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The choice τ = ⌈(8k/ε)³⌉ in the sparsification, for a rational ε ∈ (0,1]

This file proves `StTauE`, with two lemmas on real numbers.
`StTauE`: put X = 8k/ε ≥ 8 and τ = ⌈X³⌉. Then X³ ≤ τ ≤ X³ + 1 ≤ (9X/8)³ = (9k/ε)³. So log₂ τ ≤
3·log₂(9X/8) ≤ 27X/8, because log₂ y ≤ y, and
log₂(e·τ·τ^(2k)) ≤ 2 + (2k+1)·27X/8 ≤ 11kX. Hence (k/τ)·log₂(e·τ·τ^(2k)) ≤ 11k²X/X³ = 11ε²/64 ≤ ε. 

### `log_le_mul_log_two`

 ln y ≤ y·ln 2 for y > 0, that is log₂ y ≤ y. 

### `works_of_cube`

 The inequality of `StTauE` between real numbers: (k/T)·log₂(e·T·T^(2k)) ≤ ε, if X = 8k/ε, k ≥ 1,
ε ∈ (0,1] and X³ ≤ T ≤ (9X/8)³. 

### `stTauE`

 τ = ⌈(8k/ε)³⌉ is large enough for k and ε, and at most (9k/ε)³. 

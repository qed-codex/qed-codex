---
{
  "module": "proof/sparsification/SparsificationLemma/Geo/S.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/S.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/S.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification theorem for τ = 2^(4s+17), with 2^(−s) in the role of ε

`stThmS` is `stThmTau` at τ = `tauOf s` and ε = 1/2^s. That this τ is large enough for k and ε, if s
≥ `s0U k`, is `UniformInK.Leaves.tauOf_worksU` (proof/sparsification/UniformInK/Top/Leaves.lean). 

### `stThmS`

 The theorem for τ = 2^(4s+17) and s ≥ `s0U k`. 

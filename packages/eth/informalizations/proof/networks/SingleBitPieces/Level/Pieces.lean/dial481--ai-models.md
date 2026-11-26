---
{
  "module": "proof/networks/SingleBitPieces/Level/Pieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/Level/Pieces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/Level/Pieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A sum over θ ∈ {0,1}^c as a sum over the words of c bits

`Pieces.sum_ofFn`: a sum over θ ∈ {0,1}^c, the index of a factorization in Definition 1, written as
functions `Fin c → Bool`, equals the same sum over the words of c bits (`words c`). 

### `sum_ofFn`

 A sum over θ ∈ {0,1}^c, written as functions, is the sum over the words of c bits. 

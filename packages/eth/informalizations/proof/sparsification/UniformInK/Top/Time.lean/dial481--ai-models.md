---
{
  "module": "proof/sparsification/UniformInK/Top/Time.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Time.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Time.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The length of the input code of a k-CNF, bounded by a power of n+2

For the code x = `SatM.enc k φ` of (k, φ), with φ a k-CNF on n variables and k ≥ 1, this file proves |x| +
1 ≤ (n+2)^(5k). 

### `length_enc_succ_le`

 The length of the code of (k, φ), plus one, is at most (n+2)^(5k), for a k-CNF φ on n variables
and k ≥ 1. 

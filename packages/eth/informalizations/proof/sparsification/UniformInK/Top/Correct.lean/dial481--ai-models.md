---
{
  "module": "proof/sparsification/UniformInK/Top/Correct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Correct.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Correct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Two lemmas on the function for the bound in n

If 2^β ≤ n + 1, then, since β ≥ k, k ≤ ⌊log₂(n+1)⌋, so that the cut-off `kcU` of the width does
nothing (`kcU_eq`).
With a pad of at least 2^n units, exhaustive counting on the decoded formula (`StBruteC`, `StDecU`)
returns the number of satisfying assignments (`brute_eq`). 

### `kcU_eq`

 If 2^β ≤ n + 1, the cut-off of the width does nothing. 

### `brute_eq`

 With a pad of at least 2^n units, exhaustive counting on the decoded formula returns the number
of satisfying assignments. 

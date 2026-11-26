---
{
  "module": "proof/networks/Paper/SecLevel_Recursion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecLevel_Recursion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecLevel_Recursion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 5 of the paper: two facts on e*, the infimum defined after Definition 4, from the last paragraph of the proof of Proposition 3

If e > e*, then (K, e) is achievable for infinitely many K; and if (K, e) is achievable for
infinitely many K, then e* ≤ e. 

 ### e*, as in the last paragraph of the proof of Proposition 3 

### `achievable_of_eStar_lt`

 "Let e > e*; then (K, e) is achievable for infinitely many K." 

### `eStar_le`

 If (K, e) is achievable for infinitely many K, then e* ≤ e. 

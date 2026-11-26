---
{
  "module": "proof/consequences/CountKSatRate/Top.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Top.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Top.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The number kept by the walk of rounds

Lemmas on the rounds `roundS` of a walk over a tree: one round, and further rounds, do not lower the
number that the walk keeps, and after any number of rounds this number
is at most the sum of the values of the leaves, under the hypothesis `StRoundSEnd` on how the walk
ends. 

 ### The number kept by the walk never goes down 

### `le_roundS`

 One round does not lower the number. 

### `iterate_le_iterate`

 Further rounds do not lower the number. 

### `iterate_le_sum`

 The number after any number of rounds is at most the sum of the values of the leaves. 

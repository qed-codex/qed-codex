---
{
  "module": "proof/consequences/Consequences/Sets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Consequences/Sets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Consequences/Sets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Two elementary bounds: c·(n + m + 2)^c and c·x

`size_square` bounds c·(n + m + 2)^c by 2c·(n + 2)^(2c) for m ≤ n², and `steps_double` bounds c·x by
2c·x for x ≥ 0, with c and 2c read as reals. 

### `size_square`

 c·(n + m + 2)^c ≤ 2c·(n + 2)^(2c) for m ≤ n². 

### `steps_double`

 c·x ≤ 2c·x for x ≥ 0, with the numbers c and 2c read as reals. 

---
{
  "module": "Zeta23/RvM/NcountWindow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/NcountWindow.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/NcountWindow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/NcountWindow.lean — window arithmetic for `Ncount`.

These lemmas (window splitting, additivity and monotonicity of the zero count) live here, in the
root `Zeta23` namespace, and are used by the Riemann–von Mangoldt files.
-/
```

 ## Window arithmetic for Ncount 

### `zerosIn_union`

 windows split: zerosIn a c = zerosIn a b ∪ zerosIn b c for a ≤ b ≤ c. 

### `Ncount_add`

 window additivity: N(a,c] = N(a,b] + N(b,c]. 

### `Ncount_mono`

 window monotonicity: (a,b] ⊆ (c,d] ⇒ N(a,b] ≤ N(c,d]. 

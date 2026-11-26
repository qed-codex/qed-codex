---
{
  "module": "proof/networks/Coding/Padding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Padding.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Padding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Padding changes neither the value nor the total

Let the network N be the network N₀ with padded settings (`Coding.PaddingOf`,
proof/networks/Coding/Defs.lean). The value of a network (Section 3) is a sum over all choices of
one setting for each node. A choice for N in which some node has a setting that is not the padding
of any setting of N₀ contributes 0, because W is 0 there.
The other choices are, one to one, the choices for N₀ with each setting padded, and they contribute
the same term. The total is a sum of the numbers c_{a,b}, which are the same. 

### `stPaddingValue`

 **Padding changes neither the value nor the total.** Used for «A setting z_a of node a is a bit
string with one bit z_a[o] for each occurrence o in cluster a» (Section 6), where Lean's settings
have one bit for each place of a literal. 

---
{
  "module": "proof/consequences/Consequences/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Consequences/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Consequences/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A definition for Section 7: what it means that a procedure counts in graphs

`CountsGraph`, used by `Consequences.tm_of_counts` (proof/consequences/Consequences/Main.lean) and
by proof/consequences/FromPrinted/GraphDefs.lean, which puts Corollary 7 on the machine of the
printed proof of Corollary 6. This file has no theorem. 

### `CountsGraph`

 A machine cut into steps returns the number f(G, s), s ≤ n, on the code of (G, s), within
c·2^{δn} steps, on states of size polynomial in n. 

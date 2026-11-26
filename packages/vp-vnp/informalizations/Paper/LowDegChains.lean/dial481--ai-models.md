---
{
  "module": "Paper/LowDegChains.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/LowDegChains.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/LowDegChains.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, proof of Lemma lem:lowdeg: chains


### `lem_lowdeg_chains`

 **Paper: proof of Lemma lem:lowdeg, the chain constants and the degree identity.** "(g,1) = ∑_l λ_{g,l} x_l,
(g,i) = ∑ κ_{g,g′,g″} ∑_{0<j<i} (g′,j)(g″,i−j) for i ≥ 2. These constants do not depend on i." Here (g,m+1) is the
coefficient of degree m+1 of the gate along the line through the point u, which is the part of that degree at u. 

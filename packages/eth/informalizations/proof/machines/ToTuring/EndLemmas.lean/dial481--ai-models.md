---
{
  "module": "proof/machines/ToTuring/EndLemmas.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/EndLemmas.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/EndLemmas.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 From «`InTimeTM δ` for every δ > 0» (3-SAT in time O(2^{δn}) on Turing machines) to ¬ ETH_TM and
back (`not_ETH_TM_iff`):
the set of δ with `InTimeTM δ` is upward closed (`InTimeTM.mono`), so its infimum is 0 exactly if it
contains every δ > 0. 

### `DecidesTM.mono`

 A machine that decides within t decides within any larger bound. 

### `InTimeTM.mono`

 More time is allowed for a larger δ. 

### `not_ETH_TM_iff`

 The negation of ETH_TM is «on Turing machines 3-SAT is in time O(2^{δn}) for every δ > 0». 

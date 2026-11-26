---
{
  "module": "proof/consequences/CountKSat/EndLemmas.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/EndLemmas.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/EndLemmas.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From «#3-SAT is in time O(2^{δn}) for every δ > 0» to the failure of the hypothesis

Plain facts on the definitions of CountKSatStatement.lean: a time bound for a counting machine may
be enlarged (`CountsTM.mono`), and the counting hypothesis `CountETH_TM` fails
if #3-SAT is in time O(2^{δn}) for every δ > 0 (`not_CountETH_TM_of`). The paper states this failure
of #ETH in Corollary 6. 

### `CountsTM.mono`

 A machine that counts within t steps counts within any larger bound. 

### `not_CountETH_TM_of`

 The hypothesis fails if #3-SAT is in time O(2^{δn}) for every δ > 0. 

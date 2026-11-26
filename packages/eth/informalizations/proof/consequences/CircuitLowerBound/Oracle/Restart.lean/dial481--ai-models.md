---
{
  "module": "proof/consequences/CircuitLowerBound/Oracle/Restart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Oracle/Restart.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Oracle/Restart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): a machine that is started again after every answer can be replaced by an oracle machine

`stRestart`: a language that is in E^NP in the second form (an ordinary machine, started again after
every answer, at most 2^{c(n+1)} rounds of at most 2^{c(n+1)} steps) is in E^NP in the first form
(an oracle machine); the oracle
machine of `Machine.lean` takes at most 2^{(2c+7)(n+1)} steps. 

### `initList_otm`

 The first configuration of the oracle machine. 

### `haltList_otm`

 The last configuration of the oracle machine. 

### `time_le`

 The time: (Y + 1)·(4Y + 3n + 12) ≤ 2^{(2c+7)(n+1)} for Y = 2^{c(n+1)}. 

### `stRestart`

 A machine that is started again after every answer can be replaced by an oracle machine. 

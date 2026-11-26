---
{
  "module": "proof/consequences/CircuitLowerBound/Tab/Sound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Sound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Sound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): rows that satisfy the conditions are a run of the machine

`acc_of_spec`: if some truth values satisfy the conditions `Spec`, then the machine accepts 1^P 0 y
for some y within 2^b steps. The first row is the start on such a word (`exists_init`); if row t is
a configuration at the positions below V, then
row t + 1 is the next configuration at the positions below V − d (`Enc.step`); the last row is the
halted configuration with the output 1 (`eq_haltList`). 

### `Enc`

 Row t is the configuration c, as far as the positions below V go. 

### `exists_case`

 At every time before the last some case holds. 

### `Enc.step`

 From a row to the next. 

### `exists_init`

 The first row is the start of the machine on 1^P 0 y, for some y. 

### `eq_haltList`

 The last row is the halted configuration with the output 1. 

### `acc_of_spec`

 If the conditions can be satisfied, the machine accepts. 

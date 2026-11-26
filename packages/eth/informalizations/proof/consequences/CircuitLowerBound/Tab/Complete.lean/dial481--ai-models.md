---
{
  "module": "proof/consequences/CircuitLowerBound/Tab/Complete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Complete.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Complete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): a run of the machine satisfies the conditions

`spec_of_acc`: if the machine accepts 1^P 0 y within 2^b steps, the rows of its run satisfy the
conditions `Spec`. With `acc_of_spec` this gives `stSpec`. 

### `rows`

 The truth values of all statements about the rows c 0, c 1, … 

### `spec_of_acc`

 If the machine accepts, the conditions can be satisfied. 

### `stSpec`

 The conditions hold for some truth values if and only if the machine accepts. 

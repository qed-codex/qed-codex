---
{
  "module": "proof/variables/VariableBound/Paper/MainTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/MainTheorem.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/MainTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The number of satisfying assignments as assignments of the variables that occur: satisfiability and a bound

For a formula over x₀ … x_(N−1) in which n of these variables occur, `numSatOcc` counts the
satisfying assignments as assignments of these n variables.
A formula is satisfiable exactly if this count is not 0 (`satisfiable_iff`), and the count is below
2^(n+1) (`numSatOcc_lt`). 

### `satisfiable_iff`

 A formula is satisfiable if and only if its number of satisfying assignments, as assignments of
the variables that occur, is not 0. 

### `numSatOcc_lt`

 The number of satisfying assignments, as assignments of the n variables that occur, is below
2^(n+1). 

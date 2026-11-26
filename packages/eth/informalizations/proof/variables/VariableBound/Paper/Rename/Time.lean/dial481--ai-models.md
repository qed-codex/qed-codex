---
{
  "module": "proof/variables/VariableBound/Paper/Rename/Time.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Time.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Time.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Time plus a polynomial in the length of the formula: the arithmetic

The padding machine halts within q·(a + 2^E + 1)^q steps on an input of length a, where E is the
exponent computed for the renamed formula, whose code has length b. `steps_split` bounds this by
q·2^q·(a + 1)^q, a polynomial
in a, plus 2q·(b + 2^E + 1)^(2q). Natural numbers only. 

### `steps_split`

 q·(a + 2^E + 1)^q ≤ q·2^q·(a + 1)^q + 2q·(b + 2^E + 1)^(2q), for all natural numbers. 

### `poly_mono`

 C·a^C grows with C, for a ≥ 1. 

### `poly_le`

 q·2^q·(a + 1)^q ≤ C·a^C for C = q·4^q and a ≥ 1. 

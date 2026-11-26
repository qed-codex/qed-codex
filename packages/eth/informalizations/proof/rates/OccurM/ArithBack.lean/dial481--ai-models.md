---
{
  "module": "proof/rates/OccurM/ArithBack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/ArithBack.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/ArithBack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The polynomial in the length of the formula is absorbed when every variable occurs

If all n variables occur then n ≤ k·m, and the code with n in unary has at most 8·(k·m)² bits.
Throughout 0 ≤ α ≤ 1, k ≥ 1 and m ≥ 2, and Y = k·m/(log₂(m+2))^α is the exponent of the bound
`SatM.bound`.

1. `sq_lg_add_two_le`: (log₂(m+2))² ≤ 128·m.
2. `lg_mul_le`: log(k·m) ≤ 130·Y.
3. `back_le`: 2^{C·km/(log m)^α} + C·a^C ≤ C'·2^{C'·Y} with C' = 650·C + 1, for every a ≤ 8·(k·m)².

Only numbers; no machine and no formula occurs in this file. 

### `sq_lg_add_two_le`

 (log₂(m+2))² ≤ 128·m for m ≥ 2. 

### `lg_mul_le`

 log(k·m) ≤ 130·k·m/(log₂(m+2))^α. 

### `back_le`

 The printed bound with the constant C, plus C·a^C for a number a ≤ 8·(k·m)², is at most the
bound `SatM.bound`, with exponent k·m/(log₂(m+2))^α, for the constant 650·C + 1. 

---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Sizes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sizes of the networks of marks for the parity checks

Inequalities between natural numbers, with explicit numerals, for the bounds U and P of the networks
of marks on 7n variables (`UbOL_le`, `g_mul_PbOL_le`, `one_le_PbOL`) and for the numbers that go
into them
(`bitOL_le`, `colMax_le`, `rowMax_le`, `occOL_le`). L = ⌈log₂(2Δ)⌉ throughout. The auxiliary
statements are in the
namespace `ClauseBound.ParityChecks.Sizes`. 

### `two_mul_le`

 2Δ ≤ 2^L. 

### `le_two_pow_clog`

 n ≤ 2^⌈log₂ n⌉. 

### `mul_qv_le`

 g·⌈N/g⌉ ≤ N + g − 1. 

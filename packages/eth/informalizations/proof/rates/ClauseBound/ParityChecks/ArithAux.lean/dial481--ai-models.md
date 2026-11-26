---
{
  "module": "proof/rates/ClauseBound/ParityChecks/ArithAux.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/ArithAux.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/ArithAux.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Bit lengths for Δ = 2^β

Facts on ⌈log₂⌉ and on the bit length, and bounds on the block length `blkOL (2 ^ β)` and on the bit
length of `blkOL (2 ^ β) * (7 * n + 1)`, for Δ = 2^β. 

### `LD_two_pow`

 ⌈log₂(2·2^β)⌉ = β + 1. 

### `size_mul_le`

 The bit length of 2^β·n. 

### `clog_le_size`

 ⌈log₂ n⌉ is at most the bit length of n. 

### `blkOL_two_pow_le`

 The length of a block for Δ = 2^β is at most 2^{2β+5}. 

### `size_blk_le`

 The bit length of the number of clauses of the three layers, for Δ = 2^β. 

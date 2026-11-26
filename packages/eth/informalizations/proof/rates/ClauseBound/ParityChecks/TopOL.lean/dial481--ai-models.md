---
{
  "module": "proof/rates/ClauseBound/ParityChecks/TopOL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/TopOL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/TopOL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Correctness of the function `AO`

`stCorrectO : StCorrectO`. For the constant c, the number n₀ is the larger of 2^20 and the n₀ of
`exists_n0 c`. If the plan is `none`, the exponent is n and the function counts exhaustively
(`StBruteC`). Otherwise the plan says that s ≥ s0K k, that Δ = 2^(betaN k s) ≤ n + 1, that n ≥ n₀,
that Δ ≤ (⌊log₂ n⌋ + 1)^c, that 2·⌈log₂(2Δ)⌉ ≤ n, and that the exponent is `needO`. Then the
parameters
satisfy what the choice of the checks needs (`exists_n0`), the pad suffices for the count of a leaf
(`StBudgetO`, `FitsOL`), so that this count is right (`StCountOL`), and for the walk
(`StWalkCount`). 

### `planAtO_some`

 What a plan says. 

### `sq_le_tauOf`

 The threshold is at least k² for every k ≤ s. 

### `LD_pos`

 ⌈log₂(2Δ)⌉ ≥ 1 for Δ ≥ 1. 

### `two_le_nbOf`

 nb ≥ 2 if 2·⌈log₂(2Δ)⌉ ≤ n. 

### `lt_two_mul_nbOf`

 n < 2·nb·⌈log₂(2Δ)⌉ if nb ≥ 1. 

### `i0_le_capM`

 i₀ is at most the cap, for n ≥ 2^20. 

### `stCorrectO`

 The end of the correctness side. 

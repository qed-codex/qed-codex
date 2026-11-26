---
{
  "module": "proof/rates/PiecesCounted/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Pieces on counted operations: first facts

The number of operations `steps` and the bound `room` on the states grow with c and with λ. From
this: pieces with parameters (ρ, c) are pieces with parameters (ρ', c') for ρ ≤ ρ' < 1 and c ≤ c',
with the same algorithm (`growWithTheParameters`).
Clauses (a), (b) and the sizes of (c) give the pure form `Pieces.Family.Is` (`toPure`): a sum over
the words of n bits is a sum over the functions from {0, …, n − 1} to the bits. 

 ### The bounds grow 

### `steps_le_of_le`

 2^{cλ} grows with c. 

### `steps_le_of_length_le`

 2^{cλ} grows with λ. 

### `pow_two_mul_le`

 (2λ)^c grows with c, for λ ≥ 1. 

### `room_le_of_le`

 The bound on the states grows with c, for λ ≥ 1. 

### `room_le_of_length_le`

 The bound on the states grows with λ. 

 ### The oracle 

### `oracle_eq_some`

 The oracle answers only for λ ≥ 1, and then with the right answer. 

 ### Growing parameters 

### `Data.Is.grow`

 Clauses (a), (b) and the sizes of (c) only weaken when ρ or c grows. 

### `Computes.grow`

 An algorithm within 2^{cλ} operations is one within 2^{c'λ} operations, for c ≤ c'. 

### `growWithTheParameters`

 `GrowWithTheParameters`: pieces with parameters (ρ, c) are pieces with parameters (ρ', c') for ρ
≤ ρ' < 1 and c ≤ c'. 

 ### The pure form 

### `toPure`

 `ToPure`: clauses (a), (b) and the sizes of (c) as pure mathematics. 

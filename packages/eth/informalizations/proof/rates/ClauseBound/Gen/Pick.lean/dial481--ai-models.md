---
{
  "module": "proof/rates/ClauseBound/Gen/Pick.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Pick.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Pick.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The general recursion: picking the level

From a bound b in unary, the largest ℓ with K_ℓ ≤ b and the schedule of level ℓ, in polynomial time.
A loop over the units of b keeps the state
(ℓ, schedule of level ℓ, K_ℓ, 2^{3ℓ+x₀}, the precision D_ℓ = 3·m·2^{ℓ+4} with m = `P.m`), all
numbers in unary, and pushes the next step as long as K_{ℓ+1} = (2^{3ℓ+x₀}·K_ℓ)² ≤ b. The state is
cut off by a pad whose length is a polynomial in b; the mathematics shows that the cut-off is never
active. 

 ### The numbers 

### `pow_le_K`

 2^{3ℓ+x₀} ≤ 8·K_ℓ. 

### `lt_K_succ`

 ℓ < K_{ℓ+1}. 

 ### The loop 

### `St`

 (ℓ, schedule, K_ℓ, 2^{3ℓ+x₀}, D_ℓ). 

### `state`

 The state at level ℓ. 

### `next`

 One round: the next step is pushed if K_{ℓ+1} ≤ b. 

### `stepB`

 An upper bound for the length of the word of one step, together with the two symbols that the
list of steps adds around it (see `len_cons`), when K_{ℓ+1} ≤ k. 

### `lenB`

 An upper bound for the length of the word of the state at a level ℓ ≤ r with K_ℓ ≤ k. 

### `D_le`

 D_ℓ ≤ 48·m·2^{3ℓ+x₀}. 

### `padOf`

 The pad of the loop. 

### `loop`

 The state after all rounds. 

### `pick`

 The level ℓ, together with the schedule of level ℓ and K_0, in unary. 

### `rounds`

 After r rounds the state is that of a level ℓ ≤ r with ℓ = 0 or K_ℓ ≤ b, and ℓ = r unless b <
K_{ℓ+1}. 

### `stPick`

 From a bound in unary: the largest ℓ with K_ℓ ≤ bound, the schedule of level ℓ and K_0, in
polynomial time. 

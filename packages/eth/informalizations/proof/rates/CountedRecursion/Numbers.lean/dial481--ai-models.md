---
{
  "module": "proof/rates/CountedRecursion/Numbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Numbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Numbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers of a level, written in unary by a loop

`numbersM x₀` has ℓ rounds; a round costs two steps (one of the body, which does nothing, and one of
the loop) and replaces (2^{3j+x₀}, K_j) by (2^{3(j+1)+x₀}, K_{j+1}). So it returns (2^{3ℓ+x₀}, K_ℓ)
after 2ℓ steps (`numbersRun`). Its states hold ℓ in unary twice, a counter, and the pair:
at most 6ℓ + 8 + 2·2^{3ℓ+x₀} + 2K_ℓ ≤ 18·g_ℓ. A round is polynomial-time in the pair
(`numbersPoly`). 

### `length_unary'`

 The length of a number in unary. 

### `size_unary'`

 The size of a number in unary. 

### `numbers_fold`

 After k rounds the pair is (2^{3k+x₀}, K_k). 

### `K_pos`

 K_ℓ ≥ 1. 

### `K_le_succ`

 K_ℓ ≤ K_{ℓ+1}. 

### `K_mono`

 K_ℓ grows with ℓ. 

### `numbersRun`

 `NumbersRun`, with C = 18. 

### `numbersStep_polyT`

 One round is polynomial-time in the pair. 

### `numbersPoly`

 `NumbersPoly`. 

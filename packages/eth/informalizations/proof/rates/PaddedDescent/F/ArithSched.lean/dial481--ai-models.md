---
{
  "module": "proof/rates/PaddedDescent/F/ArithSched.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithSched.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithSched.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The schedule (`StSched`, the chain condition, and the second part of `StA`)

`schedF pad t` computes the list of levels (K_j, g_j), j < t, in unary, together with K_t and L_t,
under the cut-off by the pad. Here: if the pad has
length at least `schedLen t`, no cut-off is active and the result is the mathematical schedule
`schedL t` with K_t and L_t (`stSched`); the schedule is
a chain of steps g·g → K that ends at 256 nodes (`chain_schedL`); and for t = `depthOf (sOf n)`,
`sOf n` ≥ 1, the length `schedLen t` is below the pad
(`schedLen_le`). 

### `Lseq_succ`

 L_{j+1} = L_j + L_j. 

### `Lseq_mono`

 L_j grows with j. 

### `schedState`

 The state of `schedF` after j rounds when no cut-off is active. 

### `schedState_succ`

 One round of `schedF` without its cut-off takes the state after j rounds to the state after j +
1 rounds. 

### `len_schedL_le`

 The word of the schedule of depth j has length at most j·(8·K_j + 8) + 2. 

### `len_schedState_le`

 The word of the state after j rounds has length at most `schedLen j`. 

### `schedLen_mono`

 `schedLen` grows with the depth. 

### `chain_schedL`

 The schedule is a chain of steps g·g → K that ends at 256 nodes. 

### `stSched`

 `StSched`: with a pad of length at least `schedLen t`, `schedF pad t` is the schedule of depth t
together with K_t and L_t in unary. 

### `schedLen_le`

 The second part of `StA`: the computation of the schedule fits under the pad. 

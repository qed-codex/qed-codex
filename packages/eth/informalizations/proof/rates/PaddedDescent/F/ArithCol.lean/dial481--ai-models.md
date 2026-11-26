---
{
  "module": "proof/rates/PaddedDescent/F/ArithCol.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithCol.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithCol.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The grid is large enough for the colouring, at every level

The colouring lemma of this development, which splits g nodes into K groups (colours) for the
balancing step (compare Lemma 8, whose condition differs), with relative error 1/D, asks for a
number m with 4·D²·m·K ≤ g and (g+2)·K < 2^m (`ColOK K g`). Here:
for K = K_j, g = g_j = K_j·2^(47+j) and D = `Dcol` = 2^18 the number m = 2^(9+j) will do, at every
level j. 

### `four_mul_Dcol_sq_mul`

 4·D²·2^(9+j)·K_j = g_j. 

### `gseq_add_two_mul_lt`

 (g_j + 2)·K_j < 2^(2^(9+j)). 

### `colOK_seq`

 The hypothesis of the colouring lemma holds for (K_j, g_j). 

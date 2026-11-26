---
{
  "module": "proof/rates/PiecesCounted/Assume.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Assume.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Assume.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # All numbers of bits at most 2λ: the new algorithm answers every question
The data `trimmed D` and the algorithm `assumeAlg Alg` are defined in `Trimmed.lean`, after the
remark following Definition 7 that all numbers of bits may be taken at most 2λ, with c + 2 for c.
Here: question by question, the new algorithm returns the right answer for the new data within
2^{(c+2)λ} operations (`assume_computes`), and the statement `MayAssume` follows. 

### `ite_cast_min`

 The smaller of two natural numbers, computed on integers. 

### `assume_computes`

 The new algorithm computes the new data within 2^{(c+2)λ} operations. 

### `mayAssume`

 `MayAssume`: pieces with parameters (ρ, c) give pieces with parameters (ρ, c + 2) with the same
d, 𝓘 and A_i and with all numbers of bits at most 2λ. 

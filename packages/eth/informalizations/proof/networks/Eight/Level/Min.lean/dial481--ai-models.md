---
{
  "module": "proof/networks/Eight/Level/Min.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Min.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Min.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The display «the smaller total» for the numbers that the algorithm compares

Procedure CLIQUE of Algorithm 1 (`levelAlg`) compares the numbers `totalG eightF g g false 0 λ y`
and `totalG eightF g g true 0 λ y`. They are the totals U_row and U_col of the two networks of ι
(`U_netOfι`), so display (36) of the proof of
Proposition 3 (`Eight.eqMinTotal`, for the networks on words `eqMinTotal_words`) bounds the smaller
one: `stMin`. 

### `stMin`

 Display (36) of the proof of Proposition 3, «min(U_row, U_col) ≤ ½(U_row + U_col) ≤ N/g + |ℛ|(11λ/3 + 8)
≤ N(ρ + 1/g) + 2g⁴», N = g⁴λ, ρ = 11/12, for the numbers that the algorithm compares. From
`eqMinTotal_words`, that is from `Eight.eqMinTotal`.
Same as in the paper; N/g is written g³λ. 

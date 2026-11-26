---
{
  "module": "proof/rates/PiecesCounted/Half.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Half.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Half.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Pieces with ρ = 1/√2 on counted operations

Theorem B: «There are pieces with parameters (1/√2, c), for an absolute constant c.»
`AppRunningTimeStatement.lean` states this with a padding string and with 𝓘 = {−2h, …, 2h} numbered
from 0 to 4h (`AppRunningTime.thmHalfPieces`). `FromPadded` carries it over, with the index set
shifted by −2h.
The shift has to be computed in polynomial time from λ in unary. It is taken as −⌊(|𝓘| − 1)/2⌋,
where |𝓘| = 4h + 1 is computed by one of the programs of the pieces, so that h itself need not be
computed. This form claims no more about the running time than `AppRunningTime.ThmHalfPieces` does:
the work is done in one step once the padding string is written. 

### `halfShift`

 The shift of the index set: −⌊(|𝓘| − 1)/2⌋. 

### `neg_half_polyT`

 −⌊(f − 1)/2⌋ is polynomial-time if f is. 

### `half_add_lt`

 (n − 1)/2 + N < 2^N for n ≤ N, N ≥ 1. 

### `halfPiecesFrom`

 `HalfPiecesFrom`. 

### `halfPieces`

 `HalfPieces`: Theorem B, for the functions of its proof. 

### `halfPiecesExist`

 `HalfPiecesExist`: Theorem B in the paper's words. 

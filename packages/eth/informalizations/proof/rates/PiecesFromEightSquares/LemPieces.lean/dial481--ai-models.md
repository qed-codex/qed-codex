---
{
  "module": "proof/rates/PiecesFromEightSquares/LemPieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesFromEightSquares/LemPieces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesFromEightSquares/LemPieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces of Lemma 2 in Appendix A

`AppRunningTime.lemPiecesPieces`: the sentences after the definition of pieces with parameters (ρ,
c), clause by clause from Lemma 2 as it is proved from the eight-square identity (`Eight.lemPieces`,
`Eight.stFact`, `Eight.stAMul`) and from
«computable in time poly(λ)» (`Eight.stKeeps`, `Eight.stPoly`). `GeneralPieces.eight_isPieces`: the
functions A_0, …, A_t of Lemma 2, with their programs, are pieces with parameters (11/12, c) for
every c ≥ 8. 

### `eight_isPieces`

 The functions A_0, …, A_t of Lemma 2, with their programs, are pieces with parameters (11/12, c)
for every c ≥ 8. 

### `lemPiecesPieces`

 The sentences after the definition of pieces, as stated in
`PiecesFromEightSquaresStatement.lean`. 

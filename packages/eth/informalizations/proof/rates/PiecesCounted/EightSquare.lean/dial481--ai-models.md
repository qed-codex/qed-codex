---
{
  "module": "proof/rates/PiecesCounted/EightSquare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/EightSquare.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/EightSquare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces made from the eight-square identity

After Definition 7 the paper notes that, by Lemma 2, the functions A_0, …, A_t of Definition 5 are
pieces with parameters (11/12, c) for every large enough integer c ≥ 8, with 𝓘 = {0, …, t}, d = 2^t.
`PiecesFromEightSquaresStatement.lean` states this with a padding string, for every c ≥ 8
(`AppRunningTime.lemPiecesPieces`). The programs do not read the padding string (`ofPadded_eight`,
`answerOf_eight`: by unfolding `Eight.eightF` and `AppRunningTime.valEight`), so ONE algorithm,
which writes a single unit and then answers in one step, serves for every c ≥ 8. It takes two steps;
each state of the run holds either the question, with at most one unit of the padding string, or the
answer, and these fit `room c λ` by the size bounds of part (c) of Definition 7. So c₀ = 8. 

### `ofPadded_eight`

 The programs of these functions do not read the padding string: the data are the same for every
c. 

### `answerOf_eight`

 Nor does the function that answers all questions. 

### `shift_zero_lt`

 The condition on the shift, for the shift 0. 

### `eight_is`

 Clauses (a), (b) and the sizes of (c), for every c ≥ 8. 

### `eight_computes`

 The one algorithm, within 2^{cλ} operations for every c ≥ 8. 

### `eightSquarePieces`

 `EightSquarePieces`, with c₀ = 8. 

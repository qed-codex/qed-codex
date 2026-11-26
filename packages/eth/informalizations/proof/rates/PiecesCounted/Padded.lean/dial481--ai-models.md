---
{
  "module": "proof/rates/PiecesCounted/Padded.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Padded.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Padded.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From the padding string to counted operations

`AppRunningTime.IsPieces` (`AppRunningTimeStatement.lean`) has six programs and a padding string of
2^{cλ} units, and numbers the index set 𝓘 from 0. The data are treated in `PaddedData.lean`. Here:
ONE function `answerOf` of (λ in unary, question) and a padding string, made from the six programs
and the shift of the index set; it is polynomial-time (`answerOf_polyT`) and gives the right answer
when the padding string has 2^{cλ} units (`answerOf_eq`).
The algorithm is `padThen` of it (`algOf`): it writes the padding string, one unit in each step, and
answers in one more step. It halts within 2^{cλ} + 1 steps, which is at most 2^{(c+1)λ}, and its
states fit `room c λ` ≤ `room (c + 1) λ` (`computes_of_answer`). So c' = c + 1 (`fromPadded`).
`computes_of_answer` is stated for a string of 2^{kλ} units with any k ≤ c, and for every c' ≥ c
with c' > k, since the pieces made from the eight-square identity (Lemma 2) take k = 0. 

 ### One function for all questions 

### `answerOf`

 The answer to a question, from the six programs and the shift: a function of ((λ in unary,
question), padding string). 

### `answer_polyT`

 The shape of `answerOf`, for any polynomial-time parts. 

### `answerOf_polyT`

 `answerOf` is polynomial-time in the question and the padding string. 

### `answerOf_eq`

 `answerOf` gives the right answer when the padding string has 2^{cλ} units. 

 ### The algorithm 

### `algOf`

 The algorithm: write 2^{kλ} units, one in each step, then answer in one step. 

### `two_pow_polyT`

 2^{kλ} is computed in polynomial time from λ in unary. 

### `algOf_polyT`

 The algorithm has polynomial-time steps. 

### `computes_of_answer`

 A function of the question and a padding string that gives the right answer at 2^{kλ} units, k ≤
c, gives an algorithm within 2^{c'λ} operations, for every c' ≥ c with c' > k. 

### `fromPadded`

 `FromPadded`, with c' = c + 1. 

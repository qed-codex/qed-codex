---
{
  "module": "proof/rates/PiecesCounted/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Sizes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sizes of questions and answers
For data that satisfy parts (a) and (b) of Definition 7 (pieces with parameters (ρ,c)) and the size
bounds of its part (c): a question that has an answer has size at most (2λ)^c + 14λ + 2cλ + 11
(with λ in unary), and the answer has size at most (2λ)^c·((2λ)^c + 2) + cλ + 4λ + 2. Both are far
below `room c λ`; the lemmas at the end put the two bounds in the form in which the later files
compare them with `room` (multiplied out by `room_eq`). 

 ### Sizes of lists and numbers 

### `size_units`

 A list of n units has size 2n + 1. 

### `size_bitList`

 A list of n bits has size 2n + 1. 

### `size_int_le`

 An integer below 2^X in absolute value has size at most X + 1. 

### `size_natCast_le`

 A natural number n, as an integer, has size at most n + 1. 

### `size_ints_le`

 A list of integers, each of size at most s. 

 ### The numbers of bits 

### `Data.Is.cap_le`

 c^row_i, c^col_i ≤ cλ + 4λ, from the bound of (b). 

 ### Questions and answers 

### `Data.Is.size_question_le`

 A question that has an answer, with λ in unary, has size at most (2λ)^c + 14λ + 2cλ + 11. 

### `Data.Is.size_answer_le`

 An answer has size at most (2λ)^c·((2λ)^c + 2) + cλ + 4λ + 2. 

 ### How they fit the bound on the states 

### `room_eq`

 The bound on the states, multiplied out. 

### `two_mul_le_pow`

 2λ ≤ (2λ)^c for c ≥ 1. 

### `Data.Is.size_question_le'`

 A question that has an answer: at most 8·(2λ)^c + 2·2^{cλ} + 11. 

### `Data.Is.size_answer_le'`

 An answer: at most (2λ)^c·(2λ)^c + 4·(2λ)^c + 2^{cλ} + 2. 

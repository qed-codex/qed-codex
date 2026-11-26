---
{
  "module": "proof/rates/PiecesCounted/Trimmed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Trimmed.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Trimmed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # All numbers of bits at most 2λ

In the pieces of Definition 7 one may assume c^row_i, c^col_i ≤ 2λ: any F : {0,1}^{2λ} × 𝒳' → ℤ
factors through 2λ bits, as F(z, z') = Σ_{θ ∈ {0,1}^{2λ}} [z = θ] F(θ, z'), and a longer
factorization is replaced by this one, with c replaced by c + 2, which pays for computing c^row_i or
c^col_i first.
`trimmed D` are the data with every longer factorization replaced; d, 𝓘 and the A_i stay.
`assumeAlg Alg` is the new algorithm. It runs Alg once on a first question (`firstQ`): the question
itself, or, for a value of a function of a factorization, the number of bits of that factorization.
Then one step hands the answer of Alg to `afterFirst`, which either has the final answer (put out in
one more step) or a second question, on which Alg runs a second time: on the question itself if the
factorization was kept, on a question for a value of A_i if the value F(θ, z') is asked for. That
makes 2·2^{cλ} + 1 steps at most (2^{cλ} + 2 if the answer is there after the first run), which is
at most 2^{(c+2)λ};
the states hold the question beside a state of Alg, and fit `room (c + 2) λ`. This file has the
data, the algorithm with its certificate and its two kinds of run, and the arithmetic; `Assume.lean`
puts them together. 

 ### The new data 

### `trimmed`

 Every factorization through more than 2λ bits is replaced by F(z, z') = Σ_θ [z = θ]·F(θ, z'), θ
a string of 2λ bits. 

### `trimmed_cap`

 The new numbers of bits. 

### `trimmed_fn_of_le`

 A factorization through at most 2λ bits is kept. 

### `trimmed_fn_first`

 The function of the first pair in the new factorization: [z = θ]. 

### `trimmed_fn_row`

 The function of the second pair in the new factorization, as a function of (x, y) and (u, v):
F(θ, z') = A_i(θ₁, θ₂, u, v). 

### `trimmed_fn_col`

 The same as a function of (x, u) and (y, v): F(θ, z') = A_i(θ₁, y, θ₂, v). 

### `toBits_bitsOf`

 A string written as a list and read again. 

### `toBits_take`

 The first half of two strings written one after the other. 

### `toBits_drop`

 The second half. 

### `sum_indicator`

 F(z, z') = Σ_θ [z = θ]·F(θ, z'), over the strings θ of 2λ bits. 

### `trimmed_is`

 The new data have clauses (a), (b) and the sizes of (c), with the same ρ and c. 

 ### The new algorithm 

### `firstQ`

 The first question: the question itself; for a value of a function of a factorization, the
number of bits of that factorization. 

### `afterFirst`

 After the first answer: the answer to the question (left), or the second question (right). 

### `assumeAlg`

 The new algorithm: Alg on the first question; one step for the hand-over; then the answer in one
more step, or Alg on the second question. 

### `firstQ_polyT`

 The first question is computed in polynomial time. 

### `afterFirst_polyT`

 So is what follows the first answer. 

### `assumeAlg_polyT`

 The new algorithm has polynomial-time steps. 

### `assumeAlg_runs_one`

 The run in which the answer is there after the first run of Alg. 

### `assumeAlg_runs_two`

 The run with a second run of Alg. 

 ### What the oracle answers 

### `oracle_cap`

 The answer to the question for a number of bits. 

### `oracle_value`

 The answer to the question for a value of A_i. 

### `oracle_fn`

 The answer to the question for a value of a function of a factorization. 

 ### The bounds 

### `four_steps_le`

 4·2^{cλ} ≤ 2^{(c+2)λ} for λ ≥ 1. 

### `two_room_le`

 2·room c λ + 3 ≤ room (c + 2) λ for c, λ ≥ 1. 

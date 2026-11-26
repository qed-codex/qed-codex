---
{
  "module": "proof/rates/CountedRecursion/AnswersDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/AnswersDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/AnswersDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Answers of two kinds, and the numbers of a level

Definitions and statements only; nothing is proved here.

**Why.** The recursion of Theorem A (b) is to be ONE machine (`QueryMachines.Tower.tower`), and a
tower has one type of answers. Its machines ask three things: the tables of a clique (an integer),
the pieces (an integer, or the list 𝓘), and a call of the solver (an integer). So the type of
answers is that of the pieces, `PiecesCounted.Answer` = ℤ ⊕ List ℤ, and an integer v is the answer
`Sum.inl v`.
* `asInt`, `asList`: how an answer is read. An answer of the wrong kind is read as 0, or as the
  empty list; with the oracles of the statements this does not happen.
* `askInt h`, `askList h`: ask the query h a and read the answer.
* `readAs r M`: a machine M that was built for answers of type A, run where the answers have type A'
  and are read by r. (The library of machines with query access has `mapAsk` for the queries; this
  is its counterpart for the answers. It lets `Printed.bruteMachine` be used as it is.)
* `numbersM x₀`: «K_ℓ» and «g_ℓ = 2^{3ℓ+x₀}K_ℓ» in unary from ℓ in unary. K_ℓ is doubly exponential
  in ℓ and a step must take time polynomial in the size of the state, so the numbers cannot be
  written in one step. The loop has ℓ rounds and keeps the pair (2^{3j+x₀}, K_j), both in unary; a
  round replaces (p, K) by (8p, (pK)²), which is polynomial-time in the pair. 

### `PieceQuery`

 A query to the pieces: λ in unary and the question. 

### `Ans`

 The one type of answers: an integer, or (for 𝓘) a list of integers. 

### `asInt`

 An answer read as an integer. 

### `asList`

 An answer read as a list of integers. 

### `askInt`

 Ask the query h a; the answer is read as an integer. 

### `askList`

 Ask the query h a; the answer is read as a list of integers. 

### `readAs`

 The same machine where the answers have another type and are read by r. 

### `ReadAsRuns`

 The runs are the same, if the new oracle, read by r, is the old one. 

### `ReadAsPoly`

 Polynomial-time steps are kept, if r is polynomial-time. 

### `PricesScale`

 If every price is raised at most k times, so is the cost. (For one price for all queries this is
`QueryMachines.StSlowDown`.) 

 ### The numbers of a level 

### `numbersStep`

 One round: (2^{3j+x₀}, K_j) becomes (2^{3(j+1)+x₀}, K_{j+1}) = (8·2^{3j+x₀}, (2^{3j+x₀}K_j)²),
all in unary. 

### `numbersM`

 From ℓ in unary: (2^{3ℓ+x₀}, K_ℓ) in unary, by ℓ rounds. 

### `NumbersRun`

 The loop returns (2^{3ℓ+x₀}, K_ℓ) after 2ℓ steps, on states of size linear in g_ℓ. One constant
for all x₀ and ℓ. 

### `NumbersPoly`

 The loop has polynomial-time steps. 

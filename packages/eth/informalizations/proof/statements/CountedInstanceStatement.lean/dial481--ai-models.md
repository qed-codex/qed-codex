---
{
  "module": "proof/statements/CountedInstanceStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/CountedInstanceStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/CountedInstanceStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The hypothesis of Theorem D (a) holds for the recursion of Theorem A (b) on the pieces of Appendix B, in counted operations

Statements only (no definition of a machine, no theorem, no proof).

**The text** (Theorem D (b)): «The pairs (K_ℓ, e_ℓ) of (40), for the pieces of Appendix B, satisfy
this hypothesis, and e_ℓ = Θ((log K_ℓ)^{−1/2}).» The hypothesis is that of Theorem D (a): constants
and numbers with K_ℓ ≥ 2, K_ℓ < K_(ℓ+1) ≤ K_ℓ^C₀ and (log K_ℓ)^(−C₀) ≤ e_ℓ ≤ 1; K_ℓ and a number in
[e_ℓ, 2e_ℓ] can be computed from ℓ in time polynomial in K_ℓ; and
«one deterministic algorithm, given ℓ ≥ 0, λ, B ≥ 1 and query access to tables with |W_w| < 2^B,
outputs the value of the (K_ℓ, λ)-clique within 2^{e_ℓK_ℓ²λ}·(K_ℓ(λ+B))^{C₀K_ℓ²} operations».

**What is here.** `TheRecursionMeetsTheHypothesis`: all clauses at once, in counted operations, for
ONE machine that is named: `ExplicitCost.cliqueMachine (c + 2) x₀ Alg`, the recursion of Theorem A (b)
with the algorithm Alg of pieces D run inside. The statement says of D and Alg: they are pieces with
parameters (1/√2, c + 2) in the sense of Definition 7
in counted operations; all their numbers c^row_i, c^col_i are at most 2λ; and their d, 𝓘 and A_s are
those of the proof of Theorem B (`AreThePiecesOfAppHalfPieces`). The c + 2 comes from «We may and do
assume c^row_i, c^col_i ≤ 2λ … (and c by c + 2 …)». The clauses on numbers alone are
`ThePairsMeetTheClauses`. The implication
`TheRecursionMeetsTheHypothesisFrom` records from what the statement follows: Theorem B, that
assumption and Theorem A (b), all in counted operations, and the clauses on numbers.

**What it is for.** With the step from counted operations to the padding string
(proof/rates/CountedToPadded/Defs.lean) it lets Theorem D and the Main Theorem rest on Theorem A
(b), Lemma 8 and Definition 7 in counted operations.

**Where it differs from the text.** What `CliqueLevelsStatement.lean`, `PiecesCountedStatement.lean`
and proof/rates/CountedRecursion/RecursionDefs.lean list; in particular `CliqueLevels.Solves` adds a
bound on memory, and x₀ is asked to satisfy 2^{x₀} ≥ c + 7 for the c of Theorem B, where Theorem A
prints 2^{x₀} ≥ c + 5 for the c after the replacement. 

### `ThePairsMeetTheClauses`

 The clauses of the hypothesis of Theorem D (a) that speak of numbers alone, for the pairs (K_ℓ,
e_ℓ) of display (40) at ρ = 1/√2. For every x₀ ≥ 18 and every C₀ ≥ 10: K_ℓ ≥ 2, K_ℓ < K_(ℓ+1) ≤
K_ℓ^C₀ and (log K_ℓ)^(−C₀) ≤ e_ℓ ≤ 1 (`CliqueLevels.Levels`); K_ℓ is computed by the named program
`CliqueLevels.levelsUnder x₀`;
`PairsToBound.fractionHalf` computes a number in [e_ℓ, 2e_ℓ]; and e_ℓ ≤ (3x₀+6)/√(log K_ℓ), the
upper half of «e_ℓ = Θ((log K_ℓ)^{−1/2})». 

### `AreThePiecesOfAppHalfPieces`

 The d, 𝓘 and A_s of D are those of the proof of Theorem B: with h = `AppHalfPieces.hOf λ` and
μ(x) the partition of h with number x in the lexicographic list: 𝓘 = {−2h, …, 2h}, d = h!, A_s =
`AppHalfPieces.piece`. (As in `PiecesCounted.HalfPieces`, without its clause on c^row_s, c^col_s,
which the assumption c^row_s, c^col_s ≤ 2λ may change.) 

### `TheRecursionMeetsTheHypothesis`

 **«The pairs (K_ℓ, e_ℓ) of (40), for the pieces of Appendix B, satisfy this hypothesis»**, in
counted operations. There are a constant c, an integer x₀ ≥ 18 with 2^{x₀} ≥ c + 7, a constant C₀,
and pieces D with their algorithm Alg, with parameters (1/√2, c + 2), with all c^row_i, c^col_i ≤ 2λ
and with the d, 𝓘 and A_s of the proof of
Theorem B, such that the machine E = `cliqueMachine (c + 2) x₀ Alg` has polynomial-time steps and,
given ℓ, λ, B and query access to tables with |W_w| < 2^B, outputs the value of the (K_ℓ, λ)-clique
within 2^{e_ℓK_ℓ²λ}·(K_ℓ(λ+B))^{C₀K_ℓ²} operations (`CliqueLevels.Solves`), for the K_ℓ and e_ℓ of
display (40) at ρ = 1/√2; and the
clauses on numbers hold with the same C₀. The last clause is the upper half of «e_ℓ = Θ((log
K_ℓ)^{−1/2})», with a natural number in front, the form in which the «In particular» of Theorem D (a)
takes it; the lower half is not stated here. 

### `TheRecursionMeetsTheHypothesisFrom`

 How: Theorem B in counted operations, for the functions of its proof, gives pieces with
parameters (1/√2, c); «We may and do assume …» gives pieces with parameters (1/√2, c + 2), the same
d, 𝓘 and A_s, and all numbers of bits at most 2λ; Theorem A (b) in counted operations gives a
constant for the machine on them; the constant is
made at least 10 (`CliqueLevels.SolvesGrowsWithTheConstant`: «with the larger of C₀ and 10»); the
clauses on numbers. 

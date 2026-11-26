---
{
  "module": "proof/variables/FixedWidthSteps/RouteDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/RouteDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/RouteDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The bound in n for fixed k: the forms that show the route

`FixedWidth.Counts α` says «there is a machine»; by its wording it says nothing about the route of a
proof. The proof in the paper (in the proof of Theorem A (c)), sentence by sentence:
(1) «The second statement follows from Theorem D (a), (2) whose conditions n ≥ K₀^17 and k ≤ (log
    n)^{1/4} hold for all but finitely many n when k is fixed; (3) for the finitely many other n the
    algorithm tries all assignments, (4) and a formula with k ≤ 2 is read as a 3-CNF.
(5) Its hypothesis holds by (a) and (b), with the larger of C₀ and 10: (6) e_ℓ ≥ ½ρ^ℓ ≥ 2^{−ℓ−1} ≥
    1/log K_ℓ, (7) and a number between 0.85ρ^ℓ and ρ^ℓ lies in [e_ℓ, 2e_ℓ].»
The statements of this file are these sentences, two steps that the text leaves unsaid
(`RateOfThePairs`, `SmallCasesAreWithinTheBound`), the main statement for every machine, and three
implications that fix how they hang together. Nothing is proved here.

* `HypothesisHolds`: (5) and (7), for the named solver: the recursion of part (b) on the pieces. It
  is `PairsToBound.TheRecursionHasLevels` (proof/variables/PairsToBound/Defs.lean: the statement of
  «Its hypothesis holds by (a) and (b)», which Step 6 of Appendix D cites) with the clause on the
  number of the proviso. It says «there is a C₀ that depends on c
  alone»; that this is the larger of the C₀ of (b) and 10 is not stated.
* `ChainOfInequalities`: (6) and (7) as inequalities. `RateOfThePairs`: e_ℓ = O((log K_ℓ)^{−α'}), by
  part (a), which the «In particular» of Theorem D (a) asks.
* `ConditionsHoldEventually`: (2). `ReadAsThree`: (4), as a sentence; see below for what the
  algorithm does.
* `EveryChoiceCounts` (the main statement): for EVERY solver with a sequence of levels with e_ℓ ≤
  a/(log K_ℓ)^α, EVERY machine M with the conclusion of Theorem D (a) for it and EVERY machine Mb
  that tries all assignments: EVERY machine N that chooses between M (on the code rewritten at the
  largest
  number of literals in a clause, or 3 if that is larger) and Mb by the test of (2) counts, for
  every fixed k, within the printed bound.
* `HypothesisHoldsFrom`, `EveryChoiceCountsFrom`, `SentenceFromTheSteps`: how the statements hang
  together, up to the printed sentence.

**Where the algorithm differs from the text.** The test, the front end, «tries all assignments» and
«chooses» are those of the proof of Theorem D (b) from Theorem D (a)
(proof/variables/PairsToBound/Defs.lean, proof/machines/TwoMachines/Defs.lean), that is, of Step 6
of Appendix D. The proof of Theorem A (c) tests the fixed k and reads
k ≤ 2 as 3. The algorithm here, as in Steps 5 and 6, takes the largest number of literals in a
clause of its input, or 3 if that is larger; this number is at most max(k, 3), and smaller if the
declared k is larger than the longest clause. So one machine serves all k, and `ReadAsThree` is not
used by it:
`PairsToBound.WidthOr3Stmt` takes its place. 

### `ChainOfInequalities`

 (6) and (7). For ½ ≤ ρ < 1, x₀ ≥ 18 and every ℓ: e_ℓ ≥ ½ρ^ℓ ≥ 2^{−ℓ−1} ≥ 1/log K_ℓ; and every
    real number between 0.85ρ^ℓ and ρ^ℓ lies in [e_ℓ, 2e_ℓ]. 

### `RateOfThePairs`

 By part (a): e_ℓ ≤ 0.85·ρ^ℓ ≤ 0.85·((3x₀+6)/log K_ℓ)^{α'}, so e_ℓ ≤ (3x₀+6)/(log K_ℓ)^{α'}. 

### `HypothesisHolds`

 (5) and (7): «Its hypothesis holds by (a) and (b), with the larger of C₀ and 10». For every c
    there is a C₀, which depends on c alone, such that for ALL pieces with parameters (ρ, c) and
    every x₀ ≥ 18 with 2^x₀ ≥ c + 5 the named solver, the recursion of part (b) on these pieces, is
polynomial-time and has a sequence Q of levels in the sense of the hypothesis of Theorem D (a), for
the numbers e_ℓ and K_ℓ of the display that defines them in Theorem A, with the constant C₀; the
level is picked by the named program; and every `num` as in the proviso computes a number in [e_ℓ,
2e_ℓ] in the
sense of that hypothesis. (The fields of Q are the rest of the hypothesis: K_ℓ ≥ 2, K_ℓ < K_(ℓ+1) ≤
K_ℓ^C₀, (log K_ℓ)^(−C₀) ≤ e_ℓ ≤ 1, the solver is right when the padding string has 2^need units, and
need ≤ e_ℓK_ℓ²λ + C₀K_ℓ²·log(K_ℓ(λ+B)).) 

### `ConditionsHoldEventually`

 (2): «whose conditions n ≥ K₀^17 and k ≤ (log n)^{1/4} hold for all but finitely many n when k
is fixed». 

### `ReadAsThree`

 (4): «a formula with k ≤ 2 is read as a 3-CNF». 

### `SmallCasesAreWithinTheBound`

 (3), the arithmetic: for fixed k and finitely many n, trying all assignments is within the
bound. For all c, k, n₀ and 0 ≤ α there is a C with 2^{c·n}·n^{c·k} ≤ 2^{C·n·log log n/(log n)^α}
for 4 ≤ n < n₀. 

### `EveryChoiceCounts`

 **The main statement.** Let 0 < α, let S be a solver with a sequence Q of levels and e_ℓ ≤
a/(log K_ℓ)^α for all ℓ; let M with C′ have the conclusion of Theorem D (a) for S and Q; let Mb with
c try all assignments; let `pre` rewrite the code at the largest number of literals in a clause, or
3 if that is
larger, and let `test` be the test «n ≥ K₀^17 and this number is at most (log n)^{1/4}» (the
conditions of (2), for this number in place of k), with K₀ = K at the level 0. All of these are
arbitrary. Then EVERY machine N that chooses, by `test`, between M behind `pre` and Mb on the input
as it is, for whatever q, counts for every fixed k ≥ 1 within the
printed bound, with a constant C that may depend on k. 

### `HypothesisHoldsFrom`

 (5) to (7): that the hypothesis holds, from the levels of the recursion and the chain of
    inequalities. 

### `EveryChoiceCountsFrom`

 (2) to (4): the main statement, from the «In particular» of Theorem D (a), which holds for every
    machine, the conditions for all but finitely many n, the finitely many other n, and what is
    known of the width that the algorithm takes. 

### `SentenceFromTheSteps`

 (1): the printed sentence, from Theorem D (a) with the number in [e_ℓ, 2e_ℓ], that its
hypothesis holds, the rate of the pairs, that a test can choose between any two machines, that the
front end and the test exist, that some machine tries all assignments, and the main statement. All
premises are to be
proved as theorems, so by its statement alone this implication shows nothing; it fixes the route,
which the proof of `FixedWidth.CountsFromPieces` takes. 

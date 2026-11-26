---
{
  "module": "proof/threesat/Suffices/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «It suffices …», for deciding, from Lemma 4 as an enumeration (definitions and statements only)

The proofs of Theorem 2 in proof/networks/Eight/, proof/threesat/ThreeSatOnTree/ and
proof/threesat/ThreeSatPrinted/ take Lemma 4 at one place, the property `Eight.SufficesSparse δ M S`
(proof/networks/Eight/SecProof_Proof.lean). It differs from the printed sentence: the machine Mc for
sparse formulas must work for EVERY number m of clauses, not only for m ≤ Mn; there is no «plus a
polynomial in n».
`SufficesPrinted δ M S` has both as printed, so it asks less of Mc and says more of S. The
construction S is `satLoop τ`, lines 1 to 4 of Algorithm 1 in their deciding form: go through the
formulas of Lemma 4 one after the other (`Enumerate.produced`: the outputs ψ ∪ 𝒩), test each with
Mc, and return «satisfiable» at the first that passes (`Exits.walkUntil`).
The last sentence of the proof, «Lemma 4 yields at most 2^{δn/3} such formulas, in time 2^{δn/3}
times a polynomial in n, … so the total time is O(2^{δn})», is `StTotal`: (number of formulas) ×
(cost of one) + (cost of the enumeration).
This file has no proofs. 

### `satLoop`

 **Lines 1 to 4 of Algorithm 1**, for a fixed parameter τ of Lemma 4 and a machine Mc in the
place of Count: decode the input into (n, φ); answer «unsatisfiable» if φ has an empty clause (not a
clause in the paper);
«for each Φ in the list that Lemma 4 computes from φ and ε do» (line 2), then, in place of lines 3
and 4 of the paper (which add up 2^{n'}·Count(Φ)), return "satisfiable" at the first Φ with Count(Φ) >
0 and "unsatisfiable" if there is none. The formulas are produced one at a time; the list is not
stored. 

### `DecidesSparse`

 What is asked of the machine Mc: to decide whether a 3-CNF Φ with m ≤ Mn clauses is satisfiable,
in time O(2^{δ'm}) plus a polynomial in n (the deciding form of the paper's sentence, which counts).
For every n and every 3-CNF Φ on n variables with m ≤ M·n clauses, Mc returns within A·2^{δ'm} +
A·(n+1)^A steps, on states of size at most A·(size Φ + n)^A, an integer that is positive exactly if
Φ is satisfiable. Nothing is asked for other Φ. 

### `SufficesPrinted`

 **It suffices to decide whether a 3-CNF Φ with m ≤ Mn clauses is satisfiable, in time O(2^{δ'm})
plus a polynomial in n** (the deciding form of the paper's sentence, which counts), δ' = δ/(3M), as
a property of the constant M and of a construction S of machines: S keeps polynomial-time steps, and
whenever Mc does what the sentence says, S Mc decides 3-SAT on n variables within c·2^{δn} steps. 

### `StPrintedGivesSparse`

 The printed property gives `Eight.SufficesSparse`, the property that the proofs of Theorem 2
use: a machine that works for every m works for m ≤ Mn. 

### `StLoopRuns`

 **The run of lines 1 to 4**, for an enumeration and any test: let φ be a 3-CNF on n variables
and let Mc return on every formula that is TESTED (those produced up to and including the first with
a positive result) within t steps the integer v Φ. Then `satLoop τ Mc`, started on the code of φ,
returns within
(number of formulas tested)·(t + 2) + τ⁶·n + 2 steps whether v Φ > 0 for some formula produced.
Beyond the states of Mc (of size at most Sm) the states have size polynomial in the length of the
input; the constant c does not depend on Mc, n or φ. 

### `StTotal`

 **«Lemma 4 yields at most 2^{δn/3} such formulas, in time 2^{δn/3} times a polynomial in n, … so
the total time is O(2^{δn})»**: the arithmetic. N formulas, N ≤ 2^{δn/3}; each costs at most
A·2^{δ'm} + A(n+1)^A, rounded up to a whole number of steps, and 2 steps of the walk, with δ'm ≤
δn/3: together at most A·2^x + A(n+1)^A + 3 with x ≤ δn/3; the enumeration costs D·n + 2 more. 

### `StSuffices`

 **«By Lemma 4 with ε = δ/3, … it suffices …»**: from Lemma 4 as an enumeration
`Enumerates (δ / 3) M τ`, for its constant M = M(δ/3) and its parameter τ (not in the paper). 

### `StLoopRunsOf`

 The run of lines 1 to 4 from the walk that halts at the first leaf that passes. 

### `StSufficesOf`

 The same with what it rests on in its hypotheses: the run of the loop, the count of the total
time, and (for the polynomial-time steps of the loop) those of `Exits.foldUntil`. 

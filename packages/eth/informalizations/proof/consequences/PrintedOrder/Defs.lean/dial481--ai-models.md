---
{
  "module": "proof/consequences/PrintedOrder/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The printed reasons on the path (definitions and statements only)

Corollaries 6 and 5 are proved in proof/consequences/SplitCount/ and proof/consequences/SplitSat/,
and proof/consequences/ThmCount/ draws Theorem C from Theorem D(b). In three places a sentence of
the printed proof has a Lean statement there, but the end theorem does not pass through it. Here the
end theorems are stated along a route that does pass through these statements.

1. **Corollary 6.** «… into at most 2^{εn} k-CNFs on the same variables, each with O(n) clauses, no
   two of which share a satisfying assignment, so that their numbers of satisfying assignments add
   up.» In proof/consequences/SplitCount/ the sum comes from a lemma of
   proof/consequences/CountKSat/ on one step of the tree, and `SplitCount.StDisjointLeaves` stands
   beside it.
   Here: `StAddUp` (for EVERY list of formulas: if no two share a satisfying assignment and an
   assignment satisfies ψ exactly if it satisfies one of them, the numbers add up), `StCovered` (the
   second condition, for the leaves of the tree), `StRootSame` (the root has the satisfying
   assignments of the given formula), `StTreeAddsUp` (the sum over the leaves, proved from
   `SplitCount.StDisjointLeaves`, `StCovered`, `StRootSame` and `StAddUp`), `StStepAdds` (the same
   for one step, proved from `SplitCount.StDisjoint` and `StAddUp`),
   `StBounds` (the bounds of the sparsification, without the sum), so that the sum can only come
   from the leaves.
2. **Corollary 5.** «Theorem 2 gives s_3 = 0, which is the negation of ETH» … «By a theorem of
   Impagliazzo, Paturi and Zane […], which rests on their Sparsification Lemma, s_3 = 0 implies s_k =
   0 for every k ≥ 3» In proof/consequences/SplitSat/ the implication for machines cut into steps
   (`SplitSat.StImplication`) is proved, but the end theorem takes the parameters of the reduction
   directly. Here: `StThreeSatFamily` (Theorem 2 gives a family of procedures for 3-SAT, one for
   each exponent), and the end theorem for k > 3 goes: family, implication, Turing machine.
3. **Theorem C.** proof/consequences/ThmCount/ proves that Theorem D(b) gives Theorem C, for every
   machine, and does not apply it. Here it is applied to the proof of Theorem D(b).

What stays different from the paper is said in the heads of these three folders: above all, the
implication of 2 is for machines cut into polynomial-time steps, not for arbitrary algorithms, and 3
is not the route of the printed sketch of Appendix C.
This file has no theorem. 

### `Holds`

 The assignment a satisfies the formula ψ (a literal (v, b) holds if a v = b). 

 ### Corollary 6 

### `StAddUp`

 **«no two of which share a satisfying assignment, so that their numbers of satisfying
assignments add up»** (to the number of the given formula), for EVERY formula ψ and EVERY list L of
formulas, counted on n variables: if no assignment (of all the variables x₀, x₁, …) satisfies two
formulas at different places of L, and an assignment satisfies ψ exactly if it satisfies some
formula of L, then the number of satisfying assignments of ψ is the sum of those of the formulas of
L. 

### `StCovered`

 An assignment satisfies a node of the counting tree exactly if it satisfies some leaf below it,
at every depth of the cut. 

### `StRootSame`

 The formula at the root (with the empty side list) has the satisfying assignments of the given
formula. 

### `StTreeAddsUp`

 **The numbers of the leaves add up to that of the given formula**, for all thresholds, every
width and every depth of the cut. It is proved in this development from
`SplitCount.StDisjointLeaves`, `StCovered`, `StRootSame` and `StAddUp`. 

### `StStepAdds`

 The same for one step of the tree: it is the statement `CountKSat.StStepCount` of
proof/consequences/CountKSat/. It is proved in this development from `SplitCount.StDisjoint` and
`StAddUp` (the list of the two children), and handed to `CountKSat.stProgC`, which has it as a
hypothesis, in the place of proof/consequences/CountKSat/'s own proof. 

### `BoundsPlain`

 `SplitCount.SparsifiesPlain` WITHOUT the sum: the bounds on the tree alone. ψ has variables
below n and nonempty clauses of at most k literals. The tree of depth Dd·n has at most 2^{εn}
leaves. The formula of a leaf has at most Bl·n clauses of at most max k 2 literals, on the same
variables. The stack of the walk never holds more than Dd·n + 1 nodes, each with at most (|ψ| +
n)·Sk clauses. 

### `StBounds`

 The sparsification part of the proof of Corollary 6 without the sum: for every k and ε > 0 some
threshold parameter τ gives the bounds. It is proved in this development from `CountKSat.stProgC`,
which is handed `StStepAdds`. 

### `CountingAgain`

 The end theorem of proof/consequences/SplitCount/, along this route: the last steps of
proof/consequences/SplitCount/ are repeated with the sparsification part (`SplitCount.StStepTwo`) as
a hypothesis, and the end theorem is `SplitCount.endFrom` applied to the result. 

 ### Corollary 5 

### `StThreeSatFamily`

 **«Theorem 2 gives s_3 = 0», for machines cut into steps**: there is a family of procedures for
3-SAT, one for each exponent δ₃ > 0, each with polynomial-time steps, and each member is the machine
of Theorem 2 in its decision form without its reader at some level ℓ and threshold parameter τ. It
is proved in this development from `SplitSat.stCore3`. 

### `StHosted`

 **k-SAT on Turing machines from ANY family of procedures for 3-SAT, through the implication.**
For EVERY family Ds with `Sat3SubexpBy Ds`, every k ≥ 3 and δ > 0 there are τ and δ₃ > 0 such that (1)
`REDUCE k τ (Ds δ₃)` ITSELF has polynomial-time steps and decides k-SAT with the exponent δ; (2) a
Turing machine with finite alphabets simulates it with polynomial overhead; (3) that Turing machine
decides k-SAT within ⌊c·2^{δn}⌋ steps.
It is proved in this development from `SplitSat.StImplication`. 

### `EthAndSethAgain`

 The end theorem of proof/consequences/SplitSat/, in the order of the print, proved in this
development from `StThreeSatFamily`, `StHosted` and `SplitSat.StTiedThreeTM`: s_3 = 0 from
`StTiedThreeTM`; for k > 3, the family of `StThreeSatFamily` is handed to `StHosted`. 

 ### Theorem C 

### `CountRateFromBoundInN`

 Theorem C in the wording of PaperSentencesStatement.lean with the paper's exponent α/10, α =
1/2: #3-SAT on n ≥ 2 variables in time 2^{O(n/(log n)^{1/20})}. It is proved in this development as
`ThmCount.stTheorem` applied to the proof of Theorem D(b)
(`RecursionWithPieces.Forms.thmVariablesB`). This is NOT the route of the printed sketch of Appendix
C. 

---
{
  "module": "proof/variables/RecursionToBound/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) along the printed Step 5: definitions and statements

**The text.** Theorem D (a), hypothesis: «Suppose that K_ℓ and a number in [e_ℓ, 2e_ℓ] can be
computed from ℓ in time polynomial in K_ℓ». Step 5: «The algorithm takes for k the largest number of
literals in a clause of its input, or 3 if that is larger; the bound increases with k. Take ε ≤ 1
between e and 2e, for the e of Step 4.
An output without clauses counts 2^n. Every other output is a formula Φ as above, with Δ the larger
of 2 and the largest number of its clauses in which one variable occurs; so log Δ ≤ 3k·log(8k/e) + 2 =
O(k·log(k/e)). As e ≥ (log n)^(−C₀) and k ≤ (log n)^(1/4), this is at most 3k(3 + (C₀ + 1/4)·log log
n) + 2, which is at most 4kC₀·log log n for
large n, because C₀ ≥ 1. Run Steps 2 to 4 on each of the at most 2^(2en) outputs and add the
results. The time is 2^(2en)·n^{O(k)}·2^{O(ekn·log Δ)} = 2^{O(k²·e·n·log(k/e))}, because k·log n ≤
en for large n. Here n is large if it exceeds a bound that depends only on the constants of the
hypothesis. For the finitely many smaller n ≥ K₀^17, and the
k ≤ (log n)^(1/4) that go with them, trying all assignments is within the bound.»

**Another form in this development.** `MainTheoremForms.ThmVariablesA` has a precision 2^(−s) ≤ e_ℓ
in place of the number in [e_ℓ, 2e_ℓ].

**What is defined here**, in the order of the text. S is a solver for cliques, `pick` picks the
level for n, `num` computes the number in [e_ℓ, 2e_ℓ], n₁ is the bound from which on n is «large».
* `PairsToBound.NumberBetween S Q num` (proof/variables/PairsToBound/Defs.lean): the printed clause
  of the hypothesis; `num` gets ℓ and K_ℓ in unary, so its time is polynomial in K_ℓ.
* `epsOf r`: ε = min(r, 1) for the number r = a/b. `widthOr3F ψ`: this k. `thresholds k r`: the
  thresholds of the sparsification for k and ε. This Δ is
  `SparsificationLemma.StepSparsify.DeltaOf n Φ`
  (proof/sparsification/SparsificationLemma/StepSparsifyDefs.lean).
* `countOutput`: «An output without clauses counts 2^n»; every other output ψ ∪ 𝒩
  (`SparsificationLemma.out x`, every clause written once) is counted by Steps 2 to 4
  (`VariableBound.countD`) with its own Δ. `countAll`: the walk through the tree of the
  sparsification (`StepSparsify.walkSG`) that adds these counts.
* `needOutputs`, `needWalk`: the exponent of a padding string that suffices. As the exponent must be
  computed from the input before any output is known, and nothing says that the exponent of the
  solver grows with the label length, `needOutputs` is the MAXIMUM over all Δ from 2 to the bound on
  the occurrences, cut off at n + 1.
* `planAt`, `plan`, `expo`, `count`: the algorithm. If n < n₁ it tries all assignments. Else it
  sparsifies and counts.

**The statements.** `ThmVariablesAWithNumberBetween`: Theorem D (a) with the printed clause.
`ThmVariablesAForEveryMachine`: for all large n₁ some machine computes the named function
`count S n₁ Q.pick num`, and EVERY machine that computes it has the bound of Theorem D (a).
`WalkTreeIsSparsify`: the outputs at the leaves of the tree that the function walks are the outputs
`SparsificationLemma.Cal.sparsify`, of which
proof/sparsification/SparsificationLemma/StepSparsify.lean proves the sentences of Step 5 one by
one. `OutputsAreFew`, `OwnDeltaIsBounded`, `OutputsAreWithinTheSetting`, `OneOutputCost` (Step 4's
conclusion), `WalkCost`, `ExponentIsWithinTheBound`, `PlanFailsOnlyAboveN`, `CutOffIsIdle`,
`WidthOnTheCode`, `CountIsRight`, `CountIsPolynomialTime`: the sentences of Steps 4 and 5 for this
function. «For the finitely many smaller n …» is `MainTheoremForms.StepSparsifySmallStmt`, which the
proof of `ThmVariablesAForEveryMachine` uses (End.lean).

**What differs from the text.** (1) Cost is the length of a padding string. (2) A guard that the
text does not have: if the exponent computed exceeds n, the function tries all assignments (which is
then no slower). It cannot be dropped: a solver's exponent is computable only under a bound given in
unary. `PlanFailsOnlyAboveN` says that for n ≥ n₁ this is the only case in which the
function does not sparsify. (3) k is cut off at ⌊log₂(n+1)⌋ in the call, so that 2^k is polynomial
on ALL inputs; `CutOffIsIdle`: in the range of Theorem D (a) the cut-off does nothing. (4) The label
length in the call of the solver is ⌊(U + gP/K)/K²⌋ + 1, at bounds on U and P that do not depend on
the formula (`ClauseBound.Alg.valS`). B′ is not handed to the solver; it stands only in the
exponent, as `ClauseBound.Alg.bitsS`, which is at most the printed B′ for K ≥ 5. (5) Outside the
range
n ≥ K₀^17, 3 ≤ k ≤ (log n)^(1/4), of which Theorem D (a) says nothing, nothing is claimed of the
number that the function returns nor of its exponent: for n ≥ n₁ outside this range it may sparsify
with a padding string that is too short and return a wrong number. Polynomial time
(`CountIsPolynomialTime`) and the guard (`PlanFailsOnlyAboveN`) hold on all inputs. (6) n₁ and the
constant of the bound are chosen after the solver, the sequence of levels and `num`; the text says
that they depend only on the constants of the hypothesis. (7) One padding string serves all outputs,
so its exponent is a maximum over Δ where the text adds up
times. (8) Lean's formulas are lists: a formula with an empty clause counts 0, clauses that contain
a variable together with its negation are deleted first, and the side list of the walk starts with
the n clauses xᵢ ∨ ¬xᵢ, which `SparsificationLemma.out` drops. (9) The exponent of the walk has,
besides εn and O(k·log n), a term O(k·log(k/ε)): the stack is bounded through the length (β₁ + … +
β_(k−1))·n of a path, not through the number of nodes. `WalkCost` states it; it is absorbed because
k·log(k/e) ≤ k²·e·n·log(k/e). (10) α and ⌈log₂ x⌉ in the thresholds are rounded up to natural
numbers (`SparsificationLemma.Cal.alphaC`). 

 ### The numbers of Step 5 

### `epsOf`

 «Take ε ≤ 1 between e and 2e»: ε = min(a/b, 1) for the number a/b in [e, 2e]; as e ≤ 1 it is
again in [e, 2e]. 

### `widthOr3F`

 «the largest number of literals in a clause of its input, or 3 if that is larger». 

### `thresholds`

 The thresholds of the sparsification for k and ε = `epsOf r`: θ₀ = 2, θ_c = α·β_c with α =
⌈2(k−1)²·ε⁻¹·⌈log₂(32(k−1)²/ε)⌉⌉, where the numbers β_c (for clauses of size c; not the β of the
paper) are those of the definition of `Cal.thetaC`. 

### `occBound`

 The bound on the number of clauses of an output in which one variable occurs: 2·(θ₀ + … +
θ_(k−1)) + 2; for k ≥ 3 and 0 < ε ≤ 1 it is at most 2·(8k/ε)^(3k) + 2. 

 ### The count 

### `countOutput`

 The count of the output at the node x: «An output without clauses counts 2^n. Every other output
is a formula Φ as above, with Δ the larger of 2 and the largest number of its clauses in which one
variable occurs»: Steps 2 to 4 (`VariableBound.countD`) with this Δ
(`SparsificationLemma.StepSparsify.DeltaOf`). The output is `SparsificationLemma.out x`: the side
clauses of one literal and the clauses of the formula at x,
every clause written once. 

### `countAll`

 «Run Steps 2 to 4 on each of the … outputs and add the results»: the walk, with the thresholds
for k and ε, through the tree of the sparsification of the decoded formula d = (n in unary, clauses)
without the clauses that contain a variable together with its negation; 0 if d has an empty clause. 

 ### The exponent of the padding string 

### `needAt`

 What the count of one output with this Δ needs: the networks, the list of profiles, the list of
checks (the three fields of `VariableBound.FitsD`). 

### `needAtC`

 The same, computed under the bound b in unary: `none` if the exponent of the solver is larger
than the bound. 

### `deltas`

 The numbers Δ that an output can have: 2, …, the bound on the occurrences, cut off at n + 1. 

### `needOutputs`

 The maximum of `needAt` over these Δ. 

### `needOutputsC`

 The same, computed under the bound b: `none` if one of them is. 

### `needWalk`

 What the walk needs: its rounds (at most 2^(εn) outputs, so fewer than 2^(⌈εn⌉+1) nodes) and its
stack. 

 ### The algorithm 

### `planAt`

 The exponent for width k, n variables, the index i and the number r, if n ≥ n₁ and the exponent
is at most n. 

### `widthU`

 This k, read from the input. 

### `numU`

 The number in [e, 2e] for the level ℓ picked for n, «the largest ℓ with K_ℓ ≤ n^(1/17)». 

### `plan`

 The plan for the input x, with this k cut off at ⌊log₂(n+1)⌋, as in the call. 

### `expo`

 The exponent of the padding string: that of the plan, or n. 

### `count`

 **The algorithm of Theorem D (a)**, as a function of (input, padding string): the number of
satisfying assignments of the formula written in p.1, in n + 1 bits. Without a plan (n < n₁, or the
exponent exceeds n) it tries all assignments; else it sparsifies and counts each output. 

 ### The statements 

### `ThmVariablesAWithNumberBetween`

 **Theorem D (a), with the printed clause on the number in [e_ℓ, 2e_ℓ].** For every
polynomial-time solver S for cliques with a sequence Q of levels and every `num` as in
`NumberBetween` there are one machine with finite alphabets and one constant C′ with the bound
`MainTheoremForms.ThmVariablesAFor`. 

### `ThmVariablesAForEveryMachine`

 The same for every machine that computes the named function: there is a number n₀ such that for
every n₁ ≥ n₀ (i) there are a machine with finite alphabets and a q such that the machine computes
`count S n₁ Q.pick num` with the exponent `expo S n₁ Q.pick num`, and (ii) EVERY machine M that
computes this function with this exponent, for whatever q, has the bound of Theorem D (a) with some
constant C′. 

### `WalkTreeIsSparsify`

 The outputs at the leaves of the tree that `countAll` walks are the outputs of the
sparsification as proof/sparsification/SparsificationLemma states it: for k ≥ 3, 0 < r, a k-CNF ψ on
n variables and every D ≥ (β₁ + … + β_(k−1))·n = `Cal.depthC`, a bound on the length of a path, the
leaves of the tree from `rootC`, mapped by `SparsificationLemma.out`, are the list
`SparsificationLemma.Cal.sparsify k n ε ψ`, ε = `epsOf r`. So the theorems
`SparsificationLemma.StepSparsify.outputs_le`,
`exactly_one`, `count_eq_sum`, which are sentences of Step 5 on the sparsification, speak of what
the function counts. 

### `OutputsAreFew`

 «… each of the at most 2^(2en) outputs». For k ≥ 3, a number r with e ≤ r ≤ 2e, 0 < e ≤ 1, and a
k-CNF ψ on n variables there are at most 2^(εn) ≤ 2^(2en) outputs, ε = `epsOf r`; and e ≤ ε ≤ 2e, ε
≤ 1. 

### `OutputsAreWithinTheSetting`

 «Every other output is a formula Φ as above, with Δ …; so log Δ ≤ 3k·log(8k/e) + 2 … which is at
most 4kC₀·log log n for large n». For every C₀ ≥ 1 there is an n₁ such that for all n ≥ n₁, all k
with 3 ≤ k ≤ (log n)^(1/4), all real e with (log n)^(−C₀) ≤ e ≤ 1 and all r with e ≤ r ≤ 2e: every Δ
with 2 ≤ Δ ≤ `occBound k r` has
log Δ ≤ 3k·log(8k/e) + 2 and Δ ≤ (log n)^(4kC₀) (so it is within «Setting and parameters»), Δ ≤ n +
1, and n ≥ 29·⌈log₂(2Δ)⌉ + 19 (what `VariableBound.StCountD` asks). That the Δ of an output is at
most `occBound k r` is `OwnDeltaIsBounded`. The middle step of the text, 3k·log(8k/e) + 2 ≤ 3k(3 +
(C₀ + 1/4)·log log n) + 2 ≤ 4kC₀·log log n, is the third conjunct. 

### `OwnDeltaIsBounded`

 In every output a variable occurs in at most `occBound k r` clauses: for k ≥ 3, 0 < r and a
k-CNF ψ on n variables, every output Φ has `DeltaOf n Φ ≤ occBound k r`. 

### `OccBoundIsThePrinted`

 «So every variable occurs in at most 2(8k/ε)^(3k) + 2 clauses of each output»: for k ≥ 3 and 0 <
r the bound `occBound k r` is at most 2·(8k/ε)^(3k) + 2, ε = `epsOf r`. 

### `BoundsGrowWithDelta`

 The bounds on the total, on P, on the number of profiles and on the lists grow with Δ. (So the
arithmetic of proof/variables/VariableBound/Top, which is stated for Δ a power of two, bounds every
Δ below that power.) 

### `OneOutputCost`

 Step 4, its conclusion: «Hence the number of satisfying assignments of Φ is computed in time
2^{O(ekn·log Δ)}.» For every polynomial-time solver with a sequence of levels there are A and n₁
such that for all n ≥ n₁, the level ℓ of n, all k with 3 ≤ k ≤ (log n)^(1/4) and all Δ with 2 ≤ Δ ≤
(log n)^(4kC₀) the exponent for one output with this Δ is at most A·e_ℓ·k·n·log Δ. 

### `WalkCost`

 Step 5: the sparsification «produces at most 2^(εn) outputs in time 2^(εn)·n^{O(k)}»; here with
an extra factor (8k/ε)^{O(k)} (item (9) of the module comment). There is a c such that for k ≥ 3, n
≥ 2 and 0 < r the exponent for the walk is at most εn + c·k·(log n + log(8k/ε)). 

### `ExponentIsWithinTheBound`

 «The time is 2^(2en)·n^{O(k)}·2^{O(ekn·log Δ)} = 2^{O(k²·e·n·log(k/e))}, because k·log n ≤ en
for large n.» For every polynomial-time solver with a sequence of levels and every `num` as in the
hypothesis there are A and n₁ such that for all n ≥ n₁, the level ℓ of n and all k with 3 ≤ k ≤ (log
n)^(1/4) the sum `needOutputs` + `needWalk`, which is the exponent of the padding string where there
is a plan, is at most
A·k²·e_ℓ·n·log(k/e_ℓ). It follows from `OneOutputCost`, `WalkCost`, `OutputsAreWithinTheSetting` and
`MainTheoremForms.StepSparsifyLargeStmt` (k·log n ≤ en). 

### `PlanFailsOnlyAboveN`

 For n ≥ n₁ the function sparsifies unless the exponent exceeds n: if `planAt S n₁ k n i r` is
`none` and n₁ ≤ n, then n < `needOutputs S k r i n` + `needWalk k r n`; and if it is `some v`, then
v is that sum. For polynomial-time solvers. 

### `CutOffIsIdle`

 In the range of Theorem D (a) the cut-off of k does nothing: if k ≤ (log n)^(1/4) and n ≥ 1,
then min(k, ⌊log₂(n+1)⌋) = k. 

### `WidthOnTheCode`

 On the code of (k, φ) the function reads «the largest number of literals in a clause, or 3»:
`widthU (SatM.enc k φ)` is `PairsToBound.widthOr3 φ`, for k ≥ 1 and a k-CNF φ; and for the level ℓ
of n, the index that it picks is that of ℓ and the number that it takes is `num` at (ℓ, K_ℓ). 

### `CountIsRight`

 The function is right in the range of Theorem D (a): for every polynomial-time solver with a
sequence of levels and `num` as in the hypothesis there is an n₀ such that for every n₁ ≥ n₀, all n
≥ K₀^17, all k with 3 ≤ k ≤ (log n)^(1/4), every k-CNF φ on n variables and every padding string of
at least 2^(`expo`) units, `count` on the code of (k, φ) is the number of
satisfying assignments in n + 1 bits. k is the width declared in the input; the function itself
takes `widthOr3F`. 

### `CountIsPolynomialTime`

 The function and its exponent are polynomial-time in (input, padding string), on ALL inputs, for
every n₁, if the solver, `pick` and `num` are. 

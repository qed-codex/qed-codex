---
{
  "module": "proof/consequences/SplitCount/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 6 (#k-SAT in time O(2^{δn})) along its printed proof: the machine and the statements (no proofs)

The proof has four steps.
1. For every δ' > 0, the proof of Theorem 2, with K and g chosen from δ' as there (we may assume δ'
   ≤ 1), computes Z, and hence the number Z·2^{n'} of satisfying assignments of a 3-CNF with m ≥ 1
   clauses in which n' of the n variables do not occur, in time O(2^{δ'm}) plus a polynomial in n;
   with no clauses the number is 2^n. (The paper says only «For k = 3 this is Theorem 2».) Here:
   `timesFreeAfter Cnt`, `StStepOneFor` (for EVERY machine Cnt that computes Z as Section 6 says),
   `StComputesZ` (Section 6's machine, for every K and every algorithm for cliques with the exponent
   δ'/12), `countThree ℓ`, `StCountIsNetworkMachine` and `StStepOne` (for COUNT of Algorithm 1). «By
   the work of Dell et al. … this case suffices»: `StSuffices`, for EVERY procedure that does what
   step 1 says.
2. «their form of the Sparsification Lemma turns a k-CNF on n variables, for any ε > 0, into at most
   2^{εn} k-CNFs on the same variables, each with O(n) clauses, no two of which share a satisfying
   assignment, so that their numbers of satisfying assignments add up.» Here: `SparsifiesPlain`,
   `StStepTwo`, and for «no two of which share …» `StDisjoint`, `StDisjointLeaves`.
3. «each of these is turned into a 3-CNF with O(n) clauses and O(n) variables and the same number of
   satisfying assignments, by the standard width reduction …» Here: `Eight.Width.widthP` and
   `StStepThree`.
4. «The constants in O(n) depend on k and ε, so choosing ε = δ/3 first and then applying Theorem 2
   with a small enough value in place of δ gives time O(2^{δn}).» Here: `deltaPrime` and
   `StCountsAt`.

The machine `COUNTsplit k ℓ τ` does just this: read the input; write 0 if some clause is empty;
otherwise walk the tree of the sparsification for counting (the tree of
proof/consequences/CountKSat/, after Dell, Husfeldt, Marx, Taslaman and Wahlén: the child that gets
the petals also gets «every literal of the heart is false», kept on a side list that the branching
rule never reads, as Appendix C does, where Dell et al. add these clauses to the formula itself,
which can change the tree; the branching rule and the thresholds `WidthK.theta τ` are those of
proof/consequences/WidthK/, Lean's own, not those of their Lemma A.1, and not the thresholds
`UniformInK.thetaU` of the tree that the deciding route in proof/consequences/SplitSat/ walks); at
each leaf apply the width reduction,
run COUNT of Algorithm 1 at level ℓ on the 3-CNF (`Eight.ViaGrouping.COUNTp ℓ`: the network has 3
places per clause), multiply by 2^{n'}; write the sum.
So no network for a width above 3 is ever made; the side list of the tree does not begin with the
clauses xᵢ ∨ ¬xᵢ; the constants for K_ℓ and e_ℓ are those of Section 6 (72/δ' and δ'/12).

Different from the paper: Step 1 is instantiated with COUNT of Algorithm 1 (Section 8) at a level ℓ
with K_ℓ ≥ 72/δ', e_ℓ ≤ δ'/12 and g_ℓ = 3K_ℓ⁸, where the proof of Theorem 2 (Section 6) takes some K
≥ 72/δ' for which (K, δ'/12) is achievable, from e* = 0, without naming the algorithm for cliques:
the constants are Section 6's, the algorithm for cliques is Section 8's CLIQUE(ℓ) (`StStepOneFor`
and `StSuffices` hold for every machine with the contract, so also for Section 6's);
«O(2^{δ'm}) plus a polynomial in n» becomes «A·2^{δ'm} steps on states of size polynomial in n and
the size of Φ», so that on the Turing machine the polynomial multiplies 2^{δ'm} and is not added to
it; a node of the tree carries n in unary (the width reduction needs a name for its first fresh
variable, and the factor needs n); a leaf has clauses of at most max(k, 2) literals in the bound
taken over from proof/consequences/CountKSat/ (for k ≥ 3 that is k);
time is counted in steps of a machine cut into polynomial-time steps, and then in steps of Mathlib's
Turing machine.
This file has no theorem. 

 ### The machine 

### `NNode`

 A node of the tree with n in unary beside it. 

### `rootPlain`

 The root: the formula as the rule looks at it, and an EMPTY side list. 

### `stepPlain`

 The step of the tree; n is handed down unchanged. 

### `leafPlain`

 What is counted at a node: (n in unary, side list and formula). 

### `timesFreeAfter`

 Step 1 of the proof, with the machine that computes Z as a parameter: on (n in unary, Φ) run Cnt
on Φ, which gives Z, and return Z·2^{n'}. 

### `countThree`

 Step 1 with COUNT of Algorithm 1 at level ℓ. 

### `engineBy`

 The whole procedure without the reader of the input, with the procedure D for 3-CNFs as a
parameter: on (n in unary, formula), 0 if there is an empty clause; otherwise walk the tree, at each
leaf apply the width reduction and then D, and add up; the sum in n + 1 bits. 

### `engineSplit`

 The procedure with COUNT of Algorithm 1 at level ℓ. 

### `ENGINEsplit`

 The procedure at width k, level ℓ, threshold parameter τ of the sparsification. 

### `COUNTsplit`

 The machine for #k-SAT: the reader of the input, then the procedure. 

 ### Step 1 

### `ComputesZ`

 What Section 6 says of the machine that computes Z («Cost»): on a 3-CNF Φ with m clauses, Cnt
returns Z, the number of assignments of the variables occurring in Φ that satisfy Φ, within
A·2^{δ'm} steps, on states of size at most A·(size Φ)^A. It is the conclusion of
`Eight.ViaGrouping.COUNTp_cost`. 

### `CountsThree`

 What step 1 says of a procedure D: on (n in unary, Φ), for a list Φ of m clauses of at most 3
literals each on x₀ … xₙ₋₁ (m = 0, empty clauses and repeated clauses included), D returns the
number of satisfying assignments of Φ on n variables within A·2^{δ'm} steps, on states of size
polynomial in n and the size of Φ. 

### `StStepOneFor`

 **Step 1, computes Z, and hence the number Z·2^{n'}, for EVERY machine that computes Z.** 

### `StComputesZ`

 **The proof of Theorem 2, with K and g chosen from δ' as there, computes Z, in the form of
Section 6.** Let 0 < δ' ≤ 1, let K ≥ 2 with K ≥ 72/δ', let E be ANY algorithm for cliques on K nodes
with the exponent δ'/12 (`E.Within K (δ'/12)`; «(K, δ'/12) is achievable» asks besides that the
steps of E are polynomial time, which this statement does not need), and g = 3K⁸. The algorithm of
the printed proof of Lemma 1 with E, run on the network of Φ on g clusters, computes Z as Section 6
says.
It is proved (`SplitCount.stComputesZ`) from `Eight.ViaGrouping.stLemGrouping` and
`Eight.ViaGrouping.count_cost_of`. 

### `StCountIsNetworkMachine`

 COUNT of Algorithm 1 at level ℓ is the machine of `StComputesZ` at K = K_ℓ and E = CLIQUE(ℓ).
(By unfolding definitions.) 

### `StStepOne`

 **Step 1 for COUNT of Algorithm 1.** Let 0 < δ' ≤ 1. At every level ℓ with K_ℓ ≥ 72/δ' and e_ℓ ≤
δ'/12 (Section 6's constants; the level ℓ stands for Section 6's achievable K), `countThree ℓ` does
what step 1 says. Proved from `StComputesZ` at K = K_ℓ and E = CLIQUE(ℓ) (`StCountIsNetworkMachine`;
CLIQUE(ℓ) has the exponent e_ℓ ≤ δ'/12: `Eight.ViaGrouping.CLIQUEp_within`) and `StStepOneFor`, so
that Section 6's form is on the path. 

 ### Step 2 

### `SparsifiesPlain`

 `step` (with `rootPlain`) sparsifies width k for counting. ψ has variables below n and nonempty
clauses of at most k literals. The tree of depth Dd·n has at most 2^{εn} leaves. The formula of a
leaf has at most Bl·n clauses of at most max k 2 literals, on the same variables.
The numbers of satisfying assignments of the leaves add up to that of ψ. The stack of the walk never
holds more than Dd·n + 1 nodes, each with at most (|ψ| + n)·Sk clauses.
It is `CountKSat.SparsifiesC` without the clauses xᵢ ∨ ¬xᵢ at the root and without «every variable
occurs in every leaf». 

### `StDisjoint`

 «no two of which share a satisfying assignment»: at every node the two children have no common
satisfying assignment, and an assignment satisfies the node exactly if it satisfies one of them.
(With «the root has the count of the formula» and the sum over the leaves, `CountKSat.StRootCount`
and `CountKSat.StSumLeaves`, this gives the sum in `SparsifiesPlain`. The proof of `StStepTwo` may
take the sum from `CountKSat.SparsifiesC`, where it comes from `CountKSat.StStepCount`, which says
the same for the numbers on n variables; so this is a statement beside the path, there for the
paper's words.) 

### `StDisjointLeaves`

 «no two of which share a satisfying assignment», for the outputs: no assignment satisfies the
formulas of two different leaves of the tree below any node, cut at any depth. 

### `StStepTwo`

 **Step 2.** For every k and ε > 0 some threshold parameter τ works. 

 ### Step 3 

### `StStepThree`

 **Step 3**, for the program. Let Ψ be a formula on x₀ … xₙ₋₁ with m clauses of at most w
literals. `widthP` returns (n₃ in unary, Ψ₃) with: Ψ₃ has at most 3 literals per clause, variables
below n₃, no clause twice; n₃ ≤ n + (w−3)·m; at most m + 3(w−3)·m clauses;
and Ψ₃ has on n₃ variables as many satisfying assignments as Ψ on n. 

 ### Step 4 and the end 

### `deltaPrime`

 «then applying Theorem 2 with a small enough value in place of δ»: a leaf has at most Bl·n
clauses of at most w literals, its 3-CNF at most (1 + 3(w−3))·Bl·n clauses; δ' = min(δ/(3·(1 +
3(w−3))·(Bl+1)), 1). 

### `StSuffices`

 **«By the work of Dell et al. … this case suffices», for EVERY procedure D that does what step 1
says.** Let k ≥ 1 and δ > 0, let `step` sparsify width k for counting with ε = δ/3 and leaves of at
most Bl·n clauses, and let D do what step 1 says with an exponent δ' ≥ 0 such that δ'·(1 +
3(max(k,3) − 3))·(Bl + 1) ≤ δ/3.
Then `engineBy step D` serves as the procedure for #k-SAT with the exponent δ (`Eight.Serves`: on (N
in unary, ψ) it returns the number of satisfying assignments in N + 1 bits within c·2^{δN} steps, on
states of polynomial size). 

### `StCountsAt`

 **Step 4, with the machine named.** Let k ≥ 1 and δ > 0, let `step` sparsify width k for
counting with ε = δ/3 and leaves of at most Bl·n clauses, and δ' = `deltaPrime δ (max k 3) Bl` (for
the paper's k ≥ 3, max(k, 3) = k). At every level ℓ with K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12,
`engineSplit step ℓ` serves as the procedure for #k-SAT with the exponent δ. Proved from `StStepOne`
and `StSuffices`. 

### `StCert`

 The steps of the procedure are polynomial time, if the step of the tree and the steps of the
parameter are. 

### `StEngineCounts`

 **Corollary 6 for machines cut into steps, with the machine named**, in the form in which
Corollary 7 and the circuit lower bound for E^NP (Section 7) take it
(`Eight.ViaGrouping.EngineCounts`; there for every k ≥ 1: below 3 the width reduction changes
nothing). 

### `StCOUNTsplitCounts`

 **#k-SAT with the machine named.** For every k ≥ 1 and δ > 0 there are a level ℓ and a threshold
parameter τ such that `COUNTsplit k ℓ τ` has polynomial-time steps and writes the number of
satisfying assignments of a k-CNF on n variables, in n + 1 bits, within c·2^{δn} steps, on states of
size polynomial in the length of the input. 

### `StTiedTM`

 **Tied to the machine, on Mathlib's Turing machines.** For every k ≥ 1 and δ > 0 there are ℓ, τ
such that (1) `COUNTsplit k ℓ τ` ITSELF has polynomial-time steps and writes the number of
satisfying assignments of a k-CNF on n variables within c·2^{δn} steps, on states of size polynomial
in the length of the input; (2) a Turing machine M with finite alphabets simulates it with
polynomial overhead
(whenever that machine ends on a word x with a word w within T steps on states of size at most S, M
started on x halts with w within q·(T+1)·(|x|+S+1)^q steps); (3) M counts the satisfying assignments
of k-CNFs within ⌊c·2^{δn}⌋ steps. (Without (1), a machine that runs the named machine and another
one side by side would meet (2) and (3).) 

### `ThreeSatStatement`

 The end theorem has the statement `ThreeSatStatement` (below), the statement of Corollary 6 in
PaperSentencesStatement.lean. Both of its halves are proved from `StTiedTM`: the second, «#ETH is
false», from `StTiedTM` at k = 3 by the generic `not_CountETH_TM_of` of
proof/consequences/CountKSat/EndLemmas.lean.
The end theorem is proved through `SplitCount.endFrom : StTiedTM → ThreeSatStatement`, which has the
tied statement as HYPOTHESES. Of the theorems of this development, the proof of `SplitCount.endFrom`
uses only lemmas that say nothing about a particular machine (such as `not_CountETH_TM_of`); so what
it says about machines can only come from the hypotheses.
The proof of `StStepTwo` takes the bound on the tree from `CountKSat.StProgC` (the tree does not
depend on the side list), and the count of a leaf never uses the clauses xᵢ ∨ ¬xᵢ. 

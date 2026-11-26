---
{
  "module": "proof/consequences/SplitSat/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 5 (s_k = 0 for every k ≥ 3) along the reduction that its proof cites: the machines and the statements (no proofs)

The printed proof: «Theorem 2 gives s_3 = 0 … By a theorem of Impagliazzo, Paturi and Zane, which
rests on their Sparsification Lemma, s_3 = 0 implies s_k = 0 for every k ≥ 3; the reduction
(sparsify, then split every long clause into clauses of 3 literals with new variables) uses no
randomness».

Here the reduction is a machine with the procedure for 3-SAT as a PARAMETER:
`REDUCE k τ D`: read the k-CNF; answer «no» if there is an empty clause; walk depth first the tree
of a sparsification of k-CNFs (here the procedure of Appendix C at width k, with the threshold
parameter τ; see (5) below); at each leaf split every long clause (`Eight.Width.widthP`) and ask D
whether the 3-CNF is satisfiable; answer «yes» if some leaf passes.
* `StReduce` is the cited implication for machines cut into steps, tied: for EVERY procedure D that
  decides 3-SAT on N variables within c·2^{δ₃N} steps, `REDUCE k τ D` decides k-SAT on n variables
  within c'·2^{δn} steps, as soon as δ₃·(1 + (k−3)·B) ≤ δ/3, where B·n bounds the clauses of a leaf.
* `StImplication`: so «3-SAT in O(2^{δN}) steps for every δ > 0» implies «k-SAT in O(2^{δn}) steps
  for every δ > 0», for machines cut into polynomial-time steps: for every family of procedures for
  3-SAT, the machine for k-SAT is the reduction run on a member of that family.
* `core3 ℓ τ` is the machine of Theorem 2 in its decision form (`ThreeSatPrinted.SATCp ℓ τ`, the
  deciding form of procedure #Sat of Algorithm 1) without its reader of the input, and `StCore3` is
  Theorem 2 for it. `StCore3Eq`: it IS that machine after the reader.
* `SATsplit` is REDUCE on it; `StSATsplit` names the machine; the end theorem has the statement
  `PaperSentences.CorEth`.

Different from the paper.
(1) The cited theorem speaks of arbitrary algorithms for 3-SAT. Here D ranges over the machines cut
    into steps whose states stay of polynomial size; nothing is said of an arbitrary Turing machine.
    So this does not prove «s_3 = 0 implies s_k = 0» for the numbers s_k of Definition 6. Instances
    have no clause written twice (`SatK.IsKCNF`), as in KSatStatement.lean, so that a time bound in
    n alone can hold.
(2) The splitting is the one of the proof of Corollary 6: the new variable y stands for l₁ ∨ l₂,
    with the clauses y ∨ l₃ ∨ …, ¬y ∨ l₁ ∨ l₂, y ∨ ¬l₁, y ∨ ¬l₂. The usual splitting has only the
    first two; the other two do no harm.
(3) A node of the tree carries n in unary, which the splitting needs to name its new variables.
(4) The list of the sparsification is not stored: each formula is tested when the walk reaches it.
(5) The tree is that of the procedure behind the Lean form of Lemma 4 (thresholds
    `UniformInK.thetaU τ`: θ 0 = 1, θ i = 4·τ^(2i−1)), run at width k
    (`SparsificationLemma.TreeWalk.lemSparsification_walk_k`). The paper cites the Sparsification
    Lemma of Impagliazzo, Paturi and Zane for k-CNFs; its own Lemma 4 is stated for 3 literals. The
    thresholds are neither theirs nor Calabro's.
(6) Two sentences of the printed proof have no statement here: the equivalence cited from
    Impagliazzo and Paturi («For all k ≥ 3, s_k > 0», «For some k, s_k > 0», «s_3 > 0»), and «so
    SETH implies ETH». As propositions about the numbers s_k they follow at once from Corollary 5
    and would show nothing; their content is a statement about every algorithm for 3-SAT, and for
    machines cut into steps that content is `StImplication`. The sentences after Definition 6 (s_k ≤
    1, s_k ≤ s_{k+1}, the limit, «ETH is the same as s_3 > 0») and the remark on randomized
    algorithms are in KSatFreeCodeStatement.lean,
for the numbers `SatFree.s k` defined there with a code that does not depend on k, not for
`SatK.sTM k`, in which `PaperSentences.CorEth` is written.
This file has no theorem. 

 ### What is asked of a procedure for 3-SAT 

### `DecidesW`

 The procedure D, cut into steps, decides w-SAT with the exponent δ and the constant c: on (N in
unary, ψ), for ψ with at most w literals per clause, variables below N and no clause written twice,
it ends within c·2^{δN} steps, on states of size at most c·(N+2)^c, with the bit «ψ is satisfiable».
No code of formulas as words is involved. 

### `Decides3`

 The same at width 3: D decides 3-SAT. 

### `Simulates`

 The Turing machine M simulates the machine Ms, cut into steps, with polynomial overhead:
whenever Ms ends on a word x with a bit b within T steps on states of size at most S, M started on x
halts with b within q·(T+1)·(|x|+S+1)^q steps. 

 ### The reduction 

### `NFml`

 A formula with n in unary beside it. 

### `stepN`

 The step of the tree; n is handed down unchanged. 

### `reduceCore`

 The reduction without the reader of the input, for any step of a tree. 

### `REDUCE`

 **The reduction of k-SAT to 3-SAT**, with the procedure D for 3-SAT as a parameter: sparsify at
width k with the threshold parameter τ, split every long clause, ask D. 

 ### One leaf 

### `StLeaf`

 «split every long clause into clauses of 3 literals with new variables». Let x be a formula on
x₀ … xₙ₋₁ with at most B·n clauses of at most k literals. `widthP` returns (N in unary, x₃) with: at
most 3 literals per clause, variables below N, no clause twice, N ≤ (1 + (k−3)·B)·n, and x₃ is
satisfiable exactly if x is. 

### `StSparsifyK`

 «sparsify»: for every k ≥ 3 and ε > 0 some threshold parameter τ makes the tree of the procedure
at width k sparsify width k: at most 2^{εn} leaves, each a formula on the same variables with at
most B·n clauses of at most k literals, and the formula is satisfied by an assignment exactly if
some leaf is. It comes from `SparsificationLemma.TreeWalk.lemSparsification_walk_k`. 

 ### The cited implication, for machines cut into steps 

### `StReduceCore`

 **The reduction is correct and fast, for EVERY procedure D.** Let k ≥ 3 and δ > 0; let the tree
with parameter τ sparsify width k with at most 2^{δn/3} leaves of at most B·n clauses; let D decide
3-SAT with an exponent δ₃ ≥ 0 such that δ₃·(1 + (k−3)·B) ≤ δ/3. Then the reduction without its
reader decides k-SAT with the exponent δ, in the sense of `DecidesW k`. (This form has no code of
formulas as words, so it serves every code and every caller.) 

### `StReduce`

 The same with the reader of the input in front: `REDUCE k τ D` decides k-SAT with the exponent δ
in the sense of `Eight.ViaGrouping.Decides`: on the code `SatK.enc k φ` of a k-CNF on n variables,
within c'·2^{δn} steps, on states of size polynomial in the length of the code. 

### `StReduceCert`

 The steps of the reduction are polynomial time if those of D are. 

### `Sat3SubexpBy`

 «3-SAT is decided within O(2^{δN}) steps, for every δ > 0», by a family of machines cut into
polynomial-time steps, one for each δ. 

### `StImplication`

 **«s_3 = 0 implies s_k = 0 for every k ≥ 3», for machines cut into steps**: for EVERY family Ds
of procedures for 3-SAT, one for each exponent δ₃ > 0, and for every k ≥ 3 and δ > 0, the reduction
run on ONE MEMBER OF THAT FAMILY, `REDUCE k τ (Ds δ₃)`, has polynomial-time steps and decides k-SAT
with the exponent δ. 

 ### Theorem 2 in its decision form as the procedure 

### `core3`

 The deciding form of procedure #Sat of Algorithm 1 (on the tree of the procedure behind Lemma 4,
at level ℓ, with threshold parameter τ) without its reader of the input; N is not looked at. 

### `StCore3Eq`

 The machine of Theorem 2 is the reader of the input followed by `core3`. 

### `StCore3`

 **«Theorem 2 gives s_3 = 0»**, for the machine of Theorem 2 in its decision form without its
reader: for every δ > 0 there are ℓ and τ such that `core3 ℓ τ` has polynomial-time steps and
decides 3-SAT with the exponent δ. It comes from the tied form of Theorem 2,
`ThreeSatPrinted.algPseudocode_decides_viaC`. 

### `SATsplit`

 k-SAT by the reduction to the algorithm of Theorem 2: τ is the threshold parameter of the tree
at width k; ℓ₃ and τ₃ are the level and the threshold parameter of the algorithm for 3-SAT. 

### `StSATsplit`

 **k-SAT with the machine named.** For every k ≥ 3 and δ > 0 there are τ, ℓ₃, τ₃ such that
`SATsplit k τ ℓ₃ τ₃` has polynomial-time steps and decides k-SAT with the exponent δ. (It holds at k =
3 too, where the reduction sparsifies once more in front of the algorithm of Theorem 2; the end
theorem takes s_3 = 0 from Theorem 2 directly, as the paper does, and uses this statement for k > 3.) 

### `StTiedTM`

 **Tied to the machine, on Mathlib's Turing machines.** For every k ≥ 3 and δ > 0 there are τ,
ℓ₃, τ₃ such that (1) `SATsplit k τ ℓ₃ τ₃` ITSELF has polynomial-time steps and decides k-SAT with
the exponent δ; (2) a Turing machine M with finite alphabets simulates it with polynomial overhead
(`Simulates`);
(3) M decides k-SAT within ⌊c·2^{δn}⌋ steps. (Without (1), a machine that runs the named machine and
    another one side by side would meet (2) and (3).) 

### `StTiedThreeTM`

 **«Theorem 2 gives s_3 = 0», tied to the machine of Theorem 2 in its decision form.** For every
δ > 0 there are ℓ, τ such that (1) `ThreeSatPrinted.SATCp ℓ τ` (the deciding form of procedure #Sat
of Algorithm 1, with its own reader) ITSELF has polynomial-time steps and decides 3-SAT with the
exponent δ; (2) a Turing machine M with finite alphabets simulates it with polynomial overhead; (3)
M decides 3-SAT within ⌊c·2^{δn}⌋ steps. (`SatK.enc 3 φ` is `Sat3.enc φ` by definition.) It comes
from `ThreeSatPrinted.algPseudocode_decides_viaC`. 

### `ThreeSatStatement`

 The end theorem has the statement `PaperSentences.CorEth` of PaperSentencesStatement.lean. For k >
3 its proof uses `StTiedTM`; at k = 3 it uses `StTiedThreeTM`, as the paper does («Theorem 2 gives
s_3 = 0»); then the generic `SatK.sTM_eq_zero_of`.
The end theorem is proved from the two tied statements `StTiedTM` and `StTiedThreeTM` taken as
HYPOTHESES; besides them its proof uses only lemmas that say nothing about a particular machine
(such as `SatK.sTM_eq_zero_of`), so that what the end theorem says about machines can only come from
the hypotheses. 

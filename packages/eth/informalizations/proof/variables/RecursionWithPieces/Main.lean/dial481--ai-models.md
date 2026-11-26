---
{
  "module": "proof/variables/RecursionWithPieces/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionWithPieces/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionWithPieces/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The end theorems for the function for Theorem 1 on the recursion of Appendix A with the pieces of Appendix B

**What is proved.**
* `RecursionWithPieces.tiedAt_of`, and in the form of a statement of
  proof/variables/RecursionWithPieces/Defs.lean
  `RecursionWithPieces.tiedEvery : StepSparsify.Serves Θ Lc → TiedEvery Θ`: for thresholds Θ that
  serve and for all (c, P₀, A, val) that are the pieces of Appendix B
  (`GeneralPieces.Tied.IsPiecesB`), the seven statements of
  `TiedAt Θ c P₀ A val`.
* `RecursionWithPieces.tiedAll : StepSparsify.Serves Θ Lc → TiedAll Θ`: with the theorem on pieces
  with ρ = 1/√2 (`AppRunningTime.thmHalfPieces`), which says that such c, P₀, A, val exist.
* `RecursionWithPieces.tiedAllCal : TiedAllCal`: this for `StepSparsify.thCal`, the thresholds θ_0 =
  2, θ_c = α·β_c, which we take to be Calabro's (the paper does not print them, and they were not
  checked against Calabro's dissertation), with α = ⌈2(k−1)²ε⁻¹⌈log₂(32(k−1)²/ε)⌉⌉, for max(k, 3) in
  place of k and ε = 2^(−s);
  these thresholds serve by `StepSparsify.servesCal`.
* A corollary of `tiedAllCal` that names no function: `SatM.targetUniform_all`. By its statement it
  shows nothing about the route; `tiedAllCal` does.

**How the pieces are put together.**
* Appendix B: `AppRunningTime.thmHalfPieces` gives the pieces. Appendix A:
  `GeneralPieces.par_of_isPieces` («we may and do assume»), `GeneralPieces.seq_of_pick` (the
  recursion on the schedule of display (40) is a solver with a sequence of levels; every step by
  case (ii) of the
  lemma on groupings with explicit cost), `GeneralPieces.thmRunningTime_b_tied`,
  `GeneralPieces.thmRunningTime_c_m_tied` (parts (b) and (c), first sentence).
* Three statements are proved in proof/rates/GeneralPieces. Each is a hypothesis of the step that
  uses it, and each is about the top levels, where a network on 3K⁸ nodes is rebalanced to K nodes
  and handed to the solver for cliques. The
  paper does this by case (i) of the lemma on groupings with explicit cost; and so do the proofs
  used here (proof/rates/GeneralPieces/Top/CaseI.lean).
  1. `ClauseBound.Alg.StValS` (the solver returns the value of any network; Step 4 of Appendix D;
     hypothesis of `VariableBound.Net.Ev.stEvD`): here `GeneralPieces.Top.stValS2`.
  2. `ClauseBound.Alg.StCountG` (the same for the network of a k-CNF, in the algorithm for the bound
     in m; hypothesis of `ClauseBound.Alg.TopVal.stCorrectM`): here `GeneralPieces.Top.stCountG2`.
  3. `ClauseBound.Alg.StTopArith` (the exponent of the algorithm for the bound in m; hypothesis of
     `ClauseBound.Both.TimeM.stTimeM`): here `GeneralPieces.TopDisplay.stTopArith2`, through the
     display in the proof of Theorem A(c) (the bound on the logarithm of the number of operations).
  So the theorems from these three up to the merged function (`evAB`, `evXFAB`, `countAB`,
  `correctDGAB`, `correctBDGAB`, `algAB`) are proved here.
* Steps 1 to 3 (Lemmas 12 and 13, the search, the networks), the walk with the thresholds Θ, the
  certificates of polynomial time, the merge of the exponents and the arithmetic of Steps 4 to 6 are
  those of proof/variables/VariableBound, proof/sparsification/StepSparsify and
  proof/variables/SparsifyThenCount.
* Step 6 for this solver: `master_of_isPiecesB` (proof/variables/RecursionWithPieces/Master.lean).
  The padding machine: `VariableBound.tied_of_alg`. The plan is used:
  `SparsifyThenCount.stPlanUsed`, `SparsifyThenCount.stRateZero`.

**What it does not say.** What the module comment of proof/variables/RecursionWithPieces/Defs.lean
lists. 

 ### Step 4 through case (i) of the lemma on groupings with explicit cost, and what rests on it 

### `evAB`

 Steps 3 and 4: one evaluation is the right side of the display of Step 1 of Appendix D that
gives X(𝓛) and F(𝓛) modulo powers of 2, under the hypotheses of `VariableBound.Net.StEvD`. The value
of each network comes from the solver by case (i) of the lemma on groupings with explicit cost
(`GeneralPieces.Top.stValS2`). 

### `evXFAB`

 The programs compute X(𝓛), and F(𝓛) if X(𝓛) = 0, under the hypotheses of
`VariableBound.Net.StEvXF`; from `evAB`. 

### `countAB`

 Steps 1 to 4: the count of one sparse formula is right (`VariableBound.StCountD`); from
`evXFAB`. 

### `correctDGAB`

 For thresholds that serve and every polynomial-time solver with a sequence of levels, the
function `ADG Θ` for the bound in n is right on every k-CNF, for every k ≥ 1 and every n, when the
pad has length at least 2^(eD …);
from `countAB`. 

### `correctBDGAB`

 For thresholds that serve and every polynomial-time solver with a sequence of levels, the merged
function `ABDG Θ` is right on every k-CNF, for every k ≥ 1 and every n, when the pad has length at
least 2^(eBD …); from
`correctDGAB`, with the network of the formula in the algorithm for the bound in m rebalanced by
case (i) (`GeneralPieces.Top.stCountG2`). 

### `algAB`

 For thresholds Θ that serve (with the bound Lc) and every solver with a sequence of levels,
under the hypotheses of `VariableBound.StEndS`: the merged function `ABDG Θ` and the exponent
function `eBD` are an algorithm for the two rates; from
`correctBDGAB`, with the exponent of the algorithm for the bound in m bounded through the display in
the proof of Theorem A(c) (the bound on the logarithm of the number of operations)
(`GeneralPieces.TopDisplay.stTopArith2`). 

 ### The end theorems 

### `tiedAt_of`

 For thresholds Θ that serve (with the bound Lc) and (c, P₀, A, val) that are the pieces of
Appendix B: the seven statements of `TiedAt`. 

### `tiedEvery`

 For thresholds Θ that serve (with the bound Lc): `TiedEvery Θ`, the seven statements of `TiedAt`
for all (c, P₀, A, val) that are the pieces of Appendix B. This is `tiedAt_of` in the form of a
statement of proof/variables/RecursionWithPieces/Defs.lean. 

### `tiedAll_of_tiedEvery`

 `TiedEvery Θ` and the theorem on pieces with ρ = 1/√2, both hypotheses, give `TiedAll Θ`. 

### `tiedAll`

 For thresholds Θ that serve (with the bound Lc): `TiedAll Θ`. The constant c and the programs
for the pieces are those of `AppRunningTime.thmHalfPieces`; the statement does not name them. 

### `tiedAllCal`

 **The end theorem, tied to its function.** There are a constant c and programs (P₀, val) for the
pieces of Appendix B such that: the recursion of Appendix A on them, on the schedule of display (40)
with the least x₀ of the theorem on the
general recursion, satisfies parts (b) and (c), first sentence, of that theorem; the function
`fnAll StepSparsify.thCal`, which sparsifies with the thresholds `StepSparsify.thCal`
(proof/variables/RecursionWithPieces/Defs.lean says what they are), counts each output by Steps 1 to
4 of Appendix D (`VariableBound.countD`) on that recursion,
with the level chosen by the named program `pickAB`, and is merged with the algorithm for the bound
in m on the same recursion, is with the exponent function `expAll` an algorithm for the rates of
Theorem 1; one machine puts out its value
on every input, with the pad of 2^(expAll x) units, and counts within the three bounds; a second
machine does the same for «some bit is 1»; and for every width and all large n the plan is used. The
statement fixes what the machines put out
and a bound on their steps, not the steps themselves; it names the algorithm and does not force the
argument by which the groupings exist, nor the way in which a network at the top level is handed to
the solver. The constant c and the programs are existentially quantified. What differs from the
printed text is listed in
proof/variables/RecursionWithPieces/Defs.lean. 

### `targetUniform_all`

 A corollary of `RecursionWithPieces.tiedAllCal`. One machine and one constant for all k ≥ 1: #k-SAT
on n ≥ 1 variables in time 2^{O(k²·n·log log n/√(log n))}; with m ≥ 1 clauses in which all variables
occur, in time 2^{O(k·m/√(log m))}; and, on n ≥ 1
variables that all occur, in time 2^{O(min of the two exponents)}. The statement names none of the
objects of proof/variables/RecursionWithPieces. 

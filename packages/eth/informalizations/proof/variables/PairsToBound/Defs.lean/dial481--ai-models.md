---
{
  "module": "proof/variables/PairsToBound/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (b) from Theorem D (a): definitions and statements

**The text.** Theorem D (b): «The pairs (K_ℓ, e_ℓ) of (40), for the pieces of Appendix B, satisfy
this hypothesis, and e_ℓ = Θ((log K_ℓ)^(−1/2)). So there are a deterministic algorithm and an
absolute constant C such that, for all integers k ≥ 1 and n ≥ 4, the algorithm computes the number
of
satisfying assignments of a k-CNF on n variables in time 2^{C·k²·n·log log n/√(log n)}.» Step 6 of
the proof, sentence by sentence:
(1) «By Theorem B, Theorem A applies with ρ = 1/√2 and α′ = 1/2.» (2) «That its pairs satisfy the
    hypothesis of Theorem D (a) is checked in the proof of Theorem A (c).» (3) «By Theorem A (a) and
    its proof, ½ρ^ℓ ≤ e_ℓ ≤ 0.85ρ^ℓ and x₀2^ℓ ≤ log K_ℓ ≤ (3x₀+6)2^ℓ, so e_ℓ = Θ((log K_ℓ)^(−1/2)).»
(4) «Here the constants of the hypothesis are absolute, because the constant c of Theorem B is.» (5)
    «So for n ≥ K₀^17 and 3 ≤ k ≤ (log n)^(1/4) the algorithm of Theorem D (a) takes time
    2^{O(k²·n·log log n/√(log n))} with an absolute constant.» (6) «As in Step 5, k is the largest
    number of literals in a clause, or 3 if that is
larger, which multiplies k² by at most 9.» (7) «In the other cases, that is, if n < K₀^17 or this k
exceeds (log n)^(1/4), the algorithm tries all assignments; as there are fewer than (2n+1)^k ≤
n^(2k) clauses, this takes time 2^n·n^{O(k)}, reading the input included.»
(8) «It is within the bound: log n ≤ n/√(log n) ≤ n·log log n/√(log n) for n ≥ 4, so k·log n ≤
    k²·n·log log n/√(log n); if k > (log n)^(1/4), then k²·n·log log n/√(log n) ≥ n·log log n ≥ n;
    and if n < K₀^17, then n·log log n/√(log n) ≥ n/√(17·log K₀).»

**Elsewhere.** `MainTheoremForms.ThmVariablesB` also follows from the joining theorem
(`RecursionWithPieces.tiedAllCal`), which proves Step 6 for a named function directly.

**What is stated here.**
* `ThePairsSatisfyTheHypothesis`: sentences (1), (2), (4). For ALL pieces with parameters (1/√2, c),
  the named solver `RecursionWithPieces.solverAB` (the recursion of Appendix A on them) has a
  sequence of levels in the sense of the hypothesis of `MainTheoremForms.ThmVariablesA`, with K_ℓ
  and e_ℓ the numbers of display (40) at ρ = 1/√2 and x₀ = `GeneralPieces.x₀Of c`, the level is
  picked by the named program `RecursionWithPieces.pickAB`, the solver is polynomial-time, a number
  in [e_ℓ, 2e_ℓ] is computed, and the constants depend on c alone (sentence (4)).
* `ThetaOfThePairs`: sentence (3), its four inequalities and the two-sided bound with explicit
  constants.
* `MainRegimeBound`: sentence (5), for EVERY machine with the conclusion of (a).
* `widthOr3`, `RewritesAtWidthOr3`, `TestsTheMainRegime`: sentences (6), (7): the front end and the
  test of the algorithm of Step 6.
* `TriesAllWithin Mb c`, `ExhaustiveMachineExists`: sentence (7): a machine that counts within
  2^{c·n}·n^{c·k} steps.
* `FallBackIsWithinTheBound`: sentence (8), the printed inequalities.
* `EveryChoiceMeetsThmVariablesB` (the main statement): for EVERY solver with a sequence of levels
  with e_ℓ ≤ a/√(log K_ℓ), EVERY machine M with the conclusion of (a) for it, and EVERY machine Mb
  that tries all assignments within 2^{c·n}·n^{c·k} steps: EVERY machine N that chooses between M
  (on the code rewritten at this k) and Mb by the printed test meets the bound of (b).
* `ThmVariablesBFromThmVariablesA`: existence and the main statement in one.
  `ThmVariablesAImpliesThmVariablesB`: the implication between the propositions.

**What differs from the text.** The hypothesis of (a) is Lean's (cost as the length of a padding
string; see proof/variables/VariableBound/Printed/ThmVariablesADefs.lean). The choice costs a power
q, and exhaustive counting on Mathlib's machine takes 2^{c·n}·n^{c·k} steps where the text has
2^n·n^{O(k)} operations; both go into C. K₀ depends on the pieces, which are arbitrary, so the test
has K₀ as a parameter. 

 ### Sentences (1) to (4): the pairs 

### `NumberBetween`

 «… a number in [e_ℓ, 2e_ℓ] can be computed from ℓ in time polynomial in K_ℓ» (Theorem D (a),
hypothesis). `num` is polynomial-time in (ℓ in unary, K_ℓ in unary) and returns the numerator and
the denominator of a number in [e_ℓ, 2e_ℓ]. 

### `TheRecursionHasLevels`

 «That its pairs satisfy the hypothesis of Theorem D (a) is checked in the proof of Theorem A
(c)»; there: «Its hypothesis holds by (a) and (b), with the larger of C₀ and 10». The general form,
for every ρ and x₀ of Theorem A: for every c there is a C₀, which depends on c alone, such that for
ALL pieces with parameters (ρ, c) and every x₀ ≥ 18 with 2^x₀ ≥ c + 5 the named solver, the
recursion of Theorem A (b) on these pieces, is polynomial-time and has a sequence Q of levels in the
sense of the hypothesis of Theorem D (a) for the numbers K_ℓ, e_ℓ of display (40), with the constant
C₀, and the level is picked by the named program `ClauseBound.Gen.Pick.pick`. 

### `fractionHalf`

 The fraction for ρ = 1/√2: 2^(−ℓ/2) for even ℓ and (7/5)·2^(−(ℓ+1)/2) for odd ℓ, a number
between 0.85ρ^ℓ and ρ^ℓ (`GeneralPieces.Between.num`, `den`). It does not look at K_ℓ. 

### `ThePairsSatisfyTheHypothesis`

 «The pairs (K_ℓ, e_ℓ) of (40), for the pieces of Appendix B, satisfy this hypothesis»; «Here the
constants of the hypothesis are absolute, because the constant c of Theorem B is.» For every c there
are constants C₀ and Cp, which depend on c alone, such that for ALL P₀, A, val that are pieces with
parameters (1/√2, c) as Appendix A defines them (those of
Appendix B are such pieces) there is a sequence Q of levels of the solver
`RecursionWithPieces.solverAB P₀ val c`, the recursion of Appendix A on them, for the numbers e_ℓ =
`Levels.Gen.e (1/√2) x₀ ℓ`, x₀ = `GeneralPieces.x₀Of c` (the least integer with x₀ ≥ 18 and 2^x₀ ≥ c + 5),
with the constant C₀, such that: the solver is polynomial-time; K at the ℓ-th index is K_ℓ =
`Levels.Gen.K x₀ ℓ`; the level is
picked by `RecursionWithPieces.pickAB P₀ val c`; `fractionHalf` computes a number in [e_ℓ, 2e_ℓ],
the printed clause; and ℓ ↦ ℓ + 1 is a precision with the constant Cp.
The fields of Q are the rest of the hypothesis of Theorem D (a): K_ℓ ≥ 2, K_ℓ < K_(ℓ+1) ≤ K_ℓ^C₀,
(log K_ℓ)^(−C₀) ≤ e_ℓ ≤ 1, the solver is right when the padding string has 2^need units, and need ≤
e_ℓK_ℓ²λ + C₀K_ℓ²·log(K_ℓ(λ+B)).
The LAST clause is not the paper's: it is what `MainTheoremForms.ThmVariablesA`, Lean's statement of
Theorem D (a), takes in place of the number in [e_ℓ, 2e_ℓ]. With s = ℓ + 1 the ε = 2^(−s) of that
form is about e_ℓ², not between e_ℓ and 2e_ℓ; `MainTheoremForms.Precision` allows this because it
only asks 2^(−s) ≤ e_ℓ and 2^s ≤ (2/e_ℓ)^Cp. 

### `ThetaOfThePairs`

 «By Theorem A (a) and its proof, ½ρ^ℓ ≤ e_ℓ ≤ 0.85ρ^ℓ and x₀2^ℓ ≤ log K_ℓ ≤ (3x₀+6)2^ℓ, so e_ℓ =
Θ((log K_ℓ)^(−1/2)).» For ρ = 1/√2, every x₀ ≥ 18 and every ℓ: the four inequalities, and
½·√x₀/√(log K_ℓ) ≤ e_ℓ ≤ 0.85·√(3x₀+6)/√(log K_ℓ). 

 ### Sentence (5): the main regime 

### `MainRegimeBound`

 «So for n ≥ K₀^17 and 3 ≤ k ≤ (log n)^(1/4) the algorithm of Theorem D (a) takes time
2^{O(k²·n·log log n/√(log n))}». For every solver S with a sequence Q of levels and every natural
number a with e_ℓ ≤ a/√(log K_ℓ) for all ℓ, EVERY machine M and constant C′ with the conclusion of
Theorem D (a) (`MainTheoremForms.ThmVariablesAFor`): there is a C such
that for all n ≥ K₀^17, all k with 3 ≤ k ≤ (log n)^(1/4) and every k-CNF φ on n variables the same M
counts the satisfying assignments of φ within 2^{C·k²·n·log log n/√(log n)} steps. 

 ### Sentences (6) and (7): the algorithm of Step 6 

### `widthOr3`

 «k is the largest number of literals in a clause, or 3 if that is larger». 

### `WidthOr3Stmt`

 φ is a k-CNF for k = `widthOr3 φ` if it has no clause twice; this k is at least 3; and it is at
most max(k, 3) for every k for which φ is a k-CNF, «which multiplies k² by at most 9». 

### `TheBoundIncreasesWithTheWidth`

 «the bound increases with k» (Step 5): for n ≥ 4 and k ≤ k′ the time 2^{C·k²·n·log log n/√(log
n)} at k is at most that at k′; for 3 ≤ k ≤ k′ and 0 < e ≤ 1 the same holds of
2^{C·k²·e·n·log(k/e)}. 

### `RewritesAtWidthOr3`

 `pre` maps the code of (k, φ) to the code of (`widthOr3 φ`, φ), for every k ≥ 1 and every k-CNF
φ. 

### `TestsTheMainRegime`

 The printed test: on the code of (k, φ), k ≥ 1, φ a k-CNF on n variables, `test` is true if and
only if n ≥ K₀^17 and this k, `widthOr3 φ`, is at most (log n)^(1/4). 

### `FrontEndAndTestExist`

 For every K₀ there are a polynomial-time front end and a polynomial-time test of this kind. 

### `TriesAllWithin`

 «… the algorithm tries all assignments; … this takes time 2^n·n^{O(k)}, reading the input
included.» Mb, started on the code of (k, φ), for k ≥ 1, n ≥ 2 and a k-CNF φ on n variables, puts
out the number of satisfying assignments within 2^{c·n}·n^{c·k} steps. 

### `Computes`

 On every bit string x the machine M puts out f (x, padding string of 2^(e x) units) within
q·(|x| + 2^(e x) + 1)^q steps. 

### `exhaust`

 Exhaustive counting as a function of (input, padding string): how many numbers below 2ⁿ, cut off
at the length of the padding string, code a satisfying assignment of the formula written in the
input (`UniformInK.bruteU`), in n + 1 bits. 

### `EveryExhaustiveMachineTriesAll`

 EVERY machine that computes exhaustive counting with a padding string of 2ⁿ units tries all
assignments within 2^{c·n}·n^{c·k} steps, for some c. 

### `ExhaustiveMachineExists`

 There is such a machine, and it is tied to exhaustive counting: on EVERY bit string x it
computes `exhaust` with a padding string of 2ⁿ units, n the number of variables written in x. 

### `ClauseCountPowStmt`

 «as there are fewer than (2n+1)^k ≤ n^(2k) clauses»: (2n+1)^k ≤ n^(2k) for n ≥ 3; that a k-CNF
has at most (2n+1)^k clauses is `MainTheoremForms.ClauseCountStmt`. 

 ### Sentence (8) 

### `FallBackIsWithinTheBound`

 «It is within the bound: log n ≤ n/√(log n) ≤ n·log log n/√(log n) for n ≥ 4, so k·log n ≤
k²·n·log log n/√(log n); if k > (log n)^(1/4), then k²·n·log log n/√(log n) ≥ n·log log n ≥ n; and
if n < K₀^17, then n·log log n/√(log n) ≥ n/√(17·log K₀).» 

 ### The conclusion of (b) 

### `EveryChoiceMeetsThmVariablesB`

 **The main statement.** Let S be a solver with a sequence Q of levels and e_ℓ ≤ a/√(log K_ℓ) for
all ℓ; let M with C′ have the conclusion of Theorem D (a) for S and Q; let Mb with c try all
assignments; let `pre` rewrite the code at k = `widthOr3 φ` and `test` be the printed test with K₀ =
K at the level 0. All of these are arbitrary.
Then EVERY machine N that chooses, by `test`, between M behind `pre` and Mb on the input as it is,
for whatever q, meets the bound of Theorem D (b) with some constant C: for all k ≥ 1, n ≥ 4 and
every k-CNF on n variables, within 2^{C·k²·n·log log n/√(log n)} steps. 

### `ThmVariablesBFromThmVariablesA`

 Existence and the main statement in one, under the hypotheses of `EveryChoiceMeetsThmVariablesB`
on S, Q, a, M, C′, with the alphabets of M finite: (1) there are Mb, c, `pre`, `test`, N, q as
there, with `pre` and `test` polynomial-time and the alphabets of Mb and N finite, where Mb computes
the named function `exhaust` and N carries out the named computation
`TwoMachines.choose` on codings of M and Mb; (2) every such N meets the bound of Theorem D (b). 

### `ThmVariablesAImpliesThmVariablesB`

 If Theorem D (a) holds (`MainTheoremForms.ThmVariablesA`) and Theorem B holds
(`AppRunningTime.ThmHalfPieces`: the functions of Appendix B are pieces with parameters (1/√2, c),
for some c), then Theorem D (b) holds. The route is in `ThePairsSatisfyTheHypothesis`,
`ThetaOfThePairs` and `ThmVariablesBFromThmVariablesA`. 

---
{
  "module": "proof/maintheorem/NamesInOrder/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The Main Theorem when the variables are x₀ … x_(n−1) and each occurs: definitions and statements

**The text.** The paper states at the head of Section 2: «The variables of a formula on n variables
are x_1,…,x_n; a formula in which n variables occur, as in the Main Theorem, is one on n variables
each of which occurs in some clause.» With this convention Theorem 1, the first sentence of Theorem
A (c) and Corollary 11 add no polynomial in the length of the formula to their bounds,
and the proof of Corollary 11 renames nothing. The general case: for a formula on N ≥ n variables of
which n occur, renaming these to x_1,…,x_n takes time polynomial in the length of the formula, and
the number of satisfying assignments of all N variables is 2^{N−n} times the number computed here.
The bodies of these statements are in `MainTheoremFormsStatement.lean`:
`MainTheoremForms.MainTheoremFor M C`: for every k ≥ 1 and every k-CNF φ on x₀ … x_(n−1) with m ≥ 2
clauses, n ≥ 4, in which every variable occurs, M, started on 1ᵏ 0 1ⁿ 0 and the clauses
(`SatM.enc k φ`), puts out the number of satisfying assignments within 2^{C·min{km/√(log m),
k²·n·log log n/√(log n)}} steps, rounded down, with
nothing added; `MainTheoremForms.CorMinFor M C`: the same with the minimum of the two powers of 2.

**Why this statement.** `MainTheoremForms.MainTheoremAllOccur` says only that some machine has this
bound. Here, as in proof/maintheorem/MainRoute, the bound is stated for EVERY machine that is made
in the way of the proof of Corollary 11. As the names are x₀ … x_(n−1), nothing has to be renamed:
the machine with the bound in m and the machine with the bound of Theorem D (b) both take the input
as it is, and are run in alternation on it.

**What is stated here.**
* The inequalities by which the polynomial goes: `VariablesAreFew` (n ≤ km, as every variable
  occurs), the number of clauses (`MainTheoremForms.ClauseCountStmt`: m ≤ (2n+1)^k, as no clause is
  repeated), `CodeIsShort`, `PolynomialIsBelowTheBoundInM`, `PolynomialIsBelowTheBoundInN`,
  `PolynomialIsBelowTheBound`, `AlternationCostGoesIntoC`.
* `MeetsBoundInMAlone`: the first sentence of Theorem A (c), at α′ = 1/2.
  `BoundInMWithoutThePolynomial`: every machine that meets the bound in m with a polynomial added
  (`MinOfBounds.MeetsBoundInM`) meets it with nothing added. `BoundInMHolds`: some machine with
  finite alphabets has the bound.
* `EveryDirectAlternationMeetsTheBound`, the main statement: for EVERY machine M₁ with the bound in
  m, nothing added, and EVERY machine M₂ with the bound of Theorem D (b), EVERY machine that runs
  the two in alternation on the input as it is has `MainTheoremForms.CorMinFor` and
  `MainTheoremForms.MainTheoremFor`. That the two are the same, «This is the Main Theorem», is
  `MainTheoremForms.CorMinIsMainTheoremStmt`.
* `AssembledDirectly`, `BuiltDirectly`: as `MainRoute.AssembledAsPrinted` and
  `MainRoute.BuiltAsPrinted`, without the front end that renames.
* `OnEverySolver`: the chain for every algorithm for cliques with levels and e_ℓ = O((log
  K_ℓ)^(−1/2)); `ForAllPieces`: for the recursion of Appendix A on the pieces of Appendix B;
  `MainTheoremHolds`: `MainTheoremForms.MainTheoremAllOccur`; `CorMinHolds`:
  `MainTheoremForms.CorMinAllOccur`.
* `GeneralFormFollows`, the general case, first half: for EVERY machine with
  `MainTheoremForms.MainTheoremFor`, EVERY machine that puts a front end that renames the variables
  that occur before it meets, for any names, the bound of the Main Theorem with a polynomial in the
  length of the formula added (`MinOfBounds.MeetsMinBound`), a form that the paper does not state as
  a theorem. `GeneralFormFollowsAsPropositions`: so `MainTheoremForms.MainTheoremAllOccur` gives
  `MainTheoremForms.MainTheoremCompact`.

**What differs from the text.** What proof/maintheorem/MainRoute/Defs.lean lists, but for the
renaming. The variables are x₀ … x_(n−1) where the paper has x_1, …, x_n. The width k is declared in
the input and n is written in unary. 

 ### The inequalities by which the polynomial goes 

### `VariablesAreFew`

 As every variable occurs and a clause has at most k literals, n ≤ k·m. 

### `CodeIsShort`

 The length of the input 1ᵏ 0 1ⁿ 0 and the clauses: k + n + 2 + m·k·(⌊log₂ (2n)⌋ + 1) bits; this
is at most 6·(km)² if every variable occurs, and at most k·(2n+1)^(k+3) as no clause is repeated (k
≥ 1, n ≥ 1). 

### `PolynomialIsBelowTheBoundInM`

 A polynomial in km is below the bound in m: for every c there is a c′ such that c·(6(km)²)^c ≤
2^{c′·km/√(log m)}, rounded down, for all k ≥ 1 and m ≥ 2. 

### `PolynomialIsBelowTheBoundInN`

 A power of k·(2n+1)^(k+3) is below the bound in n: for every c there is a c′ such that
c·(k·(2n+1)^(k+3))^c ≤ 2^{c′·k²·n·log log n/√(log n)}, rounded down, for all k ≥ 1 and n ≥ 4. 

### `PolynomialIsBelowTheBound`

 So a polynomial in the length of the input is below the bound of the Main Theorem: for every c
there is a c′ such that, for every k ≥ 1 and every k-CNF φ on n ≥ 4 variables, each of which occurs,
with m ≥ 2 clauses, none repeated: c·(length of the input)^c ≤ 2^{c′·min{km/√(log m), k²·n·log log
n/√(log n)}}, rounded down. 

### `AlternationCostGoesIntoC`

 The cost of the alternation goes into C: for all C₁, C₂ and q there is a C such that, for the
same k and φ, with L the length of the input: q·(min(2^{C₁·km/√(log m)}, 2^{C₂·k²·n·log log n/√(log
n)}) + L + 1)^q ≤ 2^{C·min{km/√(log m), k²·n·log log n/√(log n)}}, all powers of 2 rounded down as
in the statements. 

 ### The first sentence of Theorem A (c) and Corollary 11, with nothing added 

### `MeetsBoundInMAlone`

 The first sentence of Theorem A (c), at α′ = 1/2, for the machine M and the constant C: for
every k ≥ 1 and every k-CNF φ on x₀ … x_(n−1) with m ≥ 2 clauses in which every variable occurs, M
puts out the number of satisfying assignments within 2^{C·km/√(log m)} steps, rounded down. 

### `BoundInMWithoutThePolynomial`

 EVERY machine that meets the bound in m with a polynomial in the length of the input added meets
it with nothing added, with another constant. 

### `EveryDirectAlternationMeetsTheBound`

 **The main statement**: Corollary 11 from the first sentence of Theorem A (c) and Theorem D (b).
Let M₁ with C₁ meet the bound in m, with nothing added, and M₂ with C₂ the bound of Theorem D (b);
M₁, C₁, M₂, C₂ are arbitrary. Then EVERY machine N that runs M₁ and M₂ in alternation on the input
as it is, for whatever q, has the bound of Corollary 11 (`MainTheoremForms.CorMinFor`), which is
that of the Main
Theorem (`MainTheoremForms.MainTheoremFor`), with some constant C. 

 ### The chain 

### `AssembledDirectly`

 The machine N is assembled as the proof of Corollary 11 says when nothing has to be renamed:
there are a machine M₂ made as Step 6 of Appendix D says (`MainRoute.ChosenAsPrinted`) and a machine
M₁ that computes fm with the exponent em such that N runs M₁ and M₂ in alternation on the input as
it is. 

### `BuiltDirectly`

 The same with everything that “assembled” should mean for a machine that is exhibited: all five
machines have finite alphabets; the front end of Step 6 of Appendix D and its test are
polynomial-time; M₂ carries out the named computation `TwoMachines.choose` on codings of Ma and Mb,
and N the named computation `TwoMachines.alt` («one operation of each at a time») on codings of M₁
and M₂. 

### `BuiltIsAssembledDirectly`

 A machine that is built directly is assembled directly and has finite alphabets. 

### `OnEverySolver`

 **The chain for every solver.** Let S be a polynomial-time solver for cliques with a sequence Q
of levels and let `num` compute a number in [e_ℓ, 2e_ℓ] (the hypothesis of Theorem D (a)). There is
an n₀, chosen after S, Q and `num`, such that, if e_ℓ ≤ a/√(log K_ℓ) for all ℓ, for a natural number
a, then for every n₁ ≥ n₀: EVERY machine that computes the function for the bound in m on S
(`ClauseBound.Alg.AM`) meets the bound in m with nothing added; EVERY machine assembled directly
from machines that compute the function of Steps 1 to 5 of Appendix D on S
(`RecursionToBound.count`), exhaustive counting, and the function for the bound in m on S has the
bound of Corollary 11, which is that of the Main Theorem, with nothing added; and a machine built
directly from such machines exists. 

### `ForAllPieces`

 The chain for ALL pieces of Appendix B and all large n₁: EVERY machine that computes the
function for the bound in m on the recursion of Appendix A on the pieces (`MainRoute.fnM`) meets the
bound in m with nothing added; EVERY machine assembled directly from machines that compute the two
named functions on that recursion (`MainRoute.fnN`, `MainRoute.fnM`) and exhaustive counting has the
bound of
Corollary 11, which is that of the Main Theorem, with nothing added; and a machine built directly
from such machines exists. 

### `MainTheoremHolds`

 **The Main Theorem, for the variables x₀ … x_(n−1), each of which occurs**: one machine with
finite alphabets and one constant C with `MainTheoremForms.MainTheoremFor`. It says only that some
machine has the bound; the route is in `ForAllPieces`, from which, with Theorem B, it is read off. 

### `BoundInMHolds`

 **The first sentence of Theorem A (c)**, at α′ = 1/2: one machine with finite alphabets and one
constant C with `MeetsBoundInMAlone`. It says only that some machine has the bound; the machine of
the proof computes the function for the bound in m on the recursion of Appendix A on pieces of
Appendix B (`ForAllPieces`, first clause). 

### `CorMinHolds`

 **Corollary 11, for the variables x₀ … x_(n−1), each of which occurs**: one machine with finite
alphabets and one constant C with `MainTheoremForms.CorMinFor`; read off `ForAllPieces` in the same
way. 

 ### The general case 

### `GeneralFormFollows`

 «For a formula on N ≥ n variables of which n occur, renaming these to x_1,…,x_n takes time
polynomial in the length of the formula …». For EVERY machine N with the bound of the Main Theorem
with nothing added, every front end `ren` that renames the variables that occur, and EVERY machine
N′ that runs N behind `ren` (`Wrap.Wraps N ren id N′ q`, for whatever q): N′ meets the bound of
Corollary 11 with a polynomial in the length of the code added, a form that the paper does not
state, for a k-CNF over any names x₀ … x_(V−1) in which n ≥ 4 variables occur, on the compact code
(`MinOfBounds.MeetsMinBound`), and so the same form of the bound of Theorem 1
(`Wrap.CountsCompactKCNFWithinMinBound`). 

### `GeneralFormFollowsAsPropositions`

 So the Main Theorem for the variables x₀ … x_(n−1) gives the Main Theorem for any names, on the
compact code, with a polynomial in the length of that code added. Both are theorems, so by its
statement alone this shows little; what an arbitrary machine gives is said by `GeneralFormFollows`. 

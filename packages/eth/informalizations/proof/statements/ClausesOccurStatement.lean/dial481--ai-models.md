---
{
  "module": "proof/statements/ClausesOccurStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ClausesOccurStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ClausesOccurStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The bound in the number m of clauses, for formulas over arbitrary names of the variables

Definitions and statements only (no theorem, no proof). Imports `MainTheoremFormsStatement.lean`
(formulas over arbitrary names, the compact code, «as assignments of the variables that occur») and
`AppRunningTimeStatement.lean`
(pieces with parameters (ρ, c), α' = log(1/ρ), the other parts of Theorem A).

## The sentences of the paper that are stated here

* Theorem A (c), first sentence: «One deterministic algorithm counts the satisfying assignments of a
  k-CNF with m ≥ 2 clauses in which n variables occur, as assignments of these n variables, in time
  2^{O(km/(log m)^{α'})},
  where the O depends on ρ and c but not on k.» Here a term polynomial in the length of the formula
  is added to the bound. This is `CountsFromPieces`.
* After Theorem B: «With Theorem A this gives the exponent log(1/ρ) = ½ of log m, that is, the bound
  in m of the Main Theorem.» This is `BoundInClauses`.
* Theorem A as a whole, with the first sentence of (c) in this form and the other parts as in
  `AppRunningTimeStatement.lean`: `RunningTimesFromPieces`.

## How to read it

* «One deterministic algorithm» is a Turing machine M of Mathlib (`Turing.FinTM2`) all of whose
  alphabets are finite; time is its number of steps. M and the constant C come before k, N and φ, so
  there is one machine for all
  widths, and C does not depend on k. In `CountsFromPieces` they come after ρ and c.
* φ is a formula over the names x₀ … x_(N−1), of which only some need occur; `SatK.IsKCNF k φ`: at
  most k literals in each clause, no clause written twice; m is `φ.length`.
* `MainTheoremForms.numOcc φ` is the number n of variables that occur,
  `MainTheoremForms.numSatOcc φ` the number of satisfying assignments as assignments of these n
  variables. The output has n + 1 bits, lowest first.
* The input is the compact code `MainTheoremForms.encC k φ`: 1ᵏ 0, then 1ʷ 0 with w = ⌊log₂(2N)⌋ +
  1, then k slots of w bits per clause. N is not written, names are in binary. «The length of the
  formula» is the length of this word.
  This is exact when N is one more than the largest name; for a larger N the code is longer, and the
  statement, which holds for every N, contains the case of that least N.
  The forms with `Unary` in their names take `SatM.enc k φ`, which has N in unary; they are weaker
  where names are much larger than their number.
* `MainTheoremForms.lg` is the paper's log = log₂, without any shift of its argument. The bound has
  the printed form 2^{C·…} + C·(length)^C, with no factor in front of the power; it is rounded down
  to a natural number.

## Where these statements differ from the printed sentences

* Steps of a multi-stack Turing machine in place of operations of a word RAM; the width k is
  declared in the input, in unary; lists in place of sets. These are the differences of the Main
  Theorem's statement
  (`MainTheoremFormsStatement.lean`, «Where a sentence here differs from the paper's»).
* The Main Theorem asks that n ≥ 4 variables occur. Theorem A (c) has no hypothesis on n, and
  `BoundInClauses` has none either: it is stronger than the branch in m of the Main Theorem. (Some
  variable does occur: a formula with
  m ≥ 2 clauses, none written twice, has a clause that is not empty, `SomeVariableOccursStmt`.)
* The hypothesis 1 ≤ k is redundant, for the same reason; it is kept so that the hypotheses read as
  in `MainTheoremFormsStatement.lean`.
* `AppRunningTime.ThmRunningTime.c_m` and `AppRunningTime.BoundInM` speak of formulas in which every
  variable occurs, with m ≥ 1, on the code with N in unary. The links between them and the
  statements of this file are `AllOccurOfUnaryStmt` here and
  `OccurM.EveryWrapperCounts`, `OccurM.EveryWrapperCountsUnary` in proof/rates/OccurM/TiedDefs.lean. 

 ### The bound 

### `expClauses`

 The exponent in the number m of clauses, as in Theorem A (c), k·m/(log m)^α′, with any α in
place of α′. 

### `timeClauses`

 The time 2^{C·km/(log m)^α}, rounded down. 

### `ExpHalfStmt`

 At α = ½ the exponent is that of the Main Theorem, k·m/√(log m). No hypothesis on k or m. 

 ### The sentence, for a given machine and constant, and for some machine and constant 

### `CountsFor`

 For the machine M and the constant C: for every k ≥ 1, every N and every k-CNF φ over x₀ …
x_(N−1) with m ≥ 2 clauses, M, started on the compact code of (k, φ), computes the number of
satisfying assignments of φ, as
assignments of the variables that occur in φ, within 2^{C·km/(log m)^α} + C·(length of the compact
code)^C steps. 

### `Counts`

 One deterministic algorithm counts the satisfying assignments of a k-CNF with m ≥ 2 clauses, as
assignments of the variables that occur in it, in time 2^{O(km/(log m)^α)} plus a polynomial in the
length of the formula, where
the O does not depend on k: the sentence of Theorem A (c) with a given exponent α in place of α',
and with a term polynomial in the length of the formula added to the bound. 

### `CountsUnaryFor`

 As `CountsFor`, with `SatM.enc k φ` as input, which has N in unary. 

### `CountsUnary`

 As `Counts`, with `SatM.enc k φ` as input, which has N in unary. 

### `AllOccurOfUnaryStmt`

 What the sentence gives for the formulas in which every variable occurs, for the SAME machine:
let 0 ≤ α ≤ 1 and let M, with the constant C, count as in `CountsUnaryFor α`. Then for some constant
C', for every k ≥ 1 and every k-CNF φ over
x₀ … xₙ₋₁ with m ≥ 2 clauses in which all n variables occur, M computes the number of satisfying
assignments (among all 2ⁿ) within C'·2^{C'·km/(log₂(m+2))^α} steps: the polynomial in the length of
the formula is absorbed. This is the body of
`SatM.CountInRate` for m ≥ 2 (that statement also covers m = 1, of which the printed sentence says
nothing). 

### `SomeVariableOccursStmt`

 A formula with at least two clauses, none written twice, contains a variable. 

 ### Theorem A (c), first sentence; the sentence after Theorem B; Theorem A 

### `CountsFromPieces`

 Theorem A (c), first sentence. Suppose that there are pieces with parameters (ρ, c), and let α' =
log(1/ρ). Then one machine and one constant C, which may depend on ρ and c but not on k, count as in
`Counts α'`. 

### `CountsUnaryFromPieces`

 The same with N in unary in the input. 

### `BoundInClausesFor`

 The bound in m of the Main Theorem for the machine M and the constant C: as `CountsFor`, within
2^{C·km/√(log m)} + C·(length of the compact code)^C steps, with the exponent written as in the Main
Theorem (`MainTheoremForms.expM`). 

### `BoundInClauses`

 After Theorem B: «the bound in m of the Main Theorem». One machine with finite alphabets and one
constant C with `BoundInClausesFor`. The Main Theorem's hypothesis that n ≥ 4 variables occur is not
needed for this bound and is not made. 

### `BoundInClausesIsHalfStmt`

 For every machine and every constant, the bound in m of the Main Theorem is `CountsFor` at α =
½. 

### `BoundInClausesFromStmt`

 «With Theorem A this gives …»: the step from Theorem B and the first sentence of Theorem A (c)
to the bound in m. 

### `RunningTimesFromPieces`

 Theorem A, with the first sentence of (c) in the form of `CountsFromPieces`, that is, with a
term polynomial in the length of the input added to the bound. Parts (a), (b), the second sentence
of (c) and (d) are those of `AppRunningTime.ThmRunningTime`, word for word. 

### `RunningTimesFromPieces.a`

 (a) 

### `RunningTimesFromPieces.b`

 (b); C₀ depends only on c. 

### `RunningTimesFromPieces.c_m`

 (c), first sentence, with a term polynomial in the length of the input added to the bound 

### `RunningTimesFromPieces.c_n`

 (c), second sentence, as in `AppRunningTime.ThmRunningTime`: for every fixed k. The printed
  proviso (a number between 0.85ρ^ℓ and ρ^ℓ can be computed from ℓ in time polynomial in K_ℓ) is not
  needed by the proof in this development and is not made. 

### `RunningTimesFromPieces.d`

 (d), as in `AppRunningTime.ThmRunningTime`. In this development it follows from the 3-SAT
  bound `Sat3.InRateTM` with the exponent 3/19 of log n in place of α'/10, which is the stronger
  bound, as α'/10 ≤ 1/10 < 3/19 (α' ≤ 1 since ρ ≥ ½); the printed proof of (d) is not formalized. 

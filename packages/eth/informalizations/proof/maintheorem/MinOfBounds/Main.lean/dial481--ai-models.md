---
{
  "module": "proof/maintheorem/MinOfBounds/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MinOfBounds/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MinOfBounds/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 11 from Theorem A (c) and Theorem D (b): the proofs

proof/maintheorem/MinOfBounds/Defs.lean divides the proof of Corollary 11 into five numbered
sentences. The proof here follows sentences (1) to (4); sentence (5), a second way to the same
bound, is not followed here.
* Sentence (1), the renaming of the variables that occur to 1, …, n, is in
  proof/maintheorem/MinOfBounds/Rename.lean; the printed proof of Corollary 11 does not have it.
* Sentence (3), «Both compute the same number», is `bothComputeTheSameNumber`: the two hypotheses
  are applied to the renamed formula, in which every variable occurs, which has as many clauses as φ
  and is a k-CNF on n variables.
* Sentence (2), the alternation, is `alternation_outputs`: let N run M₁ and M₂ in alternation behind
  a function that renames, with the same last step `post` after either. By the definition of
  `TwoMachines.Alternates` and by sentence (3), N puts out `post` of the number within
  q·(min(t₁, t₂) + L + 1)^q steps, where t₁ and t₂ are the two bounds and L is the length of the
  compact code.
* Sentence (4), «this constant goes into C», is `MinOfBounds.overheadGoesIntoC` of
  proof/maintheorem/MinOfBounds/Arith.lean; it needs that the code of the renamed formula is
  polynomially long (`MinOfBounds.renamedCodeIsPolynomial`).
* `everyAlternationMeetsMinBound` takes `post` to be the identity,
  `everyAlternationDecidesWithinMinBound` takes it to be “some bit is 1”.
* That a function that renames and a machine that alternates exist is
  `MinOfBounds.renamingFrontEndExists` and `TwoMachines.everyTwoMachinesCanBeAlternated`.
* The sentence that follows the proof, «This is the Main Theorem», is `minBoundIsTheMainTheorem`:
  the minimum of the two powers of 2 is 2 to the minimum of the two exponents
  (`VariableBound.Paper.timeCor_eq`). 

### `propositionsUnfold`

 The three propositions unfold to “there are a machine with finite alphabets and a constant with
this body”. 

### `boundInMSuffices`

 Every machine with the body of `AppRunningTime.BoundInM` and the constant C meets the bound in m
with the constant 3C: the factor C in front goes into the exponent (`bound_le_timeM`), and the
polynomial that is added only makes the bound larger. 

### `bothComputeTheSameNumber`

 «Both compute the same number.» The two hypotheses are applied to the renamed formula
`VariableBound.Rename.ren φ`. 

### `alternation_outputs`

 The alternation with any last step. Let `pre` rename the variables that occur, let M₁ with C₁
meet the bound in m and M₂ with C₂ the bound of Theorem D (b), and let N run M₁ and M₂ in
alternation behind `pre`, with the same function `post` after either. Then there is a constant C
such that, for every k ≥ 1 and every
k-CNF φ with m ≥ 2 clauses in which n ≥ 4 variables occur, N, started on the compact code of (k, φ),
puts out `post` of the number of satisfying assignments of φ, as assignments of these n variables,
within the bound of Corollary 11 with the constant C. 

### `everyAlternationMeetsMinBound`

 **The main statement.** Every machine that runs M₁ and M₂ in alternation behind a function that
renames the variables that occur meets the bound of Corollary 11. 

### `everyAlternationDecidesWithinMinBound`

 The same for deciding: “some bit is 1” of the number of satisfying assignments in n + 1 bits is
the bit “this number is not 0”, and φ is satisfiable if and only if this number is not 0. 

### `minBoundFromTheTwoTheorems`

 Existence, by `renamingFrontEndExists` and `TwoMachines.everyTwoMachinesCanBeAlternated`, and
the main statement. 

### `decidingFromTheTwoTheorems`

 The same for deciding; “some bit is 1” is polynomial-time (`VariableBound.Rename.anyBit_polyT`). 

### `theTwoTheoremsImplyMinBound`

 The bound in m and Theorem D (b) imply Corollary 11 on the compact code: take a machine for each
of the two, a machine that runs them in alternation behind the renaming, and the constant that the
main statement gives for it. 

### `minBoundIsTheMainTheorem`

 «This is the Main Theorem.» The two bounds are the same number, because the minimum of the two
powers of 2 is 2 to the minimum of the two exponents. 

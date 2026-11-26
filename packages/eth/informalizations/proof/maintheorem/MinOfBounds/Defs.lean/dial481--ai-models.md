---
{
  "module": "proof/maintheorem/MinOfBounds/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MinOfBounds/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MinOfBounds/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 11 from Theorem A (c) and Theorem D (b): definitions and statements

**The text** (proof of Corollary 11), five sentences; (1) is not in the printed proof of Corollary 11. (1)
Rename the variables that occur to x₁, …, xₙ (here x₀, …, xₙ₋₁). (2) «Run the algorithm of Theorem A
(c), with the pieces of Appendix B,
and the algorithm of Theorem D (b) in alternation, one operation of each at a time, and output the
result of the one that stops first.» (3) «Both compute the same number.» (4) «This multiplies the
number
of operations of the faster one by a constant; as km/√(log m) and n·log log n/√(log n) are at least
2, this constant goes into C.» (5) Or run only the one with the smaller exponent. «This is the Main
Theorem.»


**What is stated here.** The two theorems enter as hypotheses on ARBITRARY machines:
* `MeetsBoundInM M₁ C₁`: the first sentence of Theorem A (c) at α′ = 1/2 (counting the satisfying
  assignments of a k-CNF with m ≥ 2 clauses in time 2^{O(km/(log m)^α′)}, here with a polynomial in
  the length of the formula added), asked only of the formulas on x₀ … xₙ₋₁ in which every variable
  occurs, which is all that the proof needs after the renaming: on the code
  of (k, φ), for k ≥ 1 and such a k-CNF φ with m ≥ 2 clauses, M₁ puts out the number of satisfying
  assignments within 2^{C₁·km/√(log m)} + C₁·(length of the code)^C₁ steps. `BoundInMSuffices`:
  every machine with the body of `AppRunningTime.BoundInM` has it.
* `MainTheoremForms.ThmVariablesBFor M₂ C₂`: the body of `MainTheoremForms.ThmVariablesB`.
* `renamedCode k φ`, `RenamesTheVariablesThatOccur pre`: sentence (1). `pre` maps the compact code
  of (k, φ) to the code of (k, φ with every variable replaced by its position in the list of the
  variables that occur). `RenamedCodeIsTheCodeOfARenaming` says that this bit string is
  `SatM.enc k φ'` for a formula φ' on x₀ … xₙ₋₁ with the properties that the proof uses.
* `BothComputeTheSameNumber`: sentence (3).
* `EveryAlternationMeetsMinBound` (the main statement): EVERY machine N that alternates M₁ and M₂
  behind such a `pre` (`TwoMachines.Alternates`) meets the bound of Corollary 11 on the compact
  code, with some constant C. All that is known of N is that it alternates M₁ and M₂, so its speed
  can only come from the two hypotheses.
* `EveryAlternationDecidesWithinMinBound`: the same with the last step “some bit is 1”.
* `MinBoundFromTheTwoTheorems`: existence of `pre` and N, and the statement on every alternation, in
  one.
* `OverheadGoesIntoC`: sentence (4), as arithmetic.
* `TheTwoTheoremsImplyMinBound`, `MinBoundIsTheMainTheorem`: the implications between the
  propositions.

**What differs from the text.** The overhead of the alternation is a power q where the text has a
constant factor; both go into C. Sentence (5), the second way, is what
`RecursionWithPieces.tiedAllCal` follows; it is not stated here. 

 ### The two hypotheses and the conclusion, for given machines and constants 

### `timeM`

 The time 2^{C·km/√(log m)}, rounded down. 

### `MeetsBoundInM`

 The bound in m for the machine M and the constant C: for every k ≥ 1 and every k-CNF φ on x₀ …
xₙ₋₁ with m ≥ 2 clauses in which every variable occurs, M, started on `SatM.enc k φ`, puts out the
number of satisfying assignments within 2^{C·km/√(log m)} + C·(length of `SatM.enc k φ`)^C steps. 

### `BoundInMSuffices`

 Every machine with the body of `AppRunningTime.BoundInM` (= `SatM.TargetSqrt`: m ≥ 1, within
C·2^{C·km/√(log₂(m+2))} steps, with no polynomial in the length of the code added) meets the bound
in m in the form above, with some constant. 

### `MeetsMinBound`

 The body of `MainTheoremForms.CorMinCompact` for the machine N and the constant C: for every k ≥
1, every V and every k-CNF φ over x₀ … x_(V−1) with m ≥ 2 clauses in which n ≥ 4 variables occur, N,
started on the compact code of (k, φ), puts out the number of satisfying assignments, as assignments
of these n variables, within
min{2^{C·km/√(log m)}, 2^{C·k²·n·log log n/√(log n)}} + C·(length of the compact code)^C steps. 

### `DecidesWithinMinBound`

 The same for deciding: the output is one bit, which is 1 if and only if φ is satisfiable. 

### `PropositionsUnfold`

 The three propositions say that there are a machine with finite alphabets and a constant with
these bodies; this holds by unfolding the definitions. 

 ### Sentence (1): renaming 

### `renamedCode`

 The code of (k, φ with the variables that occur renamed): every variable is replaced by its
position in the list `occL` of the variables that occur, each once (`VariableBound.Rename.renF`;
`Groundwork.Decode.toN` forgets the bound on the names), and the result, a formula on n variables
where n is the length of that list, is written as `SatM.enc` writes a formula
(`VariableBound.Rename.encN`):
1ᵏ 0, then 1ⁿ 0, then k slots per clause. 

### `RenamedCodeIsTheCodeOfARenaming`

 For every k and every φ over x₀ … x_(V−1) there is a formula φ' over x₀ … xₙ₋₁, where n is the
number of variables that occur in φ, such that: `renamedCode k φ` is `SatM.enc k φ'`; φ' is φ with
every variable replaced by its position in `occL`, a list without repetition of exactly the
variables that occur; φ' has as many clauses as φ; it is a
k-CNF if φ is; every one of its n variables occurs; and its number of satisfying assignments, among
all 2ⁿ, is the number of satisfying assignments of φ as assignments of the variables that occur. 

### `RenamesTheVariablesThatOccur`

 Sentence (1): the variables that occur are renamed to x₀, …, xₙ₋₁ (the paper's x₁, …, xₙ). `pre`
maps the compact code of (k, φ) to `renamedCode k φ`, for every k ≥ 1 and every k-CNF φ. Nothing is
asked of `pre` on other bit strings. 

### `RenamingFrontEndExists`

 There is a polynomial-time function that does it. 

 ### Sentence (3) 

### `BothComputeTheSameNumber`

 «Both compute the same number.» Let M₁ meet the bound in m and M₂ the bound of Theorem D (b).
For every k ≥ 1 and every k-CNF φ with m ≥ 2 clauses in which n ≥ 4 variables occur, both machines,
started on the code of the renamed formula, put out the same bit string, the number of satisfying
assignments of φ as assignments
of the n variables that occur, in n + 1 bits: M₁ within 2^{C₁·km/√(log m)} + C₁·(length of that
code)^C₁ steps and M₂ within 2^{C₂·k²·n·log log n/√(log n)} steps. 

 ### Sentence (4) 

### `RenamedCodeIsPolynomial`

 The code of the renamed formula is at most polynomially longer than the compact code: there is a
number a with |`renamedCode k φ`| ≤ a·|`encC k φ`|^a for every k ≥ 1 and every k-CNF φ. (It writes n
in unary, and n ≤ km.) 

### `OverheadGoesIntoC`

 «… as km/√(log m) and n·log log n/√(log n) are at least 2, this constant goes into C.» For all
C₁, C₂, q and a there is a C such that for all k ≥ 1, m ≥ 2, n ≥ 4, L ≥ 1 and L₁ ≤ a·L^a:
q·(min(2^{C₁·km/√(log m)} + C₁·L₁^C₁, 2^{C₂·k²·n·log log n/√(log n)}) + L + 1)^q ≤ min{2^{C·km/√(log
m)}, 2^{C·k²·n·log log n/√(log n)}} + C·L^C, all powers of 2 rounded down as in the statements. 

 ### Sentence (2), and the corollary 

### `EveryAlternationMeetsMinBound`

 **The main statement.** Let `pre` rename the variables that occur, let M₁ with C₁ meet the bound
in m (Theorem A (c), first sentence, at α′ = 1/2) and M₂ with C₂ the bound of Theorem D (b); M₁, C₁,
M₂, C₂ are arbitrary. Then EVERY machine N that runs M₁ and M₂ in alternation behind `pre`, for
whatever q,
meets the bound of Corollary 11 with some constant C. By itself this does not say that such `pre`, N
and q exist; `RenamingFrontEndExists` and `TwoMachines.EveryTwoMachinesCanBeAlternated` do, when the
alphabets of M₁ and M₂ are finite. 

### `EveryAlternationDecidesWithinMinBound`

 The same for deciding: the last step after either machine is “some bit is 1” (`Wrap.someBit`). 

### `MinBoundFromTheTwoTheorems`

 Existence and the main statement in one. For EVERY machine M₁ with finite alphabets and every C₁
that meet the bound in m, and EVERY machine M₂ with finite alphabets and every C₂ that meet the
bound of Theorem D (b): (1) there are a polynomial-time `pre` that renames the variables that occur,
a machine N with finite
alphabets and a number q such that N runs M₁ and M₂ in alternation behind `pre`, and N carries out
the named computation `TwoMachines.alt` on codings of M₁ and M₂ («one operation of each at a time»);
and (2) for EVERY `pre` that renames the variables that occur, polynomial-time or not, and every q,
EVERY machine N that runs M₁ and M₂ in alternation behind `pre` meets the bound of Corollary 11 with
some constant C. 

### `DecidingFromTheTwoTheorems`

 The same for deciding. 

 ### ### The implications between propositions 

### `TheTwoTheoremsImplyMinBound`

 If the bound in m (`AppRunningTime.BoundInM`) and Theorem D (b)
(`MainTheoremForms.ThmVariablesB`) hold, so does Corollary 11 on the compact code. What arbitrary
machines as in the hypotheses give is said by `MinBoundFromTheTwoTheorems`. 

### `MinBoundIsTheMainTheorem`

 «This is the Main Theorem.» For every machine and every constant, the bound of Corollary 11 on
the compact code is the bound of Theorem 1 on the compact code
(`Wrap.CountsCompactKCNFWithinMinBound`, the body of `MainTheoremForms.MainTheoremCompact`). 

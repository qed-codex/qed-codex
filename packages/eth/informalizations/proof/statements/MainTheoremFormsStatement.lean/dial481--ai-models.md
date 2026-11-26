---
{
  "module": "proof/statements/MainTheoremFormsStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/MainTheoremFormsStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/MainTheoremFormsStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem 1, Corollary 11 and Theorem D (b), in the paper's wording

Definitions only (no theorem, no proof). Imports `UniformInKStatement.lean` (and through it
`FixedWidthVariableBoundStatement.lean`, `ClauseBoundStatement.lean`, `CountKSatStatement.lean`,
`KSatStatement.lean`, `ThreeSatStatement.lean`) and Mathlib.

## How to read it

* «A deterministic algorithm» is a Turing machine M of Mathlib (`Turing.FinTM2`: deterministic,
  finitely many stacks) all of whose alphabets are finite. Time is its number of steps.
* In every statement the machine M and the constant C come first, then the width k, the number n of
  variables and the formula φ. So there is ONE machine for all widths and sizes, and C does not
  depend on k.
  C is a natural number.
* A k-CNF on n variables is `φ : CNF n` with `SatK.IsKCNF k φ` (`KSatStatement.lean`): a list of
  clauses over x₀ … xₙ₋₁, at most k literals in each, no clause written twice. m is `φ.length`.
* «n variables occur» is `SatM.AllOccur φ` (`ClauseBoundStatement.lean`): every one of x₀ … xₙ₋₁
  occurs in φ, positively or negatively.
* `CountsWithin M k φ t`: M, started on `SatM.enc k φ` (1ᵏ 0, then 1ⁿ 0, then k slots per clause),
  halts after at most t steps with the number of satisfying assignments of φ, among all 2ⁿ
  assignments of
  x₀ … xₙ₋₁, in n + 1 bits, lowest bit first, as output.
* `DecidesWithinC M k φ t`: M, started on the compact code `encC k φ`, halts after at most t steps
  with one bit as output, which is 1 if and only if φ is satisfiable.
* `lg` is the paper's log: «log = log₂», real-valued, WITHOUT any shift of its argument. `expM k m` =
  k·m/√(log m) and `expN k n` = k²·n·log log n/√(log n) are the two exponents as printed.
* The bounds (`timeMin`, `timeN`, `timeCor`, `timeMin3`) have the printed form 2^{C·…}, with no
  factor in front; they are rounded down to a natural number, because steps are counted in natural
  numbers. Powers are Mathlib's `Real.rpow`.
* Theorem 1, Theorem D (b) and Corollary 11 come twice: `…For M C` says it of a given machine and
  constant, and the sentence itself says that there are such M and C. `TogetherAllOccur` says that
  ONE machine and ONE constant serve all three.
* `DecidesWithinC` (deciding) and `timeMin3` (the time for 3-CNFs) are definitions that no numbered
  sentence of the paper has.

## Where a sentence here differs from the paper's

* The paper counts operations on words in the word RAM model (Sections 2 and 3); here time is steps
  of a multi-stack Turing machine.
* The width k is part of the input, in unary. It is a declared width: at least the length of the
  longest clause; the k of the bounds is the declared one.
* The paper's k-CNF is a finite set of clauses, and a clause is a set of literals; here a formula is
  a list without repetition whose clauses are lists. So the same literals in another order are
  another clause, a literal
  may be repeated inside a clause, and the empty clause is allowed. These are more inputs than the
  paper's, and all are handled; for the same set of clauses, m is at least the paper's m.
* The hypotheses are a promise on the input: nothing is said about inputs that are not codes of such
  formulas.
* The paper's Theorem 1 and Corollary 11 speak of formulas whose n variables, named x₁ … xₙ (Section 2),
  all occur; other formulas are first renamed, in time polynomial in their length.
  `MainTheoremAllOccur` and `CorMinAllOccur` speak of formulas over x₀ … xₙ₋₁ in which all variables
  occur, and add no polynomial. `MainTheoremCompact` and `CorMinCompact` allow names x₀ … x_(N−1),
  of which n occur, and add C·(length of the input)^C.
  Their input is the compact code `encC k φ`, in which N is not written; its length is, up to
  padding that the bound absorbs, that of the formula with names in binary, so these statements have
  the form of the paper's together with the remark after Corollary 11.
  The code `SatM.enc k φ` of `CountsWithin` and `CountsOccWithin` instead contains N in unary, so
  its length is k + N + k·m·(⌊log₂(2N)⌋ + 1) + 2, which for names much larger than their number is
  much more than the length of the formula with names in binary.
* Theorem D (b) also says that the pairs (K_ℓ, e_ℓ) satisfy the hypothesis of Theorem D (a) and that
  e_ℓ = Θ((log K_ℓ)^{-1/2}). Only its conclusion («So there are …») is here. 

 ### Vocabulary 

### `lg`

 The paper's log: «log = log₂». 

### `expM`

 The exponent in the number m of clauses, as printed: k·m/√(log m). 

### `expN`

 The exponent in the number n of variables, as printed: k²·n·log log n/√(log n). 

### `CountsWithin`

 M, started on the code of (k, φ), halts after at most t steps with the number of satisfying
assignments of φ (among all 2ⁿ assignments of x₀ … xₙ₋₁), in n + 1 bits, as output. 

### `timeMin`

 The time of Theorem 1, rounded down: 2^{C·min{km/√(log m), k²·n·log log n/√(log n)}}. 

### `timeN`

 The time of Theorem D (b), rounded down: 2^{C·k²·n·log log n/√(log n)}. 

### `timeCor`

 The time of Corollary 11, rounded down: min{2^{C·km/√(log m)}, 2^{C·k²·n·log log n/√(log n)}}. 

 ### Theorem 1, for formulas over x₀ … xₙ₋₁ in which all variables occur 

### `MainTheoremFor`

 The bound of Theorem 1 for the machine M and the constant C: for every k ≥ 1 and every k-CNF φ
with m ≥ 2 clauses over n ≥ 4 variables that all occur, M computes the number of satisfying
assignments within
2^{C·min{km/√(log m), k²·n·log log n/√(log n)}} steps. 

### `MainTheoremAllOccur`

 Theorem 1, with the constant of its O named: there are a deterministic algorithm and an absolute
constant C such that, for every k ≥ 1 and every k-CNF with m ≥ 2 clauses in which n ≥ 4 variables
occur,
the algorithm computes the number of satisfying assignments of these n variables in time 2^{C min{k²
n log log n/√(log n), km/√(log m)}}.
Here the variables are x₀ … xₙ₋₁ and all occur; in the paper they are x₁ … xₙ (Section 2). 

 ### Theorem D (b), and the number of clauses of a k-CNF 

### `ThmVariablesBFor`

 The bound of Theorem D (b) for the machine M and the constant C: for every k ≥ 1, every n ≥ 4
and every k-CNF φ on n variables (any number of clauses, none included; variables need not occur), M
computes the number of
satisfying assignments within 2^{C·k²·n·log log n/√(log n)} steps. 

### `ThmVariablesB`

 Theorem D (b), the conclusion. «So there are a deterministic algorithm and an absolute constant
C such that, for all integers k ≥ 1 and n ≥ 4, the algorithm computes the number of satisfying
assignments of a k-CNF on n
variables in time 2^{C k² n log log n/√(log n)}.» 

### `ClauseCountStmt`

 The remark in Section 2 of the paper: «a k-CNF on n variables has fewer than (2n+1)^k clauses».
Here «at most»: the empty clause is allowed, and for k = 1 there are exactly 2n + 1 lists of at most
one literal. No hypothesis on k or n. 

 ### Corollary 11, for formulas over x₀ … xₙ₋₁ in which all variables occur 

### `CorMinFor`

 The bound of Corollary 11 for the machine M and the constant C: for every k ≥ 1 and every k-CNF
φ with m ≥ 2 clauses over n ≥ 4 variables that all occur, M computes the number of satisfying
assignments within
min{2^{C·km/√(log m)}, 2^{C·k²·n·log log n/√(log n)}} steps. 

### `CorMinAllOccur`

 Corollary 11. «There are an absolute constant C and a deterministic algorithm that, given a
k-CNF, for any k ≥ 1, with m ≥ 2 clauses in which n ≥ 4 variables occur, computes the number of its
satisfying assignments, as
assignments of these n variables, in time at most min{2^{C·km/√(log m)}, 2^{C·k² n log log n/√(log
n)}}.» Here the variables are x₀ … xₙ₋₁ and all occur; in the paper they are x₁ … xₙ (Section 2). 

### `CorMinIsMainTheoremStmt`

 After Corollary 11: «This is the Main Theorem.» For every machine and every constant the two
bounds are the same. 

 ### One machine and one constant for all of them 

### `TogetherAllOccur`

 ONE machine with finite alphabets and ONE constant C satisfy the bound of Theorem 1, the bound
of Theorem D (b) and the bound of Corollary 11. 

 ### Width 3 

### `timeMin3`

 The time 2^{C·min{m/√(log m), n·log log n/√(log n)}}, rounded down. 

 ### Formulas over arbitrary names of the variables

Here φ is a formula over the names x₀ … x_(N−1), of which only some need occur. n is the number of
those that occur (`numOcc`), and the satisfying assignments are counted «as assignments of these n
variables»
(`numSatOcc`); neither definition mentions a renaming. The code `SatM.enc k φ` (1ᵏ 0, then 1ᴺ 0,
then k slots of ⌊log₂(2N)⌋ + 1 bits per clause) contains N in unary; the compact code of the next
section does not. 

### `Occurs`

 The variable xᵢ occurs in φ, positively or negatively. 

### `numOcc`

 The number of variables that occur in φ. 

### `numSatOcc`

 The number of satisfying assignments of φ, as assignments of the variables that occur in φ. 

### `CountsOccWithin`

 M, started on the code of (k, φ), halts after at most t steps with the number of satisfying
assignments of φ, as assignments of the n variables that occur in φ, in n + 1 bits, as output. 

### `AllOccurStmt`

 If all variables occur, the two ways of counting agree: n is the number of all variables, and
the number of satisfying assignments is `SatK.numSat`. 

 ### The compact code: no number in unary but k and the number of bits of a name

In `SatM.enc k φ` the number N of names is written in unary. In the compact code `encC k φ` only the
number w = ⌊log₂(2N)⌋ + 1 of bits of a slot is; everything else is the same. Its length is k + w + 2 +
k·m·w.
This is not the shortest code with names in binary, since every name is padded to w bits and every
clause to k slots; but with N one more than the largest name it is at most k·(ℓ+3)², where ℓ is the
number of bits of the
formula with its names in binary, and k^C is below the exponential term. So a name may be
exponentially larger than the input is long, and the bound is the paper's up to the constant C. N is
not written; no output depends on it. 

### `encC`

 The compact code of (k, φ): 1ᵏ 0, then 1ʷ 0 with w = ⌊log₂(2N)⌋ + 1, then k slots per clause, w
bits per slot, low bit first. It is `SatM.enc k φ` with 1ʷ in place of 1ᴺ. 

### `LengthEncCStmt`

 The length of the compact code: k + w + 2 + m·k·w with w = ⌊log₂(2N)⌋ + 1. No hypothesis on φ. 

### `CountsOccWithinC`

 M, started on the compact code of (k, φ), halts after at most t steps with the number of
satisfying assignments of φ, as assignments of the n variables that occur in φ, in n + 1 bits, as
output. 

### `DecidesWithinC`

 M, started on the compact code of (k, φ), halts after at most t steps with one bit as output,
which is 1 if and only if φ is satisfiable. 

### `MainTheoremCompact`

 Theorem 1, with the compact code as input. One machine with finite alphabets and one constant C:
for every k ≥ 1, every N and every k-CNF φ over x₀ … x_(N−1) with m ≥ 2 clauses in which n ≥ 4
variables occur, the machine
computes the number of satisfying assignments, as assignments of these n variables, within
2^{C·min{km/√(log m), k²·n·log log n/√(log n)}} + C·(length of the compact code)^C steps. 

### `CorMinCompact`

 Corollary 11, with the compact code as input: as `MainTheoremCompact` (k ≥ 1, any N, a k-CNF
with m ≥ 2 clauses in which n ≥ 4 variables occur), within
min{2^{C·km/√(log m)}, 2^{C·k²·n·log log n/√(log n)}} + C·(length of the compact code)^C steps. 

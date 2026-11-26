---
{
  "module": "proof/statements/VariablesFixedWidthStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/VariablesFixedWidthStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/VariablesFixedWidthStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The bound in the number n of variables, for fixed k

Definitions and statements only (no theorem, no proof). Imports `ClausesOccurStatement.lean` (and
through it `MainTheoremFormsStatement.lean`, `AppRunningTimeStatement.lean`).

## The sentences of the paper that are stated here

* Theorem A (c), second sentence: «For fixed k and n ≥ 4 variables the time is 2^{O(n log log n/(log
  n)^{α'})}, provided that a number between 0.85ρ^ℓ and ρ^ℓ can be computed from ℓ in time
  polynomial in K_ℓ, as is the case for ρ = 11/12 and for ρ = 1/√2.»
  This is `CountsFromPieces`, with `Proviso` and `ProvisoHolds`.
* Theorem A as a whole, with both sentences of (c) with the printed hypotheses and quantifiers, in
  steps of a Turing machine: `RunningTimesFromPieces`.

## How to read it

* «One deterministic algorithm … For fixed k … the time is»: ONE machine M with finite alphabets,
  fixed before k; for every k ≥ 1 a constant C, which may depend on k. Both may depend on ρ, c, x₀.
* φ is a k-CNF on the n variables x₀ … xₙ₋₁ (`SatK.IsKCNF k φ`). This n is that of Theorem D (a),
  from which the sentence is proved: the number of all variables, not of those that occur as in the
  first sentence of (c); variables need not occur, and any number of clauses is allowed. The count
  is that of all 2ⁿ assignments, in n + 1 bits (`MainTheoremForms.CountsWithin`); the input is
  `SatM.enc k φ` (1ᵏ 0, 1ⁿ 0, k slots per clause).
* `MainTheoremForms.lg` is the paper's log = log₂, without any shift. The bound has the printed form
  2^{C·…}, rounded down. For n ≥ 4 we have log n ≥ 2 and log log n ≥ 1.
* The numbers K_ℓ of the proviso are those of the display that defines K_ℓ in Theorem A, for the x₀
  of Theorem A (`Levels.Gen.K x₀ ℓ`). «In time polynomial in K_ℓ»: the function gets ℓ and K_ℓ in
  unary and is polynomial-time (`Groundwork.PolyT`); it returns the numerator and the denominator of
  the number.

## Where these statements differ from the printed sentence

* Steps of a multi-stack Turing machine in place of operations of a word RAM; the width k is
  declared in the input, in unary; lists in place of sets: as for the Main Theorem.
* The machine is not that of the first sentence of (c) (`ClausesOccur.CountsFromPieces`): as in the
  printed proof, it is the algorithm of Theorem D (a) with a fall-back.
* `AppRunningTime.ThmRunningTime.c_n` is stronger in that it has no proviso, and weaker in that its
  machine is chosen after k. Its bound (shifted logarithms, a factor C in front) and its code
  (`SatK.enc k φ`, without 1ᵏ 0) convert to those of this file for fixed k. 

### `expVariables`

 The exponent in the number n of variables, as printed in Theorem A (c): n·log log n/(log n)^α. 

### `timeVariables`

 The time 2^{C·n·log log n/(log n)^α}, rounded down. 

### `CountsFor`

 For the width k, the machine M and the constant C: for every n ≥ 4 and every k-CNF φ on n
variables, M computes the number of satisfying assignments within 2^{C·n·log log n/(log n)^α} steps. 

### `Counts`

 One machine with finite alphabets, and for every width k ≥ 1 a constant C, with `CountsFor`. 

### `IsBetween`

 `num`, given ℓ and K_ℓ in unary, returns the numerator and the denominator of a number between 0.85·ρ^ℓ
and ρ^ℓ. (For ρ > 0 the denominator is not 0, since in Lean a fraction with the denominator 0 is 0.) 

### `Proviso`

 The proviso: «a number between 0.85ρ^ℓ and ρ^ℓ can be computed from ℓ in time polynomial in
K_ℓ». 

### `ProvisoHolds`

 «… as is the case for ρ = 11/12 and for ρ = 1/√2.» For every x₀. 

### `CountsFromPieces`

 Theorem A (c), second sentence. Suppose that there are pieces with parameters (ρ, c), let α' =
log(1/ρ), let x₀ ≥ 18 be an integer with 2^x₀ ≥ c + 5, and let the proviso hold. Then one machine
counts, for every fixed k ≥ 1, the satisfying assignments of a k-CNF
on n ≥ 4 variables within 2^{C·n·log log n/(log n)^{α'}} steps, with a constant C that may depend on
k. 

### `RunningTimesFromPieces`

 Theorem A, with both sentences of (c) with the printed hypotheses and quantifiers, in steps of a
Turing machine. Parts (a), (b) and (d) are those of `AppRunningTime.ThmRunningTime`, word for word. 

### `RunningTimesFromPieces.a`

 (a) 

### `RunningTimesFromPieces.b`

 (b); C₀ depends only on c. 

### `RunningTimesFromPieces.c_m`

 (c), first sentence: variables need not occur 

### `RunningTimesFromPieces.c_n`

 (c), second sentence: with the proviso, one machine for all k 

### `RunningTimesFromPieces.c_proviso`

 «as is the case for ρ = 11/12 and for ρ = 1/√2» 

### `RunningTimesFromPieces.d`

 (d), as in `AppRunningTime.ThmRunningTime`. The printed proof of (d) is not formalized; (d)
  follows from a bound of the same form with the larger exponent 3/19 in place of α'/10. 

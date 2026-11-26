---
{
  "module": "proof/rates/OccurM/TiedDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/TiedDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/TiedDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The bound in m for formulas over arbitrary names: the forms that show the route

`ClausesOccur.Counts α` says «there is a machine»; by its wording it says nothing about the route of
a proof. The proof of Theorem A (c) in the paper uses a preparation that lists the occurrences and
the tests (here it also numbers the variables that occur),
the network of the formula, case (i) of Lemma 8 (the lemma on groupings with explicit cost) and the
algorithm of part (b). The statements of this file name these things. Nothing is proved here.

* `Prepares pre`: what the preparation does. On the compact code of (k, φ) the function `pre`
  returns the code `SatM.enc k ψ` of a k-CNF ψ over exactly n = `numOcc φ` variables, all of which
  occur, with as many clauses as φ and with
  as many satisfying assignments as φ has as assignments of the variables that occur.
* `prepA S pick`, `prepE S pick`: the named top level in m (`ClauseBound.Alg.AM`, `eM`) with the
  named preparation `VariableBound.Rename.rencC` in front.
* `TopOccur S pick α`: the bound in m for these two named functions; `TopOccurOfTopStmt`: it follows
  from `GeneralPieces.Tied.TopM`, the same for formulas in which every variable occurs.
* `CountsFromPiecesTied`, `BoundInClausesTied`: Theorem A (c), first sentence, and the bound in m of
  the Main Theorem, for the named programs on the recursion of part (b).
* `EveryWrapperCounts`: for EVERY machine M that counts within the bound on formulas in which every
  variable occurs, EVERY machine N that runs a preparation and then M counts within the printed
  bound on every k-CNF with k ≥ 1 and m ≥ 2. 

 ### The preparation 

### `Prepares`

 `pre` numbers the variables that occur: for every k ≥ 1 and every k-CNF φ over x₀ … x_(N−1),
`pre` maps the compact code of (k, φ) to the code of (k, ψ) for a k-CNF ψ over n = `numOcc φ`
variables, all of which occur in ψ, with
as many clauses as φ, whose number of satisfying assignments is that of φ as assignments of the
variables that occur. 

### `PreparesUnary`

 The same for the code `SatM.enc k φ`, which has N in unary. 

### `PreparationStmt`

 The two named preparations are such, and they are polynomial-time. 

 ### The named programs 

### `prepA`

 The top level in m after the preparation, a function of (input, pad). 

### `prepE`

 Its exponent, a function of the input. 

### `TopOccur`

 The bound in m for the named top level after the named preparation, for an algorithm S for
cliques and a way to pick its level. 

### `TopOccur.poly_A`

 both functions are polynomial-time 

### `TopOccur.correct`

 the function returns the number of satisfying assignments, as assignments of the n variables
  that occur, in n + 1 bits, if the pad has 2^prepE units 

### `TopOccur.rate`

 the exponent is O(k·m/(log m)^α), the O not depending on k 

### `TopOccur.machine`

 one machine computes, on every input x, the named function at (x, 2^{prepE x} units) within
  q·(|x| + 2^{prepE x} + 1)^q steps, and it counts within the printed bound 

### `prepAUnary`

 As `prepA`, for the code with N in unary. 

### `prepEUnary`

 As `prepE`, for the code with N in unary. 

### `TopOccurUnary`

 As `TopOccur`, for the code `SatM.enc k φ`, which has N in unary, and the preparation
`VariableBound.Rename.renc`. 

### `TopOccurOfTopStmt`

 The step: from the bound in m for the named top level on formulas in which every variable occurs
to the bound for the same top level after the preparation, on every k-CNF with k ≥ 1 and m ≥ 2
(correctness: m ≥ 1). For every algorithm for cliques, every way to pick its
level and every exponent 0 ≤ α ≤ 1. 

### `CountsFromPiecesTied`

 Theorem A (c), first sentence, for the named programs: for all pieces with parameters (ρ, c) and
every x₀ ≥ 18 with 2^x₀ ≥ c + 5, the preparation, then the top level in m on the recursion of part (b)
on these pieces. 

### `BoundInClausesTied`

 The bound in m of the Main Theorem for the named programs: for some programs (P, val) for the
pieces of Appendix B, with a constant c, and the least x₀ of Theorem A. 

### `UntieStmt`

 From the tied forms, which name the programs, to the forms that only say «there is a machine». 

 ### For every machine 

### `EveryWrapperCounts`

 Let 0 ≤ α ≤ 1, let `pre` number the variables that occur, and let M, with the constant C, count
within C·2^{C·km/(log₂(m+2))^α} steps on the formulas in which every variable occurs (the body of
`SatM.CountInRate`). Then EVERY machine
N that wraps M, with `pre` before it and nothing after it, for whatever q, counts on every k-CNF
with k ≥ 1 and m ≥ 2 as in `CountsFor α`, with some constant. All that is known of N is
`Wrap.Wraps M pre id N q`. That such `pre`, N and q exist is said by
`PreparationStmt` and `Wrap.EveryMachineCanBeWrapped`. 

### `EveryWrapperCountsUnary`

 The same for the code with N in unary. 

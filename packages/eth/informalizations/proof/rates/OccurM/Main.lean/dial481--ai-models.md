---
{
  "module": "proof/rates/OccurM/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem A (c), first sentence, and the bound in m of the Main Theorem, for formulas over arbitrary names

The route, as in the paper:

1. `countsFromPiecesTied`: part (c), first sentence, for the named programs (given programs for the
   pieces, from which the machine is built). `GeneralPieces.thmRunningTimeCm_tied` gives it on
   formulas in which every variable occurs (the network of the formula, case (i) of Lemma 8, the
   algorithm of
   part (b)), and `topOccurOfTop` puts the preparation in front. 0 ≤ α' ≤ 1 because ½ ≤ ρ < 1.
2. `untie`: from the named programs to «there is a machine», with the least x₀ of Theorem A.
3. `ClausesOccur.countsFromPieces`: Theorem A (c), first sentence, by 1 and 2.
4. `ClausesOccur.boundInClausesFrom`, `boundInClauses`: «With Theorem A this gives the exponent
   log(1/ρ) = ½ of log m, that is, the bound in m of the Main Theorem», from Theorem B and 3.
5. `boundInClausesTied`: the same for the named programs. `ClausesOccur.runningTimesFromPieces`:
   Theorem A as a whole, the other parts from `AppRunningTime.thmRunningTime`. 

### `boundInClausesIsHalf`

 For every machine and every constant, the bound in m of the Main Theorem is `CountsFor` at α =
½. 

### `countsFromPiecesTied`

 Theorem A (c), first sentence, for the named programs: the preparation, then the top level in m
on the recursion of part (b). 

### `boundInClausesTied`

 The bound in m of the Main Theorem for the named programs, on programs for the pieces of
Appendix B; α' = log √2 = ½. 

### `untie`

 From the forms for the named programs (the tied forms: the machine is built from given programs
for the pieces) to the forms with «there is a machine»: the machine and the constant are those of
the field `machine`; x₀ is the least one of Theorem A. 

### `countsFromPieces`

 Theorem A (c), first sentence. 

### `countsUnaryFromPieces`

 The same with N in unary in the input. 

### `boundInClausesFrom`

 «With Theorem A this gives …»: from Theorem B and the first sentence of Theorem A (c) to the
bound in m; α' = log √2 = ½. 

### `boundInClauses`

 After Theorem B: the bound in m of the Main Theorem. 

### `runningTimesFromPieces`

 Theorem A, with the first sentence of (c) as printed. 

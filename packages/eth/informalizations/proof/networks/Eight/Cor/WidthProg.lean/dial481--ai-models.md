---
{
  "module": "proof/networks/Eight/Cor/WidthProg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/WidthProg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/WidthProg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 6: the width reduction is polynomial-time

`splitN n x` is the width reduction of `WidthDefs.lean` (the same `splitAll`, then `List.dedup`) for
a formula x whose variables are natural numbers below n; the fresh variables are n, n + 1, ….
`widthP` takes the number of variables in unary with the formula, the form in which
the programs of this development take an input, and returns the number of variables of the image in
unary with the image. `widthP_polyT`: it is polynomial-time in the sense of `Groundwork.PolyT`.
For the certificate the two recursions are written without recursion (`clauseP`, `allP`) and shown
to give the same lists (`splitClause_eq`, `splitAll_eq`).
`toN_widthReduce`: on an instance φ, read with numbers as variables (`Decode.toN`), the program
returns `widthReduce φ` read in the same way. `cntN_splitN`: so it keeps the number of satisfying
assignments, in the form `CountKSat.cntN` of the counting programs.
No machine and no bound on its time is made from this here. 

### `freshN`

 The fresh variables n, n + 1, …, n + N − 1. 

### `splitN`

 The width reduction of a formula with numbers as variables, all below n. 

### `widthP`

 The same with the numbers of variables in unary. 

### `clauseP`

 `splitClause` without recursion, for at most s − 3 fresh variables, s the number of literals of
C. Counting from 0, the i-th fresh variable stands for the disjunction of the literal before it (the
first literal of C, or the fresh variable number i − 1) and the literal number i + 1 of C; the last
clause is the last fresh variable with the rest of C. 

### `allP`

 `splitAll` without recursion: the clause number j takes its fresh variables after those of the
clauses before it. 

### `numFresh_unary`

 The number of fresh variables in unary: it is at most the number of literals written. 

### `widthP_polyT`

 The width reduction, with the numbers of variables in unary, is polynomial-time. 

 ### The program gives the width reduction of `WidthDefs.lean` 

### `splitClause_map`

 Renaming the variables commutes with `splitClause`. 

### `splitAll_map`

 Renaming the variables commutes with `splitAll`. 

### `toN_widthReduce`

 `widthReduce φ`, with its variables read as numbers, is what the program returns on φ with its
variables read as numbers. 

### `cntN_splitN`

 The number of satisfying assignments in the form of the counting programs of this development:
on the formula of an instance, the program keeps it. 

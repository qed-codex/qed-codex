---
{
  "module": "proof/networks/Eight/Cor/WidthDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/WidthDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/WidthDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 6: the width reduction that keeps the number of satisfying assignments (definitions and statements only)

The paper: «each of these is turned into a 3-CNF with O(n) clauses and O(n) variables and the same
number of satisfying assignments, by the standard width reduction, which introduces a constant
number of [fresh] variables for each clause.
The number is preserved if each [fresh] variable is forced, by three clauses of at most 3 literals,
to equal the disjunction of the two literals that it replaces in a long clause; Dell et al. do not
spell this out.»

One step: a clause l₁ ∨ l₂ ∨ l₃ ∨ l₄ ∨ … (more than 3 literals) becomes y ∨ l₃ ∨ l₄ ∨ …, with a
variable y that occurs nowhere else, and the three clauses ¬y ∨ l₁ ∨ l₂, y ∨ ¬l₁, y ∨ ¬l₂ (`forced`)
are added. The step is repeated on the
shorter clause until 3 literals are left (`splitClause`), so a clause with s > 3 literals takes s −
3 fresh variables and becomes 1 + 3(s − 3) clauses. `splitAll` does this for every clause, each with
fresh variables of its own.
`widthReduce φ` is the result for a formula φ on x₀ … xₙ₋₁ in the sense of `ThreeSatStatement.lean`:
a formula on x₀ … x_{n+N−1}, where N = `numFresh φ` and the fresh variables are xₙ … x_{n+N−1}.

The statements, proved in `Width.lean`: `StForced` (the three clauses say y = l₁ ∨ l₂), `StRestrict`
and `StExtend` (a satisfying assignment of the image, read on x₀ … xₙ₋₁, satisfies φ; a satisfying
assignment of φ extends to one of the image in exactly one way),
and `StWidth` (the image is an instance of 3-SAT with the same number of satisfying assignments; at
most (k − 3)·m fresh variables and at most m + 3(k − 3)·m clauses for a k-CNF with m clauses).

Different from the paper: a clause is a list here, so a literal may stand twice in it. If l₁ = l₂,
the step writes the clause y ∨ ¬l₁ twice, and an instance (`SatK.IsKCNF`) may not have a clause
written twice. So `widthReduce` ends by striking out repetitions
of clauses (`List.dedup`). This changes neither the set of clauses nor the satisfying assignments.
The first four definitions are for any type V of variables, because they are used for V = Fin (n +
N) here and for V = ℕ in programs. This file imports only `CountKSatStatement.lean` (and Mathlib). 

### `neg`

 The opposite literal. A literal is a variable with the value of it that makes the literal true,
as in `Sat3.Lit`. 

### `forced`

 The three clauses ¬y ∨ l₁ ∨ l₂, y ∨ ¬l₁, y ∨ ¬l₂. 

### `splitClause`

 One clause, with a list of fresh variables: while the clause has more than 3 literals and a
fresh variable y is left, put y in the place of the first two literals and add the three clauses for
y. 

### `splitAll`

 All clauses: a clause with s literals takes the next s − 3 fresh variables of the list (none if
s ≤ 3). 

### `numFresh`

 The number of fresh variables: s − 3 for each clause with s > 3 literals. 

### `Holds`

 The assignment a makes a literal of every clause true (the condition in `Sat3.Satisfiable` and
in `SatK.numSat`). 

### `widthReduce`

 The width reduction of a formula on x₀ … xₙ₋₁. The variables of φ keep their numbers, the fresh
ones are xₙ … x_{n+N−1}, N = `numFresh φ`; a clause that comes out several times is kept once. 

 ### The statements 

### `StForced`

 «each [fresh] variable is forced, by three clauses of at most 3 literals, to equal the
disjunction of the two literals that it replaces»: an assignment satisfies the three clauses exactly
if it makes y true exactly when it makes l₁ or l₂ true;
and the three clauses have at most 3 literals. 

### `StRestrict`

 A satisfying assignment of the image, read on the variables x₀ … xₙ₋₁ of φ, satisfies φ. 

### `StExtend`

 A satisfying assignment of φ is the restriction of exactly one satisfying assignment of the
image. 

### `StWidth`

 The width reduction, as the proof of Corollary 6 uses it. For every formula φ on n variables the
image is an instance of 3-SAT (at most 3 literals per clause, no clause written twice) on n +
`numFresh φ` variables with the same number of
satisfying assignments. If φ has m clauses with at most k literals each, there are at most (k − 3)·m
fresh variables and at most m + 3(k − 3)·m clauses. (In ℕ, k − 3 is 0 for k ≤ 3.) 

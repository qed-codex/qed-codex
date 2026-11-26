---
{
  "module": "proof/consequences/CountKSat/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The counting program: definitions

The sparsification tree of the branching rule `pickK` writes a k-CNF as an OR of sparse formulas,
which may share satisfying assignments. Dell, Husfeldt, Marx, Taslaman and Wahlén
(arXiv 1206.1775, Appendix A) make the branches exclude each other. In the notation of Appendix C,
where a node branches on a set H of literals (the heart) and the clauses Q = {E∖H : E ∈ F} (the
petals), the child that gets Q also gets «every literal of H is false».
Here a node of the tree is a pair: the formula that the branching rule looks at, and a side list of
clauses that the rule never looks at. The clauses «every literal of H is false» go on
the side list, so the first components of the nodes form exactly the tree of `pickK` alone, as in
Appendix C. The side list starts with the clauses xᵢ ∨ ¬xᵢ, i < n. They are always true,
and they make every variable occur, so that the value of the network of a leaf is its number of
satisfying assignments on all n variables.
This file has definitions only. 

 ### The tree 

### `CNode`

 A node: the formula that the rule looks at, and the side list. 

### `negU`

 «Every literal of H is false», as clauses of one literal. 

### `stepC`

 The light child (the first component; the call on ψ ∪ {H} in Appendix C) gets the heart H as a
clause. The heavy child (the second component; the call on ψ ∪ Q) gets the petals Q = {E∖H : E ∈ F},
and on its side list «every literal of H is false». 

### `taut`

 The clauses xᵢ ∨ ¬xᵢ for i < n. 

### `rootC`

 The root, from the number of variables in unary and the formula. 

### `leafF`

 The formula of a node: the side list and the formula that the rule looks at. 

 ### Counting on n variables 

### `ext`

 An assignment to x₀ … xₙ₋₁, continued by false. 

### `cntN`

 The number of assignments to x₀ … xₙ₋₁ that make a literal of every clause of x true. 

 ### The machine cut into steps 

### `walkSum`

 The sum, over the leaves below root a, of the numbers that T returns. 

### `outW`

 The result as a word: n + 1 bits, lowest first. 

### `countMK`

 The counting machine: read the input by `decU` as (n in unary, formula); the count is 0 if there
is an empty clause; otherwise walk the tree of `step`
and add up the counts of the leaves; write the sum as a word. M returns the count of one sparse
formula. 

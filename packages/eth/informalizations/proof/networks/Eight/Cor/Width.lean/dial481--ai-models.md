---
{
  "module": "proof/networks/Eight/Cor/Width.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/Width.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/Width.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 6: the width reduction keeps the number of satisfying assignments (proofs)

Proofs of the four statements of `WidthDefs.lean`: `stForced`, `stRestrict`, `stExtend`, `stWidth`.
The paper gives the reason in one sentence («The number is preserved if each new variable is forced
… to equal the disjunction of the two literals that it replaces»); spelled out:
* `holds_forced`: the three clauses say y = l₁ ∨ l₂.
* Downwards (`splitClause_sound`, `splitAll_sound`): from y ∨ l₃ ∨ … and ¬y ∨ l₁ ∨ l₂ follows l₁ ∨
  l₂ ∨ l₃ ∨ …; this needs nothing about y.
* Upwards (`splitClause_extend`, `splitAll_extend`): give y the value of l₁ ∨ l₂. This needs that
  the fresh variables differ from each other and occur nowhere in the formula.
* Only one way (`splitClause_unique`, `splitAll_unique`): the value of y is determined by those of
  l₁ and l₂, which are variables of the formula or fresh variables set earlier. This needs that no
  fresh variable is left unused.
* Sizes: `splitAll_width`, `length_splitAll` (exactly m + 3N clauses before repetitions are struck
  out), `numFresh_le`.
All of this is for any type of variables. The last section takes V = Fin (n + N) and counts:
restriction to x₀ … xₙ₋₁ is a bijection between the satisfying assignments of the image and those of
φ (`numSat_widthReduce`). 

 ### Satisfaction 

### `holds_congr`

 Two assignments that agree on the variables of a formula satisfy it or not together. 

### `holds_forced`

 The three clauses say y = l₁ ∨ l₂. 

### `stForced`

 `StForced`. 

 ### One clause 

### `splitClause_sound`

 An assignment that satisfies the clauses made from C satisfies C. (No condition on the variables
ys.) 

### `splitClause_vars`

 A variable of a clause made from C is one of ys or a variable of C. 

### `splitClause_extend`

 An assignment that satisfies C can be changed on the fresh variables ys so that it satisfies the
clauses made from C. 

### `splitClause_unique`

 Two assignments that satisfy the clauses made from C and agree on the variables of C agree on
the fresh variables, if all of these are used. 

### `splitClause_width`

 With enough fresh variables every clause made from C has at most 3 literals. 

### `length_splitClause`

 The number of clauses made from C: 1, and 3 for each fresh variable that is used. 

 ### All clauses 

### `splitAll_sound`

 An assignment that satisfies the image satisfies the formula. (No condition on the variables
ys.) 

### `splitAll_extend`

 An assignment that satisfies the formula can be changed on the fresh variables so that it
satisfies the image. 

### `splitAll_unique`

 Two assignments that satisfy the image and agree on the variables of the formula agree on the
fresh variables, if all of these are used. 

### `splitAll_width`

 With enough fresh variables every clause of the image has at most 3 literals. 

### `length_splitAll`

 With enough fresh variables the image, before repetitions are struck out, has exactly m + 3N
clauses: m the number of clauses of the formula, N the number of fresh variables. 

### `numFresh_le`

 At most k − 3 fresh variables for each clause of a k-CNF. 

 ### Formulas on x₀ … xₙ₋₁ 

### `freshFin`

 The fresh variables xₙ … x_{n+N−1}. 

### `lift`

 The formula, read as a formula on n + N variables. 

### `stRestrict`

 `StRestrict`. 

### `stExtend`

 `StExtend`. 

### `numSat_widthReduce`

 The number of satisfying assignments is kept. 

### `stWidth`

 `StWidth`. 

---
{
  "module": "proof/consequences/SplitSat/Leaf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Leaf.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Leaf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 5: «split every long clause into clauses of 3 literals with new variables»

`stLeaf` proves `SplitSat.StLeaf`. The program `Eight.Width.widthP` works on formulas with numbers
as variables. A formula whose variables are below n is `Decode.toN φ` for a formula φ on n variables
(`GraphProblems.exists_toN`); on it the program returns `widthReduce φ` read in the same way
(`Eight.Width.toN_widthReduce`).
What is said of `widthReduce φ` is stated in proof/networks/Eight/Cor/WidthDefs.lean and proved in
proof/networks/Eight/Cor/Width.lean: if φ has m clauses of at most k literals, the image is an
instance of 3-SAT with at most (k − 3)·m new variables (`stWidth`); a satisfying assignment of the
image, read on the old variables, satisfies φ (`stRestrict`); a satisfying assignment of φ extends
to one of the image (`stExtend`).
The number of satisfying assignments is not used here. 

### `widthP_replicate`

 The program on (n in unary, x), written out: n + (number of new variables) in unary, and the
formula with its long clauses split. 

### `widthP_eq`

 The first part of what the program returns is a number in unary. 

### `nodup_toN`

 A formula in which no clause is written twice stays so when its variables are read as numbers. 

### `exists_instance`

 A formula with numbers below n as variables, at most k literals per clause and no clause written
twice is `Decode.toN φ` for an instance φ of k-SAT on n variables. 

### `satisfiable_widthReduce`

 The formula with its long clauses split is satisfiable exactly if the formula is: one direction
restricts an assignment to the old variables, the other extends it to the new ones. 

### `stLeaf`

 **One leaf**: «split every long clause into clauses of 3 literals with new variables». For a
formula x on x₀ … xₙ₋₁ with at most B·n clauses of at most k literals, `widthP` returns (N in unary,
x₃) with at most 3 literals per clause, variables below N, no clause twice, N ≤ (1 + (k−3)·B)·n, and
x₃ is satisfiable exactly if x is. 

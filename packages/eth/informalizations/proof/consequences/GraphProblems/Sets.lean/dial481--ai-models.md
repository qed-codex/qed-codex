---
{
  "module": "proof/consequences/GraphProblems/Sets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Sets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Sets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 7: what the formulas of Independent Set and Dominating Set say

An assignment a to x₀ … xₙ₋₁ is the set S = {v | a v = true} of vertices. This file shows that a
satisfies the formula of Independent Set if and only if S is an independent set, and the formula of
Dominating Set if and only if S is a
dominating set, so that the number of satisfying assignments with exactly s true variables is the
number of such sets of size s. It also bounds the width, the variables and the number of clauses of
a formula with one clause of two literals for each chosen pair of vertices,
and derives the decision problems from the numbers of independent sets, cliques, vertex covers and
dominating sets of a given size. 

### `trueSet`

 The set of the variables that an assignment makes true. 

### `mem_trueSet`

 A variable is in the set if and only if it is true. 

### `cntS_eq_ncard`

 If the assignments that satisfy ψ are those whose set has the property P, then ψ has as many
satisfying assignments with s true variables as there are sets of size s with the property P. 

### `mem_pairs`

 The pairs are those of two numbers below n. 

### `sat_pairs_iff`

 An assignment satisfies the formula with one clause of two literals of the same sign b for every
pair chosen by q if and only if, for every such pair, one of its two variables has the value b. 

### `shaped_pairs`

 Width, variables and number of clauses of such a formula. 

### `sat_indepF`

 An assignment satisfies the formula of Independent Set if and only if its set is independent. 

### `sat_domF`

 An assignment satisfies the formula of Dominating Set if and only if its set is dominating. 

### `stIndep`

 The formula of Independent Set has as many satisfying assignments with s true variables as the
graph has independent sets of size s. 

### `stDom`

 `StDom`: for the formula `domF` of a graph G, `cntS n s` is the number of dominating sets of G
with s vertices. 

### `stDecide`

 There is an independent set or a clique with at least s vertices, or a vertex cover or a
dominating set with at most s ≤ n vertices, if and only if the number of those of size exactly s is
not 0. 

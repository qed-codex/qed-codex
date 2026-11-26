---
{
  "module": "proof/consequences/CountKSatRate/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Counting satisfying assignments for clauses of width k, with a padded input: definitions

This file holds, for every width k, definitions for counting the satisfying assignments of a formula
written in the input: the depth-first walk `walkS` of the sparsification tree, on the
pairs (formula, side list) of `proof/consequences/CountKSat/Defs.lean`, which adds up the values of
the leaves; the formula `leafM` of a node, built from its formula and its side list;
the number `nK k` of variables written in the input; exhaustive counting `bruteN k` with fuel; the
padding machine `padMW` with a word as result; and a bound `stackLenC` on the length
of the word of a state of the walk. The width k is a constant of the definitions, not a part of the
input.
This file has definitions only. 

 ### The walk that adds up 

### `roundS`

 One round of the depth-first walk that keeps only the sum of the values of the leaves met so
far. 

### `walkS`

 The depth-first walk of the counting tree for width k, one round for each unit of the pad. 

 ### The functions 

### `sideU`

 The side list made short in every variable: the clauses of one literal, each of them once. The
other clauses of a side list are the clauses xᵢ ∨ ¬xᵢ, which are always
true. A count on all n variables, whether they occur or not, does not need them. 

### `leafM`

 The formula of a node: its side list made short, followed by its formula. It has the same
satisfying assignments as `leafF x`, and a variable occurs in at most two clauses of its first part. 

### `nK`

 The number of variables written in the bit string x, read as the code of an instance of k-SAT. 

### `bruteN`

 Exhaustive counting with fuel: among the assignments number 0, …, 2^n − 1 (assignment number y
gives the variable i the i-th binary digit of y), cut off at the length of
the pad, how many satisfy the formula written in the bit string. 

 ### The padding machine with a word as result 

### `padMW`

 The stepped machine: the state is the input with the present pad, or the result. One step
doubles the pad, or, once the pad has length at least 2^(e x), applies B. 

### `stackLenC`

 An upper bound for the length of the word of a state of the walk: at most bsum τ k · n + 1
nodes, each a formula of at most 2^k·m clauses of at most k literals and a side
list of at most 2n clauses of at most 2 literals, all on variables below n; and a number below
2^(n+1). 

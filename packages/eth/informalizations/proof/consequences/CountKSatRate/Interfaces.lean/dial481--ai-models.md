---
{
  "module": "proof/consequences/CountKSatRate/Interfaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Interfaces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Interfaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The interface statements, as propositions

Statements that one file needs from another are written here as definitions `St… : Prop`. Nothing is
proved and nothing is assumed: this file has no
theorem. One file proves `theorem … : St…`; a file that needs the statement takes `(h : St…)` as a
hypothesis.
The width k of the clauses is a variable of every statement in which it occurs. 

 ### The tree 

### `StTreeK`

 The sparsification lemma for counting at width k ≥ 1, with a short side list. ψ has variables
below n and nonempty clauses of at most k literals, and τ ≥ k². The tree of
`stepC (theta τ) k` of depth bsum τ k · n has at most Σ_{j ≤ kn/τ} C(bsum τ k · n, j) leaves. The
formula of a leaf has at most (leafC τ k + 2)·n clauses. At a leaf, the
formula that the rule looks at has nonempty clauses of at most k literals on variables below n, and
every variable occurs in at most leafC τ k of them; every clause of the side
list is one of the clauses xᵢ ∨ ¬xᵢ or has exactly one literal, and its variables are below n. The
counts of the leaves add up to the count of ψ. The stack of the walk never
holds more than bsum τ k · n + 1 nodes, each a formula of at most 2^k·|ψ| clauses of at most k
literals and a side list of at most 2n clauses of at most 2 literals. 

 ### The walk 

### `StRoundS`

 The state of the summing walk after i rounds: the stack of the plain walk, and the sum of the
values of the leaves that the plain walk has listed. 

### `StRoundSEnd`

 After at least 2·(number of leaves) − 1 rounds the stack is empty and the number is the sum of
the values of the leaves. 

### `StWalkS`

 If the pad has at least 2·(number of leaves) − 1 units and the word of every state of the walk
fits under the pad, then `walkS` returns the sum of the values of the leaves. 

 ### Correctness 

### `StStateLen`

 The word of a state of the counting walk has length at most `stackLenC k τ n m`. 

### `StBruteC`

 With a pad of at least 2^n units, exhaustive counting is correct. 

 ### The polynomial-time certificates 

### `StCertWalkS`

 The summing walk is polynomial-time in the pad. 

 ### The machine 

### `StPaddedW`

 Let `e` (from bit strings to numbers) and `B` (from a bit string and a list of units to a bit
string) be polynomial-time. There are a Turing machine `N` with finite
alphabets and a number `q` such that on every bit string `x` the machine halts with the output B (x,
the list of 2^(e x) units) within q · (|x| + 2^(e x) + 1)^q steps. 

---
{
  "module": "proof/consequences/CountKSat/Interfaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Interfaces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Interfaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The interface statements, as propositions

Every statement that one file needs from another is written here as a definition `St… : Prop`.
Nothing is proved and nothing is assumed: this file has no
theorem. One file proves `theorem … : St…`; a file that needs the statement takes `(h : St…)` as a
hypothesis. 

 ### The input and the output 

### `decU`

 The input as (n in unary, formula). 

### `StDecU`

 `decU` reads the code of a formula with at most k literals per clause, k ≥ 1. 

### `StCertDecU`

 `decU` is polynomial-time. 

### `StCntToN`

 The formula read with natural numbers as variables has the same count. 

 ### One sparse formula 

### `StCountValue`

 A correct evaluator of networks, run on `satP g k`, returns the value of the network
of φ in at most A·2^{δm} steps, m the number of clauses, and within size A·(size φ)^A. 

 ### The tree 

### `StStepCount`

 The satisfying assignments of a node are those of its two children, and no assignment satisfies
both: the counts add up. 

### `StRootCount`

 The root has the count of the formula. 

### `StSumLeaves`

 A quantity that is the sum of its values at the two children, at every node with the invariant
G, is the sum of its values at the leaves. 

### `SparsifiesC`

 `step` (with `rootC`) sparsifies width k for counting. ψ has variables below n and nonempty
clauses of at most k literals. The tree of depth Dd·n has at most 2^{εn}
leaves. The formula of a leaf has at most Bl·n clauses of at most max k 2 literals, and exactly the
variables below n occur in it. The counts of the leaves add up to the
count of ψ. The stack of the walk never holds more than Dd·n + 1 nodes, each with at most (|ψ| +
n)·Sk clauses. 

### `StProgC`

 The sparsification lemma for counting: `stepC` with the thresholds `theta τ` sparsifies width k
for counting, with a tree of depth bsum τ k · n, and at
most 2^{εn} leaves if (k/τ)·log₂(e·τ·bsum τ k) ≤ ε. 

### `StCertStepC`

 One step of the counting tree is computed in polynomial time. 

 ### The machine 

### `StWalkSum`

 If T takes t steps on each leaf and the sum over the leaves is below 2^B, the summing walk takes
t + 2 steps per leaf and returns that sum. 

### `StHostW`

 The host for a word as output. A stepped computation M from bit strings to bit strings with
polynomial-time init, step and out runs on one multi-stack machine N of
Mathlib with finite alphabets. There is one number q such that, whenever M ends on x with the word w
within T steps and with all states of size at most S, the
machine N started on x halts with output w within q·(T + 1)·(|x| + S + 1)^q steps. 

---
{
  "module": "proof/sparsification/UniformInK/Spars/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification with geometric thresholds: definitions and interface statements

The rule, the hearts, the petals, the two children and the leaves are those of
proof/sparsification/SparsifyWidthK/Defs.lean. What differs is the invariant along a path of the
tree and, with it, the thresholds.
There every literal lies in at most 2·θ(i−1) added clauses of size i, and an added clause is charged
with the removal of that many clauses of size i, whatever its own size; this forces thresholds
that grow doubly exponentially in k. Here every nonempty SET Y of literals lies in at most
2·θ(i−|Y|) added clauses of size i, so that an added clause of size i' removes at most 2·θ(i−i')
clauses
of size i. This is in substance the count in the Sparsification Lemma of Calabro, Impagliazzo and
Paturi [CIP06]. It allows θ 0 = 1 and θ i = 4·τ^(2i−1) for i ≥ 1, which do not depend on k, as soon
as 1 ≤ k and 8k ≤ τ.
This file has definitions only. The statements `St…` are propositions; one file proves each of them. 

 ### One step and the accounts along a path 

### `AddU`

 What one step adds to F: proper subsets of clauses of F, all of one size r ≥ 1, such that every
nonempty set Y of at most r literals lies in at most 2·θ(r−|Y|) sets that are clauses of F of
size r or are added. 

### `InvU`

 The invariant along a path. N: the added clauses that are still present; a i: how many clauses
of size i were added so far. Every nonempty set Y of at most i literals lies in at most
2·θ(i−|Y|) clauses of N of size i, and a i is at most the number of clauses of size i in N plus
2·θ(i−i') for every clause of a smaller size i' added so far. 

### `NodeU`

 What holds of a node F of the tree of φ after p steps, each heavy step adding τ to t. h r counts
the heavy steps with petals of size r. 

 ### The thresholds 

### `ThrU`

 What the final count needs of thresholds θ and bounds β for width k: at most β i · n clauses of
size i < k are added along a path, n the number of variables. 

### `thetaU`

 The thresholds: θ 0 = 1 and θ i = 4·τ^(2i−1). 

### `betaSU`

 β 0 = 0 and β i = 4·τ^(2i−2): at most β i · n clauses of size i are added along a path. 

### `bsumU`

 For 1 ≤ k and 8k ≤ τ, a path of the tree on n variables has at most bsumU τ k · n steps. 

### `leafCU`

 A leaf on n variables has at most leafCU τ k · n clauses. 

 ### The interface statements 

### `StNodeRootU`

 The root of the tree is a node with both counters 0. 

### `StNodeStepU`

 Both children of a node are nodes: one more step, and τ more units at the heavy child. 

### `StNodeBoundU`

 A path has at most (β 0 + … + β (k-1))·n steps, and its heavy steps use at most k·n units, τ
each. U: the at most 2n literals. 

### `StThrU`

 The thresholds `thetaU τ` and the bounds `betaSU τ` have the three properties for width k, if 1
≤ k and 8k ≤ τ. 

### `StBetaSumU`

 β 0 + … + β (k-1) is at most `bsumU τ k`, if 2 ≤ τ. 

### `StIfaceU`

 All that the walk of the tree needs to know about the rule on finite sets, for the thresholds
`thetaU τ`, if 1 ≤ k and 8k ≤ τ. 

---
{
  "module": "proof/sparsification/SparsifyWidthK/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification of a k-CNF on finite sets: definitions

Literals are elements of any type α; a clause is a `Finset α`, a formula a `Finset (Finset α)`.
`Sat`, `Reduced`, `red` and `over` are those of
`StepMachines/Math/Sparsify.lean`: `over F j H` is the set of the clauses of F of size j that
contain H.
The branching rule is that of Impagliazzo, Paturi and Zane. A heart is a nonempty set H that lies in
at least θ (j - |H|) clauses of size j > |H|; the
petals are these clauses without H. The rule takes the smallest such j and, for it, a heart of the
largest size. The light child adds H as a clause, the heavy
child adds all petals; both keep only the inclusion-minimal clauses.
This file has definitions only; the proofs are in `SparsifyWidthK/Step.lean`,
`SparsifyWidthK/SetAlg.lean` and `SparsifyWidthK/Thresholds.lean`.
(`Mathlib.Tactic` makes the word `over` a keyword, so the files of this folder write
`Sparsify.over`.) 

 ### The rule 

### `petals`

 The clauses of size j over H, without H. 

### `light`

 The light child: H becomes a clause. 

### `heavy`

 The heavy child: the petals become clauses. 

### `Heart`

 H is a heart for the clauses of size j: nonempty, smaller than j, and in at least θ (j - |H|) of
them. 

### `Rule`

 The rule applies at F with clause size j and heart H: j is the smallest size that has a heart, H
a largest heart for j. 

### `Leaf`

 A leaf: no size up to k has a heart. 

 ### One step and the accounts along a path 

### `lay`

 The clauses of size i. 

### `AddK`

 What one step adds to F: proper subsets of clauses of F, all of one size r ≥ 1, such that every
literal lies in at most d r sets that are
clauses of F of size r or are added. 

### `InvK`

 The invariant along a path. N: the added clauses that are still present; a i: how many clauses
of size i were added so far. Every literal lies in
at most d i clauses of N of size i, and a i is at most the number of clauses of size i in N plus d i
for every smaller clause added so far. 

### `nextN`

 N after a step that adds A. 

### `nextA`

 The counts after a step that adds c clauses of size r. 

### `dg`

 The degree bound that belongs to the thresholds θ: 2·θ(i-1) at size i ≥ 1. 

### `Node`

 What holds of a node F of the tree of φ after p steps, each heavy step adding τ to t. h r counts
the heavy steps with petals of size r. 

 ### The thresholds 

### `Thr`

 What the final count needs of thresholds θ and bounds β: at most β i · n clauses of size i are
added along a path, n the number of variables. 

### `thrPair`

 (θ i, 2 + β 1 + … + β i) by one recursion. 

### `theta`

 The thresholds: θ 0 = 1 and θ (i+1) = τ · β (i+1). 

### `bsum`

 2 + β 1 + … + β i. A path of the tree has at most bsum τ k · n steps. 

### `beta`

 β (i+1) = 2 · θ i · (2 + β 1 + … + β i): at most β i · n clauses of size i are added along a
path. 

### `leafC`

 A leaf has at most leafC τ k · n clauses. 

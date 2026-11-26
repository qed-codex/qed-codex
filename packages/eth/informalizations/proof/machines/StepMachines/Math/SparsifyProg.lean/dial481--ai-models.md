---
{
  "module": "proof/machines/StepMachines/Math/SparsifyProg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SparsifyProg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SparsifyProg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The branching tree of the sparsification lemma of Impagliazzo, Paturi and Zane (compare Lemma 4
of the paper; here with the thresholds of pickP) as plain functions on
List (List (ℕ × Bool)), written with list primitives only (filter, map, all, any, elem, find?, take,
dedup, …), so that
they can be proved polynomial-time piece by piece. At a node that is not a leaf, pickP finds a
clause H and clauses P₁, …, P_r such that every H ∪ Pᵢ is a clause of the node; one child adds H,
the other adds P₁, …, P_r.
The step takes the first applicable literal among the formula's own literals. The lemmas here show
that redP agrees with redLL and that the root rootP ψ satisfies the invariant NodeP. 

### `PLit`

 A literal: (variable, the value that makes it true). 

### `PCl`

 A clause. 

### `PFml`

 A formula. 

### `subP`

 Every literal of D is in C. 

### `overP`

 The clauses of length i that contain all of S. 

### `addP`

 Put A in front and drop the clauses that contain a member of A. 

### `redP`

 The inclusion-minimal clauses. 

### `minusP`

 C without the literals of H. 

### `litsOf`

 The literals of a formula, each once. 

### `canonP`

 The literals of C in the order of ls, each once. 

### `rootP`

 The root: clauses in a normal form, no clause twice, inclusion-minimal clauses only. 

### `greedyP`

 At most k times: the first clause of l that has no literal used so far. 

### `pickP`

 The first applicable of three rules, as a clause H and clauses P₁, …, P_r.
Rule 1: a literal a lies in at least τ clauses of length 2; H = [a].
Rule 2: two different literals a, b lie together in at least τ clauses of length 3; H = [a, b].
In both, the Pᵢ are the first τ of these clauses without the literals of H.
Rule 3: a literal a lies in at least 2τ³ clauses of length 3; H = [a], and the Pᵢ are at most τ² of
these clauses
without a, pairwise disjoint, chosen greedily. 

### `stepP`

 The light child (H added) and the heavy child (P₁, …, P_r added), with H and the Pᵢ of pickP;
none at a leaf. 

### `toF`

 The clauses as finite sets. 

### `NodeP`

 The invariant of the walk: no literal twice in a clause, and a node of the tree of ψ. 

---
{
  "module": "proof/rates/PaddedDescent/F/MarkNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkNet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers, part 2: the network of one profile

Every variable lives at one of g nodes. The clauses are given as a list `Ls` of formulas, the
layers; the layer of a clause is the index of its formula in `Ls` (the paper has no layers:
the network of Step 3 of Appendix D has two kinds of objects instead). The state of a node holds the
values of its variables and one bit, the mark, for every clause that touches the node.
A marked clause must have all its literals false. The nodes that a clause touches form a chain, and
neighbours in the chain compare their marks of the clause, so that only marks are shared
between nodes. A profile prescribes, for every layer, how many marked clauses each node owns and how
many of the marks that two nodes compare are set. Inside a profile the compared marks are
written in a short code (`enc`). The sum of the values of the networks of all admissible profiles is
`trunc`. This file has definitions only. 

 ### The network of one profile 

### `qv`

 Variables per node. 

### `cls`

 All clauses with the index of their layer. 

### `tchB`

 Clause e has a literal whose variable lives at node a. 

### `tch`

 The clauses that touch a, in order. 

### `linkB`

 a < b are neighbours in the chain of the nodes that e touches. 

### `ownB`

 a is the least node that e touches. 

### `tst`

 The clauses of layer i whose marks the nodes a and b compare, in order. 

### `mark`

 The mark that the state word z of node a gives to clause e. 

### `enc`

 The block code: blocks of b bits; a block with j ones is written 1^j 0 and then the j positions,
β bits each. 

### `mu`

 The number that the profile y prescribes for the nodes a, b (a = b: owned marks) and the layer
i. 

### `MCtx`

 ((g, n, β, b in unary), (layers, profile)). 

### `markN`

 The network that markF presents. 

### `adm`

 The profile y is admissible for the cap w, for clauses of at most k literals. 

 ### Sets of marked clauses 

### `WfL`

 The layers are well formed: clauses of 1 to k literals on variables below n. 

### `vset`

 The indices of the clauses that σ violates. 

### `layP`

 The members of P in layer i. 

### `oc`

 The number of members of P in layer i that the node a owns. 

### `pw`

 The number of members of P among the clauses of layer i whose marks a and b compare. 

### `sgnP`

 The sign of P: the first layer does not count. 

### `Match`

 P has the profile y. 

### `nProf`

 The number of numbers y that are tried as profiles. 

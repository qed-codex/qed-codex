---
{
  "module": "proof/sparsification/UniformInK/Spars/Bound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Bound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Bound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The final counts along a path of the sparsification tree

This file proves `StNodeBoundU`: a path has at most (β 0 + … + β (k-1))·n steps, and the count t of
`NodeU`, in which each heavy step of the path counts τ units, is at most k·n.
By the invariant `InvU` every literal lies in at most 2·θ(i−1) added clauses of size i that are
still present, so there are at most 4·θ(i−1)·n of them. With the inequality
`InvU.acc` and `ThrU.step`, induction on i gives that at most β i · n clauses of size i < k are
added along a path.
The section `Count` of proof/sparsification/SparsifyWidthK/Step.lean proves the analogous bound;
there an added clause is charged the same number of removals whatever its size, here 2·θ(i−i') for
size i'. 

### `card_lay_le`

 At most 4·θ(i−1)·n added clauses of size i ≥ 1 are still present. U: the at most 2n literals. 

### `acc_le`

 At most β i · n clauses of size i < k are added along a path. 

### `subset_of`

 If the clauses of φ are subsets of U, so are the clauses of every node. 

### `bound`

 A path has at most (β 0 + … + β (k-1)) · n steps, and the count t of `NodeU`, in which each
heavy step counts τ units, is at most k · n. 

### `stNodeBoundU`

 `Bound.bound`, in the form of the interface. 

---
{
  "module": "proof/sparsification/UniformInK/Tree/Tree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Tree/Tree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Tree/Tree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification lemma for counting with the geometric thresholds

This file proves `StTreeU` of proof/sparsification/UniformInK/Tree/Defs.lean from `StIfaceU` of
proof/sparsification/UniformInK/Spars/Defs.lean. Its proof follows that of `CountKSatRate.stTreeK`
(proof/consequences/CountKSatRate/Tree.lean). The lemma
`CountKSatRate.Tree.tree_of` there holds for all thresholds and bounds that satisfy `Iface` and
`Refines`, and is used here with the thresholds `thetaU τ`, the depth bound `bsumU τ k · n`, a
budget of k·n units
of which a heavy step spends τ, and at most `leafCU τ k · n` clauses in a leaf. As there, τ ≥ k²
bounds the side list by 2n clauses, and `length_occ_le_of_none` of
proof/rates/PaddedDescent/F/MarkDeg.lean bounds the
number of clauses of a leaf in which a variable occurs. 

### `one_le_thetaU`

 Every threshold is at least 1, if τ ≥ 1. 

### `stTreeU`

 From `StIfaceU`: the sparsification lemma for counting at width k with the thresholds `thetaU τ`
and a side list of at most 2n clauses, the interface statement `StTreeU`. 

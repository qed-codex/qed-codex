---
{
  "module": "proof/threesat/Exits/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Procedure Count with line 6, and «Cost» for it

Algorithm 1, line 6: «if m = 0 then return 1». Proof of Theorem 2: «If m = 0 the number is 2^n; let
m ≥ 1.» … «So, with the preparation, Z is computed in time O(2^{δ'm}) plus a polynomial in n».
* `stCountNil`: on the formula without clauses Count returns 1 in one step, at every level.
* `COUNT_polyTimeSteps`: the steps of Count take polynomial time, if those of the algorithm for
  networks and of Clique(ℓ) do.
* `stCountCostOf`: «Cost» for Count, from Lemma 1 for Network(ℓ), the polynomial-time steps of the
  algorithm of Lemma 1, and the bound for Clique(ℓ). For m = 0: one step, and the number of
  satisfying assignments of the formula without clauses is 1 (`Eight.numSat_nil`). For m ≥ 1: the
  paragraph «Cost», which is generic in the algorithm for networks
  (`Eight.ViaGrouping.count_cost_of`, proof/networks/Eight/ViaGrouping/Count.lean). The test of line
  6 costs no step of its own and one unit of size.
`COUNT_polyTimeSteps` is a step inside the proof of `stCountCostOf`, not a statement of
AlgDefs.lean. 

### `stCountNil`

 **Line 6 of Algorithm 1**: «if m = 0 then return 1». On the formula without clauses Count
returns 1 in one step, at every level. 

### `COUNT_polyTimeSteps`

 The steps of Count, at the level ℓ, take polynomial time, if the algorithm for networks keeps
polynomial-time steps and Clique(ℓ) has them. (Section 6: «Z is computed in time O(2^{δ'm}) plus a
polynomial in n». The bound on the number of steps bounds the time only together with this.) 

### `stCountCostOf`

 **Section 6, «Cost», for Count**: «So, with the preparation, Z is computed in time O(2^{δ'm})
plus a polynomial in n». From Lemma 1 for Network(ℓ), the polynomial-time steps of the algorithm of
Lemma 1, and the bound for Clique(ℓ). 

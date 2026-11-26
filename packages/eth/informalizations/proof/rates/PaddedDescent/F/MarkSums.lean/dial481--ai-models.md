---
{
  "module": "proof/rates/PaddedDescent/F/MarkSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkSums.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sums that are cut off, and their product over good layers

An assignment σ violates v clauses of a layer. The inclusion-exclusion sum Σ_j (−1)^j·C(v, j) is 1
if v = 0 and 0 otherwise; cut off at j ≤ w it is still that
as long as v ≤ w (`Tsg_of_le`). Likewise Σ_{j ≤ w} C(v, j) = 2^v as long as v ≤ w (`Tpl_of_le`). The
layers are good (`Good`) if every assignment that satisfies all
later layers violates at most w clauses of a layer. Then, for EVERY assignment, the product of the
signed sums over the layers is 1 if the assignment satisfies all
layers and 0 otherwise (`prod_Tsg`): at the last layer with a violated clause the sum is exact and
is 0, whatever the earlier factors are. So one evaluation
`trunc n w (Λ :: rest)` is the sum of 2^(number of violated clauses of Λ) over the assignments that
satisfy rest (`trunc_of_good`), and with an empty first layer it
is the number of assignments that satisfy all layers (`trunc_nil_cons`). 

### `Tsg_of_le`

 The signed sum cut off at w is exact for v ≤ w: it is 1 if v = 0 and 0 otherwise. 

### `Tpl_of_le`

 The unsigned sum cut off at w is exact for v ≤ w: it is 2^v. 

### `nvio_eq_zero`

 σ violates no clause of L exactly if every clause of L has a true literal. 

### `prod_Tsg`

 For good layers and every assignment, the product of the signed sums is 1 if the assignment
satisfies all layers and 0 otherwise. 

### `trunc_of_good`

 One evaluation on good layers: the sum of 2^(number of violated clauses of the first layer) over
the assignments that satisfy the other layers. 

### `trunc_nil_cons`

 With an empty first layer, one evaluation on good layers is the number of assignments that
satisfy all layers. 

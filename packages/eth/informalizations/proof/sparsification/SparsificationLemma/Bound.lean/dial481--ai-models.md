---
{
  "module": "proof/sparsification/SparsificationLemma/Bound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Bound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Bound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The counts along a path, for thresholds with `ThrC`

This file proves `StThrOfU` (the conditions `ThrU` together with 2 ≤ β 1 imply the conditions
`ThrC`) and `StBoundC`: a path has at most (β 0 + … + β (k-1))·n steps, and its steps of the second
kind use at most
(k−1)·n units, τ each. It follows the argument of proof/sparsification/UniformInK/Spars/Bound.lean,
except in two places.
At size 1 the number of added clauses is bounded directly. By `InvU.acc` it is at most the number of
those that are still present, since no clause of size 0 is ever added, and there are only 2n clauses
of one literal.
In the count of the units, the size r = 0 contributes nothing: a step of the second kind that adds
clauses of size 0 would add θ 0 ≥ 1 of them, and none is ever added. 

### `stThrOfU`

 The conditions `ThrU` together with 2 ≤ β 1 imply the conditions `ThrC`: `ThrC.step` asks at the
sizes i ≥ 2 what `ThrU.step` asks at all sizes i ≥ 1. 

### `acc_le`

 At most β i · n clauses of size i < k are added along a path. 

### `bound`

 A path has at most (β 0 + … + β (k-1)) · n steps, and its steps of the second kind use at most
(k−1) · n units, τ each. 

### `stBoundC`

 `Bound.bound`, in the form of the statement. 

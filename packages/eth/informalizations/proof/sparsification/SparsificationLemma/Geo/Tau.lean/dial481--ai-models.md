---
{
  "module": "proof/sparsification/SparsificationLemma/Geo/Tau.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/Tau.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/Tau.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification theorem for the geometric thresholds, for any τ ≥ 8k that is large enough for ε

`stThmTau` puts together the general theorem `SparsificationLemma.stGen` for the thresholds
`thetaU τ`, «exactly one output» (`SparsificationLemma.stExactlyOne`), the bound on the occurrences
(`stDegGeo`) and the estimate
`WidthK.Thresholds.sum_choose_le_two_rpow` of a sum of binomial coefficients. The general theorem
counts at most (k−1)·n/τ steps of the second kind on a path; here k·n/τ is enough. 

### `le_bsumU`

 k ≤ τ^(2k), if 2 ≤ τ. 

### `stThmTau`

 The theorem for any τ ≥ 8k with (k/τ)·log₂(e·τ·τ^(2k)) ≤ ε. 

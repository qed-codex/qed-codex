---
{
  "module": "Zeta23/PairCeiling/RowCert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/RowCert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/RowCert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/RowCert.lean — an integer certificate format for NEAR-CUE grid laws (NearCUE.lean): from kernel-checkable enclosures
lo_j ≤ K·S(j) ≤ hi_j (j = 1..N, scale K) the checker verifies |N·S(j) − j| ≤ τ for 0 < j < N and |D(1)| = |T_N/N − 1/2| ≤ d₁ with
rational τ = tn/td, d₁ = dn/dd, by pure integer arithmetic; the soundness theorem turns an accepted certificate plus the displayed
hypothesis EnclOK (that the true S lies in the enclosures) into the hypotheses of ceiling_nearCUE.
-/
```

### `RowCertData`

 certificate data: N, scale K, enclosures for j = 1..N, τ = tn/td, d₁ = dn/dd. 

### `rowsOK`

 the row checks: the enclosure of row j+1 lies within τ of j+1 whenever j+1 < N. 

### `sumLo`

 sums of the lower / upper enclosure ends. 

### `checkRows`

 **the checker** (pure integer arithmetic). 

 ## Soundness 

### `rows_sound`

 the row checks give the near-CUE hypothesis on the covered range. 

### `sums_sound`

 the enclosure sums enclose K·(S(j+1) + … + S(j+|l|)). 

### `cert_of_checkRows`

 **soundness of the row checker.** 

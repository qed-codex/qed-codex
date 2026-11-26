---
{
  "module": "proof/rates/CountedRecursion/Totals.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Totals.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Totals.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The totals of the two networks of a pattern

Proof of Theorem A (b), the step from ℓ to ℓ + 1: by Definition 7 (b), display (36) in the proof of
Proposition 3 becomes U = min(U^row, U^col) ≤ N/g + |ℛ|(4ρλ + c·log(2λ)) ≤ N(ρ + 1/g) +
(c/4)g⁴log(2λ).
* `capSum_piecesOf`: c^row_i + c^col_i ≤ 4ρλ + c·log(2λ), for the largest of these sums.
* `totalG_lists`: the totals computed from the lists are those computed from the pieces.
* `totalsAre : TotalsAre`: the totals that the solver compares are the totals U of the two networks
  (`ClauseBound.Alg.GridNet.U_gridN`).
* `smallerTotal : SmallerTotal`: the display, for every g ≥ 2: the minimum is at most the average
  (`ClauseBound.Gen.Chain.total_min_le`), clause (b) of Definition 7, and |ℛ| ≤ g⁴/4. 

### `capSum_piecesOf`

 c^row_i + c^col_i ≤ 4ρλ + c·log(2λ), for the largest of these sums. 

### `totalG_lists`

 The totals computed from the lists are those computed from the pieces. 

### `totalsAre`

 **The totals that the solver compares are the totals U of the two networks.** 

### `smallerTotal`

 **U = min(U^row, U^col) ≤ N/g + |ℛ|(4ρλ + c·log(2λ)) ≤ N(ρ + 1/g) + (c/4)g⁴log(2λ).** 

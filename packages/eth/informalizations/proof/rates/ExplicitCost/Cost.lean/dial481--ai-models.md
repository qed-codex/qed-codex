---
{
  "module": "proof/rates/ExplicitCost/Cost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/Cost.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/Cost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The cost of an entry, with one constant for all K and g

`entryCostExplicit : EntryCostExplicit`, with c₁ = 10. The count of the steps is taken from results
proved elsewhere in this development:
* `Eight.ViaGrouping.Table.tableM_runs` (proof/networks/Eight/ViaGrouping/Table.lean): if every
  group has at most m nodes (here m = ⌊2g/K⌋), the step machine for an entry takes at most
  2^{Pm}·(g²(4τ + 4) + 1) steps, EXPLICIT numbers, and its states are bounded by a sum of products
  of K, g, P, B, L and of sizes. (The constant that depends on K and g enters only in
  `tableM_runs_coarse`.)
* With one-step procedures («ask», with the oracle built in: `Printed.asked_isNetworkP`) this is a
  count of own steps and queries of `Printed.tableQ K g asked` (`Printed.tableQ_close`,
  `QueryMachines.stClose`); at τ operations for a query it is multiplied by τ
  (`QueryMachines.stSlowDown`): `tableQ_within_explicit`.
* The machine that reads K and g runs step for step as `tableQ K g asked`, on states larger by four
  copies of K and g in unary (`mirrors_entryData`).
* For 1 ≤ K ≤ g, x < K^g and L ≤ 2gP all of this is at most (g(P+B))^{10} (`factor_le`,
  `states_le`): each of the two is at most 256·(g(P+B))², and g(P+B) ≥ 2 (`Sizes.sq_le_pow`).
The value of the entry and the strict bound |W̃_γ| < 2^{B'} do not depend on how K and g are given;
they are taken from proof/threesat/Printed (`Printed.stToLists`, `Printed.abs_display_lt`). 

 ## The entry, and its count with explicit numbers 

### `mergedVal_eq_display`

 The integer that the step machine for an entry returns is the display of W̃_γ(Θ). 

### `display_close`

 The display reads only the numbers P_a, c_{a,b} of the procedures. 

### `tableQ_within_explicit`

 **The machine of Lemma 1 for K and g, with explicit numbers**: an entry costs at most
2^{P⌊2g/K⌋}·(8g² + 1)·τ operations. 

 ## The arithmetic 

### `sq_le_pow`

 256·X² ≤ X^{10} for X ≥ 2. 

### `basic_facts`

 What is used of g, P, B: with q = P + B, X = g·q and A = g²·q. 

### `factor_le`

 «each a product of at most g² values»: the factor 8g² + 1 is at most (g(P+B))^{10}. 

### `states_le`

 All states have size at most (g(P+B))^{10}. 

 ## The statement 

### `entryCostExplicit`

 **The cost of an entry, with one constant**: c₁ = 10, for all K, g and all networks. 

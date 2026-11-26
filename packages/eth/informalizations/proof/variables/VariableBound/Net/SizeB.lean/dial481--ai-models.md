---
{
  "module": "proof/variables/VariableBound/Net/SizeB.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/SizeB.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/SizeB.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3, «The parameters»: the size of the weights, and display (69)

`abs_WD_le`: «A marked incidence that touches a is owned by a or has a test at a, so a setting of an
admissible profile has at most (k + 1)M of them; as |σ_i| ≤ 2^i, condition (ii) holds with B = (k + 1)M +
1», for the
weights W_a. In the order of the text: `own_or_test` (owned by a or a test at a), `card_marked_le`
(at most μ_(a,1) + Σ_(b ≠ a) μ_(a,b,1) marked incidences), `sum_mu_le_totP` and `marked_le` (at most
(k + 1)M), `abs_sig_le`
(|σ_i| ≤ 2^i).
`stP`: display (69), gP ≤ 2(n + g)(1 + Δ(t̄ + 3)) + 2(10n + g)·s̄ + g. 

 ### The lists of objects (the same lemmas are in proof/variables/VariableBound/Net/Val.lean) 

### `mem_tch`

 Membership in the list of the objects that touch a. 

### `nodup_tch`

 No object occurs twice in the list of the objects that touch a. 

### `linkB_iff`

 {a, b} with a < b is a test of e iff e touches a and b and no node between them. 

### `ownB_iff`

 a owns e iff e touches a and no smaller node. 

### `mem_tst`

 Membership in the list of the objects of kind i with the test {a, b}. 

### `nodup_tst`

 No object occurs twice in the list of the objects with the test {a, b}. 

### `length_filter_eq_card`

 The length of a filtered list without repetitions is the number of elements of the set that it
lists. 

### `sum_map_range`

 The sum of a list indexed by 0, …, R − 1 as a sum over a finite set. 

 ### A marked incidence that touches a is owned by a or has a test at a 

### `own_or_test`

 Step 3, «The parameters»: an object that touches the node a is owned by a or has a test {c, a}
with a node c < a. 

### `mk`

 The marked incidences that touch a, in the setting z. 

### `okD_spec`

 What a setting of the profile y has: μ_(a,κ) marked objects of kind κ owned by a, and μ_(a,b,κ)
marked objects of kind κ with the test {a, b}. 

### `card_marked_le`

 Step 3, «The parameters»: a setting z of the node a < g in the network of the profile y has at
most μ_(a,1) + Σ_(b ≠ a) μ_(a,b,1) marked incidences. 

### `sum_mu_le_totP`

 The numbers μ_(a,b,κ) of the pairs {a, b} with one fixed node a < g add up to at most μ_κ, the
sum over all pairs. 

### `marked_le`

 Step 3, «The parameters»: «a setting of an admissible profile has at most (k + 1)M of them»
(marked incidences), for well-formed data, a node a < g and a setting z of the network of the
admissible profile y. 

 ### |σ_i| ≤ 2^i 

### `abs_sig_le`

 Step 3, «The parameters»: |σ_i| ≤ 2^i. 

### `abs_prod_sig_le`

 A product of numbers σ_(q_j) is at most 2 to the sum of the q_j in absolute value. 

### `sum_qj_le`

 The numbers q_j of the checks with home a add up to at most the number of marked incidences that
touch a. 

### `abs_WD_le`

 Step 3, «The parameters»: «condition (ii) holds with B = (k + 1)M + 1», for the weights: |W_a(z)|
≤ 2^B for g > 0 nodes, well-formed data, an admissible profile y, every node a < g and every word z. 

 ### Display (69) 

### `mul_qv_le`

 g·⌈N/g⌉ ≤ N + g. 

### `stP`

 Display (69): gP ≤ 2(n + g)(1 + Δ(t̄ + 3)) + 2(10n + g)·s̄ + g, for g > 0, s̄ ≥ 0 and r̄ ≤ 10n,
with P = ⌈2P₀⌉ and P₀ = ⌈n/g⌉(1 + Δ(t̄ + 3)) + ⌈r̄/g⌉·s̄. 

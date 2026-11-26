---
{
  "module": "proof/threesat/Printed/GroupingEntry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/GroupingEntry.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/GroupingEntry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Lemma 1, «Cost», first half: one entry of W̃_γ

Proof of Lemma 1, «Cost»: the sum defining W̃_γ(Θ) has at most (2^P)^{2g/K} = 2^{2gP/K} terms, each
a product of at most g² values; so |W̃_γ| < 2^{B'} with B' = ⌈2gP/K⌉ + g²B, and one entry costs
2^{2gP/K}·poly(P + B)·τ operations.
* `asked_isNetworkP`: the four procedures «ask», with the oracle of a network built in, give that
  network in the sense of `Eight.ViaGrouping.IsNetworkP`, each within ONE step; `size_netInput_le`:
  the input of Definition 2(iii) has size linear in P + B;
* `card_factors_le`, `abs_term_le`: «each a product of at most g² values»; each value is below 2^B,
  so at most 2^B − 1;
* `card_settings_le`: «at most (2^P)^{2g/K} = 2^{2gP/K} terms»;
* `abs_display_lt`: «So |W̃_γ| < 2^{B'}», strictly, as Definition 4 asks (the proof goes through the
  bound 2^{P⌊2g/K⌋ + g²B}, which equals 2^{B'} when K divides 2g);
* `stEntryCost`: the count of `Eight.ViaGrouping.tableM_display` at one step per procedure is a
  count of own steps and queries (`QueryMachines.stClose`, `Printed.tableQ_close`); at τ operations
  per query it is multiplied by τ (`QueryMachines.stSlowDown`). 

 ## The procedures «ask» give the network 

### `getD_ofFn`

 The entry number a of a list written with `List.ofFn`. 

### `size_listOfFn_le`

 A list of g things of size at most M. 

### `asked_mem_close`

 «Is z ∈ S_a?», asked, with the oracle built in: one step, then the answer is read as yes if it
is not 0. 

### `asked_W_close`

 W_a(z), asked, with the oracle built in: one step. 

### `asked_Ψ_close`

 Ψ_{a,b}(z, z'), asked, with the oracle built in: one step. 

### `asked_f_close`

 f_{a,b}(z, θ), asked, with the oracle built in: one step. 

### `c_le`

 c_{a,b} ≤ P, by (i) of Definition 2. 

### `asked_isNetworkP`

 **Definition 2(iii) by queries.** The four procedures «ask», with the oracle of the network N
built in, give N in the context `netInput N P B`, each within one step. 

### `size_netInput_le`

 The input of Definition 2(iii), all numbers in unary, has size linear in P + B. 

 ## «each a product of at most g² values» 

### `three_le_one`

 Of three conditions that exclude one another at most one holds. 

### `card_factors_le`

 A term of the display has at most g² factors: one for each node of the group, one for each pair
of nodes of the group, one for each pair of a node of the group and a node outside. 

### `abs_prod_le_pow`

 A product of n integers, each at most m in absolute value, is at most m^n in absolute value. 

### `one_le_two_pow_sub`

 1 ≤ 2^B − 1 for B ≥ 1. 

### `abs_term_le`

 «each a product of at most g² values»: each value is below 2^B, so a term of the display is at
most (2^B − 1)^{g²} in absolute value. 

### `card_settings_le`

 «The sum defining W̃_γ(Θ) has at most (2^P)^{2g/K} = 2^{2gP/K} terms», with ⌊2g/K⌋, the largest
number of nodes that (G1) allows in a group. 

### `le_bitsOut`

 P·⌊2g/K⌋ + g²B ≤ B'. 

### `abs_display_lt`

 **«So |W̃_γ| < 2^{B'} with B' = ⌈2gP/K⌉ + g²B»**, strictly: at most 2^{P⌊2g/K⌋} terms, each at
most (2^B − 1)^{g²} < 2^{g²B}, since g, B ≥ 1. 

 ## One entry 

### `poly_le`

 D·X + M·X^k ≤ c·X^c. 

### `stEntryCost_of`

 **Proof of Lemma 1, «Cost», first half**, from the coding of a setting of a node of a clique. 

### `stEntryCost`

 **Proof of Lemma 1, «Cost», first half.** 

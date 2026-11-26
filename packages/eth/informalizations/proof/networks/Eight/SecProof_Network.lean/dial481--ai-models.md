---
{
  "module": "proof/networks/Eight/SecProof_Network.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecProof_Network.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecProof_Network.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 6 of the paper, «Proof of Theorem 2»: sentences on the network of Φ

The network of Φ is `Paper.networkOf g Φ` (proof/networks/Paper/SecProof_Proof.lean). This file
gives a statement of its own to sentences of the paragraphs «Clusters, occurrences, equality tests»
and «Cost», in the words defined in
proof/networks/Eight/SecProof_NetworkDefs.lean:
* «Hence Z is the number of assignments of the variables occurring in Φ that satisfy Φ»:
  `network_value_eq`;
* «An occurrence lies in at most two tests»: `card_tests_at_le_two`;
* «The total number of tests is the number of occurrences minus the number of variables that occur,
  hence at most 3m − 1»: `card_tests_add`, `card_tests_le`;
* «U counts each test between two clusters twice, so U ≤ 2(3m − 1) < 6m»: `network_total_eq`,
  `network_total_le_twice`, `network_total_lt`;
* «The remaining factor C₁2^{δ'g}(P + B)^{C₁}τ is polynomial in m, hence O(2^{δ'm/4})»:
  `remaining_factor`;
* the display of the exponent, with its strict inequality: `network_exponent_lt`.
Nothing here depends on Lemma 2 or on its pieces. 

 ## «Z is the number of assignments of the variables occurring in Φ that satisfy Φ» 

### `mem_occurring`

 A variable occurs in Φ if some literal of some clause of Φ is a literal of it. 

### `network_value_eq`

 **Section 6.** «Hence Z is the number of assignments of the variables occurring in Φ that
satisfy Φ.» Z is the value of the network of Φ on g ≥ 1 clusters; Φ has at most 3 literals per
clause. Same as in the paper.
(Empty clauses are allowed here; then both sides are 0.) The proof goes through the sentence before
it, «a term is 1 exactly if all occurrences of each variable carry the same bit and every clause has
a true occurrence»
(`Groundwork.SatNet.value_eq_card_good`), and a bijection between such terms and the satisfying
assignments. 

### `numSat_nil`

 The formula without clauses: no variable occurs, and the one assignment of no variables
satisfies it. 

### `numSat_pos_iff`

 «… and Φ is satisfiable if and only if Z > 0», read off the count: some assignment of the
occurring variables satisfies Φ exactly if some assignment of all variables does. 

 ## «Clusters, occurrences, equality tests»: the number of tests, and the total U 

### `exists_link_of_earlier`

 An occurrence with an earlier occurrence of the same variable is the second occurrence of a
test. 

### `card_tests_at_le_two`

 «An occurrence lies in at most two tests.» Same as in the paper. 

### `card_testsOf_eq`

 There are as many tests as occurrences that are not the first of their variable. 

### `card_first_eq`

 There are as many first occurrences as variables that occur. 

### `card_testsOf_add`

 «The total number of tests is the number of occurrences minus the number of variables that
occur», written without subtraction. 

### `card_out_eq`

 The tests from cluster a to cluster b, counted by their first occurrences. 

### `card_tests_back_eq_zero`

 No test leads from a cluster to an earlier one: the earlier occurrence comes first. 

### `sum_card_tests_eq`

 The tests between two different clusters, sorted by the cluster of the first and the cluster of
the second occurrence. 

### `U_net_eq`

 «U counts each test between two clusters twice», for the network on functions
(`Groundwork.SatNet.net`). 

 ### The same for the network of Φ on g clusters 

### `card_occurrences_le`

 At most 3 occurrences per clause. 

### `card_tests_add`

 **Section 6.** «The total number of tests is the number of occurrences minus the number of
variables that occur». Same as in the paper; written without subtraction. 

### `card_tests_le`

 **Section 6.** «… hence at most 3m − 1», for m ≥ 1. Same as in the paper (also if some clauses
are empty). 

### `network_total_eq`

 **Section 6, «Cost».** «U counts each test between two clusters twice». Same as in the paper. 

### `network_total_le_twice`

 **Section 6, «Cost».** «… so U ≤ 2(3m − 1)», for m ≥ 1. Same as in the paper. 

### `network_total_lt`

 **Section 6, «Cost».** «… < 6m», for m ≥ 1. Same as in the paper. 

### `network_total_nil`

 For m = 0 there is no test, and U = 0. 

 ## «The remaining factor … is polynomial in m, hence O(2^{δ'm/4})» 

### `remaining_factor_query`

 **Section 6, «Cost».** «The remaining factor C₁2^{δ'g}(P + B)^{C₁}τ is polynomial in m, hence
O(2^{δ'm/4})», with P = 6m̄, m̄ = ⌈m/g⌉ (written (m + g − 1)/g), B = 1 and a cost τ ≤ c(m + 1)^c of
a query: for all C₁, c, g and δ' > 0 there is a constant A with C₁·2^{δ'g}·(6m̄ + 1)^{C₁}·c(m + 1)^c
≤ A·2^{δ'm/4} for every m. Same as in the paper, with «polynomial in m» for τ made explicit. 

### `remaining_factor`

 The same with τ = 1, the cost of a query to the network of Φ in the model used here (a value of
W or f is computed in one step; that these steps take polynomial time is
`Groundwork.Prog.satP_keeps`):
C₁·2^{δ'g}·(6⌈m/g⌉ + 1)^{C₁} ≤ A·2^{δ'm/4} for every m. 

 ## «Cost»: the exponent 

### `network_exponent_lt`

 **Section 6, «Cost».** «With e = δ'/12, K ≥ 72 and 1/K ≤ δ'/72, the exponent in Lemma 1 is eU +
e·gP/K + 2gP/K < ½δ'm + (1/144)δ'(m + g) + (1/6)δ'(m + g) = (97/144)δ'm + (25/144)δ'g», from U < 6m
and gP ≤ 6(m + g). Same as in the
paper, with the strict inequality. K ≥ 72 follows from K ≥ 72/δ' and δ' ≤ 1. 

### `network_exponent_lt'`

 «… ≤ ¾δ'm + δ'g.» 

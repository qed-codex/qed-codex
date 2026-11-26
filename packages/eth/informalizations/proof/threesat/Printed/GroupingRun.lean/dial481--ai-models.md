---
{
  "module": "proof/threesat/Printed/GroupingRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/GroupingRun.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/GroupingRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 1 for the algorithm of its proof

Proof of Lemma 1, «Cost»: run the algorithm for (K, e) with L, B' in the roles of λ, B, which is
legitimate because Definition 4 covers all integer tables; answer each of its at most C·2^{eK²L}(B' +
L)^C queries by computing the entry; since K²L ≤ K² + U + gP/K and L ≤ 2gP, the bound follows.
The machine is `groupingMachine K g M` (proof/threesat/Printed/Programs.lean), for ANY machine M
that does what Definition 4 asks (`AchievedBy`). A query of Definition 2(iii) costs τ operations
throughout.
* `subst_within_of`: answering each query by computing the entry: if M takes T operations, a query
  counted as one, and each entry costs at most E operations, the whole costs at most T·(E + 2) (from
  `QueryMachines.StSubst`);
* `optBind_within`, `mapIn_within`: the search first, then the run; the search asks nothing;
* `bitsOut_le_Bp`: B' as a quotient of natural numbers and as the ceiling of a real number;
* `groupingMachine_computes`: the steps put together, for every g ≥ K for which the search finds a
  good grouping; the arithmetic is that of proof/networks/Eight/ViaGrouping/Main.lean
  (`Cost.bound_follows`, `Cost.base_le`);
* `stGroupingTiedOf`: g = 3K⁸. 

 ## The three steps on machines 

### `subst_within_of`

 **Answering each query by computing the entry.** M takes at most T operations, a query counted
as one; N answers each query within E operations at the prices w'. Then M with its queries answered
by N takes at most T·(E + 2) operations at the prices w'. 

### `mapIn_within`

 A function applied to the input. 

### `optBind_within`

 First a step machine R, which asks nothing; if its result is some i, then N on (a, i). 

 ## Arithmetic 

### `bitsOut_le_Bp`

 B' = ⌈2gP/K⌉ + g²B, written with a quotient of natural numbers, is at most the same written with
the ceiling of a real number (they are equal). 

### `poly_le_three`

 D·X + M·X^k + M'·X^k' ≤ c·X^c. 

 ## Lemma 1 

### `groupTables`

 The tables W̃ of the clique of the groups, as Definition 4 takes tables: a function of the
number of the node and of the setting. 

### `clique_groupTables`

 The clique with these tables is the clique of the groups. 

### `run_clique_within`

 **Running the algorithm for (K, e) with L, B' in the roles of λ, B, and answering each query by
computing the entry**: for a good grouping number x, the machine M, given (L, B'), with its queries
answered by `tableQ`, outputs the value of the network within T_M·(E + 2) operations, where T_M ≤
C·2^{eK²L}(B' + L)^C and
E = c₁·2^{P⌊2g/K⌋}·τ is the cost of one entry. 

### `groupingMachine_computes`

 The bound of Lemma 1 for the algorithm of its proof, on networks on [g], for every g ≥ K for
which the search finds a good grouping (hypothesis `hS`; for g = 3K⁸ this is
`Eight.ViaGrouping.StSearch`). 

### `stGroupingTiedOf`

 **Lemma 1 for the algorithm of its proof, from ANY machine that does what Definition 4 asks**,
with the steps of the proof in its hypotheses. 

---
{
  "module": "proof/threesat/Printed/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 6, «Cost», for a machine that does what Lemma 1 says

Section 6: the network of Φ on g clusters satisfies Definition 2 with P = 6m̄ and B = 1; Lemma 1 is
applied to it; «So … Z is computed in time O(2^{δ'm})». Here Lemma 1 is `Printed.ComputesNetworks`
(PrintedStatement.lean): a machine with query access, in which each query of Definition 2(iii) costs
τ operations. Its queries are answered by the procedures of the network of Φ (`formulaProcs`), one
step each.
* `formula_isNetwork`: «Definition 2 holds», with B = 1 handed over;
* `onFormula`: Lemma 1 applied to the network of Φ (through `StOnProcedures`, a hypothesis here);
* `cost_of_bound`: the paragraph «Cost», sentence by sentence, for any step machine that obeys the
  bound of Lemma 1 on the network of Φ. It is the proof of `Eight.ViaGrouping.count_cost_of`
  (proof/networks/Eight/ViaGrouping/Count.lean) after its first line, which does not look at the
  machine again;
* `cost_with_first_line`: line 6 of Algorithm 1, «if m = 0 then return 1»;
* `stCountCost_of`: «Cost» for Count(ℓ). 

 ### «Definition 2 holds» 

### `formula_isNetwork`

 The network of Φ, given by the procedures `formulaProcs`, is a network in the sense of
Definition 2 with parameters P = max{1, 2k·m̄}, B = 1, τ = 1. This is
`Eight.ViaGrouping.satNet_isNetworkP`; what is added is that the procedures hand over B = 1. 

### `formulaProcs_keeps`

 The procedures have polynomial-time steps and the lengths are given in unary. 

### `onFormula_poly`

 A machine for networks with polynomial-time steps, on the network of Φ: polynomial-time steps. 

 ### Lemma 1, applied to the network of Φ 

### `size_under`

 The part of the states that comes from answering the queries by procedures, put under one
constant. 

### `onFormula`

 **Lemma 1, applied to the network of Φ.** If NM does what Lemma 1 says for (K, e) on networks on
[g], then NM, with its queries answered by the procedures of the network of Φ, returns the value Z
of that network within C·2^{eU + (e+2)·gP/K}·(P + 1)^C steps: B = 1 and τ = 1. The bounds are
written as in `Eight.ViaGrouping.Correct.onFormula`; C = 3C₁ + 5 (the 3 is that of `StOnProcedures`:
a query takes τ + 2 ≤ 3τ steps). 

 ### «Cost» 

### `length_lt_size`

 A list is shorter than its size. 

### `cost_of_bound`

 **Section 6, «Cost».** «So … Z is computed in time O(2^{δ'm})», and «Z is the number of
assignments of the variables occurring in Φ that satisfy Φ», for any step machine Mc that returns
the value of the network of Φ within the bound of Lemma 1 with e = δ'/12 and K ≥ 72/δ'. The
sentences of the paper in their order: what Z is (`Eight.network_value_eq`); U < 6m
(`Eight.network_total_lt`) and gP ≤ 6(m + g); the exponent (`Eight.network_exponent_lt'`); the
remaining factor (`Eight.remaining_factor`). The case m = 0 is run through as well (then U = 0, P = 1). 

 ### «if m = 0 then return 1» 

### `cost_with_first_line`

 **Line 6 of Algorithm 1** in front of a machine that counts: the bounds hold with A + 4 in the
place of A. On the formula without clauses the result 1 is the number of satisfying assignments of
no variables (`Eight.numSat_nil`), after one step. 

### `firstLine_poly`

 Line 6 keeps polynomial-time steps. 

 ### Count(ℓ) 

### `stCountCost_of`

 **Section 6, «Cost», for Count**, from «(K_ℓ, e_ℓ) is achievable» by Clique(ℓ), Lemma 1 for the
algorithm of its proof, its polynomial-time steps, and Lemma 1 for networks given by procedures. 

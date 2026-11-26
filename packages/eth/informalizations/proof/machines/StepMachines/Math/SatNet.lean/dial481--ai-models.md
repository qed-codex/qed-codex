---
{
  "module": "proof/machines/StepMachines/Math/SatNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SatNet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SatNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The network of a k-CNF, as in Section 6 of the paper (for k-CNFs, the proof of Theorem A (c)).
The clauses are cut into `g` clusters, the nodes. A state
of a cluster holds a bit for each literal slot, one-bit equalities join consecutive occurrences of a
variable, and the
weight of a cluster checks its clauses. The value of the network (`Network`, Groundwork.Net.Defs)
counts the states at which all weights
and interactions are 1 (`value_eq_card_good`); `good_toState`, `exists_model` and `toState_inj`
relate these states to the models over the occurring variables. 

### `Consec`

 `q` is the next slot after `p` (in the order of `idx`) that carries the variable of `p`. 

### `Consec.succ_unique`

 A slot has at most one successor. 

### `Consec.pred_unique`

 A slot has at most one predecessor. 

### `eq_of_consec`

 Equal on consecutive occurrences implies equal on all occurrences of a variable. 

### `Sl`

 A slot of a cluster: (clause of the cluster, place in the clause). 

### `Slot`

 A slot: a cluster and a slot of it. 

### `idx`

 The place of a slot in the reading order of the formula. 

### `lit`

 The literal written in a slot, if any. 

### `lab`

 The variable written in a slot, if any. 

### `Link`

 An equality test of Section 6 of the paper: `q` is the next occurrence of the variable at `p`. 

### `weight`

 Weight of a cluster: empty slots hold 0, its clauses hold, its internal equalities hold. 

### `Good`

 All weights and interactions are 1 at `z`. 

### `IsModel`

 A model over the occurring variables: satisfies `φ`, and is 0 on the variables that do not
occur. 

### `exists_slot`

 Every literal of every clause is written in some slot. 

### `toState`

 The state that an assignment induces. 

 ### The network 

### `Out`

 The slot `s` of cluster `a` has its next occurrence in cluster `b`. 

### `net`

 The network of `φ`: `g` clusters of `μ` clauses of `k` places. A label of clusters a < b holds a
bit for each
slot of a whose next occurrence is in b (0 at the other slots). 

### `Ψ_of_lt`

 The interaction of clusters a < b is the product of the equalities between them. 

### `value_eq_card_good`

 The value counts the states at which all weights and interactions are 1. 

 ### Sizes 

### `card_used_le`

 At most `k` slots per clause are used. 

### `sum_out_le`

 The equalities that leave cluster `a` forwards. 

### `sum_in_le`

 The equalities that reach cluster `a` from before. 

### `U_net_le`

 The label bits `c a b`, summed over all ordered pairs of clusters (`U`), are at most 2k times
the number of clauses. 

### `sized_net`

 The network has size 2kμ: at most 2^(2kμ) states a cluster and at most 2kμ label bits at a
cluster. All entries
are 0 or 1, so within 2^B for every `B`. 

### `le_mul_ceil`

 `g` clusters of ⌈m/g⌉ clauses hold all `m` clauses. 

### `mul_size_le`

 With μ = ⌈m/g⌉ clauses a cluster, `g` times the size 2kμ of `sized_net` is at most 2k(m+g). 

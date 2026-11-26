---
{
  "module": "proof/networks/Eight/ViaGrouping/SatPsi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/SatPsi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/SatPsi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 6, «Clusters, occurrences, equality tests»: Ψ_{a,b} of the network of Φ, and «Definition 2 holds»

For the definitions of proof/networks/Eight/ViaGrouping/SatPsiDefs.lean, for clauses of at most k
literals (the paper: k = 3):
* «factorized by f_{a,b}(z_a, θ) = [z_a|_b = θ]»: `satF_eq` (the f of the network `wordNet` is this
  function);
* «Put Ψ_{a,b}(z_a, z_b) = [z_a|_b = z_b|_a]»: `satPsi_eq` (this is the Ψ of the network `wordNet`,
  which is defined there as the sum over θ);
* the procedure answers in one step (`satPsiM_runs`), and this step takes polynomial time
  (`satPsi_polyT`, `satProcs_keepsP`);
* «Definition 2 holds», with B = 1 and P = max{1, 2k·m̄} (the paper: k = 3, P = 6m̄):
  `satNet_isNetworkP`, by the bridge `stBridge` of proof/networks/Eight/ViaGrouping/Bridge.lean. 

 ## z_a|_b, f and Ψ 

### `satF_eq`

 «f_{a,b}(z_a, θ) = [z_a|_b = θ]», θ ∈ {0,1}^{c_{a,b}}: the function f of the network `wordNet`
is the one that the paper prints. 

### `satPsi_eq`

 **Ψ of the network of Φ.** «Put Ψ_{a,b}(z_a, z_b) = [z_a|_b = z_b|_a]»: the function `satPsi` is
the Ψ_{a,b} of the network `wordNet` (there: the sum over θ of f_{a,b}·f_{b,a}). 

 ## The procedure: one step, which takes polynomial time 

### `satPsi_polyT`

 A value of Ψ is computed in polynomial time from Φ and the query. 

### `satPsiM_isPolyT`

 The procedure for Ψ has polynomial-time steps. 

### `satPsiM_runs`

 The procedure for Ψ answers a query on two settings in one step, on states of the size within
which the procedures for W and f answer. 

### `satPf_unary`

 P is given in unary. 

### `satProcs_keepsP`

 The procedures of the network of a formula have polynomial-time steps, the lengths P_a, c_{a,b}
and the number P are given in unary. 

 ## «Definition 2 holds» 

### `satNet_isNetworkP`

 **Section 6.** «The network of Φ is the following network on [g] with P = 6m̄ and B = 1. …
Definition 2 holds: Σ_{b ≠ a} c_{a,b} ≤ 2·3m̄ = P, all values are 0 or 1, and τ is polynomial in m».
The network of Φ, with the procedure `satPsiM` for Ψ, is a network in the sense
of Definition 2 (without the part of condition (iii) that gives B to the algorithm as input), with
parameters P = max{1, 2k·m̄}, B = 1, τ = 1; it has the value and the total of the network `wordNet`.
Different from the paper: k literals per clause in place of 3; P ≥ 1 also if Φ has no clause; τ = 1,
since a value is computed in
one step, which takes polynomial time (`satProcs_keepsP`); every string of k·m̄ bits is a setting (a
clause has k places, and W is 0 unless the bits at places without a literal are 0). 

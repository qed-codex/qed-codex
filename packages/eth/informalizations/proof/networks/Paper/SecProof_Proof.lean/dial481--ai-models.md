---
{
  "module": "proof/networks/Paper/SecProof_Proof.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecProof_Proof.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecProof_Proof.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 6 of the paper: formulas as the algorithm holds them, the network of a formula ("Clusters, occurrences, equality tests"), and the bound on its total U 

 ### Formulas inside the algorithm 

### `Formula`

 A formula as the algorithm holds it in memory: a list of clauses, a clause being a list of
literals (number of the variable,
value that makes the literal true). 

### `Formula.Is3CNF`

 Nonempty clauses of at most 3 literals, on the variables x₀, …, xₙ₋₁ (the paper's "3-CNF on n
variables"). 

 ### The network of a formula 

### `clusterSize`

 m̄ = ⌈m/g⌉, the number of clauses of a cluster. 

### `networkOf`

 **The network of Φ** on [g] ("Clusters, occurrences, equality tests"). Cluster a consists of the
clauses number a·m̄, …, a·m̄ + m̄ - 1.
A setting of node a has one bit for each of the 3m̄ positions (3 per clause) of its cluster; W_a is
1 exactly if every clause of the
cluster has a true occurrence, the tests inside the cluster hold, and the bits at positions without
a literal are 0; c_ab is
the number of tests between the clusters a and b, and f_ab(z, θ) = [z restricted to these tests =
θ].
Differences from the paper: every clause has exactly 3 positions, some of which may be empty, and
the occurrences of a variable are
listed in reading order. 

### `network_total_le`

 "U < 6m". (Here: U ≤ 6m.) 

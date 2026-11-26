---
{
  "module": "proof/rates/CountedRecursion/Brute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Brute.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Brute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Brute force, at any price of a query

Proof of Theorem A (b), the case ℓ = 0: brute force sums 2^{λK₀(K₀−1)/2} ≤ 2^{e₀K₀²λ} terms, each at
a cost of at most (K₀(λ+B))^{C₅}. The machine is `Printed.bruteMachine K`: the sum over all choices
of one string per edge of the product over the nodes of the table entries.
A term costs K queries and K + 1 own steps. So if a query costs tq operations, the whole costs
2^{λK(K−1)/2}·(K(tq + 1) + 1), for every tq, also 0 (`brute_within`); all numbers are explicit, for
every K (also K = 1).
The count follows `Groundwork.brute_runs` (proof/machines/StepMachines/Prog/Brute.lean), which is
the same count for step machines. 

### `clique_value_eq`

 The value of the clique as the network of Definition 3 is the sum over one string per edge, for
every K and λ. By `Value.stCliqueValue`, which has no condition on K and λ. (`Printed.stCliqueValue`
says the same for K ≥ 2 and λ ≥ 1.) 

### `brute_within`

 Brute force on K nodes, if a query to the tables costs tq operations. The input is (λ, B) in
unary. 

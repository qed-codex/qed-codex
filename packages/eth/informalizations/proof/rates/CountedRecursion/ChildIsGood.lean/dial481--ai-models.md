---
{
  "module": "proof/rates/CountedRecursion/ChildIsGood.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ChildIsGood.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ChildIsGood.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A call is good

`childIsGoodFrom : ChildIsGoodFrom`. Proof of Theorem A (b): Case (ii) of Lemma 8 applies to the
network with the smaller total (with B₁ in the role of B), so the lemma's L satisfies K²L ≤ U + 2ζN +
K² ≤ (ρ + 3ζ)N + (c/4)g⁴log(2λ) + K². Proof of Lemma 8: the (K, L)-clique with the tables W̃_γ has
the value of the network, and |W̃_γ| < 2^{B'}.
The clauses, in the order of the statement:
* the level, L and B' are read off the context (`at_call`);
* the callee is well formed: L ≥ 1, B' ≥ 1, and |W̃_γ| < 2^{B'} is the second half of
  `EntryCostExplicit`;
* its value is that of the clique of the groups (`child_value`), which is that of the network
  (`ValueIsKept`);
* U is the smaller of the two totals (`TotalsAre`, `total_direction`), which is bounded by
  `SmallerTotal`; then `LabelBound`. 

### `callNet_total_le`

 U = min(U^row, U^col) ≤ … ≤ N(ρ + 1/g) + (c/4)g⁴log(2λ), for the network that the solver takes. 

### `childIsGoodFrom`

 **A call is good**, from Lemma 8 up to the call, its L, the bound on the entries, the fact that
the value of the clique is that of the network, and the printed steps on the network with the
smaller total. 

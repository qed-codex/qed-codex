---
{
  "module": "proof/threesat/Printed/LevelNetworks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelNetworks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelNetworks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Proposition 3: «Both networks satisfy Definition 2», with a table query at the cost of one operation

Proof of Proposition 3, paragraph «Two networks for each ι»: «Both networks satisfy Definition 2
with P = g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the role of B, and with τ = poly(B + λ)».
This development has this sentence for procedures that are step machines
(`Eight.ViaGrouping.levelNetP_isNetworkP`, proof/networks/Eight/ViaGrouping/LevelEnd.lean), for any
procedure R that answers the queries to the tables of the clique within t steps. Here R is «ask the
tables» with the tables built in, and t = 1
(`StAskServes`, a hypothesis of this file); `gridProcs_close` says that the procedures of
proof/threesat/Printed/, with the tables built in, are those of proof/networks/Eight/, and that they
give the printed B₁. So the two networks are networks in the sense of `SecNetworks.IsNetwork`, B₁
given (`grid_isNetwork_of`).
`stBothNetworks_of` reads this for machines with query access (the four procedures as one machine
answer the queries of Definition 2(iii): `answerOf_runs`,
proof/threesat/Printed/GroupingProcs.lean): steps of the machine with the tables built in are own
steps plus queries (`QueryMachines.stClose`). 

 ## Small facts 

### `poly_absorb`

 A polynomial in X ≤ 5Y is at most A'·Y^{A'}. 

 ## The sentence 

### `grid_isNetwork_of`

 **«Both networks satisfy Definition 2 with P = g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the
role of B, and with τ = poly(B + λ)»** (proof of Proposition 3, «Two networks for each ι»), in the
form that the proof of Proposition 3 in this folder uses: Definition 2 is `SecNetworks.IsNetwork`
((iii) as four step machines; B₁ is GIVEN by them), for the procedures `gridProcs` with the tables
of the clique on g² nodes built in: they give the network `levelNetP g tr λ y`, the printed B₁
included, within a·(B + λ)^a steps.
The context is (c, y), where c holds λ and B in unary. The hypothesis: «ask the tables», with the
tables built in, answers in one step. 

### `stBothNetworks_of`

 **«Both networks satisfy Definition 2 with P = g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the
role of B, and with τ = poly(B + λ)»**, a query to the tables counted as one operation. 

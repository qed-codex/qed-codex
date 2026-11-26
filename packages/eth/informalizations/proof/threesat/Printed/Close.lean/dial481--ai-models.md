---
{
  "module": "proof/threesat/Printed/Close.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Close.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Close.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The named machines, with the oracle built in, are the step machines of this development 

### `tableQ_close`

 One entry W̃_γ(Θ): with the oracle built in, `tableQ` is `Eight.ViaGrouping.tableM` on the
procedures with the oracle built in. 

### `sideWQ_close`

 The weight of a row: with the tables built in, `sideWQ` is `Groundwork.Prog.sideWP`. 

### `bruteMachine_close`

 Brute force: with the tables built in, `bruteMachine` is `Groundwork.brute`. 

### `answer_close`

 The four procedures as one machine: `close` goes to each of them. 

### `gridProcs_close`

 The two networks of ι: with the tables built in, `gridProcs` is `Eight.ViaGrouping.levelProcs`,
except that its bound `B` is B₁ = gB + g²λ + 1 of the proof of Proposition 3. 

### `networkOn_close`

 A machine for networks run on procedures that may ask: with the oracle built in, its queries are
answered by the procedures with the oracle built in. 

### `levelMachine_close`

 The algorithm of the proof of Proposition 3: with the tables built in, it is the loop of
`Eight.ViaGrouping.levelAlgP` over the machine `groupingMachine` of Lemma 1. 

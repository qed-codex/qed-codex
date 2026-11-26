---
{
  "module": "proof/variables/FixedWidthSteps/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The end theorems

The premises of the three implications of RouteDefs.lean are fed in: those on numbers from this
folder; the «In particular» of Theorem D (a) from
proof/variables/VariableBound/Printed/ThmVariablesA.lean; the others from
`TwoMachines`, `PairsToBound` and `RecursionToBound`. In Theorem A as a whole, parts (a), (b) and (d)
come from proof/rates/GeneralPieces/ThmRunningTime.lean and the first sentence of (c) from
proof/rates/OccurM/Main.lean. 

### `hypothesisHolds`

 «Its hypothesis holds by (a) and (b)», including the clause that a number in [e_ℓ, 2e_ℓ] can be
computed, which the proviso of Theorem A (c) supplies. 

### `everyChoiceCounts`

 The step of Theorem A (c), second sentence, that rests on the «In particular» of Theorem D (a):
its conditions hold for all but finitely many n, the other n are within the bound, and k ≤ 2 is read
as 3. 

### `countsFromPieces`

 Theorem A (c), second sentence. 

### `runningTimesFromPieces`

 Theorem A, with both sentences of (c) with the printed hypotheses and quantifiers, in steps of a
Turing machine. 

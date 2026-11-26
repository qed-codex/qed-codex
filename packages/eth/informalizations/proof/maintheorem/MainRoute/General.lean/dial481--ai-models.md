---
{
  "module": "proof/maintheorem/MainRoute/General.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/General.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/General.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The chain for every solver, from the statements of its steps

`routeOn_of` proves `RouteOnEverySolver`. It takes the statements of the steps as hypotheses, each
under the name it has where it is proved: Theorem D (a) for every machine that computes the function
of Steps 1 to 5 (proof/variables/RecursionToBound); `EveryChoiceMeetsThmVariablesB`,
`EveryExhaustiveMachineTriesAll`, the front end and the test, the exhaustive machine
(proof/variables/PairsToBound); `EveryAlternationMeetsMinBound`, for counting and for deciding, the
renaming front end, `MinBoundIsTheMainTheorem` (proof/maintheorem/MinOfBounds). The two tools are in
proof/machines/TwoMachines. No arithmetic is done: each field is an application of the statement of
its step to the objects of the steps before. The solver, its levels and the function for
the bound in m are arbitrary. 

### `routeOn_of`

 The chain for every solver, from the statements of the steps. 

---
{
  "module": "proof/rates/CountedRecursion/Answers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Answers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Answers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Answers read by a function; prices raised

Facts on machines with query access; runs and costs are followed by induction over a run or over the
list of its queries:
* `readAsRuns`, `readAsPoly`: `readAs r M` runs as M does, if the new oracle, read by r, is the old
  one; and it has polynomial-time steps if M has and r is polynomial-time.
* `pricesScale`: if every price is raised at most k times, so is the cost. 

### `readAs_reaches`

 `readAs r M` runs as M does (from a state). 

### `readAsRuns`

 `ReadAsRuns`. 

### `readAsIsPolyQ`

 The certificate of `readAs r M`. 

### `readAsPoly`

 `ReadAsPoly`. 

### `sum_map_le_mul`

 The sum of the prices of a list of queries, if every price is raised at most k times. 

### `pricesScale`

 `PricesScale`. 

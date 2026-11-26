---
{
  "module": "proof/machines/StepMachines/Prog/Range.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Range.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Range.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Loops over y < N a (N a possibly huge, y a binary natural): fold, sum, product, «first». 

### `rangeStart`

 The first point of the loop over y < N a. 

### `rangeNext`

 The next point of the loop over y < N a. 

### `rangeG`

 g, seeing only the counter of the point. 

### `foldRange`

 The loop over y = 0, 1, …, N a - 1; the body sees (a, y). 

### `foldRange_runs`

 The body takes t y steps on (a, y) and returns v y. Steps of the loop: Σ_{y < N a} (t y + 1).
Result: the fold of g
over y = 0, …, N a - 1. Sc bounds the size of the accumulator, Sm the size inside the body. 

 ### Sum 

### `addG`

 The accumulator of a sum. 

### `zeroC`

 The start of a sum. 

### `sumRange`

 Σ_{y < N a} M(a, y). 

### `sumRange_runs`

 Steps: Σ_{y < N a} (t y + 1). Result: Σ_{y < N a} v y. V bounds every |v y|. 

 ### Product 

### `mulG`

 The accumulator of a product. 

### `oneC`

 The start of a product. 

### `prodRange`

 ∏_{y < N a} M(a, y). 

### `prodRange_runs`

 Steps: Σ_{y < N a} (t y + 1). Result: ∏_{y < N a} v y. V ≥ 1 bounds every |v y|. 

 ### «The first index whose result passes the test» 

### `firstG`

 The accumulator of «first». 

### `noneC`

 The start of «first». 

### `firstRange`

 The least y < N a such that p holds of M(a, y), if there is one. 

### `firstRange_runs`

 Steps: Σ_{y < N a} (t y + 1); the loop does not stop early. Result: the least y < N a such that
p holds of v y. 

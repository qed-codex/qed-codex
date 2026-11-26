---
{
  "module": "proof/machines/StepMachines/Math/RebalanceArith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/RebalanceArith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/RebalanceArith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Arithmetic for the size bound of the rebalancing. A network on g nodes, each with
at most 2^P states and P label bits, with U label bits over all ordered pairs and B-bit weights, is
merged into an
instance of the problem on K nodes with β ≤ 1 + U/K² + gP/K³ bits per edge. From this bound on β
follows β ≤ 3gP. The size bound takes
natural numbers with S' ≤ S + c₁(sc+P+B)^{c₁}, sc' ≤ c₁(sc+P) and Stot ≤ c₁(sc+P+B)^{c₁} + S' +
A(sc'+B'+β)^A to Stot ≤ S + A'(sc+P+B)^{A'}. 

### `beta_le`

 β ≤ 3gP. 

### `size_le`

 The sizes in the rebalancing. Here S, S', sc, sc' and Stot are natural numbers tied only by the
hypotheses: S' ≤ S + c₁(sc+P+B)^{c₁}, sc' ≤ c₁(sc+P) and Stot ≤ c₁(sc+P+B)^{c₁} + S' +
A(sc'+B'+β)^A. Then Stot exceeds S by at most a polynomial in sc + P + B. 

---
{
  "module": "proof/machines/StepMachines/Prog/BruteE.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/BruteE.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/BruteE.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Two facts about evaluators of Z, the sum over all labellings of the edges: `Correct K ε` (Z in
about 2^{ε·K²·λ} steps) is monotone in ε,
and brute force, the loop over all labellings of the edges, is correct with ε = 1/2. 

### `nilC`

 The default word, as a function of the context. 

### `bruteE`

 Brute force (`brute`, the loop over all labellings of the edges) as an evaluator. 

### `Evaluator.Correct.mono`

 `Correct K ε` is monotone in ε. 

### `bruteE_correct`

 Brute force is correct with ε = 1/2: it loops over the 2^{(K(K-1)/2)·λ} labellings, and K(K-1)/2
≤ K²/2. 

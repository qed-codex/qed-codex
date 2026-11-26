---
{
  "module": "proof/variables/VariableBound/Net/StepCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/StepCost.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/StepCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 4 of Appendix D: the number of bits with which the clique solver is called

Step 4 of Appendix D: «Take a network on [g] with parameters P, B, τ and total U, and let L = ⌈(U +
gP/K)/K²⌉ and B′ = ⌈2gP/K⌉ + g²B.» The program calls the clique solver with the label length
`lamS K g U P` and the number of bits
`bitsS K g P B` of proof/rates/ClauseBound/Alg/TopNet.lean, which serve every network. This file
computes the second on g = 3K⁸ nodes: 2g/K = 6K⁷ (`two_g_div`), and so
bitsS = 6K⁷P + (6K⁸ + 36K¹⁵)B (`bitsS_eq`). 

### `two_g_div`

 2g/K = 6K⁷ for g = 3K⁸ and K ≥ 1. 

### `bitsS_eq`

 On g = 3K⁸ nodes, K ≥ 1, the number of bits of the program is 6K⁷P + (6K⁸ + 36K¹⁵)B. 

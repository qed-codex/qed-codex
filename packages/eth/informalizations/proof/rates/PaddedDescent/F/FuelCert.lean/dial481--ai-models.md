---
{
  "module": "proof/rates/PaddedDescent/F/FuelCert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/FuelCert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/FuelCert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The certificates for Fuel.lean: `rng`, `sumF`, `prodL`, `cap` are polynomial-time, and so is
every fold whose state is capped by the
pad after each round (`foldl_cap`), without any side condition. `Unary` is made a second property
for the tactic `fun_prop`, so that side goals
«this number is given in unary» are found by the tactic. 

 ### Unary as a property for fun_prop 

### `replicate_polyT`

 A number given in unary, written out as a list of units. 

 ### rng, sums and products 

 ### The length of a word, the cap, the capped fold 

### `foldl_cap`

 A fold whose state is capped by the pad after every round is polynomial-time, with no side
condition. 

---
{
  "module": "proof/rates/ClauseBound/Both/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Both/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Both/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The running time of the padding machine against the bound in n and the bound in m: statements

Two algorithms are functions of (input, pad), and both compute from the input the exponent of a pad
that suffices (`eM` of proof/rates/ClauseBound/Alg/Top.lean for the bound in m, `eO` of
proof/rates/ClauseBound/ParityChecks/TopDefs.lean
for the bound in n). `StTimeO` and `StTimeM` say that q·(|x| + 2^e + 1)^q, for the exponent e of the
one or of the other, is within the bound in n, respectively within the bound in m (there when every
variable occurs and there is a clause). 

 ### The running time of the padding machine against the two bounds (TimeM.lean for the bound in m) 

### `StTimeO`

 For the exponent of the algorithm for n: q·(|x| + 2^e + 1)^q is within the bound in n, for a
suitable c, every n₀ and every q. 

### `StTimeM`

 For the exponent of the algorithm for m. 

---
{
  "module": "proof/machines/Tower/Toy/Machines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Toy/Machines.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Toy/Machines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A toy recursion: the certificates

The ten functions of the two machines (Toy/Defs.lean) are written with eliminators and «if», so
`fun_prop` proves nine of them polynomial-time as they stand; the tenth, the step of the procedure,
is the identity and is certified by `PolyT.id'`. The tower has its certificate from `towerPoly`. 

### `solIsPoly`

 The certificate of the solver. 

### `innIsPoly`

 The certificate of the procedure. 

### `toyPoly`

 The tower of the toy has polynomial-time steps; the depth is part of its input. 

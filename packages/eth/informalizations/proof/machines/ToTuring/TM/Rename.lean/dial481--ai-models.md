---
{
  "module": "proof/machines/ToTuring/TM/Rename.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Rename.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Rename.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 A fragment written for few stacks, run on some of the stacks of a machine with more: stacks are
renamed along an injective
map, and the stacks outside its image are not touched. All stacks have one alphabet A. 

### `renK`

 The statement on the renamed stacks. 

### `Frag.ren`

 The fragment on the renamed stacks. 

### `agree_update`

 Stacks that agree along φ still agree after the same stack was overwritten on both sides. 

### `stepAux_renK`

 One statement: on stacks that agree along φ, the renamed statement ends at the same label with
the same local state, on
stacks that agree along φ, and it leaves the stacks outside the image of φ alone. 

### `run_renK`

 Runs of a machine become runs of the renamed machine. 

### `Frag.ren_runs`

 If S and S' agree with T and T' along φ and with each other outside the image of φ, a run of P
from T to T' becomes a
run of `P.ren φ` from S to S' with the same number of steps. 

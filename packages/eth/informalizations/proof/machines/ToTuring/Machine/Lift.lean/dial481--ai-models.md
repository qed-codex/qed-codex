---
{
  "module": "proof/machines/ToTuring/Machine/Lift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Machine/Lift.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Machine/Lift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The stacks of the final machine: the four work stacks and one stack of bits, for input and
output (Mathlib asks that the
alphabets of the input stack and of the output stack be in bijection with Bool). A fragment over the
work stacks runs in the
final machine and does not touch the stack of bits. 

### `Γio`

 The alphabets of the final machine: bits on `none`, Sym on the work stacks. 

### `liftIO`

 A statement over the work stacks, in the final machine. 

### `Frag.io`

 A fragment over the work stacks, in the final machine. 

### `withIO`

 The contents of the five stacks: the bits W, and S on the work stacks. 

### `update_withIO`

 Overwriting a work stack commutes with adding the stack of bits. 

### `liftCfg`

 A configuration over the work stacks, in the final machine with the bits W. 

### `stepAux_liftIO`

 A statement, lifted to the final machine, does what it does over the work stacks alone, and does
not touch the bits. 

### `run_liftIO`

 Runs over the work stacks are runs of the final machine. 

### `Frag.io_runs`

 A run of a fragment over the work stacks is a run of the same length of `P.io`, and leaves the
bits W as they were. 

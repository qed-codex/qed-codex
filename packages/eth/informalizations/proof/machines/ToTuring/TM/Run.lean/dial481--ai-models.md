---
{
  "module": "proof/machines/ToTuring/TM/Run.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Run.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Run.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Runs of exactly n steps of a partial step function, and a statement of one of Mathlib's
multi-stack machines (`Turing.TM2`)
placed in a larger machine with more labels. 

 ### Runs of exactly n steps 

### `Run`

 n steps of f lead from a to b. 

### `Run.iterate`

 The same in Mathlib's form (`StateTransition.EvalsTo`): n iterations of `flip bind f` lead from
`some a` to `some b`. 

 ### A statement placed in a larger machine 

### `place`

 Labels are carried along ι; where the statement would halt, the larger machine goes on at e (or
halts if e = none). 

### `placeCfg`

 The same for configurations. 

### `run_place`

 If the larger machine M' holds the placed statements of M, every run of M is a run of M' of the
same length. 

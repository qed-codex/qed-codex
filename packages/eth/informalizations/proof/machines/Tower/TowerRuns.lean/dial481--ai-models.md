---
{
  "module": "proof/machines/Tower/TowerRuns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/TowerRuns.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/TowerRuns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Runs of the tower

A run of the solver, with its calls and queries answered as the specification says, is a run of
`nest Sol Inn` with the list env beside every state (`sol_sim`); the same for the procedure
(`inn_sim`). So `nest Sol Inn` meets the hypothesis of
`SelfCallRuns` with the good inputs, values, depths and costs of `Chain.lean` (`nest_within`), and
`TowerRuns` is its conclusion on the input `Sum.inl ([], c)`. 

### `NSt`

 The states of `nest Sol Inn`. 

### `sol_sim`

 A run of the solver on the instance at the end of a chain is a run of `nest Sol Inn` with the
list env beside every state, at the prices of `Chain.lean`. 

### `inn_sim`

 The same for a run of the procedure. 

### `nest_within`

 `nest Sol Inn` meets the hypothesis of `SelfCallRuns`. 

### `tower_reaches`

 The tower has the runs of `selfCall (nest Sol Inn)`. 

### `towerRuns`

 The tower returns the value of every well-formed instance, at the cost of the recursion. 

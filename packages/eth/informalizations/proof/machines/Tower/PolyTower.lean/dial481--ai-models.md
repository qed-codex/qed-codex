---
{
  "module": "proof/machines/Tower/PolyTower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/PolyTower.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/PolyTower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates of polynomial-time steps for `nest Sol Inn` and for the tower

The states of `nest Sol Inn` are pairs of a list of contexts and a state of the solver or of the
procedure; the five functions of `nest` call those of `Sol` and `Inn` once and move the list. The
tower has the states, step, result, query
and resumption of `selfCall (nest Sol Inn)`, so its certificate is that of `Poly.lean` with another
start. 

### `upQuery_poly`

 Where a query goes is computed in polynomial time from the list and the query. 

### `nest_init_poly`

 The start of `nest Sol Inn`. 

### `nest_step_poly`

 Its step. 

### `nest_out_poly`

 Its result. 

### `nest_ask_poly`

 Its query. 

### `nest_resume_poly`

 How it goes on with an answer. 

### `nestIsPoly`

 The certificate of `nest Sol Inn`. 

### `towerIsPoly`

 The certificate of the tower. 

### `towerPoly`

 The tower has polynomial-time steps, once and for all depths, if the solver and the procedure
have. 

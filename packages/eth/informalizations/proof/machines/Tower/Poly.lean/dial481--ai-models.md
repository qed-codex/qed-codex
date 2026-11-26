---
{
  "module": "proof/machines/Tower/Poly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Poly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Poly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Polynomial-time steps of `selfCall M`

The states of `selfCall M` are lists of states of M, written as lists of their words (the instance
of `Enc` for lists over the coding that comes with the certificate of M). One step looks at the
first two entries of the list only, and
calls a bounded number of the five functions of M on them; so it is a composition of polynomial-time
functions, whatever the length of the list. Each function is first written with eliminators (the
form in which the tactic `fun_prop`
knows the closure lemmas), then shown equal to the definition by cases. The coding of the states of
M is found through the instance `IsPolyQ.under` of proof/machines/QueryMachines/Poly.lean. 

 ### A machine that calls itself 

### `rstep_poly`

 One step of the stack. 

### `rask_poly`

 The query of the whole. 

### `rresume_poly`

 The answer goes to the running activation. 

### `rout_poly`

 The result of the whole. 

### `selfCallIsPoly`

 The certificate of `selfCall M`. 

### `selfCallPoly`

 `selfCall M` has polynomial-time steps, once and for all depths of the recursion, if M has. 

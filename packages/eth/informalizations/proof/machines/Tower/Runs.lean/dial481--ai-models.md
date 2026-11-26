---
{
  "module": "proof/machines/Tower/Runs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Runs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Runs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Runs of `selfCall M`

The lemma `selfCall_from` is about a run of M from any state s on the input a, with any stack K of
waiting activations below it and any continuation: if the whole reaches b within tk operations once
the running activation has halted
with `val a`, then it reaches b from `s :: K` within the cost of M's run plus tk. Strong induction
on the depth outside (a call is a run of M on an input of smaller depth, on the stack `s :: K`),
induction on the run inside. The bound on
the sizes is a hypothesis of the lemma: the stack below, and room for `dep a + 1` activations more. 

 ### One step of the stack, case by case 

### `rout_none`

 While the running activation has not halted, the whole has not. 

### `rask_halted`

 A halted activation asks nothing. 

### `rask_none`

 An activation that asks nothing: the whole asks nothing. 

### `rask_call`

 A call is not a query of the whole. 

### `rask_query`

 A query that is not a call is the query of the whole. 

### `rstep_step`

 An own step of the running activation. 

### `rstep_call`

 A call starts a new activation on top. 

### `rstep_pop`

 The result of a halted activation goes to the one below it. 

### `size_stack`

 The size of a stack. 

 ### The run 

### `selfCall_from`

 A run of M from any state, on any stack of waiting activations and with any continuation (see
the head of this file). 

### `selfCallRuns`

 `selfCall M` returns `val a` within `T a` operations on every good input a. 

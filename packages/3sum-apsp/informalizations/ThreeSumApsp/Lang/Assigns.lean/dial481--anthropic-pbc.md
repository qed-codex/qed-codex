---
{
  "module": "ThreeSumApsp/Lang/Assigns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Assigns.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Assigns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A statement changes only the local variables that it assigns

`s.assigns` lists the local variables that the statement `s` assigns: the targets of its
assignments and the result variables of its calls.  A run of `s` leaves every other local variable
as it was (`Exec.loc_eq_of_notMem_assigns`), so every fact about `s` may be extended by "all other
locals are as before" (`Ends.keeping`).  A lemma about a piece of program text therefore speaks
about the memory and about the locals that the piece assigns, and about no other local.


### `Stmt.assigns`

 The local variables that a statement assigns: the targets of its assignments and the result
variables of its calls. 

### `Exec.loc_eq_of_notMem_assigns`

 A run leaves a local variable that the statement does not assign as it was. 

### `Ends.keeping`

 **All other locals are as before.**  Whatever holds after a statement, it also holds that the
locals that the statement does not assign are unchanged. 

### `Ends.keepingBut`

 **All other locals are as before**, for a list `xs` that contains the locals that the statement
assigns. 

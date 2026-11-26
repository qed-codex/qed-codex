---
{
  "module": "ThreeSumApsp/Lang/Renumber.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Renumber.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Renumber.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Two programs in one: relocation of procedures

A program grows by appending procedures.  To put two programs, each with its own numbering of
procedures, into one, the second is placed behind the first (`Program.behind`), and the numbers of
the procedures that it calls are shifted by the length of the first (`Stmt.shift`).

A run of a statement in P is then a run of the shifted statement, with the same states and the
same number of steps (`Exec.shift`, an induction on the run in which only the case of a call has
anything to do: `Program.getElem?_behind_right`).  So everything proved with `Ends` carries over
(`Ends.shift`, `Ends.shift_append`).


### `Stmt.shift`

 The statement with n added to the number of every procedure that it calls. 

### `Program.behind`

 The program P placed behind the program Q. 

### `Program.getElem`

 Procedure p of P is procedure `p + Q.length` of P placed behind Q, with its calls
shifted. 

### `Exec.shift`

 **Relocation.**  A run in P is a run, with the same states and the same number of steps, of
the shifted statement in P placed behind Q. 

### `Ends.shift`

 What is proved about a statement in P holds for the shifted statement in P placed behind
Q. 

### `Ends.shift_append`

 The same with more procedures appended behind. 

---
{
  "module": "ThreeSumApsp/Lang/RunsStayInLimits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/RunsStayInLimits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/RunsStayInLimits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Runs stay within their limits

Facts about the semantics of the light language; none of them mentions the compiler.  A state is
bounded if every variable and every cell holds a number of absolute value at most `lim.word`.

* The value of a safe expression in a bounded state is such a number (`Expr.abs_val_le`).
* A run that starts in a bounded state ends in one (`Exec.bounded`): induction on the run.  An
  assignment and a store write the value of a safe expression; a call starts in a frame that holds
  the values of safe expressions and zeros (`bounded_callFrame`, a case of `bounded_frame`).
* A run does not change the cells from `lim.space` on (`Exec.mem_outside`).

The compiler's proof needs the first two because a word of the machine stands for a number only as
long as the number is in the range of words, and the third because its end theorem speaks of all
cells of the memory, also of those that the run may not touch.


### `abs_update_le`

 Writing a bounded number into a bounded function. 

### `Expr.abs_val_le`

 The value of a safe expression in a bounded state fits in a word. 

### `bounded_frame`

 A frame that holds words, over a memory that holds words, is a bounded state. 

### `bounded_callFrame`

 The state in which a procedure starts is bounded, if the state of the caller is bounded and the
arguments of the call are safe. 

### `Exec.bounded`

 A run that starts with words in all variables and cells ends with words in all of them. 

### `Exec.mem_outside`

 A run does not change the cells from lim.space on. 

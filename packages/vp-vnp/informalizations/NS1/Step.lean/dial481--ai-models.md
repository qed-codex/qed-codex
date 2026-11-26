---
{
  "module": "NS1/Step.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Step.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Step.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One round

A program that guesses budgets, multiplies by the powers of the constants, forms a plain instance, cuts it into
pieces, and applies a given program to every piece.


### `sumF`

 Sums over runs, with a function of the value. 

### `app`

 Apply a fixed program. 

### `LP`

 Apply the program `D` to all trees of a list. The argument is (this program, the list). 

### `zq`

 The plain instance for a program `p`, an argument `z` and budgets `t`. 

### `ZE`

 Form the plain instance: `fp` gives the program, `g` guesses the budgets. 

### `stepF`

 One round: guess budgets, multiply, form the plain instance, cut it with `G`, apply `D` to the pieces. 

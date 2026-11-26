---
{
  "module": "NS1/Eval.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Eval.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Eval.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The interpreter

`IF` at `(IF, (f, (x, t)))` simulates the formula `f` at `x` with the budgets `t`; its value is the value of the run
and the budgets that are left.


### `lett_rel`

 `let`, for lists that correspond to other lists. 

### `selF`

 Choose by the length of the value of `b`. 

### `fF`

 The formula in the environment. 

### `fX`

 The argument in the environment. 

### `fS`

 The budgets in the environment. 

### `fO`

 The opcode. 

### `fA`

 The arguments of the formula. 

### `rec'`

 Recursive call. 

### `call1`

 First call, with the environment kept. 

### `call2`

 Second call, with everything kept. 

### `caseL`

 The cases of the interpreter. 

### `IF`

 The interpreter. 

### `env`

 The environment of the interpreter. 

### `rec_ev`

 A recursive call. 

### `simS`

 The runs that stay within the budgets, with what is left. 

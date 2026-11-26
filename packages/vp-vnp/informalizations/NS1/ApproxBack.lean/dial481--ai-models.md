---
{
  "module": "NS1/ApproxBack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxBack.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxBack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# An approximate accelerator gives an exact one

The program that reads the coefficient of ε^0 out of an approximate accelerator, its constants and its size.


### `KV.app_rel`

 Runs that give values with weights, then a formula at the values. 

### `finF`

 Accept only with the counter at 0; then run the plain instance. The argument is (argument, (budgets, counter)). 

### `extF`

 The program of the extraction: guess with `g`, then check the counter and run the plain instance. 

### `extF_kv`

 **The value of the extraction.** 

### `xcst`

 The sizes of the fixed programs of the extraction. 

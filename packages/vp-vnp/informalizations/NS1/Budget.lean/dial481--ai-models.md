---
{
  "module": "NS1/Budget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Budget.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Budget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Budgets

A budget is a trie with numbers (in binary, lowest digit first) at its leaves; the leaves are named by the paths.


### `Bt`

 Budgets. 

### `Bt.none`

 no name 

### `Bt.leaf`

 a name with a number 

### `Bt.node`

 names that begin with 0, names that begin with 1 

### `decw`

 Subtract 1. 

### `dec`

 Subtract 1 at a name. 

### `decAll`

 Subtract 1 at all names of a bill. 

### `zero`

 All numbers are 0. 

### `ht`

 A bound for the time to subtract 1. 

### `nds`

 The number of nodes and digits. 

### `enc`

 Budgets as trees. 

---
{
  "module": "NS1/Util.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Util.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Util.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Words of trees, parts of lists, choices, straight-line programs


### `wordT`

 The brackets of a tree, in preorder; `t0`: empty, `t1`: a node. 

### `wordB`

 Write the brackets of a tree in front of a list. The argument is (this program, (tree, list)). 

### `wordF`

 The brackets of a tree. 

### `nzB`

 Is a number not 0? The argument is (this program, number). 

### `takeB`

 Take elements from a list, as many as a binary number says. The argument is (this program, (number, (elements
taken, in reversed order, list))); the value is (elements taken, rest). 

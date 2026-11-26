---
{
  "module": "Nc/Acc/Loop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Acc/Loop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Acc/Loop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The program that guesses a parse tree

The argument of the loop is (the loop, (budget, (stack of gates, tree of pairs of letters))).


### `appBits_gives`

 Concatenation of lists of bits. 

### `gwd`

 Guess a word. 

### `stepW`

 A step of the walk. The argument is (tree, path so far, reversed). 

### `walkF`

 Guess a path in a tree. 

### `lc`

 The code of a letter. 

### `topF`

 The gate on top of the stack; the argument is (argument of the loop, anything). 

### `nameL`

 The name of the weight of an input. 

### `nameK`

 The name of the weight of a product gate. 

### `leafB`

 An input is read. 

### `intB`

 A product gate. 

### `leafF`

 Guess an input. 

### `intF`

 Guess a product gate. 

### `loopF`

 The loop. 

### `loopF_kv`

 **The loop computes the sum over the parse trees.** 

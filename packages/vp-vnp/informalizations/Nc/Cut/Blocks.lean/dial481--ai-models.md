---
{
  "module": "Nc/Cut/Blocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/Blocks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/Blocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Blocks of a run

A run of `K * T` steps is cut into `K` blocks of `T` steps. The value of the automaton is a sum, over the states
between the blocks, over the ways to cut the inputs, and over the common segments `X s α β` written on tape `s`
by block `α` and read by block `β` (staircase support), of the product of the weights of the blocks.


### `prod_path`

 A product of matrices as a sum over paths. 

### `blockW`

 The weight of the blocks of `T` steps from `q` to `q'` that emit `v`. 

### `wordsLe`

 Words of length at most `T`. 

### `blockW_ne_zero`

 A block emits at most `T` letters on a channel. 

### `runVal_blocks`

 The value as a sum over states and over what the blocks emit. 

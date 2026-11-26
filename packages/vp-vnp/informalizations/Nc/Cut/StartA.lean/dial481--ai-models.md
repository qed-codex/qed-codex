---
{
  "module": "Nc/Cut/StartA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/StartA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/StartA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Start, I: segments

For given states between the blocks, the sum over what the blocks emit is a sum over the common segments of the
parties on all tapes, with staircase support.


### `blockW_sum_le`

 A block emits at most `T` letters in all. 

### `partyW_sum_le`

 A party writes at most `T` letters in all. 

### `segW`

 The product of the weights of the parties. 

### `segs`

 Segments of at most `T` letters. 

### `segW_ne_zero`

 What the non-vanishing of the product of the weights means. 

### `sum_segs`

 **Segments.** 

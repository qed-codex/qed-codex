---
{
  "module": "Nc/RunWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/RunWord.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/RunWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Places of letters in runs and in the code of the inputs


### `emit_getElem`

 The letter that is emitted at a step sits at the place counted before the step. 

### `exists_emit`

 Every letter of a channel is emitted at some step. 

### `wordOf`

 The words one after the other, each followed by a separator. 

### `base`

 The place of the first letter of word `k`. 

### `eq_of_read`

 A code that is read at all places of `v` is the code of `v`. 

### `code`

 The one-hot code of the inputs. 

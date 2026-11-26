---
{
  "module": "proof/consequences/CountKSatRate/Stack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Stack.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Stack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The length of the word of a state of the counting walk

`stackLenC k τ n m` bounds the length of the word of a state of the counting walk at width k
(`stStateLen`, which proves the interface statement `StStateLen` of
proof/consequences/CountKSatRate/Interfaces.lean). The bounds for the word of a list and of a
formula, `len_list_le` and `len_fml_le`, are those of `proof/rates/PaddedDescent/F/Top.lean`. 

### `stStateLen`

 The word of a state of the counting walk has length at most `stackLenC k τ n m`. 

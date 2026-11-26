---
{
  "module": "proof/rates/PaddedDescent/F/LenList.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/LenList.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/LenList.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Three small facts about lists: the length of the word of a list whose members are short, the
length of a `flatMap`, and a sum over a
`flatMap`. They are used for the work list of the descent and for the stack of the walk. Here `len`
is the length of the word that stands
for a value on a stack. 

### `len_list_le`

 A list of k values, each with a word of length at most c − 2, has a word of length at most k·c + 2. 

### `len_list_le'`

 The same when only a bound k on the number of members is known. 

### `length_flatMap_le`

 If e a has at most c members for every member a of w, then w.flatMap e has at most (length of
w)·c members. 

### `sum_map_flatMap`

 The sum of z over w.flatMap e is the sum, over the members a of w, of the sums of z over e a. 

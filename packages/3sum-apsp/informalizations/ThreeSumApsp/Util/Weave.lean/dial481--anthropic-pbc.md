---
{
  "module": "ThreeSumApsp/Util/Weave.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Weave.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Weave.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Interleaving two strings of digits along a mask

A mask is a list of truth values, one for each level.  `weaveList mask outer inner` runs through the
levels and takes the next digit of `inner` at a level with the entry `true` and the next digit of
`outer` at a level with the entry `false`.  A program that forms the number with these digits by
Horner's rule needs one pass over the mask and two pointers: at level `ℓ` the pointer into `inner`
has passed as many digits as there are entries `true` among the first `ℓ` entries of the mask, and
the pointer into `outer` as many as there are entries `false` (`getD_weaveList`).


### `weaveList`

 Two lists of digits interleaved along a mask: at a level with the entry `true` stands the next
digit of `inner`, at a level with the entry `false` the next digit of `outer`.  A missing digit
counts as 0. 

### `length_weaveList`

 `weaveList` has one digit for each level. 

### `getD_weaveList`

 The digit of `weaveList` at level `ℓ`: the next unused digit of `inner` or of `outer`. 

### `lt_of_mem_weaveList`

 If the digits of both lists are below a positive number `b`, so are the interleaved digits. 

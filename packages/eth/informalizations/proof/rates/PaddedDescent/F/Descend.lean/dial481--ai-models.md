---
{
  "module": "proof/rates/PaddedDescent/F/Descend.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Descend.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Descend.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The descent through all levels computes Z (`StBrute` and `StD`)

`descend pad sched I` turns one instance into the list of all its descendants at the bottom level,
and `bruteF` evaluates each by brute force. Here: if
the pad is long enough (`Fits`), the sum of the results is the sum Z of the instance I (`stD`). What
one level does (`StE`) and that a well-formed
instance has a short word (`StT3b`) are taken as hypotheses; other files prove them. `Fits.head`
says that the current work list fits under the pad. 

 ### The bottom: brute force under fuel computes Z 

### `stBrute`

 `StBrute`: brute force computes the sum Z of an instance if the pad has a unit for every
labelling. 

 ### The budget of the work list 

### `Fits.head`

 The current work list fits under the pad. 

 ### `StD` 

### `Descend.descend_list`

 `StD` for a work list: the steps of the schedule followed by brute force do not change the sum
of Z over the list. 

### `stD`

 `StD`: all levels and then brute force compute the sum Z of the instance at the top. 

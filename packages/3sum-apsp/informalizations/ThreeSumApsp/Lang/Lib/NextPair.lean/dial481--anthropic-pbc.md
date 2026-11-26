---
{
  "module": "ThreeSumApsp/Lang/Lib/NextPair.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/NextPair.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/NextPair.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# From a pair to the next pair

A loop that runs through the pairs (a, b) with a, b < n in the order of their numbers t = a n + b
keeps a = t / n and b = t % n in two local variables, so that no division is needed.
`nextPair A B N` is the step from one pair to the next, and `Ends.nextPair` is its rule.


### `nextPair`

 b := b + 1; if b = n then b := 0; a := a + 1.  The locals A, B and N hold a, b and n. 

### `Ends.nextPair`

 **From the pair number t to the pair number t + 1.** 

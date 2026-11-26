---
{
  "module": "ThreeSumApsp/Lang/Lib/Copy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Copy.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Copy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Copying and filling a segment

copy(src, dst, n) copies n cells from src to dst (the two segments do not overlap), within
`copyTime n` steps.  fill(dst, n, x) writes x into n cells from dst, within `fillTime n` steps.
Both change no other cell (`copy_meets`, `fill_meets`).  Each of the two is one pass over the cells
from dst, so `Ends.pass` says what it does, and the proof only says what round i reads.


 ## copy 

### `Src`

 The local variables of copy: the arguments src, dst and n, and the counter. 

### `copyBody`

 copy(src, dst, n): for i < n, dst[i] := src[i]. 

### `copyTime`

 The time of copy. 

### `copy_meets`

 **copy(src, dst, n)** copies the n cells from src to dst and changes nothing else. 

 ## fill 

### `Dst`

 The local variables of fill: the arguments dst, n and x, and the counter. 

### `fillBody`

 fill(dst, n, x): for i < n, dst[i] := x. 

### `fillTime`

 The time of fill. 

### `fill_meets`

 **fill(dst, n, x)** writes x into the n cells from dst and changes nothing else. 

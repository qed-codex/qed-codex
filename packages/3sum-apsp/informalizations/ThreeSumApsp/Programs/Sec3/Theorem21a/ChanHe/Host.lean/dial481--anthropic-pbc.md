---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of the reduction from 3SUM to Convolution-3SUM

Theorem 21(a), after [CH20, Theorem 5.1]: 3SUM on n numbers reduces to
instances of Convolution-3SUM.  This file holds the outermost procedure of the reduction.

s3(n, U, x, fr), with a parameter κ that is fixed with the program: the host replaces the bound U by
U' = max U (n^κ) and calls core(n, 2U', x, fr) (`CoreSpec`).  So on all inputs with U ≤ n^κ the
solver of Convolution-3SUM is asked for instances of one and the same length and bound (`chTime`).
The power n^κ is computed by κ multiplications; the text of the program has one assignment for each
of them (`hostPow_ends`).  `hostCall_ends` is the call of core, and `host_spec` the whole.


### `Num`

 The number n of numbers, and at the end the answer. 

### `Bound`

 The bound U. 

### `Addr`

 The address of the numbers. 

### `Free`

 The free pointer. 

### `Power`

 n^κ, and then max U (n^κ). 

### `hostPow`

 κ multiplications of Power by n. 

### `hostBody`

 s3(n, U, x, fr): Power := max U (n^κ), and then the answer of the procedure number pCore (core)
on (n, 2 Power, x, fr). 

### `hostPow_ends`

 **The κ multiplications** take n^j to n^(j + κ), if all these powers fit in a word. 

### `hostCall_ends`

 **The call of core**, with max U (n^κ) in Power. 

### `host_spec`

 **The host**: from the specification of core to what the task 3SUM asks. 

---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/LibraryContracts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/LibraryContracts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/LibraryContracts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: the routines of the general library

The programs of the reduction call five routines of the general library: the remainder, the two
logarithms, the sieve and sorting.  Each theorem here says that the routine meets the specification
under which the reduction calls it (`EmodSpec`, `Log2Spec`, `Clog2Spec`, `PrimesSpec`, `SortSpec`).
The library's theorem about the body gives the result.  What is left is to read the limits off the
need, and to compare the library's count of steps with the rounder time function of the
specification.


### `clog_le_log_succ`

 `⌈log₂ x⌉ ≤ ⌊log₂ x⌋ + 1`. 

### `emodSpec_of`

 The remainder. 

### `log2Spec_of`

 The logarithm, rounded down. 

### `clog2Spec_of`

 The logarithm, rounded up. 

### `primesSpec_of`

 The sieve. 

### `sortSpec_of`

 Sorting.  The program holds sort at the number p, and half, merge and copy, which sort
calls. 

---
{
  "module": "ThreeSumApsp/Util/Flag.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Flag.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Flag.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The answer of a decision problem as a number

A routine for a decision problem returns 1 for yes and 0 for no: `flag p` is this number for the
proposition `p`.


### `flag`

 The answer of a decision problem as a number: 1 for yes, 0 for no. 

### `flag_of`

 The answer yes is written as 1. 

### `flag_of_not`

 The answer no is written as 0. 

### `flag_eq_one_iff`

 The number 1 means yes. 

### `flag_congr`

 Equivalent questions have the same answer. 

### `flag_mem`

 An answer is 0 or 1. 

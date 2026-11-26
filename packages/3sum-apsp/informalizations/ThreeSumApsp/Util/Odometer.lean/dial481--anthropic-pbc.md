---
{
  "module": "ThreeSumApsp/Util/Odometer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Odometer.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Odometer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Counting in base `b` without division: an odometer

The word RAM has no division.  A program that runs through all strings of `n` digits, for instance
through all choices of one vertex in each part of a graph (Corollary 39), keeps the digits of a
number that grows by 1.  `incDigits` is the step, and it counts: it takes the digits of `c` to the
digits of `c + 1` (`incDigits_digitsLE`).


### `incDigits`

 Add 1 to a number given by its digits in base `b`, least significant digit first (an odometer);
a carry out of the most significant digit is dropped. 

### `digitsLE`

 The `n` digits of `c` in base `b`, least significant first, which is the order in which an
odometer runs through them. 

### `length_digitsLE`

 There are `n` digits. 

### `lt_of_mem_digitsLE`

 The digits in base `b` are below `b`. 

### `digitsLE_succ`

 The least significant digit, and the digits of the quotient by `b`. 

### `incDigits_digitsLE`

 The odometer counts: adding 1 to the `n` digits of `c` gives the `n` digits of `c + 1`. 

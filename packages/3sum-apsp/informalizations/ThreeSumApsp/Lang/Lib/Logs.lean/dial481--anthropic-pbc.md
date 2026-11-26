---
{
  "module": "ThreeSumApsp/Lang/Lib/Logs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Logs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Logs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Logarithms, the cube root and halves, without division

Four routines on local variables only; none of them touches the memory.

* log2(x) returns ⌊log₂ x⌋ (0 for x = 0) by doubling (`log2_meets`).
* clog2(x) returns ⌈log₂ x⌉ (0 for x ≤ 1) by doubling (`clog2_meets`).
* cbrtCeil(n) returns the least s with s³ ≥ n, which is ⌈n^{1/3}⌉, by counting up
  (`cbrtCeil_meets`).
* half(h) returns ⌈h/2⌉ by counting up (`half_meets`).

Each of them is one loop that tries the candidates 0, 1, 2, … in turn.  Local variable 0 holds the
argument and receives the result, local variable 1 holds the candidate (`Arg`, `Cand`), and the two
logarithms keep a power of two in local variable 2 (`Power`).


### `Arg`

 The local variables of the routines: the argument, which the result replaces, the candidate,
and a power of two. 

 ## The logarithm, rounded down 

### `log2Body`

 log2(x): the candidate is L, and the power is 2^(L + 1). 

### `log2Time`

 The time of log2. 

### `log2_meets`

 **log2(x)** returns ⌊log₂ x⌋ and leaves the memory as it is. 

 ## The logarithm, rounded up 

### `clog2Body`

 clog2(x): the candidate is L, and the power is 2^L. 

### `clog2Time`

 The time of clog2. 

### `clog2_meets`

 **clog2(x)** returns ⌈log₂ x⌉ and leaves the memory as it is. 

 ## The cube root, rounded up 

### `exists_le_cube`

 Some cube is at least n. 

### `cbrtLeast`

 The least s with s³ ≥ n. 

### `one_le_cbrtLeast`

 The number ⌈n^{1/3}⌉ is at least 1 for n ≥ 1. 

### `cbrtLeast_pow_le`

 The cube of the rounded cube root is at most 8 n. 

### `abs_cube_le`

 The squares and cubes of the candidates fit in a word. 

### `cbrtCeilBody`

 cbrtCeil(n): the candidate is s. 

### `cbrtCeilTime`

 The time of cbrtCeil. 

### `cbrtCeil_meets`

 **cbrtCeil(n)** returns the least s with s³ ≥ n and leaves the memory as it is. 

 ## Halves, rounded up 

### `halfBody`

 half(h): the candidate is r. 

### `halfTime`

 The time of half. 

### `half_meets`

 **half(h)** returns ⌈h/2⌉ and leaves the memory as it is. 

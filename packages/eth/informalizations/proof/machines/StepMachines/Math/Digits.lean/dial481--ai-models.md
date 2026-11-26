---
{
  "module": "proof/machines/StepMachines/Math/Digits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Digits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Digits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The patterns ι, functions from the rectangles to {0,…,n} (the ι of the proof of Proposition 3),
as numbers: the number y stands for the pattern that gives
rectangle number q the digit number q of y in base n+1. The rectangle on the rows a < b and the
columns i < i' has the
number tri a b · C(g,2) + tri i i'. 

 ### Two digits in mixed radix 

### `mixed_inj`

 x·n + y with y < n determines x and y. 

### `mixed_lt`

 x·n + y < m·n for x < m and y < n. 

### `mixed_surj`

 Every number below m·n is x·n + y with x < m and y < n. 

 ### Numbering the rectangles 

### `c2`

 The number of pairs a < b below g. 

### `nRect_eq`

 The number of rectangles is the square of the number of pairs. 

### `two_mul_c2_le`

 There are at most g²/2 pairs. 

### `rectIx`

 The number of a rectangle, from the number p of its pair of parts (rows, or columns if tr) and
the number κ of its other
pair. 

### `ixOf`

 The number of a rectangle. 

### `ixOf_bijOn`

 The rectangles get the numbers below nRect g, each number once. 

### `tri_bijOn`

 The pairs i < i' below g are numbered 0, …, c2 g − 1 by tri, each number once. 

### `digit_le`

 A digit in base n + 1 is at most n. 

### `patOf`

 The pattern written by the number y: a rectangle gets the digit of y in base n + 1 at its
number. 

### `sum_patOf`

 Summing over the numbers y < (n+1)^(nRect g) is summing over the patterns. 

### `sum_Ω_ixOf`

 A sum over the rectangles is the sum over their numbers. 

### `ZG_congr`

 ZG reads the functions G at the rectangles only. 

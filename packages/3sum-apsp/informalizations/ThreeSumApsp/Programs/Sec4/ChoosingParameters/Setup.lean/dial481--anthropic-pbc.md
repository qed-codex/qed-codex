---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Setup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Setup.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Setup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 26 and 31 in the light language: m, the places of the padded matrices, the query

m = ⌈log₄ D⌉ (`logFour`), the places of the padded matrices and of the block of Theorem 30 behind
the free pointer (`paddedXAt`, `paddedYAt`, `blockAt`), the text of the query, and the bounds on the
entries of the padded matrices. The text of the query serves all rational parameters; its
specification is `QuerySpec31`, proved in `query31_meets`.


 ## Parameters and map 

### `logFour`

 m = ⌈log₄ D⌉. 

### `paddedXAt`

 The address of the padded X. 

### `paddedYAt`

 The address of the padded Y. 

### `blockAt`

 The base address of the block of Theorem 30. 

 ## The query 

### `Row`

 The locals of query31 are its arguments I, J, N, D, aX, aY, fr; the answer replaces I. 

### `query31Body`

 query31(I, J, N, D, aX, aY, fr): if the flag is 1, the query of Theorem 30, and otherwise the
inner product. 

### `ceil_logb_four`

 The ceiling ⌈log₄ D⌉ in natural numbers. 

### `logFour_le_four_mul`

 m ≤ 4 D, because m ≤ 4^m ≤ 4 D. 

### `two_le_of_clog`

 m ≥ 1 means D ≥ 2. 

---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Layout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Layout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Layout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 4.4, the data structure: the two main procedures for the layout of the statements

The input is N, D, X, Y (`ThinPair.input []`), as in the statements of the corollaries; the free
pointer is the first cell after it. The texts `preMain31Body` and `queryMain31Body` serve all
rational parameters c and θ. Each reads N and D, computes the address of Y and the free pointer, and
calls the relocatable routine: `preMain31_meets` for the preprocessing, `queryMain31_meets` for a
query. Between them the memory satisfies `InputReady31`. The relocatable routines enter through
their specifications `PreSpec31` and `QuerySpec31`.


 ## The texts 

### `Ans`

 The locals of the two main procedures: the answer, which in a query is at first the row I, and
the column J; then N, D, the product N D, the address of Y, the free pointer, and in the
preprocessing the result of the call. 

### `preMain31Body`

 The main procedure of the preprocessing: read the sizes, compute the two addresses, call pre31,
answer 1. 

### `queryMain31Body`

 The main procedure of a query (I, J): the same five assignments, then call query31. 

### `inputEnd`

 The free pointer behind the input. 

 ## What they do 

### `InputReady31`

 **The memory holds the input and what a query needs.** 

### `preMain31_meets`

 **The main procedure of the preprocessing** leaves a memory that is ready for queries. 

### `queryMain31_meets`

 **The main procedure of a query** returns the entry and keeps the memory ready. 

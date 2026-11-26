---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/OfflineLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/OfflineLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/OfflineLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 4.4, the offline form: the main procedure for the layout of the statements

The input is N, D, |W|, X, Y, the rows of the wanted positions, their columns (the problem
`thinProduct []`); the output follows the input, and the free pointer follows the output. The text
`offlineMain32Body` serves all rational parameters c and θ: it reads the sizes, computes the
addresses of Y, of the two lists of indices and of the output and the free pointer, and calls
offline32 (`offlineMain32_meets`). The input in the statements of the corollaries
(`ThinInstance.input`) is laid out as the procedure expects (`offlineLayout32_input`). offline32
enters through its specification `OfflineSpec32`.


 ## The text 

### `Ans`

 The locals of offlineMain32: the answer (the two arguments are not used), then N, D, |W|, the
product N D, the addresses of Y, of the rows, of the columns and of the output, the free pointer,
and the result of the call. 

### `offlineMain32Body`

 offlineMain32: read the sizes, compute the addresses, call offline32, answer 1. 

### `offlineFree`

 The free pointer: behind the input and the output. 

### `map_entryN`

 The answers of offline32 are the wanted entries. 

 ## What it does 

### `OfflineLayout32`

 The memory holds the input of the offline problem, without further parameters, from cell 0 on.


### `offlineLayout32_input`

 The input in the statements is laid out in this way. 

### `OfflineLayout32.taskInput`

 In this layout the input of offline32 stands as its specification asks, with the output behind
the input and the free pointer behind the output. 

### `offlineMain32_meets`

 **The main procedure** leaves the wanted entries behind the input and returns 1. 

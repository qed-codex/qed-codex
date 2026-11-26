---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/OfflineLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/OfflineLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/OfflineLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30, the offline form: the main procedure for the trusted layout

The input is N, D, |W|, m, L, t, X, Y, the rows of the wanted positions, their columns (the problem
thinProduct [m, L, t]); the output follows the input, and the block of the data structure follows
the output.  The main procedure wantedMain reads the sizes, computes the six addresses and calls
wantedCore (`wantedMain_meets`).


### `Ans`

 The locals of wantedMain: the answer (the two arguments are not used), then N, D, |W|, the
product N D, the addresses of Y, of the rows, of the columns, of the output and of the block, and
the result of the call. 

### `wantedMainBody`

 wantedMain: read the sizes, compute the addresses, call wantedCore, answer 1. 

### `WantedLayout`

 The memory holds the input of the offline form of Theorem 30, with D = 4^m, from cell 0 on. 

### `wantedOut`

 The address of the output: the length of the input. 

### `wantedB0`

 The base address of the block of the data structure. 

### `wantedMain_meets`

 **The main procedure** leaves the wanted entries behind the input and returns 1. 

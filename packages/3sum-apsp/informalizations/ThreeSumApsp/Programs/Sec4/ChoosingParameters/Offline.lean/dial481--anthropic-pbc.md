---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Offline.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Offline.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Offline.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 4.4, the offline form: preprocess, then one query for each wanted position

Corollary 26: "Hence, for every set W of positions of an N × N matrix, the entries (XY)[I, J], (I,
J) ∈ W, can be computed deterministically in O(|W| D^{0.437} + N²/D^{0.063}) time". Its proof: "The
bound for a set W follows by asking |W| queries." Proof of Theorem 25: "ask one query for each
position of W"; for Corollary 32 the paper uses "the same argument", "With Corollary 31 in place of
Theorem 24".

offline32(N, D, w, U, x, y, wi, wj, out, fr) preprocesses the matrices at x and y (pre31, which uses
the cells from the free pointer fr on) and then asks one query for each of the w positions, whose
rows are at wi and whose columns are at wj; the answers go to out. The arguments are those of the
task `thinTask`. The text `offline32Body`, with the round `offlineAsk32` of its loop, serves all
rational parameters c and θ: they are in the body of the procedure pre31 (`pre31Body`).

A round adds one answer (`offlineAsk32_ends`), with the invariant `Answered` that the offline form
of Theorem 30 uses too, and the routine meets its specification `OfflineSpec32` for all parameters G
(`offline32_meets`).


 ## The text 

### `entryN`

 The entry (XY)[I, J] for natural numbers I, J (0 outside the matrix). 

### `Size`

 The locals of offline32. The first ten are its arguments: N, D, the number of positions, a bound
that is not used, the addresses of X, of Y, of the rows and of the columns of the wanted positions
and of the output, and the free pointer. Then come the number of the current position and the result
of a call. 

### `offlineAsk32`

 One round of offline32: ask the query for the current position and store its answer. 

### `offline32Body`

 offline32(N, D, w, U, x, y, wi, wj, out, fr): preprocess, then ask one query for each wanted
position and store its answer. 

 ## What it does 

### `ready31_congr`

 What a query needs depends only on the cells of X, of Y, and on the cells from fr on. 

### `tOffline32`

 The time of offline32: the preprocessing, and for each wanted position a query, the reading of
the position and the storing of the answer. 

### `OfflineInput32`

 **Where the input of offline32 stands**, beyond what `Input31` says: the matrices at aX and aY;
the two lists of indices, which are below N, and the output, all below the free pointer; and the
output meets neither the matrices nor the lists. 

### `OfflineSpec32`

 offline32 writes the wanted entries of XY to out. Below fr it changes only the output; nothing
is assumed about the cells from fr on. 

### `OfflineSpec32.append`

 The specification holds for the program with more procedures appended. 

### `offlineAsk32_ends`

 **One round**: the answer for position i joins the answers that are there. 

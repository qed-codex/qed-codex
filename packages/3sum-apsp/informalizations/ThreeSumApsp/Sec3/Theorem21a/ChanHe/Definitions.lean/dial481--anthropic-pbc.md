---
{
  "module": "ThreeSumApsp/Sec3/Theorem21a/ChanHe/Definitions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/Definitions.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/Definitions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(a), the reduction of Chan and He: the problems on three sets and on arrays

The problems between which the reduction of [CH20] passes on its way from 3SUM to Convolution-3SUM:
3SUM on three sets (`HasSol`), Convolution-3SUM on three arrays (`ConvSol`, and `Node.Conv` for the
arrays of a node of the recursion tree) and on one array (`ConvOne`).  An array is a function on
`ℕ`, of which only the cells below a given length are read.  `Bdd U S` says that the elements of `S`
have absolute value at most `U`.


### `HasSol`

 3SUM on three sets (Definition 2.1 of [CH20], without the requirement that the sets have the
same size). 

### `ConvSol`

 Convolution-3SUM on three arrays of length `N` (Definition 2.2 of [CH20]).  [CH20] does not say
where the indices start or what happens when `i + j` leaves the array: we number the cells from 0
and ask for `i + j < N`. 

### `ConvOne`

 Convolution-3SUM on one array of length `N`: the three arrays are the same.  This is the
`Convolution3SUM` of Section 1.2 for the first `N` cells (`convolution3SUM_iff_convOne`). 

### `Node.Conv`

 The Convolution-3SUM instance of the node has a solution, at length `N`. 

### `Bdd`

 All elements of `S` have absolute value at most `U`. 

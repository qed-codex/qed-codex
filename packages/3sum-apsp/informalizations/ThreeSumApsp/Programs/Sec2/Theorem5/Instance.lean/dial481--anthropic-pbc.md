---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Instance.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Instance.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Instance.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5: an instance of the task, in the terms of Section 2

An instance of the thin matrix product is given by lists in the memory. This file reads them as the
matrices X and Y and the set W of Section 2, and has the facts that link the two descriptions.


### `ThinX`

 The first matrix of an instance. 

### `ThinY`

 The second matrix of an instance. 

### `ThinW`

 The set of the wanted positions of an instance. 

### `Regime`

 The regime of Theorem 5, in terms of the sizes: D = 4^m with m ≥ 1, N ≥ D^18, and at
most N²/√D wanted positions. 

### `Regime.pow_le`

 N ≥ D^18, with D written as the paper's D = 4^m. 

### `InRegime`

 The sizes are in the regime of Theorem 5, for some m. 

### `Regime5`

 The regime of Theorem 5, for an instance. 

### `thinI`

 The row of the wanted position number i. 

### `thinJ`

 The column of the wanted position number i. 

### `matAt_getD`

 A list of n k numbers in the memory is an n × k matrix, row by row. 

### `matAt_thinX`

 The first matrix lies in the memory, row by row. 

### `matAt_thinY`

 The second matrix lies in the memory, row by row. 

### `abs_thinX_le`

 The entries of the first matrix are bounded by U. 

### `abs_thinY_le`

 The entries of the second matrix are bounded by U. 

### `thinEntry_eq_mul`

 The entry asked for by the task is the entry of the product of the two matrices. 

### `_root_.Light.ThinInst.Pre.lt_lenWI`

 A number of a wanted position is an index of the list of the rows. 

### `_root_.Light.ThinInst.Pre.lt_lenWJ`

 A number of a wanted position is an index of the list of the columns. 

### `_root_.Light.ThinInst.Pre.lt_lenZip`

 A number of a wanted position is an index of the list of the positions. 

### `thinI_lt`

 The rows of the wanted positions are rows of the matrix. 

### `thinJ_lt`

 The columns of the wanted positions are columns of the matrix. 

### `mem_thinI`

 The rows of the wanted positions, in the memory. 

### `mem_thinJ`

 The columns of the wanted positions, in the memory. 

### `thin_inj`

 The wanted positions are different. 

### `thinW_eq_wantedSet`

 The set of the wanted positions, from the two functions. 

### `length_thinOut`

 There is one answer for each wanted position. 

### `getD_thinOut`

 The answer number i. 

---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem21a/Convolution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21a/Convolution.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21a/Convolution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Convolution-3SUM reduces to Exact Triangle, on lists

Theorem 21(a), after [VW13, Theorem 4.3]: from `N < t²` numbers the reduction makes `2t` instances
of Exact Triangle, each on `t` vertices per part (`Theorem21.convTemplate`).  Here
the instances are lists of integers, row by row, in the form in which a routine fills them
(`convAB`, `convBC`, `convAC`): every weight is a cell of the input, or minus a cell of the input,
at an index that is computed from the two vertices, or a filler if this index is out of range
(`cellOr`).

The three lists are the instance of the template (`triOf_conv`).  So there are `i`, `j` with
`x_i + x_j = x_{i+j}` if and only if one of the `2t` instances has a zero triangle
(`convolution3SUM_vecOf_iff`), and the weights are bounded by a bound for the numbers and the filler
(`abs_convAB_le`, `abs_convBC_le`, `abs_convAC_le`).


### `cellOr`

 Cell number `z` of a list of `N` numbers, or the filler `F` if `z` is not one of
`0, …, N - 1`. 

### `convAB`

 The weights `w(a,b) = x_{a t + b}`. 

### `convBC`

 The weights `w(b,c) = x_{c t + s - b}` of instance number `s`. 

### `convAC`

 The weights `w(a,c) = -x_{(a + c) t + s}` of instance number `s`.  The filler `-F` inside the
minus sign gives the weight `F`. 

### `length_convAB`

 The first list has `t²` entries. 

### `length_convBC`

 The second list has `t²` entries. 

### `length_convAC`

 The third list has `t²` entries. 

### `cellOr_of_lt`

 At an index in range `cellOr` reads the cell. 

### `cellOr_of_not`

 At an index out of range `cellOr` returns the filler. 

### `abs_cellOr_le`

 A bound for the list and the filler is a bound for `cellOr`. 

### `triOf_conv`

 The three lists are the instance that the template of the reduction produces. 

### `abs_convAB_le`

 The weights `w(a,b)` are bounded by a bound for the numbers and the filler. 

### `abs_convBC_le`

 The weights `w(b,c)` are bounded by a bound for the numbers and the filler. 

### `abs_convAC_le`

 The weights `w(a,c)` are bounded by a bound for the numbers and the filler. 

### `convolution3SUM_vecOf_iff`

 **The reduction on lists.**  For a list of `N < t²` numbers of absolute value at most `U`: there
are `i`, `j` with `x_i + x_j = x_{i+j}` if and only if one of the `2t` instances, filled with the
filler `2U + 1`, has a zero triangle. 

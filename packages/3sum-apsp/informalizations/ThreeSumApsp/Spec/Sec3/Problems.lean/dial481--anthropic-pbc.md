---
{
  "module": "ThreeSumApsp/Spec/Sec3/Problems.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Problems.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Problems.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The problems for Section 3.4, read from lists of integers

A routine has its input in arrays.  Here an array is a list of integers, a matrix is stored row by
row, and a cell is read with `List.getD _ _ 0` (`entry`).  This file says which instance of Exact
Triangle, Negative Triangle, Convolution-3SUM, 3SUM or APSP such lists hold (`vecOf`, `triOf`,
`graphOf`), and what the (min,+)-product of two lists is (`minPlusEntry`, `minPlusList`).  Two
operations on matrices serve several reductions: `affL m c` replaces each entry `x` by `m x + c`,
and `subMat` cuts out a block.

An entry of the (min,+)-product is computed as a running minimum.  It is at most each of the sums
`A[i,k] + B[k,j]` (`minPlusEntry_le`) and it is one of them (`exists_minPlusEntry_eq`).


 ## Instances 

### `entry`

 The entry `(i, j)` of a matrix with `n` columns that is stored in the list `L`, row by row. 

### `abs_entry_le`

 A bound on the numbers of the list is a bound on the entries of the matrix. 

### `vecOf`

 The `N` numbers in a list. 

### `triOf`

 The complete tripartite graph with `n` vertices per part whose three weight matrices are in
three lists, row by row: the weight of `(a, b)` at `a n + b` of the first, of `(b, c)` at `b n + c`
of the second, of `(a, c)` at `a n + c` of the third. 

### `graphOf`

 The weight matrix of a directed graph on `n` vertices: the weight of the edge `(i, j)` is in
cell `i n + j` of `w` if cell `i n + j` of `adj` holds 1, and there is no edge otherwise. 

### `triOf_bounded`

 The weights of the instance read from three lists are bounded if the numbers of the lists
are. 

 ## Operations on matrices 

### `affL`

 The list of the numbers `m x + c`. 

### `length_affL`

 The list of the numbers `m x + c` is as long as the list of the `x`. 

### `subMat`

 The `h × h` block of an `s × s` matrix whose upper left corner is `(r0, c0)`; both row by
row. 

### `length_subMat`

 A block has `h²` entries. 

### `entry_subMat`

 The entry `(i, j)` of a block is the entry `(r0 + i, c0 + j)` of the matrix. 

### `abs_le_of_mem_subMat`

 A bound on the entries of a matrix is a bound on the entries of its blocks. 

 ## The (min,+)-product 

### `minPlusEntry`

 The smallest of `A[i,k] + B[k,j]` over `k < n`, by one pass, for `n ≥ 1`. 

### `minPlusList`

 The (min,+)-product of two `n × n` matrices, row by row. 

### `length_minPlusList`

 The (min,+)-product has `n²` entries. 

### `minPlusEntry_le`

 An entry of the product is at most each of the sums. 

### `exists_minPlusEntry_eq`

 An entry of the product is one of the sums. 

### `abs_minPlusEntry_le`

 The entries of the product of two matrices with entries of absolute value at most `U` have
absolute value at most `2U`. 

### `entry_minPlusList`

 The entry `(i, j)` of the product stands at the place `i n + j`. 

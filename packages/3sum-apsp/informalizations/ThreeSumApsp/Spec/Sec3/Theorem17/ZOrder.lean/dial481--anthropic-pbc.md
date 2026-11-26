---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/ZOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/ZOrder.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/ZOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Matrices in Z-order (Morton order)

The count of the proof of Theorem 17 needs a product of matrices over `ℤ[x]/(x^p - 1)`, "O(n^{log₂
7}) with Strassen's algorithm".  For the recursion of that algorithm a `2^K × 2^K` matrix is stored
in Z-order: the entry `(a, c)` stands at the place whose digits in base 4 are `2 a_i + c_i`, where
`a_i` and `c_i` are the binary digits of `a` and `c`.

* Places: `zIdx` maps a pair to its place, `zRow` and `zCol` map back (`zRow_zIdx`, `zCol_zIdx`,
  `zIdx_zRow_zCol`).  All three are computed one digit in base 4 at a time (`zIdx_eq`, `zRow_eq`,
  `zCol_eq`), and every proof is an induction along these equations.
* Lists: the entry `(a, c)` of `zList K M` starts at `zIdx a c * p` (`getD_zList`).
* **The four quadrants of a matrix are the four quarters of its list** (`quarter_zList`,
  `zList_succ`), which is what the recursion needs.


 ## Places 

### `spread`

 The binary digits of `i`, moved to the even places: the number with the same digits in
base 4. 

### `spreadList`

 The table of `spread`. 

### `zIdx`

 The place of the entry `(a, c)` in Z-order. 

### `zRow`

 The row of the entry at place `z`. 

### `zCol`

 The column of the entry at place `z`. 

### `spread_eq`

 The last binary digit goes to the last digit in base 4. 

### `spread_zero`

 The number 0 has no digits to move. 

### `zRow_eq`

 The row, one digit in base 4 at a time. 

### `zCol_eq`

 The column, one digit in base 4 at a time. 

### `zRow_zero`

 The place 0 is in row 0. 

### `zCol_zero`

 The place 0 is in column 0. 

### `zIdx_eq`

 The place, one digit in base 4 at a time. 

### `zIdx_lt`

 The places of a `2^K × 2^K` matrix are below `4^K`. 

### `zRow_zCol_zIdx`

 The row and the column of the place of `(a, c)` are `a` and `c`. 

### `zRow_zIdx`

 The row of the place of `(a, c)` is `a`. 

### `zCol_zIdx`

 The column of the place of `(a, c)` is `c`. 

### `zIdx_zRow_zCol`

 A place is the place of its row and its column. 

### `zRow_zCol_quadrant`

 The places of the quadrant number `t`: their rows and columns are those of the first quadrant,
moved by `2^K` down if `t ≥ 2` and to the right if `t` is odd. 

 ## Matrices as lists 

### `zList`

 A `2^K × 2^K` matrix of vectors, as one list, entry after entry in Z-order. 

### `quarter`

 The quarter number `t` of a list of length `4 q`. 

### `length_zList`

 A matrix of vectors of length `p` has `4^K p` numbers. 

### `getD_zList`

 The entry `(a, c)` of the matrix stands at the place `zIdx a c`. 

### `quarter_zList`

 **The quadrants of a matrix are the quarters of its list.** 

### `eq_append_quarters`

 A list of length `4 q` is put together from its four quarters. 

### `zList_succ`

 A matrix is put together from its four quadrants. 

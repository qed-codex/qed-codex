---
{
  "module": "ThreeSumApsp/Spec/Sec2/Theorem5/Arrays.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Arrays.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Arrays.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Arrays on strings as lists

Section 2.3.1: "An array a on the left strings of length L assigns an integer a[u] to each u that is
a left string of length L."  In a program such an array is a list: an array on the strings of length
`n` over an alphabet of `b` letters is the list of its `b^n` entries in the order of the codes
(`arrStr`), so the entry at a string is the entry of the list at the code of the string
(`getD_arrStr`), and an entry of the list is 0 if the array is 0 at the string with that code
(`getD_arrStr_eq_zero`).  The arrays on left strings, on right strings and on leaves are the cases
`arrL`, `arrR` and `arrT`.


 ## Arrays on the strings over any numbered alphabet 

### `arrStr`

 An array on the strings of length `n` over an alphabet numbered by `e : α ≃ Fin b`, as the list
of its `b^n` entries in the order of the codes. 

### `length_arrStr`

 The list has `b^n` entries. 

### `getD_arrStr_of_lt`

 The entry of the list at a number below `b^n`. 

### `getD_arrStr`

 The entry at a string is the entry of the list at its code. 

### `getD_arrStr_eq_zero`

 The entry of the list at `c` is 0 if the array is 0 at every string with the code `c`. 

 ## The three kinds of arrays of Section 2 that the programs store 

### `arrL`

 An array on the left strings of length `n`, as the list of its `7^n` entries. 

### `arrR`

 An array on the right strings of length `n`, as the list of its `7^n` entries. 

### `arrT`

 An array on the leaves (for example an encoding), as the list of its `10^n` entries. 

### `length_arrL`

 The list of an array on the left strings has `7^n` entries. 

### `length_arrR`

 The list of an array on the right strings has `7^n` entries. 

### `length_arrT`

 The list of an array on the leaves has `10^n` entries. 

### `getD_arrL`

 The entry at a left string is the entry of the list at its code. 

### `getD_arrR`

 The entry at a right string is the entry of the list at its code. 

### `getD_arrT`

 The entry at a leaf is the entry of the list at its code. 

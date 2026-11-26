---
{
  "module": "ThreeSumApsp/Lang/Lib/ArrayAt.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/ArrayAt.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/ArrayAt.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Arrays in the memory

A routine assumes the same facts about each of its arrays: which list it holds, how long the list
is, and that it lies below some address `top`, from which on the routine writes: the free pointer,
the place of the result, the scratch space.  `ListAt μ a l N top` is the record of these three
facts, and `ArrayAt μ a l N U top` adds a bound `U` on the entries.  `IndexAt μ a l N p top` is the
record for a list of natural numbers below `p`.  What a routine assumes is then a record with one
field for each array.

* `ListAt.keep`, `ArrayAt.keep`: an array stays in place when its cells do not change.
* `ListAt.mono`, `ArrayAt.mono`: `top` and `U` may grow.
* `ListAt.read`, `ArrayAt.read`, `ArrayAt.abs_read_le`: what a cell holds, and how large it is.
* `ListAt.drop_take`, `ArrayAt.drop_take`: a piece of an array is an array.
* `IndexAt.keep`, `IndexAt.read`, `IndexAt.getD_lt`: the same for natural numbers.


### `ListAt`

 The list `l` stands at address `a`: it has `N` entries, and its cells lie below `top`. 

### `ArrayAt`

 The list `l` stands at address `a`: it has `N` entries, each of absolute value at most `U`, and
its cells lie below `top`. 

### `keep`

 A list stays in place when its cells do not change.  That they lie below `top` is said again in
the description of the cells: so the promise `Kept μ μ' top` of a callee is enough as it stands. 

### `mono`

 The address `top` may grow. 

### `read`

 Reading a cell. 

### `drop_take`

 The `n` entries from place `k` on. 

### `listAt`

 An array without the bound on its entries. 

### `keep`

 An array stays in place when its cells do not change. 

### `mono`

 The bound `U` on the entries and the address `top` may grow. 

### `read`

 Reading a cell. 

### `abs_read_le`

 A cell of an array holds a number of absolute value at most `U`. 

### `drop_take`

 The `n` entries from place `k` on. 

### `IndexAt`

 The list `l` of natural numbers stands at address `a`: it has `N` entries, each below `p`, and
its cells lie below `top`. 

### `keep`

 A list of natural numbers stays in place when its cells do not change. 

### `read`

 Reading a cell. 

### `getD_lt`

 An entry is below `p`. 

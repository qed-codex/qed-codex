---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem21a/Passes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21a/Passes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem21a/Passes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One pass over a list

The routines of the reduction after Chan and He ([CH20, Theorem 5.1], one of the reductions behind
Theorem 21(a)) run through arrays from left to right.  This file says what two kinds of
passes have written after the first `i` elements, and how one more element changes it.

* A filter pass selects elements and writes a function of them: `passList`, with one lemma for an
  element that is selected (`passList_succ_of`) and one for an element that is not
  (`passList_succ_of_not`).
* A pass over a sorted list writes the distinct values and their multiplicities.  `DistSt L D i`
  says that `D` is the list of the distinct values among the first `i` elements, and `countTo L i`
  counts occurrences among them.  An element either opens a new value (`DistSt.opens`,
  `map_countTo_opens`) or repeats the last one (`DistSt.bumps`, `map_countTo_bumps`).


 ## A filter pass 

### `passList`

 What a filter pass has written after it has seen the first `i` elements. 

### `passList_zero`

 At the start nothing is written. 

### `passList_length`

 At the end all the selected elements are written. 

### `passList_succ_of`

 An element that is selected is written. 

### `passList_succ_of_not`

 An element that is not selected changes nothing. 

### `length_passList_le`

 After `i` elements at most `i` are written. 

 ## The distinct values of a sorted list 

### `countTo`

 How often `x` occurs among the first `i` elements. 

### `countTo_succ`

 One more element in the count. 

### `countTo_nonneg`

 A count is not negative. 

### `countTo_le`

 Among `i` elements a value occurs at most `i` times. 

### `DistSt`

 `D` is the list of the distinct values among the first `i` elements of `L`, and it ends with
the last of them. 

### `DistSt.zero`

 At the start there are no values. 

### `DistSt.opens`

 If element `i` of a sorted list differs from the last value written, or nothing is written yet,
then it has not occurred before, and appending it gives the distinct values among the first `i + 1`
elements. 

### `DistSt.bumps`

 If element `i` equals the last value written, then the distinct values among the first `i + 1`
elements are those among the first `i`. 

### `map_countTo_opens`

 The multiplicities after a new value: the old ones, and a 1 at the end. 

### `map_countTo_bumps`

 The multiplicities after a repeated value: the last one goes up by one. 

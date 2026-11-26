---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/FrontFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/FrontFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/FrontFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: what the lists that the first routines produce stand for

Theorem 21(a), after [CH20, Theorem 5.1].  The routines that run before the
recursion trees produce lists: the table of binary digits (`bitTable`), the selections by digits
(`pickList`), the distinct values with their multiplicities, and the doubles of the repeated values
(`twiceList`). This file has no program.  It shows that these lists represent the sets from which
the reduction makes its three-set inputs.

* A selection by one digit is `ChanHe.splitA`, a selection by two digits is `ChanHe.splitB`
  (`pick_splitA`, `pick_splitB`).
* `Values n X D C` says that `D` lists the distinct values of the input `X` and `C` how often each
  occurs.  Then `twiceList D C` represents `ChanHe.twiceSet` (`Values.twice`), and the test of
  zeroThree decides whether 0 occurs at least three times (`Values.zeroThree`).


 ## The table of binary digits 

### `bitOf`

 A binary digit of the label of a number, as an integer. 

### `bitRow`

 The `Λ` lowest binary digits of `z`. 

### `bitTable_cons`

 The table begins with the digits of the first label. 

### `bitTable_append`

 The table ends with the digits of the last label. 

### `length_bitTable`

 The table has `Λ` cells for each number. 

### `getD_bitTable`

 Cell `i Λ + β` of the table holds digit `β` of the label of the `i`-th number. 

 ## Selecting by binary digits 

### `filter_by_position`

 A filter written with positions. 

### `pickList_eq`

 The selection by cells of the table of digits is a filter of the list. 

### `bitOf_eq_iff`

 The digit as an integer, against the digit as a Boolean. 

### `pick_splitA`

 The selection by one digit gives the set `splitA`. 

### `pick_splitB`

 The selection by two digits gives the set `splitB`. 

### `length_pickList_le`

 A selection is not longer than the list. 

 ## The values of the input and how often they occur 

### `eq_ofFn_vecOf`

 A list of `n` numbers is the list of the values of its vector. 

### `toFinset_eq_image`

 The set of the members of a list of `n` numbers is the image of its vector. 

### `count_eq_card`

 How often a value occurs in a list of `n` numbers, in terms of its vector. 

### `Values`

 `D` lists the distinct values of the input `X`, and `C` how often each occurs. 

### `Values.nodup`

 No value stands twice. 

### `Values.values`

 The members of `D` are the values of the input. 

### `Values.counts`

 `C` says at how many positions each value stands. 

### `Values.of_perm`

 The distinct values of a rearrangement of the input, with how often each occurs there. 

### `Values.length_le`

 There are at most `n` distinct values. 

### `Values.zip`

 The pairs of a value and the number of its occurrences. 

### `Values.twice`

 The doubles of the repeated values. 

### `length_twiceList_le`

 There are at most as many doubles as values. 

### `Values.zeroThree`

 Whether 0 occurs at least three times. 

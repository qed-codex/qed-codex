---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/SliceFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/SliceFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/SliceFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The pruned recursion: the pure side

What the program for Pruned (Section 2.4.2) needs to know about its model Spec.prunedList, which
works on increasing lists of codes.  A code is an output string read as a number with the digits 0
to 9: the digits 0 to 8 stand for the variables z_ij and the digit 9 for z₀.  The slice at the digit
z is sliceList n z l, the codes of l with first digit z, without that digit.

* The value that belongs to a code does not depend on the list in which the code is passed
  (`prunedValue`, `prunedList_eq_map`).
* The lists passed to the children are increasing lists of codes again, and the lengths add up
  (`segStart_ten`).
* Step (4): the result is made of the slices of the children's results (`prunedList_succ`).
* Step (2): the list of a child is the merge of the slice at the output variable of its term
  (`firstList`, empty for the term P₀) and the slice at z₀ (`childList_eq_mergeUnion`).
* The running time `prunedTime` follows the recursion of the program; it is built from the times of
  a round (`roundTime`) and of steps (3) and (4) (`childTime`).  It is at most a constant times
  prunedWork, one unit for each call and for each code passed to a call (`prunedTime_le`).  One
  round is `roundTime_le`, and the ten rounds are added up by `sum_helper_lengths`.


### `prunedValue`

 The value of Pruned at the output string with code c, at the vertex whose part of the encodings
begins at position base: the sum of the products at the leaves that contribute to the string. 

### `prunedList_eq_map`

 prunedList lists the values of the codes that are passed to it. 

### `length_prunedList`

 prunedList returns one value for each code. 

### `abs_prunedValue_le`

 Section 2.4.4: "every value computed by Pruned is a sum of at most 10^L products of two encoded
numbers". 

### `lt_of_mem_sliceList`

 A code without its first digit has n digits. 

### `pairwise_childList`

 The list of a child increases. 

### `lt_of_mem_childList`

 The codes of the list of a child have n digits. 

### `sliceList_subset_childList`

 The slice at the output variable of the term t is part of the list of the child t. 

### `sliceList_nine_subset_childList`

 The slice at z₀ is part of the list of every child. 

 ## Positions of the segments 

### `segStart_succ`

 The slice at z + 1 begins where the slice at z ends. 

### `segStart_ten`

 The ten slices make up the list. 

### `segStart_mono`

 The slices stand in the order of their first digits. 

 ## The model, one level unfolded 

### `pvSum`

 The sum of the values of the code c at the first k children. 

### `pvSum_succ`

 One more child. 

### `childValues_eq_map`

 What the child t returns, also if it is not called. 

### `prunedList_succ`

 Step (4): the result is the nine slices at the variables z_ij, each with the values of its own
child, followed by the slice at z₀ with the sums over the ten children. 

### `Seg.flatMap_range`

 A concatenation lies in the memory if its pieces do, each at the sum of the lengths of the
earlier ones. 

 ## The lists of a round 

### `firstList`

 The first of the two lists that are merged for the child t: the slice at the output variable of
the term t, and nothing for the term P₀, which is number 9. 

### `childList_eq_mergeUnion`

 Step (2): "S_{P_ij} := S_{z_ij} ∪ S_{z₀} and S_{P₀} := S_{z₀}". 

### `pairwise_firstList`

 The first list increases. 

### `firstList_subset_childList`

 The first list is part of the list of the child. 

### `segStart_add_firstList_le`

 The first list ends before the slice at z₀ begins. 

### `length_childList_le`

 The list of a child is no longer than the two lists that are merged. 

 ## The running time 

### `childTime`

 The running time of steps (3) and (4) for the term t; T is the time of the recursive call as a
function of its list, and h is the constant of the helper procedures. 

### `roundTime`

 The running time of round number t of the loop over the ten terms. 

### `prunedTime`

 The running time of the program, by the recursion of the program: before the loop segBounds and
fill are called, and each of the ten rounds begins with the test of the loop. 

### `sum_map_add_mul_add_mul`

 A sum of terms a + h f(t) + C w(t), taken apart. 

### `sum_length_firstList`

 The first lists of the ten rounds are the slices before the slice at z₀. 

### `roundTime_le`

 The time of round t with the test of the loop, if the recursive call stays within C times its
work: the helpers read and write lists whose lengths are at most the lengths of the two slices. 

### `sum_helper_lengths`

 The lengths that the helpers handle in the ten rounds, added up. 

### `prunedTime_le`

 The program takes at most 50 h + 2000 steps for each call and for each code passed to a
call. 

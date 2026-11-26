---
{
  "module": "ThreeSumApsp/Spec/Sec2/Theorem5/SortedSets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/SortedSets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/SortedSets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Sets of output strings as increasing lists of codes

Section 2.4.4: "we store the sets as sorted lists, so that a slice is a segment and a union of
slices is a merge".  A set `S` of output strings is stored as the strictly increasing list `codesOf
S` of its codes.  The operations of `Pruned` (Section 2.4.2) on sets become operations on lists.
None of them uses a division; a first digit is removed by a subtraction.

* The slice `S_z` is the segment `sliceList n z` of the list with first digit `z`
  (`codesOf_sliceSet`), and the list is the concatenation of its ten segments, with the first digits
  put back (`flatMap_sliceList`).
* A union is a merge, `mergeUnion` (`codesOf_union`).
* The set `S_λ` passed to the child `λ` in step (2) is `childList` (`codesOf_childSet`).
* The restriction of an array on a set to a subset is one pass, `restrictList`
  (`restrictList_spec`).

Two increasing lists are equal if they have the same elements (`List.Pairwise.eq_of_mem_iff`): the
facts on slices and on unions are proved by describing the elements of both sides.


 ## The list of a set 

### `codesOf`

 A set of output strings as the strictly increasing list of its codes. 

### `pairwise_codesOf`

 The list of codes is strictly increasing. 

### `mem_codesOf`

 The elements of the list are the codes of the strings of the set. 

### `length_codesOf`

 Cardinalities are lengths. 

### `codesOf_lt`

 The codes are below `10^n`. 

### `codesOf_eq_nil`

 The list is empty exactly if the set is. 

### `exists_codesOf`

 An increasing list of numbers below `10^n` is the list of codes of a set. 

 ## Slices are segments 

### `between`

 The numbers `c` with `a ≤ c < b` of an increasing list: skip the numbers below `a`, then take
the numbers below `b`. 

### `sliceList`

 The segment of an increasing list of codes with first digit `z`: the codes from `z · 10^n` on
that are below `(z+1) · 10^n`, with the first digit removed by a subtraction. 

### `mem_between`

 For an increasing list `l`, the elements of `between a b l` are the numbers `c` of `l` with
`a ≤ c < b`. 

### `pairwise_between`

 The numbers between two bounds of an increasing list form an increasing list. 

### `mem_sliceList`

 A number belongs to the segment with first digit `z` of an increasing list exactly if it is
below `10^n` and, with the digit `z` before it, belongs to the list. 

### `pairwise_sliceList`

 A segment is strictly increasing. 

### `map_sliceList`

 A segment of an increasing list, with the first digit put back, is the part of the list from
`z 10^n` up to, but not including, `(z + 1) 10^n`. 

### `flatMap_sliceList_eq_takeWhile`

 The first `k` segments, with the first digits put back, are the codes below `k · 10^n`. 

### `codesOf_sliceSet`

 A slice of a set is a segment of the list. 

### `flatMap_sliceList`

 The list is the concatenation of its ten segments (with the first digits put back). 

### `sum_length_sliceList`

 The lengths of the ten segments add up to the length of the list. 

 ## Unions are merges 

### `mergeUnion`

 The union of two strictly increasing lists, by merging; a number in both lists is kept once. 

### `mem_mergeUnion`

 A number belongs to a merge exactly if it belongs to one of the two lists. 

### `lt_of_mem_mergeUnion`

 A number below all elements of two lists is below all elements of their merge. 

### `pairwise_mergeUnion`

 The merge of two strictly increasing lists is strictly increasing. 

### `codesOf_union`

 A union of sets is a merge of the lists. 

### `length_mergeUnion_le`

 A merge is not longer than the two lists together. 

### `childList`

 Step (2) of `Pruned` on lists: the set passed to the child with digit `t`.  The digit 9 is that
of `P₀` and of `z₀`: the child `P₀` gets the slice at `z₀`, and the child `P_ij` the union of the
slices at `z_ij` and at `z₀`. 

### `codesOf_childSet`

 The list of the set `S_λ` of step (2) of `Pruned`. 

 ## Restriction to a subset is one pass 

### `restrictList`

 Restriction of an array on a set to a subset, on lists: `big` is the increasing list of the set,
`vals` the list of the values in the same order, `small` the increasing list of the subset.  One
pass. 

### `restrictList_map`

 On strictly increasing lists, the second contained in the first: from the values of `f` along
`big`, `restrictList` returns the values of `f` along `small`. 

### `restrictList_spec`

 `restrictList` picks the values at the subset. 

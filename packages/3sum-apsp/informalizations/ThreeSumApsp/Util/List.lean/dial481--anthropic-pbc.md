---
{
  "module": "ThreeSumApsp/Util/List.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/List.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/List.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lists: entries with a default, blocks, sums, counting, sorted lists

General facts about lists. Arrays are lists here, and entry `i` of a list is `l.getD i d`. The
sections:

* Entries with a default: `getD` of a list that was appended to, cut, tabulated, mapped or changed
  in one place.
* Blocks: `(List.range n).flatMap f` puts the blocks `f 0, …, f (n - 1)` one after the other. Where
  an entry of a block stands, for blocks of any lengths and for blocks of one length.
* Sums: partial sums, the triangle inequality, and the sum over a list that enumerates the image of
  a finite set.
* A running minimum.
* Counting: how often a value occurs among the first entries of a list, or among the values of a
  function on `Fin n`; the list of the `j < n` with a property.
* Sorted lists: what `dropWhile` and `takeWhile` leave of a strictly increasing list; first
  occurrences in a weakly increasing list.
* Two notions of this project: `AbsLe l U` says that all members of `l` have absolute value at most
  `U`, and `sumLists` is the entrywise sum of lists of one length.


 ## Entries with a default 

### `getD_of_forall_mem`

 What holds for the default and for every member of a list holds for every `getD`. 

### `getD_append_add`

 Entry `j` of the second of two lists put together. 

### `getD_drop`

 Entry `j` of a list without its first `a` entries. 

### `getD_take_of_lt`

 Entry `j < n` of the first `n` entries. 

### `getD_map_range`

 Entry `i < n` of the table `f 0, …, f (n - 1)`. 

### `getD_map_of_lt`

 Entry `i < l.length` of `l.map f`, whatever the two defaults. Mathlib's `List.getD_map` is for
all `i`, with the default `f d`. 

### `getD_set_of_lt`

 The entries of a list in which entry `q < l.length` was replaced by `a`. 

### `getD_append_singleton`

 One more member at the end changes the entry number `l.length` only. 

### `take_succ_getD`

 The first `i + 1` entries are the first `i` entries and entry `i`. 

 ## Blocks one after the other 

### `getD_flatMap_range_sum`

 Blocks of any lengths: entry `o` of block `r` stands after the blocks `0, …, r - 1`. 

### `length_flatMap_range`

 The length of `n` blocks of length `k`. 

### `getD_flatMap_range`

 Blocks of length `k`: entry `r` of block `z` has the index `z * k + r`. 

### `length_flatMap_finRange`

 The length of `n` blocks of length `k`, numbered by `Fin n`. 

### `getD_flatMap_finRange`

 Blocks of length `k`, numbered by `Fin n`: entry `r` of block `i` has the index `i * k + r`. 

### `take_drop_flatMap_range`

 A run of `n` blocks, cut out of a list of blocks of length `k`. 

### `zipWith_flatMap_range`

 An entrywise operation on two lists of blocks of one length works block by block. 

### `length_flatMap_le`

 Blocks of length at most `c`, one for each member of `l`, have length at most `l.length * c`
in all. 

 ## Sums 

### `sum_map_range`

 The sum of the table `f 0, …, f (n - 1)` is the sum over `Finset.range n`. For a sum over
`Fin n` go on with `Finset.sum_range`. 

### `sum_map_range_mono`

 Partial sums of natural numbers grow. 

### `sum_take_succ_getD`

 One more term of a partial sum; beyond the end of the list the term is `0`. Within the list,
`List.sum_take_succ` has `l[j]` in place of `l.getD j 0`. 

### `sum_take_map_range_succ`

 One more term of a partial sum of the table `f 0, …, f (n - 1)`. 

### `sum_flatMap_map`

 A sum over a concatenation of lists is the sum of the sums over the lists. 

### `sum_filter_finRange`

 A sum over the list of the indices with a property, as a sum over a finite set. 

### `abs_sum_le_sum_abs`

 The triangle inequality for the sum of a list. 

### `abs_sum_take_le_sum_abs`

 The sum of an initial part of a list is at most the sum of the absolute values of the whole
list, in absolute value. 

### `abs_sum_take_map_le`

 If `|f x| ≤ B` for all `x ∈ l`, then every initial part of the numbers `f x` has a sum of
absolute value at most `l.length * B`. 

### `abs_sum_map_le`

 If `|f x| ≤ B` for all `x ∈ l`, then `|(l.map f).sum| ≤ l.length * B`. 

### `toFinset_eq_image_of_length_eq_card`

 If `l` has no repetitions, every member of `l` is `g x` for some `x ∈ S`, `g` is injective and
`l` has as many members as `S` has elements, then the members of `l` are exactly the `g x` with
`x ∈ S`. 

### `sum_map_eq_sum_of_length_eq_card`

 Under the same hypotheses, a sum over `l` is a sum over `S`. 

 ## A running minimum 

### `foldl_min_le`

 A running minimum over `f 0, …, f m` is a lower bound of these values. 

### `exists_foldl_min_eq`

 A running minimum over `f 0, …, f m` is one of these values. 

 ## Counting 

### `count_take_succ`

 A count among the first `i + 1` entries, from the count among the first `i` and entry `i`. 

### `count_take_succ_getD`

 A count among the first `i + 1` entries, with entry `i` read by `getD`. 

### `count_take_lt`

 If entry `i < l.length` is `x`, then `x` occurs less often before place `i` than in the whole
list. 

### `length_filter_lt_succ`

 The members with `t a < z + 1` are those with `t a < z` and those with `t a = z`. 

### `length_filter_range`

 The list of the `j < n` with `q j` has `Nat.count q n` members. 

### `getD_filter_range_count`

 In the increasing list of the `j < n` with `q j`, the member `i` has the number
`Nat.count q i`. 

### `count_take_ofFn`

 How often a value occurs among the first `i` values of a function on `Fin n`. 

### `count_ofFn`

 How often a value occurs in the table of a function on `Fin n`. 

 ## Sorted lists 

### `mem_dropWhile_lt`

 What remains of a strictly increasing list after the members below `a` are skipped. 

### `mem_takeWhile_lt`

 The members below `b` at the beginning of a strictly increasing list are all its members
below `b`. 

### `getD_notMem_take_of_sorted`

 In a weakly increasing list, an entry that is the first or differs from its predecessor has not
occurred before. 

 ## Lists of integers that are bounded in absolute value 

### `AbsLe`

 All members of the list `l` have absolute value at most `U`. 

### `AbsLe.getElem`

 A bound on the absolute values of all members bounds every entry. 

### `AbsLe.append`

 Two lists with a common bound, one after the other. 

### `AbsLe.abs_getD_le`

 A bound on the absolute values of all members bounds every `getD` with default `0`. 

 ## The entrywise sum of lists 

### `sumLists`

 The entrywise sum of lists of length `len`. 

### `sumLists_map`

 The entrywise sum of lists that are images of one list. 

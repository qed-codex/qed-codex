---
{
  "module": "ThreeSumApsp/Spec/Sec4/Theorem30/NineStrings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/NineStrings.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/NineStrings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Strings of digits with a bounded number of nines (Section 4.2, proofs of Lemma 29, Theorem 30)

All three enumerations of Section 4 come from one: `nineStrs n lo hi`, the strings of n digits
0, …, 9 in which the digit 9 (the digit of P₀) occurs at least lo and at most hi times, in
lexicographic order.

* The boxes with e stars are the leaves with between e and m - t symbols P₀, with their e lowest
  symbols P₀ turned into stars (the proof of Lemma 29).
* The leaves of order below t contributing to an output string η (the paper's w) have, at the m
  levels of its inner set Q, a string with at least m - t + 1 nines (proof of Theorem 30).
* The boxes of η have, at the m levels of Q, a string with exactly m - t nines, the nines being the
  levels of V (Section 4.2).

The file proves what the list contains (`mem_nineStrs`), that it is increasing
(`pairwise_lt_nineStrs`), how long it is (`length_nineStrs`: ∑_f binom(n, f) 9^{n-f}), and how a
routine goes through it: it starts with `nineFirst` (`head?_nineStrs`), and `nineNext` goes from
each string to the next (`nineNext_getElem`); so the string reached after i steps,
`nineStr n lo hi i`, is the member number i (`getElem_nineStrs`).  Read from the right end of the
string, `nineNext` is one pass: skip the positions that cannot be raised, raise one digit
(`nineRaise`), and fill the rest with the least admissible string, zeros followed by nines.  The
proof follows the recursion of the list: the strings with the first digit d form a block,
`nineNext` goes through each block (`nextTo_map_cons`), and from the last string of a block to the
first string of the next block (`head_nineBlocks`).


### `nineStrs`

 The strings of n digits below 10 with between lo and hi digits 9, in lexicographic order. 

### `nineFirst`

 The least string of n digits with at least lo digits 9: zeros, then lo nines. 

### `nineRaise`

 The first digit d raised by one, if that is possible, and the least admissible string of n
digits behind it. 

### `nineNext`

 The string after l, or none if l is the last one: the rest of the string goes to the string
after it, or, if it is the last one, the first digit is raised. 

### `nineStr`

 The string number i of the list, as a routine reaches it: from the first string by going to the
next one i times. 

 ## The members of the list 

### `cons_mem_nineStrs`

 The first digit is below 9, or it is a 9 and counts. 

### `ten_notMem_of_mem_nineStrs`

 The digit of the star does not occur. 

### `nineStrs_eq_nil`

 There is no string with more nines than digits, or if the bounds contradict each other. 

### `pairwise_lt_nineStrs`

 The list is strictly increasing in the lexicographic order. 

 ## The length of the list 

### `length_nineStrs_succ`

 The recursion for the length of the list. 

### `nineTerm_zero`

 Strings without a nine: one more digit, nine times as many. 

### `nineTerm_succ`

 Strings with g + 1 nines: the first digit is a nine or one of the nine other digits. 

### `sum_Icc_zero_succ`

 A sum from 0: the first summand apart. 

### `sum_Icc_succ_succ`

 A sum with both ends shifted by one. 

### `length_nineStrs`

 There are binom(n, f) 9^{n-f} strings with exactly f nines. 

 ## The first string 

### `le_of_mem_nineStrs`

 If there is a string at all, the bounds are consistent. 

### `nineFirst_succ`

 The least string begins with 0 if not all digits have to be nines. 

### `nineFirst_self_succ`

 The string of nines. 

### `flatMap_map_nil`

 Without strings of n digits there are no strings of n + 1 digits that begin below 9. 

 ## From each string to the next 

### `NextTo`

 f takes each member of the list to the following one, and the last one to z. 

### `nextTo_append`

 f goes through two lists one after the other exactly if it goes through both, and from the last
member of the first list to the first member of the second (to z if the second list is empty). 

### `NextTo.getElem`

 What `NextTo` says about the member number i. 

### `nextTo_map_cons`

 The block of the strings with the first digit d. 

### `nineBlocks`

 The blocks of the strings with the first digits a, a + 1, …, a + k - 1, followed by the block
with the first digit 9: the end of the list `nineStrs (n + 1) lo hi`. 

### `nextTo_nineBlocks_zero`

 `nineNext` goes through the last block, the strings with the first digit 9. 

### `head_nineBlocks`

 The first string after the block with the first digit a is the one to which `nineNext` goes by
raising the digit a. 

### `nextTo_nineBlocks`

 `nineNext` goes through the blocks. 

### `nextTo_nineStrs`

 `nineNext` goes through the list. 

### `nineNext_getElem`

 `nineNext` goes from each string of the list to the following one, and from the last one to
none. 

### `getElem_nineStrs`

 `nineStr n lo hi i` is the member number i of the list. 

### `isSome_nineNext_nineStr`

 There is a next string exactly if the string is not the last one of the list. 

### `length_nineStrs_pos`

 If the bounds are consistent, there is a string. 

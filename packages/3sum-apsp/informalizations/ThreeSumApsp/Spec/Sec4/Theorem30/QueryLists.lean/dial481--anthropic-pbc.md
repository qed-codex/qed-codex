---
{
  "module": "ThreeSumApsp/Spec/Sec4/Theorem30/QueryLists.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/QueryLists.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/QueryLists.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# What a query reads (proof of Theorem 30, "Query")

The output string, which the paper calls w, is η as a string of variables and w as the list of its
digits; the levels of its inner set Q are the positions of the digit 9.  w is also the list of
digits of the private leaf of η, and `scatter w s` replaces its m nines by a string s of m digits:
the paper's "forming its leaf or its box from the private leaf".  A query adds up the products at
the leaves of order below t contributing to η, and the stored values of the boxes of η (steps (2)
and (3) of the query in Section 4.3).

* `lowList`: the strings with at least m - t + 1 nines give the leaves of order below t ("Each of
  these leaves is obtained from the private leaf of w, which has P₀ at every level of Q, by picking
  fewer than t of those levels and replacing P₀ with one of the nine other terms at each of them");
* `boxesOf`: the strings with exactly m - t nines give the leaves of order exactly t, and `starRun`
  turns the leading nines into stars.  This is the second description of the boxes of w in
  Section 4.2: "For such a leaf, consider the lowest level of Q at which it chooses a term other
  than P₀, and replace its P₀ by a star at every lower level of Q (or at every level of Q, if
  t = 0).  The result is a box of w, and each box of w arises exactly once in this way".  On cubes
  the result is `starBelow`, and the members of the list are exactly the strings of the cubes
  `starBelow η τ` for these leaves τ (`mem_boxesOf_iff`; no other proof rests on this statement).
  In the first description the nines are the levels of V, and the leading nines those of F_V, which
  "is the longest initial segment of Q contained in V".  `starRunIf` is `starRun` as a pass over the
  string with one flag.

The results are `sum_lowList` and `sum_boxesOf` (a sum over one of the lists is the sum over the set
of the paper) and `sum_queryTerms_storedD` (the numbers that a query adds up have the sum of the
query of the paper). Each list is compared with its set by counting
(`List.sum_map_eq_sum_of_length_eq_card`):
1. The list has no repetitions: `scatter w` is injective on strings of m digits, and `starRun` can
   be undone (`lowList_nodup`, `boxesOf_nodup`).
2. Each member is the list of digits of a member of the set.  `scatter w s` is a leaf τ contributing
   to η with as many symbols P₀ as s has nines (`exists_leaf_scatter`).  With at least m - t + 1
   nines its order is below t (`exists_of_mem_lowList`).  With exactly m - t nines its order is t.
   The cube `starBelow η τ` has the digits of τ with stars at the levels of F_Z, where Z, the set
   of the levels of Q at which τ chooses P₀, is the nines of s.  `Unreached` is the formula for F_Z
   read on digits (`unreached_iff_mem_FV`); it holds exactly at the leading nines of s
   (`getD_scatter_starRun`), so the cube has the digits `scatter w (starRun s)`
   (`digitsC_starBelow`, `exists_leaf_of_mem_boxesOf`), and it is a box of η (`starBelow_mem`,
   `exists_of_mem_boxesOf`).
3. The lists have ∑_{d<t} α_d and α_t members (`length_lowList`, `length_boxesOf`), and so have the
   sets, by the last line of Lemma 28 (`lemma_28_counts`).


### `scatter`

 The list w with its digits 9 replaced, from the left, by the digits of s. 

### `lowList`

 The leaves of order below t contributing to the output string with the digits w, in
lexicographic order: at the m levels of Q they have at least m - t + 1 digits 9. 

### `starRun`

 The leading digits 9 turned into 10: F_V "is the longest initial segment of Q contained in V"
(Section 4.2). 

### `boxesOf`

 The boxes of the output string with the digits w.  "There is another way to describe the boxes
of w, in terms of the leaves of order exactly t contributing to w.  For such a leaf, consider the
lowest level of Q at which it chooses a term other than P₀, and replace its P₀ by a star at every
lower level of Q (or at every level of Q, if t = 0)" (Section 4.2).  Such a leaf has at the m levels
of Q a string with exactly m - t digits 9, and the leading ones are turned into stars
(`mem_boxesOf_iff`). 

### `queryTerms`

 The numbers that a query adds up, in the order in which it adds them: the products at the leaves
of `lowList`, read from the two encodings, then the stored values of the boxes of `boxesOf`;
`stored l` is the value stored for the box l. 

 ## Putting a string at the positions of the nines 

### `scatter_cons_of_ne`

 A digit other than 9 is kept. 

### `scatter_nine_cons`

 A digit 9 is replaced by the next digit of the string. 

### `length_scatter`

 The string has the length of w. 

### `mem_of_mem_scatter`

 Every digit of `scatter w s` is a digit of w or of s. 

### `getD_scatter_of_ne`

 At a position where w has no 9, its digit is kept. 

### `count_nine_scatter`

 `scatter w s` has as many nines as s. 

### `scatter_inj`

 Strings of the right length are determined by what `scatter w` makes of them. 

 ## The leading nines turned into stars 

### `starsToNines_starRun`

 Turning the stars back into nines undoes `starRun`. 

### `starRunIf`

 `starRun` continued on the rest of a string that is read digit by digit: flag says that all the
digits read so far were nines, so the run of stars goes on; otherwise the rest is kept. 

### `starRunIf_cons_of_ne`

 A digit other than 9 ends the run. 

### `starRunIf_nine_cons`

 A digit 9 becomes a star while the run goes on, and the run goes on. 

### `Unreached`

 Position i is one of "the levels that we have not reached" (F_V, Section 4.2).  Here w is the
list of digits of the output string, so its nines are the levels of Q, and u is the list of digits
of a leaf, whose nines among them are the levels of V: i is a level of Q below every level of Q ∖ V.


### `unreached_cons_zero`

 The first position is not reached if it is a level of V. 

### `unreached_cons_succ`

 A later position is not reached if the first position is no level of Q ∖ V and the position is
not reached in the rest. 

### `getD_scatter_starRun`

 Turning the leading nines of s into stars puts stars at the positions given by the formula for
F_V, and changes nothing else. 

 ## The leaves of order below t 

### `count_nine_digitsO`

 The output string has m nines. 

### `exists_leaf_scatter`

 A string of digits below 10, put at the levels of Q, gives a leaf contributing to η that
chooses P₀ as often as the string has a nine. 

### `exists_of_mem_lowList`

 Every member of the list is the list of digits of a leaf of order below t contributing to η. 

### `length_lowList`

 There are ∑_{d < t} α_d such leaves. 

### `sum_lowList`

 **The first sum of a query**: a sum over the list is the sum over the leaves of order below t
contributing to η. 

 ## The boxes 

### `unreached_iff_mem_FV`

 The formula for F_V on digits is the formula of the paper, for V = Z. 

### `digitsC_starBelow`

 The cube of the second description of the boxes (Section 4.2): its digits are those of the leaf,
with the leading nines of the string at the levels of Q turned into stars. 

### `exists_leaf_of_mem_boxesOf`

 Every member of the list arises, as in the second description of the boxes, from a leaf of order
exactly t contributing to η. 

### `exists_of_mem_boxesOf`

 Every member of the list is the list of digits of a box of η: "The result is a box of w". 

### `length_boxesOf`

 "This means that w has exactly α_t boxes." 

### `mem_boxesOf_iff`

 **The list is the second description of the boxes** (Section 4.2): its members are exactly the
strings of the cubes obtained from the leaves τ of order exactly t contributing to η by replacing P₀
"by a star at every lower level of Q". 

### `sum_boxesOf`

 **The second sum of a query**: a sum over the list is the sum over the boxes of η. 

 ## The query 

### `sum_queryTerms_storedD`

 With the values of the dynamic program for the boxes, the numbers that a query adds up have the
sum of the query of the proof of Theorem 30. 

---
{
  "module": "ThreeSumApsp/Sec5/Lemma36b.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Lemma36b.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Lemma36b.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemma 36(b)

Lemma 36(b) reduces 3SUM on `n` real numbers to polylogarithmically many calls of a counting
problem on the blocks `A_i`, `B_j` of `d` numbers.  The reduction is cited from [CVX22]; this file
proves the part that the paper argues itself: a call is one comparison count.  The rows are the
pairs `(i,k)` and the columns the pairs `(j,ℓ)`.  All numbers have the same color, so a comparison
count is the number of pairs `x < y` between two lists (`comparisonCount_eq_card_pairs`), and by
Fredman's trick this is the count that the call asks for (`lemma_36b_count`).  The lists have
`|K'|` and `|L'|` numbers, at most `d` (`lemma_36b_lists`), and forming them costs `O(nd)`
subtractions (`lemma_36b_subtractions`).


### `comparisonCount_eq_card_pairs`

 Section 5.2: "In those of Lemma 36(b), all numbers have the same color, and γ(r,c) is the number
of pairs x < y between the two lists." 

### `card_places`

 For lists `l₁`, `l₂` without repetitions, the pairs of places of `l₁.map f` and `l₂.map g` whose
entries satisfy `Q` are as many as the pairs `(a, b)` of elements of `l₁` and `l₂` with
`Q (f a) (g b)`. 

### `color_eq_of_mem_lists45`

 All numbers in the lists of Lemma 36(b) have the same color. 

### `lemma_36b_count`

 Proof of Lemma 36(b): "By Fredman's trick, the condition is A_i[k'] - A_i[k] < B_j[ℓ] -
B_j[ℓ'].  So a call is one comparison count: the rows are the n pairs (i,k) and the columns are the
n pairs (j,ℓ) ... and P := Q."  Also with ≤, and with k' and ℓ' restricted to subsets K' and L' of
[d]. 

### `lemma_36b_lists`

 Lemma 36(b): the comparison counts have "n row lists and n column lists of at most d numbers,
all of the same color"; the proof of Lemma 36: "A restriction of k' or of ℓ' deletes numbers from
the lists." 

### `lemma_36b_subtractions`

 Lemma 36(b): "forming the lists of a comparison count costs O(nd) subtractions", with
n = b * d. 

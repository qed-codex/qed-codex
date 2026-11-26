---
{
  "module": "ThreeSumApsp/Spec/Sec2/Theorem5/PrunedList.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/PrunedList.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/PrunedList.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The pruned recursion on lists

`Pruned` (Section 2.4.2) restated on increasing lists of codes: `prunedList`.  The two encodings are
two lists of `10^L` numbers, and a vertex `τ₁ ⋯ τ_k` is given by the position `base` at which its
part of the encodings begins, that is, by the code of `τ₁ ⋯ τ_k` times `10^{L-k}`.  The result is
the list of the values in the order of the list passed.

* **Correctness** (`prunedList_spec`, `prunedList_root`): by induction on the length `n = L - k` of
  the strings passed, as in the proof of Lemma 10.  A child returns the array `C_λ` of step (3) by
  the induction hypothesis.  Step (4), which puts the output together from restrictions of the
  `C_λ`, is a function of its own, `gather`, with its own lemma (`gather_spec`): the slice at `z_ij`
  comes from `C_{P_ij}`, and the slice at `z₀` is the sum of all ten `C_λ`.
* **Work** (`prunedWork_le`): `callSizes` follows the recursion of `prunedList` and lists the
  lengths of the lists passed to its calls.  These are the sizes of the sets passed to the calls of
  `Pruned` (`callSizes_spec`), and Lemma 10 bounds their total.  The work of a call is its own plus
  that of the children that are called (`prunedWork_succ`).


 ## The function 

### `gather`

 Step (4) of `Pruned` on lists.  `l` is the list passed to the call, its strings have length
`n + 1`, and `C t` is the list that the child with digit `t` has returned.  The segment of the
output with first digit `t < 9` (the slice at `z_ij`) is the restriction of `C t`, and the segment
with first digit 9 (the slice at `z₀`) is the sum of the restrictions of all ten `C t`. 

### `prunedList`

 `Pruned` on lists, steps (1) to (4) of Section 2.4.2: `prunedList EA EB n base l` is the call
that is passed the list `l` of codes of strings of length `n`, at the vertex whose part of the
encodings `EA` and `EB` begins at the position `base`.  A child whose list is empty is not called.


 ## The ten terms, in the order of their digits 

### `range_ten_eq_map`

 The numbers below 10 are the digits of the terms. 

### `univ_term_val`

 All the terms, as a multiset, in the order of their digits. 

### `sum_term_eq`

 A sum over the terms is a sum over the digits. 

### `flatMap_term_eq`

 A concatenation over the digits, as a multiset, is a union over the terms. 

### `exists_P_of_lt_nine`

 A digit below 9 is the digit of a term `P_ij` and of the output variable `z_ij`. 

### `childList_codesOf`

 `codesOf_childSet` read by digits: the list passed to the child with digit `t` is the list of
the set `S_λ` of the term `λ` with that digit. 

 ## Step (4): the output from the arrays of the children 

### `map_codesOf_succ`

 A function applied along the list of a set, slice by slice: first the slices at the nine `z_ij`,
then the slice at `z₀`. 

### `restrictList_child`

 The restriction of the array of the child with digit `t` to a slice contained in its set. 

### `gather_spec`

 What step (4) returns.  If the child with digit `t` has returned the list `C t` of the array
`g λ` on `S_λ`, then `gather` returns the list, on `S`, of any array `F` with
`F[z_ij w'] = g P_ij [w']` and `F[z₀ w'] = ∑_λ g λ [w']` for the strings of `S`. 

 ## Correctness 

### `getD_sliceAt`

 The part of an encoding below the child with digit `t` begins `t · 10^n` places further on. 

### `prunedList_spec`

 `prunedList` computes `Pruned`, at any vertex: if the parts of `EA` and `EB` that begin at the
position `base` hold the encodings `encA` and `encB` below the vertex, then on the list of a set `S`
it returns the values of `Pruned(S)` in the order of the list. 

### `prunedList_root`

 `prunedList` at the root: with the lists of the two full encodings and `base = 0`. 

 ## The calls and their work 

### `callSizes`

 The lengths of the lists passed to all the calls that `prunedList` makes, this one included: the
same recursion as `prunedList`, with the same test for an empty list. 

### `callSizes_spec`

 The lengths that `callSizes` lists are the sizes of the sets passed to the calls of `Pruned`. 

### `sum_callSizes`

 The total length of the lists passed is the total size of Lemma 10. 

### `prunedWork`

 The work of all the calls of `prunedList`, if a call that receives a list of length `s` does
`s + 1` units of work (Section 2.4.4: "each of its steps handles each string of S a constant number
of times"; here a string is one number). 

### `prunedWork_succ`

 The work of a call and of its children. 

### `callSizes_pos`

 Every call receives a nonempty list, if the first one does. 

### `prunedWork_le`

 Section 2.4.4: "By Lemma 10, the total number of operations per leaf of Leaves(W_T) is thus
O(L²)"; with one number for each string it is `O(L)`: the work of `Pruned(U)` is at most
`2 (L + 1) |Leaves(U)|`. 

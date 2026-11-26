---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Memory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Memory.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Memory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The pruned recursion: what one round does to the memory (Section 2.4.2, steps (2) to (4))

A call of pruned with n + 1 ≥ 1 levels left runs ten rounds, one for each term λ of Schönhage's
identity.  This file has no program in it.  It says what the memory looks like before round t
(`PrunedInv`) and shows that after the four calls of a round `PrunedInv` holds for t + 1.

* Step (3).  If the list of the child is empty, the round is over (`PrunedInv.next_of_nil`).  If
  not, what the recursive call assumes holds (`PrunedPre.child`); its arguments are `x.child n t`.
* Step (4).  What the two calls of pick assume holds (`Returned.pickFirst`, `Restricted.pickLast`),
  and afterwards `PrunedInv` holds for t + 1 (`Restricted.next`).

The memories after the calls are μ₁ (`Merged`), μ₂ (`Returned`), μ₃ (`Restricted`) and μ₄.  Each of
these records says which cells its call may have changed, and `RoundSizes` holds the inequalities
between the places of a round; that a list is still where it was follows from these two.


### `PrunedInv`

 The memory before round number t of the loop: the bounds of the ten slices and the codes without
their first digits are in the frame; the slices of the result at the output variables of the terms
before t are written; the slice at z₀ holds the sum over the terms before t. 

### `PrunedPre.A_nonneg`

 The bound on the numbers of the first encoding is not negative, because there are such
numbers. 

### `PrunedPre.B_nonneg`

 The bound on the numbers of the second encoding is not negative. 

### `PrunedPre.abs_getD_mul_le`

 The product of two encoded numbers is at most A B. 

### `mul_ten_pow_mul_le`

 If 10^(n+1) numbers of size X add up to at most W, then so do k 10^n of them for k ≤ 10. 

### `PrunedInv.first`

 The first list lies in the frame. 

 ## Sizes 

### `PrunedSizes`

 The arithmetic of a frame: where the slices begin and end. 

### `PrunedPre.sizes`

 The ten slices lie within the list, because together they make it up. 

### `RoundSizes`

 The arithmetic of round t: the two lists that are merged lie one behind the other among the
codes, the list of the child is no longer than the two together, the stack of the child is no larger
than a stack for all codes, the frame and that stack fit in the memory, and the part of an encoding
below the child t lies within the part below the current vertex. 

### `PrunedPre.round`

 The inequalities of round t follow from what the call assumes. 

 ## From one round to the next 

### `PrunedInv.next`

 `PrunedInv` holds for t + 1 in a memory μ₄ if the frame, the earlier results and the cells that
do not belong to the call are as before round t, the slice at the output variable of the term t is
written, and the term t is added to the slice at z₀. 

### `PrunedInv.start`

 Before the first round: segBounds has filled the frame (memory μa), and the cells of the slice
at z₀ have been cleared (memory μb). 

### `PrunedInv.result`

 After the last round the ten slices of the result stand one behind the other. 

 ## The four calls of a round 

### `PrunedArgs.child`

 The arguments of the recursive call for the term t.  Its list is the list of the child, which
stands behind the codes in the frame; its output are the cells behind that list; its stack is what
follows. 

### `PrunedArgs.childValues`

 The values of the child t. 

### `PrunedArgs.pick`

 The arguments of a call of pick in round t: the values of the child t are restricted to the list
small, which stands at the position pos among the codes in the frame, and go to the same position of
the output. 

### `Merged`

 Step (2) is done: the list of the child t has been written behind the codes, and nothing else
has changed. 

### `Returned`

 Step (3) is done: the values of the child t have been written behind its list; only these cells
and the frames above have changed. 

### `Restricted`

 The first half of step (4) is done: the slice of the result at the output variable of the term t
has been written. 

### `PrunedInv.next_of_nil`

 Step (3), for a term λ with S_λ = ∅: if the list of the child is empty, then so are the two
slices, and the round is over. 

### `PrunedPre.child`

 Step (3): what the recursive call assumes holds. 

### `Returned.pickFirst`

 Step (4), first half (c_{z_ij} is C_{P_ij} restricted to S_{z_ij}): what the first call of pick
assumes holds. 

### `Restricted.pickLast`

 Step (4), second half (c_{z₀} is the sum of the C_λ restricted to S_{z₀}): what the second call
of pick assumes holds. 

### `Restricted.acc`

 The sum over the terms before t still stands in the slice at z₀. 

### `Restricted.next`

 Step (4) is done: after the second call of pick `PrunedInv` holds for t + 1. 

 ## The values 

### `zipWith_add_pvSum`

 Adding the values of the child t to the sum over the terms before t. 

### `abs_pvSum_le`

 The sum of the values of a code at the first k children is at most k 10^n A B. 

### `PrunedPre.abs_pvSum_le`

 The sums that are formed in the slice at z₀ fit in a word. 

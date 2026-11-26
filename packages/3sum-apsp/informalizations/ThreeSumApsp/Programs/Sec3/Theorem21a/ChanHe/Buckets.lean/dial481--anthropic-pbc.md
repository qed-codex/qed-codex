---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Buckets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Buckets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Buckets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: remainders, counts, collisions, heavy elements

Four routines of the reduction of [CH20, Theorem 5.1] (for Theorem 21(a)).
They hash a set of integers modulo M.

* resid writes the remainders of the elements of a set (`resid_spec`).
* tally adds the remainders to a table of counts, or removes them from it (`tally_spec`).
* coll returns the number of colliding ordered pairs (`coll_spec`): by `coll_eq_list` it is the sum,
  over the elements, of the size of the element's bucket minus 1.
* heavy extracts the elements that are not alone in their bucket (`heavy_spec`,
  `heavyList_toFinset`).

In the statements the modulus is Mo, since in a program text M (…) reads a cell of the memory.
`keys M L` is the list of the remainders x % M of the numbers of L, as natural numbers, and `SegN`
is `Seg` for a list of natural numbers.

coll and heavy begin and end in the same way: resid writes the remainders to the free pointer, tally
counts them (`Counted`), a loop reads the counts, and tally removes them, so that the table holds
zeros again.  The three calls are `BucketPre.resid_meets`, `count_meets` and `uncount_meets`.


 ## resid 

### `Len`

 The local variables of resid: the arguments len, s, sg, M, key, fr, the counter i, and the
remainder. 

### `residBody`

 resid(len, s, sg, M, key, fr): for i < len, mem[key + i] := emod(sg * mem[s + i], M, fr). 

### `emodNeed_ok`

 What is allowed for resid covers what emod needs one level of calls further down. 

### `ResidInv`

 The memory before round i of resid: the first i remainders are written, and below the free
pointer no cell outside the len cells from key has changed. 

### `ResidInv.succ`

 A round of resid: emod has changed no cell below the free pointer, and remainder number i is
written. 

### `resid_spec`

 **resid** meets its specification. 

 ## tally 

### `Len`

 The local variables of tally: the arguments len, key, cnt, δ, and the counter i. 

### `tallyBody`

 tally(len, key, cnt, δ): for i < len, mem[cnt + mem[key + i]] += δ. 

### `TallyInv`

 The memory before round i of tally: the first i keys have been counted, and no cell outside the
count table has changed. 

### `TallyInv.succ`

 A round of tally counts the key number i. 

### `tally_spec`

 **tally** meets its specification. 

 ## The pure side: buckets, collisions and heavy elements from the list of the remainders 

### `coll_eq_list`

 The number of colliding pairs, from the list of the remainders. 

### `mem_heavy_iff`

 An element is heavy exactly if its bucket has at least two elements. 

### `heavyList`

 The heavy elements, as a sublist. 

### `heavyList_toFinset`

 The sublist consists of the heavy elements. 

 ## What coll and heavy share: the remainders are counted, used, and removed from the table 

### `BucketPre`

 What coll and heavy assume: the list L at s, a count table of zeros with a cell for each
remainder, both below the free pointer and apart, and the limits. 

### `Counted`

 Between the two calls of tally: the remainders stand at the free pointer, and the table holds
how often each of them occurs. 

### `sq_add_le_word`

 What the need provides: a sum of len counts, which is at most len², and a few more fit in a
word. 

### `sameOn_of_zeroAt`

 A table that held zeros and holds zeros again has not changed. 

### `Counted.of_sameOutside`

 What is counted stays counted if neither the remainders nor the table change. 

### `BucketMem.exists_pre`

 What coll and heavy are given, in the form in which they use it: the set is a list without
repetitions. 

### `resid_meets`

 resid(len, s, sg, M, fr, fr + len) writes the remainders of the numbers sg · x to the free
pointer. 

### `keys_meets`

 resid(len, s, 1, M, fr, fr + len) writes the remainders of the numbers of L to the free
pointer. 

### `tally_meets`

 tally(len, fr, cnt, δ), run on the remainders K at the free pointer, adds δ times the number of
occurrences of q in K to cell q of the table.  Of the hypotheses of `TallySpec` only the bound on
the table is left. 

### `count_meets`

 tally(len, fr, cnt, 1) counts the remainders. 

### `uncount_meets`

 tally(len, fr, cnt, -1) removes the remainders from the table. 

 ## coll 

### `Len`

 The local variables of coll: the arguments len, s, M, cnt, fr, the results of the calls, which
are not used, the counter i, and the sum.  Local 0 also takes the result. 

### `collSum`

 The part of coll that adds up: sum := 0; for i < len, sum += mem[cnt + mem[fr + i]] - 1. 

### `collBody`

 coll(len, s, M, cnt, fr) writes the remainders to fr, counts them, adds up, removes them from
the table, and returns the sum. 

### `collPart`

 The sum over the first `i` remainders. 

### `collPart_succ`

 The sum over the first i + 1 remainders is that over the first i, plus the term of remainder
i. 

### `collPart_bounds`

 The sum over the first `i` remainders lies between 0 and `i` times the number of remainders. 

### `collSum_ends`

 **The loop of coll** leaves the sum over all remainders in the local Total and writes no
cell. 

### `coll_spec`

 **coll** meets its specification. 

 ## heavy 

### `Len`

 The local variables of heavy: the arguments len, s, M, out, cnt, fr, the results of the calls,
which are not used, the counter i, and the number j of elements written.  Local 0 also takes the
result. 

### `heavyRound`

 A round of the loop of heavy: if 1 < mem[cnt + mem[fr + i]] then mem[out + j] := mem[s + i] and
j := j + 1. 

### `heavyCopy`

 The part of heavy that copies: j := 0; a round for each i < len. 

### `heavyBody`

 heavy(len, s, M, out, cnt, fr) writes the remainders to fr, counts them, copies the heavy
elements, removes the remainders from the table, and returns the number of heavy elements. 

### `isHeavy`

 The test of heavy: the remainder of `x` occurs at least twice among the remainders. 

### `heavyPart`

 The heavy elements among the first `i` elements of the list. 

### `heavyPart_length`

 The heavy elements among all elements of the list are the list of the heavy elements. 

### `HeavyInv`

 The state before round i of the loop of heavy: the heavy elements among the first i elements
are written, and no cell outside the output has changed. 

### `heavyRound_ends`

 **A round of the loop of heavy** copies element i if it is heavy.  μ₀ is the memory at the start
of heavy (of C only the layout and the limits are used), μ the memory at the start of the loop.  The
conclusion has the form that `Ends.for` asks of a round. 

### `heavyCopy_ends`

 **The loop of heavy** writes the heavy elements and leaves their number in the local Written. 

### `heavy_spec`

 **heavy** meets its specification. 

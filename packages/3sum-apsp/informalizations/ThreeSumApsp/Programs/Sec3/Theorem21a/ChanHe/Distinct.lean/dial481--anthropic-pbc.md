---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Distinct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Distinct.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Distinct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: distinct values, doubles of repeated values, a triple zero

Theorem 21(a), after [CH20, Theorem 5.1].  The three-set inputs of the
reduction for n numbers are made from the set of the values, from the doubles of the values that are
not 0 and occur at least twice (`ChanHe.twiceSet`), and from the set that is {0} if 0 occurs at
least three times and empty if not (`ChanHe.zeroSet`).  Three passes prepare these sets.

* zeroThree passes over the values and their multiplicities and answers whether 0 occurs at least
  three times (`zeroThree_spec`).
* twice passes over the same two lists and writes the doubles of the values that are not 0 and occur
  at least twice (`twice_spec`, with `twiceRound_runs` for one round).
* distinct passes over the sorted input and writes these two lists: the distinct values, and how
  often each occurs (`distinct_spec`, with `distinctRound_runs` for one round).

Each section first says what the pass has written or found after the first i elements, and how one
more element changes it.  The invariant of the loop is this, and the proof of a round compares the
tests of the program with the cases of that step.  The body of each loop is a block: a goal
`s.Runs lim σ R` is a pair, which says that the block s, started in σ, stays within the limits, and
that R holds of the state after it.  A procedure returns what its local 0 holds at the end.


 ## zeroThree 

### `tripleZeroUpTo`

 The answer of zeroThree for the first i values: 1 if one of them is 0 and occurs at least three
times, and 0 if not. 

### `tripleZeroUpTo_succ`

 One more value. 

### `tripleZeroUpTo_length`

 At the end the answer is the one that the specification asks for. 

### `Len`

 The locals of zeroThree: the arguments nd, val and mul, the counter, and the answer so far. 

### `zeroThreeBody`

 zeroThree(nd, val, mul): the nd values stand at val and their multiplicities at mul.  Returns 1
if the value 0 occurs at least three times, and 0 if not. 

### `ZeroThreeInv`

 The invariant of the loop of zeroThree before round number i: the answer so far is the answer
for the first i values, and the memory has not changed. 

### `zeroThree_spec`

 **zeroThree** meets its specification. 

 ## twice 

### `twicePart`

 What twice has written after it has seen the first i values. 

### `twicePart_succ`

 One more value: its double is written if it is not 0 and occurs at least twice. 

### `twicePart_length`

 At the end all the doubles are written. 

### `Len`

 The locals of twice: the arguments nd, val, mul and out, the counter, and the number of cells
written. 

### `twiceRound`

 One round of twice: the double of the next value is written if the value is not 0 and occurs at
least twice. 

### `twiceBody`

 twice(nd, val, mul, out): the nd values stand at val and their multiplicities at mul.  Writes
the doubles of the values that are not 0 and occur at least twice to out, and returns their number.


### `TwiceInv`

 The invariant of the loop of twice before round number i: the doubles for the first i values
stand at out, and no other cell has changed. 

### `twiceRound_runs`

 One round of twice keeps the invariant. 

### `twice_spec`

 **twice** meets its specification. 

 ## distinct 

### `DistinctMem`

 What distinct has written after it has seen the first i elements of the sorted list L: their
distinct values D stand at val, how often each has occurred stands at mul, and no other cell has
changed. 

### `DistinctMem.values`

 D lists the distinct values among the first i elements. 

### `DistinctMem.segVal`

 The values stand at val. 

### `DistinctMem.segMul`

 Their numbers of occurrences so far stand at mul. 

### `DistinctMem.same`

 No other cell has changed. 

### `opens`

 An element that differs from the last value opens a new cell of val and a new cell of mul. 

### `bumps`

 An element that equals the last value raises the last cell of mul by one. 

### `Len`

 The locals of distinct: the arguments n, a, val and mul, the counter, and the number of distinct
values so far. 

### `distinctOpen`

 A new value opens a new cell of val and of mul. 

### `distinctRound`

 One round of distinct: the next element opens a cell if there is no value yet or if it differs
from the last value, and raises the last cell of mul if not. 

### `distinctBody`

 distinct(n, a, val, mul): a sorted list of n numbers stands at a.  Writes its distinct values to
val and how often each occurs to mul, and returns the number of distinct values. 

### `DistinctInv`

 The invariant of the loop of distinct before round number i: the memory is as `DistinctMem`
says for the first i elements, and Values holds the number of distinct values among them. 

### `distinctRound_runs`

 One round of distinct keeps the invariant. 

### `distinct_spec`

 **distinct** meets its specification. 

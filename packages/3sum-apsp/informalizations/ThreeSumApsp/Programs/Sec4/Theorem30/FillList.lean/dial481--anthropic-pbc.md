---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/FillList.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/FillList.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/FillList.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The boxes with e stars go into the trie of their tile (Lemma 29)

"Given the two encodings of a tile, we can compute the values of all these boxes, and store them in
the trie for that tile, in O(L) time and space per box."  "We compute the values of the boxes in
increasing order of their number of stars."  This routine handles the boxes with e stars.  It goes
through the leaves with between e and m - t symbols P₀ in lexicographic order.  For each of them it
turns the first e nines into stars, which gives the next box with e stars; computes the value of the
box, for e = 0 as the product of the two encoded numbers at its code and for e ≥ 1 as the sum of the
values of ten boxes with e - 1 stars, looked up in the trie of the tile; and inserts the box with
its value into the trie.

1. The first section is about lists only: `fillAt` is the trie array after the first i boxes, and
   `StarBox` collects what the routine needs to know about a box with stars (`exists_starBox`).
2. `FillListArgs` holds the data of one run, `FillListPre` what the routine assumes, and
   `FillList.Callees` the specifications of the routines that are called.  `FillList.Inv` is the
   invariant of the loop, and `FillList.RoundFacts` what is known in a round once the box has been
   written.  A round is the call of starFirst, the value (`value_zero_spec`, `value_succ_spec`,
   `fillValue_spec`) and the end of the round (`tail_spec`); together they are `round_spec`, and
   `body_spec` is the whole run.  `fillList_spec` is the specification.


 ## The trie array after the first boxes 

### `fillAt`

 The trie array after the first i boxes with e stars. 

### `fillAt_succ`

 One more box: it is inserted with the value computed from the array so far. 

### `fillAt_rep`

 What the tries hold after the first i boxes. 

### `length_fillAt_le`

 The array grows by at most 11 L cells for each box. 

### `abs_getD_arrT_le`

 An entry of the array of an encoding is a value of the encoding. 

### `StarBox`

 What the routine needs to know about a box with e + 1 stars. 

### `StarBox.last`

 p is the position of the last star. 

### `StarBox.walk`

 The ten strings are stored in the trie. 

### `StarBox.sums`

 The partial sums of their values are bounded. 

### `exists_starBox`

 A box with e' + 1 stars, in a trie that holds the boxes with at most e' stars, is as `StarBox`
says. 

 ## The program 

### `Stars`

 The local variables of fillList: the arguments (the number e of stars, the root of the trie of
the tile, the addresses of the two encodings, the base of the trie area, the address of the free
pointer, the addresses of the leaf and of the box, their length, and m - t), whether there is
another leaf, the position of the last star, the value of the box, its code, and results that are
not used. 

### `fillValueZero`

 The value of a box without stars: the product of the two encoded numbers at its code. 

### `fillValue`

 The value of the box: for a box with stars, the sum of ten values looked up in the trie that is
being filled. 

### `fillTailStmt`

 The end of a round: insert the box with its value, and form the next leaf. 

### `fillRound`

 One round: the box of the leaf, its value, the insertion, the next leaf. 

### `fillListBody`

 fillList(e, root, encA, encB, area, free, leaf, box, len, m - t): start with the least leaf, and
handle one leaf in each round as long as there is another. 

### `leaves`

 The leaves that the run goes through. 

### `trieAt`

 The trie array after the first i boxes. 

### `value`

 The value that the routine computes for a box, from the trie array Ti. 

### `locals`

 The locals: the ten arguments, and then More, LastStar, Value, Code and Junk. 

### `Callees`

 The routines that fillList calls meet their specifications. 

### `MemInv`

 The memory ν before round number i: leaf number i, if there is one, is at cur; the first i boxes
have been inserted; the two encodings are in place. 

### `Inv`

 The invariant of the loop, before round number i: the arguments are in place, More says whether
there is a leaf number i, and the memory is as `MemInv` says. 

### `RoundFacts`

 What is known in round number i once the box has been written: l is the leaf, Ti the trie array
before the round, ν the memory. 

### `RoundFacts.next`

 nineNext goes to leaf number i + 1. 

### `RoundFacts.succ`

 The round inserts the box with its value. 

### `RoundFacts.rep`

 The trie holds the boxes with fewer stars and the first i boxes with e stars. 

### `tail_spec`

 The end of a round: the box is inserted with its value, and the next leaf is formed. 

### `value_zero_spec`

 The value of a box without stars. 

### `value_succ_spec`

 The value of a box with stars. 

### `fillValue_spec`

 The value of the box. 

### `round_spec`

 One round of the loop handles leaf number i. 

### `body_spec`

 The whole run. 

### `fillList_spec`

 **fillList** inserts the boxes with e stars, with their values, into the trie of their tile. 

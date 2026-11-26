---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/StarFirst.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/StarFirst.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/StarFirst.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The lowest symbols P₀ of a leaf turned into stars

Proof of Lemma 29: "A box in which f of the symbols are P₀ or stars is obtained from a leaf of order
m - f […] by turning the e lowest symbols P₀ of that leaf into stars, for some e ≤ f."  The routine
copies a string of L digits and writes 10 (the star) in place of its first e digits 9
(`Spec.starFirst`).  It returns the position of the last star of the copy, "the highest level at
which π has a star" (proof of Lemma 29), which the dynamic program of Lemma 29 expands
(`Spec.lastStar`).

One pass that keeps two numbers: how many nines have been turned into stars so far, and the
position of the last star so far.  The first section says how one more digit changes the copy and
the two numbers; `StarFirst.round_runs` says that a round of the program does just this;
`StarFirst.Inv` is the invariant of the loop.


 ## One more digit 

### `lastStar_concat`

 The last star of a list with one more digit. 

### `turned`

 The number of nines among the first i digits that are turned into stars. 

### `lastPos`

 The position of the last star among the first i digits of the copy (0 if there is none). 

### `getD_starFirst_eq`

 The digit of the copy: a nine becomes a star as long as fewer than e nines have been turned. 

### `turned_succ`

 One more digit: a nine is turned as long as fewer than e have been. 

### `lastPos_succ`

 One more digit: a star moves the position of the last star. 

 ## The program 

### `Src`

 The local variables of starFirst: the arguments (the address of the string, the address of the
copy, the length, the number of stars), the position, the position of the last star so far, the
digit, and the number of nines turned into stars so far.  Local 0 also takes the result. 

### `starFirstRound`

 One round: read a digit, turn it into a star if it is one of the first e nines, remember the
position if a star is written, write the digit, and go on. 

### `starFirstBody`

 starFirst(src, dst, len, stars): copy the string, with its first nines as stars, and return the
position of the last star.  The locals that are not arguments start at 0. 

### `round_runs`

 What a round does, for the digit x that is read, with c nines turned and the last star at p. 

### `Inv`

 Before round i the first i digits of the copy have been written, and the two counters are up to
date. 

### `starFirst_spec`

 **starFirst** writes the copy with the first e nines as stars, and returns the position of its
last star. 

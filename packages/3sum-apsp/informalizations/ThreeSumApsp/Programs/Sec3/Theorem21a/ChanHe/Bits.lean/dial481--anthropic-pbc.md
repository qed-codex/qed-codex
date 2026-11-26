---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Bits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Bits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Bits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: binary digits of the labels, and selection by digits

Theorem 21(a), after [CH20, Theorem 5.1].  The reduction for n numbers
splits the set of the values by one or two binary digits of the labels x + V (`ChanHe.splitA`,
`ChanHe.splitB`).  Two routines do this.

* pick copies the elements whose digits at one or two given positions have given values
  (`pick_spec`, with `pickRound_runs` for one round).  What it has written after the first i
  elements is `pickPart`, and `Pick.Ctx.step` says how one more element changes it, in terms of the
  cells that the program reads.
* bits writes the table of the binary digits of the labels, Λ cells for each element (`bits_spec`,
  with `bitsElem_ends` for one element).  It first computes 2^Λ by doubling (`bitsPow_ends`).  The
  digits of one label are found from the top down: the rest of the label is doubled, and the digit
  is 1 if the result reaches 2^Λ (`bitsRow_ends`).

Where the body of a loop is a block, the goal of a round is `s.Runs lim σ R`.  This is a pair, which
says that the block s, started in σ, stays within the limits, and that R holds of the state after
it.  A procedure returns what its local 0 holds at the end.


 ## pick 

### `pickPart`

 What pick has written after it has seen the first i elements. 

### `pickPart_succ`

 One more element: it is written if its digit β is x and, in case two is not 0, its digit β' is
x'. 

### `pickPart_length`

 At the end all the selected elements are written. 

### `Len`

 The locals of pick.  The arguments: len, s, bt, Λ, the first position β and digit x, the second
position β' and digit x', the number two, which is 0 if only the first digit counts, and out.  Then
the counter, the number of cells written, and the address of the digits of the current element. 

### `pickTake`

 The current element is selected. 

### `pickNext`

 The end of a round of pick. 

### `pickRound`

 One round of pick. 

### `pickBody`

 pick(len, s, bt, Λ, β, x, β', x', two, out): len numbers stand at s, and the table of their
digits at bt.  Copies to out the numbers whose digit β is x and, unless two is 0, whose digit β' is
x', and returns how many there are. 

### `Pick.Ctx.step`

 One more element, in terms of the cells that the program reads. 

### `PickInv`

 The invariant of the loop of pick before round number i: the elements selected among the first i
stand at out, no cell outside the output has changed, and Row holds the address bt + iΛ of the
digits of element i, which is called row. 

### `pickRound_runs`

 One round of pick keeps the invariant. 

### `pick_spec`

 **pick** meets its specification. 

 ## bits 

### `DigitsFrom`

 The digits of z from position ℓ on stand in their cells of the row of Λ cells from row, and no
cell outside the row has changed. 

### `DigitsFrom.digits`

 The digits from position ℓ on are written. 

### `DigitsFrom.same`

 No cell outside the row has changed. 

### `DigitsFrom.write`

 One more digit is written. 

### `DigitsFrom.seg`

 When all digits are written, the row holds them. 

### `Len`

 The locals of bits.  The arguments: len, s, V, Λ, bt and the free pointer, which is not used.
Then the counter, the power 2^Λ, the address of the digits of the current element, the address of
the current digit, the rest of the label, and the counter of the loop that computes the power. 

### `bitsPow`

 The power 2^Λ, by doubling. 

### `bitsRow`

 The digits of one label, from the top down: the rest of the label is kept at the top of Λ bits;
it is doubled, and the digit is 1 if the result reaches 2^Λ. 

### `bitsElem`

 The digits of the label of the current element. 

### `bitsBody`

 bits(len, s, V, Λ, bt, fr): len numbers of absolute value at most V stand at s.  Writes the Λ
lowest binary digits of each label x + V to the table at bt. 

### `BitsPowInv`

 The invariant of the loop of bitsPow before round number j: Pow holds 2^j. 

### `bitsPow_ends`

 bitsPow puts 2^Λ into Pow. 

### `BitsRowInv`

 The invariant of the loop of bitsRow before round number t: the digits from position ℓ = Λ - t
on are written, Cur points to the cell of digit ℓ, and Rest holds the lower digits, moved up to the
top of Λ bits: the number (z mod 2^ℓ) 2^(Λ - ℓ), which is `prefR Λ ℓ z`. 

### `bitsRow_ends`

 bitsRow writes the digits of z into the row. 

### `BitsInv`

 The invariant of the main loop of bits before round number i: the digits of the first i labels
stand at bt, no cell outside the table has changed, and Row holds the address bt + iΛ of the next
row. 

### `bitsElem_ends`

 One round of the main loop of bits keeps the invariant. 

### `bits_spec`

 **bits** meets its specification. 

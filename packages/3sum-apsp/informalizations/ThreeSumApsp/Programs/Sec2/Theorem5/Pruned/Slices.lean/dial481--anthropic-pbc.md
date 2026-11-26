---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Slices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Slices.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Slices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Cutting an increasing list of codes into its ten slices (step (2) of Pruned, Section 2.4.2)

segBounds goes once through an increasing list of codes of n + 1 digits.  The codes with first digit
z are consecutive; it notes where they start, and writes every code without its first digit.

* The list.  `SegInv` says where the pass stands: i codes are copied, z is the current first digit,
  and lo = z 10^n.  A code below lo + 10^n is copied (`SegInv.copy`); otherwise the pass goes on to
  the next first digit (`SegInv.advance`), and the position reached is the start of the next slice
  (`SegInv.segStart_succ`).
* The memory.  `SegMem` says what has been written, `SegMem.copy` and `SegMem.advance` what a round
  adds, and `SegMem.slices` that in the end the ten slices stand in the memory.
* The program.  `segCopy_ends` and `segAdvance_ends` treat the two kinds of rounds, and
  `segBounds_entry` the loop.  The result: a call takes at most `cSegBounds` steps for each code and
  each of the eleven bounds; afterwards the cells bnd to bnd + 10 hold the starts of the slices, the
  slice at z stands at bnd + 11 + segStart n codes z, and no other cell has changed.


 ## The program 

### `PL`

 The list of the codes. 

### `LEN`

 The length of the list. 

### `PW`

 10^n. 

### `BND`

 Where the bounds are written; the codes without first digits follow 11 cells later. 

### `CI`

 The position i in the list. 

### `CZ`

 The first digit z. 

### `LO`

 z 10^n. 

### `HI`

 (z + 1) 10^n. 

### `segCopy`

 The code at position i has first digit z: it is written without that digit. 

### `segAdvance`

 The next first digit: z := z + 1, the position reached is noted at bnd + z, and the two
thresholds move up. 

### `segBoundsBody`

 segBounds(l, len, pw, bnd). 

### `cSegBounds`

 The constant of the running time: a call takes at most cSegBounds (codes.length + 11) steps. 

 ## The list 

### `length_takeWhile_lt_eq`

 The number of codes below a, for a list in which the codes below a come first. 

### `segStart_eq_length_takeWhile`

 The start of the slice at z is the number of codes below z 10^n. 

### `getD_segStart_add`

 The codes of the slice at z, in the list. 

### `mod_eq_sub_mul_of_lt`

 A code between z pw and (z + 1) pw, without its first digit. 

### `SegInv`

 Where the pass stands: the first i codes are below lo + pw, the others are at least
lo = z pw. 

### `SegInv.copy`

 The code at position i has first digit z. 

### `SegInv.advance`

 No code that is left has first digit z. 

### `SegInv.segStart_succ`

 Then the position reached is the start of the slice at z + 1. 

### `SegInv.mod_eq`

 The code at position i without its first digit. 

 ## The memory 

### `SegMem`

 What has been written: the starts of the slices up to z, and the first i codes without their
first digits. 

### `SegMem.copy`

 One more code is copied. 

### `SegMem.advance`

 The start of the next slice is noted. 

### `SegMem.slices`

 When all codes are copied, the slice at z stands at the start of that slice. 

 ## The pass 

### `SegPre`

 What segBounds assumes. 

### `segState`

 The state of the loop. 

### `SegLoop`

 The invariant of the loop. 

### `segRest`

 The codes and the first digits that are left. 

### `SegNext`

 What a round that starts in σ achieves: the invariant holds again, and less is left. 

### `SegPre.read`

 The list lies below what is written, so it can be read at any time. 

### `SegPre.mono`

 The list increases. 

### `SegPre.all_copied`

 No code has first digit 10, so at z = 10 all codes are copied. 

### `SegInv.lo_le`

 lo = z 10^n is at most 10 · 10^n. 

### `segCopy_ends`

 The round in which a code is copied. 

### `segAdvance_ends`

 The round in which the pass goes on to the next first digit. 

### `segBounds_entry`

 **segBounds**: a call takes at most cSegBounds (codes.length + 11) steps.  Afterwards the cells
bnd to bnd + 10 hold the starts of the ten slices and the end of the last one, the slice at z stands
at bnd + 11 + segStart n codes z, and no other cell has changed. 

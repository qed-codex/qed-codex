---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/NineNext.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/NineNext.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/NineNext.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The next string of the enumeration

nineNext(a, n, lo, hi) replaces the string of n digits at a by the next string with between lo and
hi nines (`Spec.nineNext`), and returns 1; if the string is the last one, it leaves it and
returns 0.  This is the step of all three enumerations of Section 4 (proof of Lemma 29: "Generating
the boxes with e stars […] also takes O(L) operations per box"; proof of Theorem 30: "Enumerating
them also takes O(L) operations per number").

There are two passes, as in `Spec.nineNext_eq_scan`.
1. The first pass finds the last position that can be raised and the number of nines before it.  One
   round is `Spec.nineScanStep` (`scanRound_runs`), so after i rounds the locals hold
   `Spec.nineScan hi l i` (`ScanInv`).
2. The second pass computes how many nines are needed behind that position (`needStmt_runs`), raises
   the digit and writes the least admissible filling behind it (`fillTail_spec`).  What stands in
   the memory then is `Spec.raiseAt` (`segN_raiseAt`).


### `MaxNines`

 The further local variables of nineNext: the largest number of nines, the state of the scan
(whether a position that can be raised has been found, the last such position, the number of nines
before it, the number of nines seen so far), and a digit. 

 ## The first pass 

### `markStmt`

 Remember the current position and the number of nines before it. 

### `raiseTest`

 If the digit can be raised, remember its position. 

### `scanRound`

 One round of the scan: read the digit at the current position, remember the position if the
digit can be raised, count the digit if it is a nine, and go on. 

### `scanFrame`

 The locals during the scan: the arguments, the position i, the state s of the scan, and the
digit read last. 

### `scanRound_runs`

 One round of the scan is `Spec.nineScanStep`. 

### `ScanInv`

 Before round i the locals hold the state of the scan after i cells.  The memory is not
changed. 

 ## The second pass 

### `needStmt`

 The digit at the position found, and the number of nines that have to be written behind it:
lo - before, less one if the digit becomes a nine, and not below 0. 

### `needStmt_runs`

 needStmt computes the subtraction of natural numbers in `Spec.raiseAt`. 

### `segN_raiseAt`

 The string with the digits before p kept, the digit at p raised and the least filling behind it
is `Spec.raiseAt`. 

### `raiseStmt`

 The second pass: raise the digit at the position found, and write the least admissible filling
behind it. 

### `raiseStmt_spec`

 The second pass writes `Spec.raiseAt` for the position that the scan has found, and
returns 1. 

 ## The routine 

### `nineNextBody`

 nineNext(str, len, minNines, maxNines): scan the string; if a position can be raised, write the
next string and return 1, and return 0 if not.  The locals of the scan start at 0. 

### `nineNext_spec`

 **nineNext** replaces the string by the next one and returns 1, or leaves the last string and
returns 0. 

---
{
  "module": "ThreeSumApsp/Spec/Sec4/Theorem30/NineScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/NineScan.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/NineScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The successor of a string, as two passes from left to right

`nineNext`, which goes from a string with a bounded number of nines to the next one, is defined by
recursion on the string.  A machine goes through the cells of a buffer from left to right.  This
file gives the function in that shape.

* One pass over the string finds the last position whose digit can be raised, and the number of
  nines before it (`nineScan`).
* A second pass writes the next string: the digits before that position are kept, its digit is
  raised by one, and the rest is filled with zeros followed by nines (`raiseAt`).

The result is `nineNext_eq_scan`.  It is proved in two steps: `nineNext` raises the last position
that can be raised (`raisePos`, `nineNext_eq_raise`), and the scan finds that position
(`nineScanFrom_eq`).  For the routine there are, besides, an invariant of the scan
(`nineScan_inv`) and the fact that the filling fits behind the position that is raised
(`raise_fits`).


 ## The last position that can be raised 

### `canRaise`

 Whether the digit d can be raised when c nines come before it and at most hi nines are
allowed. 

### `raisePos`

 The last position of the string whose digit can be raised, with the number of nines before it;
c nines come before the string. 

### `raiseAt`

 The string with the digit at position p raised by one and the least admissible filling behind
it; c nines come before p. 

### `le_of_canRaise`

 A digit that can be raised is at most 8. 

### `raise_head`

 What `nineNext` does to the first digit when the rest of the string cannot be raised. 

### `nineNext_eq_raise`

 `nineNext` raises the last position that can be raised. 

 ## The scan from left to right 

### `NineScan`

 The state of the scan: 1 if a position that can be raised has been seen, the last such
position, the number of nines before it, and the number of nines seen so far. 

### `nineScanStep`

 One step of the scan: the cell number i holds the digit d. 

### `nineScanFrom`

 The scan of a list whose first cell has the number i. 

### `nineScan`

 The state after the first j cells. 

### `nineScanFrom_append`

 The scan of two lists one after the other: the second list is scanned from the state after the
first. 

### `nineScan_succ`

 The state after one more cell is one step of the scan from the state before that cell. 

### `nineScanFrom_eq`

 The scan finds the last position that can be raised. 

### `nineNext_eq_scan`

 **The successor by two passes.**  After the scan of the whole string, either no position can be
raised and the string is the last one, or the next string is obtained by raising the position
found. 

 ## What the scan has found 

### `NineScanInv`

 What holds of the state s of the scan after j cells: the counter holds the number of nines
among them, and the position found, if any, is one of them, can be raised, and has the recorded
number of nines before it. 

 ## The filling fits 

### `raise_fits`

 Behind a position that can be raised there is room for the nines that are still needed. 

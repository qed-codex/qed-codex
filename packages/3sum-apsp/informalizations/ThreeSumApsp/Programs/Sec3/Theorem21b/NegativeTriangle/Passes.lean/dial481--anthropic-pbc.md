---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/Passes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/Passes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/Passes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Two loops over arrays for the reduction from Negative Triangle to Exact Triangle

[VW13, Theorem 3.3] in the form needed for Theorem 21(b).  The reduction compares
the binary prefixes of shifted weights; the two loops of this file shift the weights and compute the
prefixes, one more bit at a time.

affine(len, src, m, c, dst) writes m · src[i] + c to dst[i] for i < len, in at most 20 len + 6
steps (`affine_meets`).  prefDown(len, q, r, P) makes one step of the computation of the prefixes on
the arrays q and r: it appends the next bit to q[i] and removes it from r[i], for i < len, in at
most 38 len + 6 steps (`prefDown_meets`).  For prefDown the memory after j rounds is written down
(`prefMem`), `prefDownRound_spec` says what one round does, and the loop rule does the rest.  For
m = ±1 and a list that is bounded by U, `affine_meets_of_absLe` has the side conditions in terms
of U.


 ### The locals of affine 

### `Len`

 The number of cells. 

### `Src`

 The address of the source. 

### `Factor`

 The factor m. 

### `Shift`

 The summand c. 

### `Dst`

 The address of the destination. 

### `Idx`

 The counter i. 

### `affineBody`

 affine(len, src, m, c, dst): for i < len, dst[i] := m · src[i] + c. 

 ### The locals of prefDown 

### `Len`

 The number of pairs. 

### `ArrQ`

 The address of the array q. 

### `ArrR`

 The address of the array r. 

### `Power`

 The number P with which 2 r[i] is compared (a power of two in the reduction). 

### `Idx`

 The counter i. 

### `Twice`

 2 r[i]. 

### `prefDownRound`

 One step on the pair (q[i], r[i]). 

### `prefDownBody`

 prefDown(len, q, r, P): for i < len, one step on (q[i], r[i]). 

### `affine_meets`

 **affine** writes the list of the numbers m x + c, for x in the list at src, to dst, and changes
nothing else. 

 ### prefDown 

### `prefMem`

 The memory after j rounds of prefDown: the first j pairs have made their step. 

### `prefMem_q_done`

 A cell of q that has made its step. 

### `prefMem_r_done`

 A cell of r that has made its step. 

### `prefMem_rest`

 A cell that has not been written (yet). 

### `prefMem_succ`

 What round j writes. 

### `PrefPre`

 What prefDown needs: the two arrays lie in the memory, apart from each other, and the numbers
that are formed fit in a word. 

### `prefDownRound_spec`

 **One round of prefDown** makes the step on the pair (q[j], r[j]) and leaves 2 r[j] in Twice. 

### `prefDown_meets`

 **prefDown** makes one step on every pair (q[i], r[i]), and changes nothing else. 

 ## affine with the factor ± 1 on a list with bounded entries 

### `affine_fits`

 The numbers ± y + c for |y| ≤ U lie between c - U and c + U. 

### `absLe_affL`

 A bound on the entries of the list of the numbers ± y + c. 

### `affine_meets_of_absLe`

 **affine(N, src, ± 1, c, dst)** writes the list of the numbers ± y + c to N cells above the
list, and changes nothing else. 

---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/Passes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/Passes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/Passes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Two passes over an array, for the (min,+)-product found bit by bit

Two routines of the host for [VW18, Theorem 4.2], one of the reductions behind Theorem 21(b).

addc(len, x, src, dst): dst[i] := src[i] + x, in at most 19 len + 6 steps (addc_meets).
bump(len, x, fl, lo): lo[i] := lo[i] + x (1 − fl[i]), in at most 30 len + 6 steps: where the flag
is 0 the entry grows by x (bump_meets).
Both change no other cell.  Each is one pass, so each proof only says what round j reads.


### `Len`

 The local variables of addc and bump: the arguments len, x (Summand), the array that is only
read (src or fl) and the array that is written (dst or lo), and the counter. 

### `addcBody`

 addc(len, x, src, dst): for i < len, dst[i] := src[i] + x. 

### `bumpBody`

 bump(len, x, fl, lo): for i < len, lo[i] := lo[i] + x (1 − fl[i]). 

### `addc_meets`

 **addc** writes the list with x added to every entry to dst and changes nothing else. 

### `bump_meets`

 **bump** adds x (1 − flag) to every entry of the list at lo and changes nothing else.  The flags
are 0 or 1, and V bounds the entries. 

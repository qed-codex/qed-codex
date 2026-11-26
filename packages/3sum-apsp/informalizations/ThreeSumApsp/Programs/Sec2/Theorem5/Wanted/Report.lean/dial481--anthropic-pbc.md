---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Report.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Report.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Report.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 as a program: the report

Section 2.4.4: "and report, for each (I, J) ∈ W, the value at its output string."

The pruned recursions leave the values in the sorted order of the wanted positions.  report puts
them back in the order in which the positions were given: OUT[PERM[i]] := SV[i].  It is the
counterpart of gather, which reads through the permutation.  `report_entry` is one loop with the
invariant `ReportInv`; the places PERM[i] are different, so no value is overwritten
(`ReportInv.write`).


### `ReportSpec`

 report(w, perm, sv, out): OUT[PERM[i]] := SV[i] for all i < w.  π is the list in PERM, a list of
w different indices below w; the output lies below PERM and SV. 

### `LEN`

 The number w of wanted positions. 

### `PERM`

 The permutation, sorted order to given order. 

### `VALS`

 The values, in sorted order. 

### `OUT`

 The output. 

### `POS`

 The place i in the sorted order. 

### `reportBody`

 report(w, perm, sv, out): OUT[PERM[i]] := VALS[i] for i < w, where VALS is the array at sv. 

 ## The report 

### `ReportInv`

 The first i values have been put in their places, and only the output has changed. 

### `ReportInv.write`

 One more value is put in its place; the places are different, so no earlier value is lost. 

### `report_entry`

 **report** does what `ReportSpec` says: OUT[π[i]] = SV[i] for i < w, and no cell outside the
output has changed, in at most 20 (w + 1) steps. 

---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Program.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Program.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Program.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The program of the reduction from 3SUM to Convolution-3SUM, assembled

The procedures of the reduction are appended to the program of an arbitrary solver of
Convolution-3SUM. Each of them meets its specification because the procedures that it calls meet
theirs; the last one, the host, solves 3SUM (`isHost_s3`).  That the answer is right comes from
`core_spec`, through `threeSum_iff_trees`.  With the arithmetic of `claim_CH20_Theorem_5_1_of_host`
this gives [CH20, Theorem 5.1] (Theorem 21(a)) for programs of the light language
(`claim_CH20_Theorem_5_1`).


### `emod`

 The places of the procedures in the list `chBodies`. 

### `chBodies`

 The procedures of the reduction, for a solver of Convolution-3SUM that is procedure number pC3
of a program with o procedures: the procedure at the place i of this list gets the number o + i.
The places have the names `Proc.emod`, …, `Proc.host`, in the order of the list. 

### `isHost_s3`

 **The host**: from every solver of Convolution-3SUM, the procedures of the reduction make a
solver of 3SUM. 

### `claim_CH20_Theorem_5_1`

 [CH20, Theorem 5.1] for programs of the light language: 3SUM from Convolution-3SUM. 

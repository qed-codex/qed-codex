---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/TimeBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/TimeBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/TimeBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The claim [VW13, Theorem 3.3] in the light language

The arithmetic that turns the time function of the host (`ntTime`, `isHost_nt`) into the bound
C · T(s, 6U) · log U of the claim. The host's own work, O(n² log U), is at most the time of the
solver, because a good time is at least n².


### `ntLevels_le`

 The number of levels is O(log U). 

### `claim_VW13_Theorem_3_3`

 [VW13, Theorem 3.3] for programs of the light language: Negative Triangle from Exact Triangle,
with c = 6. 

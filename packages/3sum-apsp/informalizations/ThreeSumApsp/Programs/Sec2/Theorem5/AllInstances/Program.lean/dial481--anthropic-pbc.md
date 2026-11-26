---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/Program.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/Program.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/Program.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The running-time claim "Theorem 5" for the light model, for the program of Theorem 5

programThin is program5 followed by regimeBody (the test whether an instance is in the regime of
Theorem 5), thinBruteBody (the brute force, for the instances outside it) and thinBody (the solver
for all instances). claim_theorem_5: it solves the thin matrix product on all instances, and for D ≥
4 a power of four, N ≥ D^18, w ≤ N²/√D and entries of at most N^c its time is at most a constant
times N² log² D / D^{1/18}. This is thin_claim for the program and the solver of Theorem 5.


### `programThin`

 The program of the thin matrix product on all instances. 

### `claim_theorem_5`

 **Theorem 5**, for programs of the light language. 

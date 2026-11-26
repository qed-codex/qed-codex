---
{
  "module": "ThreeSumApsp/RunningTimes/Sec2/Theorem5.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec2/Theorem5.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec2/Theorem5.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 on the word RAM

The route.  The solver of Section 2.4.4 is a procedure of the light language.  "Is solved in time T"
asks for a right answer on every input, so the procedure first tests whether the input is in the
regime of the theorem and falls back on brute force outside it; in the regime its running time obeys
the bound of the theorem (`Light.Sec2.claim_theorem_5`).  An outermost procedure reads the sizes
`N`, `D` and `|W|` from the input layout, forms the bound `N^κ` on the entries, computes the
addresses of the two matrices, of the wanted positions and of the output, and calls the solver; the
compiler turns the program into one for the word RAM (`Light.Sec3.realized_thinProduct`).


### `wordRam_theorem_5`

 **Theorem 5**, on the word RAM. 

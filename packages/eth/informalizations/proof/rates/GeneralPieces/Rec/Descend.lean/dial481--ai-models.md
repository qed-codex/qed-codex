---
{
  "module": "proof/rates/GeneralPieces/Rec/Descend.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Descend.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Descend.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # All levels, with every step in order in the sense of case (ii) of Lemma 8

This is the induction on ℓ in the proof of part (b) of the theorem on the general recursion
(Appendix A), for the value that the algorithm returns.
`descendG` starts from the state "sum 0, factor 1, work list [I]" and applies the steps of the
schedule; `solveG` evaluates the instances that are left by brute force, adds the sum and divides
by the factor. If every step of the schedule is in order (`ChainG2`) and the pad (an extra input
whose length bounds the length of every state that the program keeps, see `cap`) is long enough
(`FitsG`), the result is the value of the instance at the top. What one level does
(`StExpandG2`) is a hypothesis. Difference from the paper: the recursion is unrolled into a work
list that passes through the levels from the top down, and the divisions by d^|R| of all
levels are done at once at the end. 

 ### All levels 

### `descend_state2`

 The steps of the schedule, applied to any state that is in order: the factor is multiplied by
some q ≥ 1, and the sum plus the results of brute force on the work list at the end is q times
the sum plus the values Z of the work list at the start. 

### `stSolveG2`

 `StSolveG2`: all levels, brute force at the bottom and one division compute the sum Z of the
instance at the top. 

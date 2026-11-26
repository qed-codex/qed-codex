---
{
  "module": "Zeta23/PrimeSideB/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
  Part of the Zeta23 formalization of the paper
  "More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
-/
```


# [thm:traces], final form: `P.Valid → PaperInputs Z → ThmTracesHyp P Z`
Three lines combining `Traces.lean` (the instantiated assembly, taking the
taper facts as `LocalHypsEventually`) with `Bridge.lean` (which proves them).  Kept in its own file
so that `Traces.lean` does not depend on the Taper/Poisson tree.


### `thm_traces`

 **Theorem [thm:traces]** (the paper §5 "Summary") for the concrete prime-side matrix
([eq:Gdef] 2nd expression) — i.e. the hypothesis `ThmTracesHyp P Z` derived from `P.Valid`
and the published inputs `PaperInputs Z` alone. 

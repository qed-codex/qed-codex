---
{
  "module": "proof/consequences/GraphProblems/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From a machine cut into steps to a Turing machine, for any family of coded instances

`tm_of_stepped`: let M be a computation from bit strings to bit strings cut into polynomial-time
steps (`Stepped`, `IsPolyT`). Let a family of instances x be given with a size n = sz x, an input
word
`code x` of length at most a·(n+2)^d and an output word `out x`. If M, started on `code x`, returns
`out x` within c·2^{(δ/2)n} steps with states of size at most c·(n+2)^c, then one Turing machine of
Mathlib with finite alphabets, started on `code x`, halts with `out x` within ⌊C·2^{δn}⌋ steps. The
host is that of `proof/consequences/CountKSat/Host.lean` (`stHostW`). 

---
{
  "module": "proof/machines/StepMachines/Math/Formula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Formula.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Formula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Plain facts on the formulas and on the code `Sat3.enc` of the 3-SAT statement in
`ThreeSatStatement`: an instance of 3-SAT on n variables has at most (2n+1)³
clauses, a clause of at most 3 literals is known by its first 3 slots, and a header 1ⁿ 0 delimits
itself. 

### `eq_of_slots`

 A clause of at most 3 literals is known by its first 3 slots. 

### `Is3CNF.length_le`

 An instance on n variables has at most (2n+1)³ clauses, so its code is polynomially long. 

 ### The header of the code 

### `eq_of_header`

 The header 1ⁿ 0 delimits itself. 

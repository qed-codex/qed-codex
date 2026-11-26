---
{
  "module": "proof/threesat/Printed/HandOver.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/HandOver.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/HandOver.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A machine for networks on a network given by procedures: polynomial-time steps

Definition 2(iii): «an algorithm receives P, B and the numbers P_a, c_{a,b} as input». `networkOn`
and `networkOnSteps` (Programs.lean) write this input down from the numbers that the procedures give
(`inputOf`) and answer each query by running a procedure (`ProcsQ.answer`, `answerOf`).
This file shows that all of this is computed in polynomial time if the numbers are given in unary
and the procedures have polynomial-time steps. 

### `inputOf_polyT`

 The input of Definition 2(iii) is written down in polynomial time from numbers given in unary.
The number g of nodes is a constant. 

### `dist_polyT`

 (c, x or y) ↦ (c, x) or (c, y) is polynomial-time. 

### `bit_polyT`

 yes is 1 and no is 0. 

### `answerOf_poly`

 The four procedures as one step machine. 

### `answer_poly`

 The four procedures as one machine with query access. 

### `networkOnSteps_poly`

 A machine for networks with polynomial-time steps, on a network given by step machines with
polynomial-time steps and numbers in unary. 

### `networkOn_poly`

 The same on a network given by procedures that have query access of their own. 

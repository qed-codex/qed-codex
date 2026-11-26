---
{
  "module": "proof/rates/PiecesCounted/PadThen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/PadThen.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/PadThen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From a padding string to counted operations

In `AppRunningTimeStatement.lean`, «within T operations» is rendered by a padding string: a function
f of the input and a list of units that is polynomial-time in both and gives the right value once
the list has at least T units. `padThen N f` is the step machine that writes N a units, one in each
step, and then applies f in one step.
It halts within N a + 1 steps with the value of f at exactly N a units, its states hold the input,
the number N a and the units written so far, and its steps are polynomial-time if N and f are. This
is the extreme case (3) of the head of proof/machines/QueryMachines/Kernel.lean: the number of steps
means something only together with the bound on the states. 

### `padThen`

 Write N a units, one in each step; then f of the input and the units, in one step. A state is
(input, N a, units written so far), or the result. 

### `padThen_reaches`

 From the state with j units written, where j + k = N a, the machine halts after k + 1 more steps
with the value of f at N a units. 

### `padThen_runs`

 The machine halts within N a + 1 steps with the value of f at N a units; S bounds the input with
the number and the units, and the result. 

### `padThen_init`

 The hand-over of the input is polynomial-time. 

### `padThen_step`

 A step is polynomial-time. 

### `padThen_out`

 Reading the result is polynomial-time. 

### `padThenIsPolyT`

 The steps of the machine are polynomial-time if N and f are. 

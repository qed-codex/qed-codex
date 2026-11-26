---
{
  "module": "proof/consequences/CircuitLowerBound/Oracle/Runs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Oracle/Runs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Oracle/Runs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): from a machine that is started again after every answer to an oracle machine: the runs

The three kinds of loops (`run_mv`, `run_dr`, `run_cp`), each with its exact number of steps; the
part of a round before M runs (`run_build`); M's run and the step after it (`run_round`); the end
(`run_finish`); a query with its answer (`run_query`); and, by induction on the rounds, the whole
run (`run_protocol`). Between two rounds the machine is at the label `cpA`, all stacks of M and the
spare stack are empty,
`io` holds x and `ans` holds the answers so far, the last one on top. 

 ### The new stacks after a loop 

 ### The loops 

### `run_mv`

 The loop that moves the stack s to the stack d takes one step for each bit and one more. 

### `run_dr`

 The loop that empties the stack s. 

### `pushed`

 What the copying loop pushes on the input stack of M, above L, when it reads the bits l. 

### `run_cp`

 The copying loop. 

 ### A round 

### `run_build`

 Before M runs: the input of the round is written on the input stack of M; x and the answers are
kept. 

### `run_round`

 A whole round up to the step after M's run: the first bit c of the output of M is gone and has
decided where the machine goes on. 

### `run_finish`

 The end: x and the answers are dropped, the result goes to the output stack. 

### `run_query`

 A query and its answer: two steps. 

### `run_protocol`

 The whole run, from a point between two rounds. 

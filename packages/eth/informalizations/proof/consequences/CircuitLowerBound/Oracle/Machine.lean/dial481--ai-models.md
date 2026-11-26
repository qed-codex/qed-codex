---
{
  "module": "proof/consequences/CircuitLowerBound/Oracle/Machine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Oracle/Machine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Oracle/Machine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): from a machine that is started again after every answer to an oracle machine: the machine

Given a machine M that is started on (x, answers so far) and returns the result or the next query,
the oracle machine `otm M` has the stacks of M and three stacks of bits: `io` (its input and output;
it keeps x, first bit on
top, until the end), `ans` (the answers, the last one on top) and `sp` (a spare stack, empty between
the loops). Its query stack is the output stack of M. Its state is the state of M and a register for
one popped bit, empty
between the steps. A round:

* `cpA`: the answers go from `ans` to `sp`, and a copy of each on the input stack of M; `mvA`: they
  go back from `sp` to `ans`; `sep`: a 0 on the input stack of M;
* `mvX`: x goes from `io` to `sp`; `cpX`: it goes back, and for each bit b the bits b and 1 are
  pushed on the input stack of M, which now holds the input of the round;
* the program of M, in which «halt» is a jump to `after`;
* `after`: the first bit of the output of M is popped. If it is 1, what is left on the output stack
  of M is the query: `ask`; at `yes` and `no` the answer is pushed on `ans` and the next round
  begins.
  If it is 0: `drX` and `drA` empty `io` and `ans`, and `fin` moves the result from the output stack
  of M to `io` and halts.

This file has the definitions, one step of the machine at a label other than `ask` and at `ask`, and
the runs of M inside the machine. 

### `NS`

 The three new stacks. 

### `Ctl`

 The new labels. 

### `Γ'`

 The alphabets. 

### `Λ'`

 The labels. 

### `σ'`

 The states: the state of M and the register. 

### `St`

 The statements. 

### `Cf`

 The configurations. 

### `lift`

 A statement of M in the new machine; «halt» is a jump to `after`. 

### `mvS`

 A loop that moves the stack s to the stack d; it stands at the label me and leaves to nx. 

### `drS`

 A loop that empties the stack s. 

### `cpS`

 A loop that moves the stack s to the stack d and pushes every bit on the input stack of M,
followed by a 1 if `mark`. 

### `prog`

 The program. 

### `tm'`

 The machine. 

### `otm`

 The oracle machine: the query stack is the output stack of M. 

### `stp`

 One step of the oracle machine with the oracle O. 

 ### The stacks 

### `stk`

 The stacks of M and the new stacks. 

### `ns`

 The contents of the three new stacks. 

### `one`

 All stacks of M are empty but one. 

 ### Single steps 

### `stp_of_ne`

 A step at a label other than `ask` runs the statement at that label. 

### `stp_ask`

 A step at `ask`. 

 ### The runs of M 

### `liftCfg`

 A configuration of M in the new machine, with the register empty and the new stacks n. 

### `run_lift`

 A run of M is a run of the new machine of the same length; where M halts, the new machine is at
`after`. 

### `run_of_iterate`

 Mathlib's form of a run, read back. 

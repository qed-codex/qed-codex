---
{
  "module": "proof/machines/Wrap/Coding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Coding.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Coding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A coding of the configurations of a machine as data of the framework for polynomial time

`Coding M` bundles what the simulation uses: configurations of M written as values of the plain type
`Rep`; polynomial-time functions for the start (from bit strings to `Rep`), for one step (on `Rep`;
`CircuitLowerBound.Tab.stay M` is Mathlib's step, where a halted machine stays as it is) and for
reading the output (on `Rep`); and
bounds on the sizes. CodingExists.lean proves that every machine with finite alphabets has a coding;
Sim.lean derives the machine around M from a coding. 

### `Rep`

 The type in which configurations are written: (number of the label or «halted», number of the
state), and the stacks, in a fixed order, as lists of numbers of symbols. 

### `Coding`

 A coding of the configurations of M. 

### `Coding.rep`

 the value that stands for a configuration 

### `Coding.step`

 one step, on values 

### `Coding.init`

 the start configuration on the bit string x, as a value 

### `Coding.out`

 the output, if the value stands for a halted configuration 

### `Coding.a`

 a constant for the two bounds on sizes 

### `Coding.step_poly`

 the step is polynomial-time 

### `Coding.init_poly`

 the start is polynomial-time 

### `Coding.out_poly`

 reading the output is polynomial-time 

### `Coding.step_rep`

 the step on values is the step of M 

### `Coding.init_rep`

 the start on values is the start configuration of M 

### `Coding.out_halted`

 on a halted configuration the output is the content of the output stack 

### `Coding.out_running`

 on a configuration that is not halted there is no output 

### `Coding.size_init`

 the start configuration is at most linear in the input 

### `Coding.size_step`

 a step adds at most a constant to the size 

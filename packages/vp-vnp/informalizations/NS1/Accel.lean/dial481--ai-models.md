---
{
  "module": "NS1/Accel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Accel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Accel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Accelerators, the cut

Scales are `v ^ H` (`H = 16 / η`). `pv θ z` is the universal plain sum at `z = (program, argument)`.


### `lg`

 The number of binary digits. 

### `Plain`

 The program `z.hd` at the argument `z.tl`: all runs stop, the accepting ones within `T` steps and without named
constants. 

### `pv`

 The universal plain sum: the sum of the weights of all accepting runs of the program `z.hd` at `z.tl`. 

### `CutProg`

 A program `G` that cuts plain sums of `τ` steps on instances of size `s` into pieces of `v ^ H` steps. Its values
are lists of instances. 

### `CutHyp`

 **Theorem C (the cut, at all scales)**, as a property of the ring and its constants. 

### `IsAccT`

 The program `D`, with the constants `K` and their powers `2 ^ b`, `b < B`, has the values of all universal plain
sums of `v ^ H` steps on instances of size `v ^ (H - 32)`, in `t` steps. 

### `IsPre`

 The same, where runs have to stop only if the sum is plain. 

### `bill_le`

 A run wants at most one constant a step. 

### `UF`

 The universal program. 

### `UF_pre`

 The universal program is a program for the universal plain sums. 

### `zq_plain`

 The instances that arise from budgets are plain, and their sums are those of the runs that use up the budgets. 

---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Preprocessing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Preprocessing.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Preprocessing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 26 and 31 in the light language: the preprocessing, with rational parameters

Proof of Corollary 26: "Setting up. Let m := ⌈log₄ D⌉, and pad the inner dimension to 4^m < 4D with
zero columns of X and zero rows of Y." Proof of Corollary 31: "We repeat the proof of Corollary 26
with L := ⌈cm⌉ and t := ⌈θm⌉". Then the preprocessing of Theorem 30 on the padded matrices; "for
smaller m the corollary again holds trivially".

The routine meets its specification (`pre31_meets`). It computes m and branches. Below the threshold
it writes the flag 0 (`PreInput31.ready_small`). From the threshold on it computes L, t and the
addresses, pads X, and pads Y by a copy and a fill with zeros (`prePad31_ends`,
`matAt_padInnerRows`); then it calls the preprocessing of Theorem 30 and writes the base address and
the flag 1 (`preBuild31_ends`, `PreInput31.ready_large`).


 ## What the routine is given, and what it leaves 

### `PreCalls31`

 The routines that the preprocessing calls meet their specifications. 

### `PreInput31`

 What the preprocessing is given: besides what both routines are given, the matrices X and Y
stand at aX and aY. 

### `PreInput31.ready_small`

 Below the threshold the flag 0 is all that a query needs. 

### `PreInput31.ready_large`

 From the threshold on a query needs the flag 1, the base address, and the data structure of
Theorem 30 for the padded matrices. 

### `matAt_padInnerRows`

 **Y with zero rows**: a copy of Y followed by zeros is the padded matrix. 

 ## From the threshold on 

### `Areas31`

 The areas from the free pointer on: fr, fr + 1, fr + 2 | X' | Y' | the block of Theorem 30 from
b0 on. F = 4^m is the padded inner dimension, and R the number of cells in the zero rows of Y'. 

### `tPrePad31`

 The time of prePad31. 

### `Padded31`

 The state after prePad31: the locals hold the parameters and the addresses, the padded matrices
stand at their places, and only cells between fr and b0 have changed. 

### `prePad31_ends`

 **Setting up**: L, t, the addresses, and the padded matrices. The cell fr + 2 holds 4^m. 

### `preBuild31_ends`

 **The preprocessing of Theorem 30** on the padded matrices, the base address and the flag 1. 

 ## The routine 

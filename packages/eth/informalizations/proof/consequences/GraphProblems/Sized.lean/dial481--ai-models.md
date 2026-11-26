---
{
  "module": "proof/consequences/GraphProblems/Sized.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Sized.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Sized.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A machine for counting the satisfying assignments with exactly s true variables

`sized b E`: on (n in unary, s, ψ), for every y < (b+1)^(n/b+1) run the counting engine E on the
formula `blockF b n s y ψ` (ψ, and digit i of y true variables in block i), and add the counts up.
This file defines this machine and its parts, proves `isPolyT_sized` for it, and proves small facts
on `cntN` and `ofWord`.
The paper's proof of Corollary 7 fixes the size with a circuit of O(n) gates instead. 

### `SIn`

 The input of the machine: (n in unary, s, ψ). 

### `nY`

 The number of vectors of block sizes. 

### `buildB`

 The input of the engine for the vector y. 

### `wordZ`

 A word as an integer. 

### `sized`

 The machine. 

 ### Small facts 

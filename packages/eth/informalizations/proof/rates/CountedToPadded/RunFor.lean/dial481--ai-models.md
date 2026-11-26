---
{
  "module": "proof/rates/CountedToPadded/RunFor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/RunFor.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/RunFor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A step machine run on a padding string

Proofs of `EveryWordIsCompared`, `RunForIsRight`, `RunForPolyFrom` and `RunForPoly` (Defs.lean). 

### `reaches_size`

 The first state of a run is within the bound on the sizes. 

### `cutAt_some`

 A state of size at most S is not cut. 

### `fold_halted`

 A halted state stays to the end. 

### `fold_reaches`

 From a state from which N halts with b within T steps, the fold ends in a state with the result
b once the fuel has at least T units. 

### `len_cutAt_le`

 The output of the cut has length at most `room + 2`: a value that is kept has length at most
`room`, and `none` has length at most 2. 

### `everyWordIsCompared`

 Whether the word of a value is at most as long as a padding string is decided in polynomial
time, for every coding. 

### `runForIsRight`

 `runFor` returns the result of the machine once fuel and room suffice. 

### `runForPolyFrom`

 `RunForPoly` follows from `EveryWordIsCompared`. 

### `runForPoly`

 `runFor N` is polynomial-time for every step machine N with polynomial-time steps. 

---
{
  "module": "proof/rates/PaddedDescent/F/Fuel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Fuel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Fuel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Loops cut off by a pad

`U` is a number in unary; the pad is a `U`. Every enumeration of exponentially many things runs over
`rng pad q` (or `sumF q pad`), that is over 0, …, min q (length of the pad) − 1; every loop whose
state could grow puts `cap pad d` around
the state after each round. So all functions built this way are polynomial-time in (pad, arguments)
without any side condition, and the
mathematics is only needed to show that, for a long enough pad, no cut-off is active (`rng_eq`,
`sumF_eq`, `cap_eq`). 

### `U`

 A number in unary. 

### `rng`

 0, …, q − 1, cut off at the length of the pad. 

### `sumF`

 Σ_{y < N} f y, cut off at the length of the pad. 

### `prodL`

 ∏_{y < n} f y (n is small: no cut-off). 

### `cap`

 x if its word is no longer than the pad, else d. 

### `Meas`

 The length of the word of a value can be computed in polynomial time. 

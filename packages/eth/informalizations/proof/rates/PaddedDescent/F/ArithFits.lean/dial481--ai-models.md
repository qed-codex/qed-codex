---
{
  "module": "proof/rates/PaddedDescent/F/ArithFits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithFits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithFits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The invariant implies that the pad suffices for the whole descent

`fits_of_inv`: if the invariant `Inv` holds at level j and the
exponent e of the length of the pad dominates four explicit numbers, then `PaddedDescent.F.Fits`
holds for the schedule below level j. No programs occur
here. 

### `fits_of_inv`

 If the invariant holds at level j ≤ t, then a pad of length F ≥ 2^e suffices for the work list
at level j and for all the steps below it. 

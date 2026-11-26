---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/TimeBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/TimeBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/TimeBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# APSP from the (min,+)-product: the claim

The running time of the host (`apTime`, `isHost_ap`) in the form of the claim
`ApspFromMinPlus`: `⌈log₂ n⌉ + 1` times the sum of the time of a (min,+)-product of
matrices whose entries are bounded by `3nu` and of `O(n² (1 + log(nu)))` (for Theorem 21(b)).


### `claim_apspFromMinPlus`

 APSP from the (min,+)-product, for programs of the light language. 

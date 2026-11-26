---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem19/BruteForceClaim.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem19/BruteForceClaim.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem19/BruteForceClaim.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The running time of brute force (the proof of Theorem 19)

The `100 n³ + 100` steps of brute are within the form `C n³ (1 + log u)` in which the running times
for Exact Triangle with weights of absolute value at most `u` are stated (`claim_bruteForce`).


### `claim_bruteForce`

 "Smaller instances are solved by brute force" (proof of Theorem 19): Exact Triangle is
solved in time `C n³ (1 + log u)`, where `u` bounds the absolute values of the weights.  The factor
`1 + log u` is not needed here; it belongs to the form of the running times for this problem. 

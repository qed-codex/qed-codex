---
{
  "module": "proof/rates/OccurM/Wrapper.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Wrapper.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Wrapper.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Every wrapper counts

Let M count within the bound C·2^{C·km/(log₂(m+2))^α} (`SatM.bound`) on formulas in which every
variable occurs, let `pre` number the variables that occur, and let N wrap M with `pre` before it
and nothing after it
(`Wrap.Wraps M pre id N q`). On the code x of (k, φ), `pre x` is the code of (k, ψ) with ψ as in
`Prepares`; M puts out the number wanted within t steps, t that bound at m; so N puts it out within
q·(t + |x| + 1)^q steps.
`bound_le_pow` gives t ≤ 2^E with E ≤ (2C+1)·km/(log m)^α, and `steps_le` the printed bound.
`wrapper_counts` is this for any coding; the two end theorems are its cases for the compact code and
for the code that writes the number of variables in unary. 

### `wrapper_counts`

 For any coding `code` by nonempty words and any `pre` that numbers the variables that occur:
every wrapper counts within the printed bound, with the constant `stepsC q (2·C + 1)`. 

### `everyWrapperCounts`

 Every machine that runs a preparation and then a machine that counts within the bound
`SatM.bound` on formulas in which every variable occurs counts within the printed bound on every
k-CNF with k ≥ 1 and m ≥ 2; compact code. 

### `everyWrapperCountsUnary`

 The same for the code that writes the number of variables in unary (`SatM.enc`). 

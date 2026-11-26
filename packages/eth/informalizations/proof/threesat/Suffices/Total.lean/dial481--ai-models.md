---
{
  "module": "proof/threesat/Suffices/Total.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Total.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Total.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «so the total time is O(2^{δn})»

The last sentence of the proof of Theorem 2: «Lemma 4 yields at most 2^{δn/3} such formulas, in time
2^{δn/3} times a polynomial in n, … so the total time is O(2^{δn}).»
With E = 2^{δn/3}: there are at most E formulas; each costs at most A·E plus A(n+1)^A plus 3 steps,
and (n+1)^A is at most a constant times E, so one formula costs at most a constant times E; the
remaining term D·n + 2 of the count is again at most a constant times E. The sum is at most a
constant times E³ = 2^{δn}. That a polynomial is O(2^{δn/3}) is `Groundwork.SatNet.pow_le_two_rpow`. 

### `stTotal`

 **«Lemma 4 yields at most 2^{δn/3} such formulas, in time 2^{δn/3} times a polynomial in n, … so
the total time is O(2^{δn})»** (proof of Theorem 2). 

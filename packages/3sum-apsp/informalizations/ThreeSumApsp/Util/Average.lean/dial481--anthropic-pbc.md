---
{
  "module": "ThreeSumApsp/Util/Average.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Average.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Average.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Few indices are far above the average

Let `f` be a function with natural numbers as values on a nonempty finite set `Q`.  Division is
avoided: "`f p` is at most `k` times the average of `f`" is written
`f p * |Q| ≤ k * ∑ p' ∈ Q, f p'`.

* Fewer than `|Q|/k` indices are more than `k` times as bad as the average
  (`Finset.mul_card_above_average_lt`, Markov's inequality).
* So for `k` functions there is one index at which each of them is at most `k` times its average
  (`Finset.exists_forall_mul_card_le_mul_sum`, the union bound).


### `mul_card_above_average_lt`

 Markov's inequality: fewer than `|Q|/k` indices are more than `k` times as bad as the
average. 

### `exists_forall_mul_card_le_mul_sum`

 The union bound: one index is good for `k` functions at once, in that each function is at most
`k` times its average there. 

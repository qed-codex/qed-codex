---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary40/VHintedTimes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/VHintedTimes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/VHintedTimes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40, Conjecture 5.2: the running times of v-hinted Mv

Proof of Corollary 40: "In Phase 2, we preprocess X := M and Y := V by Corollary 26, in
O(n²/D^0.063) = O(n^{2−0.063τ}) time.  In Phase 3, the n entries of column i of MV are n queries,
which take O(n D^0.437) = O(n^{1+0.437τ}) time."  Proof of Corollary 40, "General τ": "the arguments
above go through with Phase 2 in O(n²/D^γ) = O(n^{2−γτ}) time and Phase 3 in O(n D^{1/2}) =
O(n^{1+τ/2}) time".

The argument is made once, for a data structure with given rates (`achievesVHinted_of_rates`): the
phase procedures are appended to the program of the data structure, Phase 2 takes the time of the
preprocessing and Phase 3 the time of n queries, each up to O(n) more steps
(`KitRates.phaseRun_column`).  With the rates of Corollary 26 it gives the statement for τ < 1/18
(`achievesVHinted_of_lt_eighteenth`), with the rates of Corollary 31 the statement for general τ
(`achievesVHinted_of_genParams`).


### `vProcsAt`

 The three phases, and the routine `col` that Phase 3 calls for a column of the product, as
procedures o to o + 3. 

### `achievesVHinted_of_rates`

 **v-hinted Mv over a data structure with given rates.**  Let 0 ≤ τ ≤ 1 and 1 ≤ a₃.  If at the
sizes N = n and D = t = ⌊n^τ⌋ the preprocessing takes O(n^a₂) steps and n queries take O(n^a₃), then
Phase 2 takes O(n^a₂) and Phase 3 takes O(n^a₃) time on the word RAM. 

### `achievesVHinted_of_lt_eighteenth`

 **Corollary 40, Conjecture 5.2, 0 < τ < 1/18**: v-hinted Mv is solved on the word RAM with
Phase 2 in O(n^{2−0.063τ}) and Phase 3 in O(n^{1+0.437τ}) time. 

### `achievesVHinted_of_genParams`

 **Corollary 40, Conjecture 5.2, general τ**: for parameters c, θ, ε, γ as in `GenParams` and
every 0 < τ < ε, v-hinted Mv is solved on the word RAM with Phase 2 in O(n^{2−γτ}) and Phase 3 in
O(n^{1+τ/2}) time. 

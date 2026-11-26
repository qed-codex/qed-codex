---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary40/MvHintedTimes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/MvHintedTimes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/MvHintedTimes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40, Conjecture 5.7: the running times of Mv-hinted Mv

Proof of Corollary 40: "The proof is the same, with X := N_{[n],I} and Y := V, which are both known
in Phase 2".

The argument is that of v-hinted Mv, for a data structure with given rates
(`achievesMvHinted_of_rates`, from `KitRates.phaseRun_column`).  The one difference is that Phase 2
first writes the matrix N_{[n],I}, which takes O(n t) steps; so the exponent of Phase 2 has to allow
for n t as well.  With the rates of Corollary 26 this gives the statement for τ < 1/18
(`achievesMvHinted_of_lt_eighteenth`), because n t ≤ n^{2−0.063τ}.  With the rates of Corollary 31
it gives the statement for general τ (`achievesMvHinted_of_genParams`), where n t is within the
bound for γ ≤ 1 and τ ≤ 1/2.


### `mvProcsAt`

 The three phases, and the routine `col` that Phase 3 calls for a column of the product, as
procedures o to o + 3. 

### `achievesMvHinted_of_rates`

 **Mv-hinted Mv over a data structure with given rates.**  Let 0 ≤ τ ≤ 1 and 1 ≤ a₂, a₃.  If at
the sizes N = n and D = t = ⌊n^τ⌋ the preprocessing takes O(n^a₂) steps and n queries take O(n^a₃),
and n t ≤ n^a₂, then Phase 2 takes O(n^a₂) and Phase 3 takes O(n^a₃) time on the word RAM. 

### `achievesMvHinted_of_lt_eighteenth`

 **Corollary 40, Conjecture 5.7, 0 < τ < 1/18**: Mv-hinted Mv is solved on the word RAM with
Phase 2 in O(n^{2−0.063τ}) and Phase 3 in O(n^{1+0.437τ}) time. 

### `achievesMvHinted_of_genParams`

 **Corollary 40, Conjecture 5.7, general τ**: for parameters c, θ, ε, γ as in `GenParams` and
every 0 < τ < ε with τ ≤ 1/2, Mv-hinted Mv is solved on the word RAM with Phase 2 in O(n^{2−γτ}) and
Phase 3 in O(n^{1+τ/2}) time. 

---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Costs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Costs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Costs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 4.4: the costs of the programs with rational parameters

Bounds for the time and the space of the preprocessing and for the time of a query. `CostsWithin`
says of two bounds tp and tq that they dominate the two costs of Theorem 30. A quantity that is
bounded for m < m₀ and within a constant times a cost for m ≥ m₀ is then within a constant times the
bound (`exists_le_of_small_of_large`). The overheads are absorbed by the cost expression (8) of
Theorem 30: padding, copying and filling cost O(N 4^m), and N 4^m ≤ N 10^L/(√K N₀), because K N₀ 4^m
≤ 7^L (`N_mul_pow_le_cost8`); computing L and t costs O(L). For m < m₀ everything is bounded by a
constant. This gives the results that the end theorems use: `exists_tPre31_le`,
`exists_tQuery31_le`, `exists_tOffline32_le`, `exists_structEnd_sub_le`, `exists_lim31_depth_le`.


### `CostsWithin`

 **The two bounds dominate the two costs**, at the sizes N and D: sizes and bounds are at least
1, D ≤ N, and from the threshold on the hypotheses of Theorem 30 hold and its two cost expressions,
(8) and L ∑ α_d, are at most C tp and C tq. 

### `CostsWithin.hyp`

 For m ≥ m₀ the hypotheses of Theorem 30 hold. 

### `CostsWithin.pre_le`

 For m ≥ m₀ the cost (8) is at most C tp. 

### `CostsWithin.query_le`

 For m ≥ m₀ the cost of a query is at most C tq. 

### `exists_le_of_small_of_large`

 A quantity that is bounded below the threshold, and at most a constant times a cost from the
threshold on, is at most a constant times every bound t ≥ 1 that dominates the cost. 

 ### The preprocessing 

### `exists_tPre31_le_setup`

 Setting up takes O(L + N 4^m) steps. 

### `exists_tPre31_le_cost8`

 From the threshold on the preprocessing takes O((8)) steps. 

### `exists_tPre31_le`

 **The time of the preprocessing** is at most a constant times every bound tp ≥ 1 that, from the
threshold on, dominates the cost (8) of Theorem 30. 

 ### A query 

### `exists_tQuery31_le`

 **The time of a query** is at most a constant times every bound tq ≥ 1 that, from the threshold
on, dominates the cost L ∑ α_d of Theorem 30. 

### `exists_tOffline32_le`

 **The time of the offline routine**, with k further steps, is at most a constant times tp + w
tq, for all bounds tp, tq ≥ 1 that dominate the two costs of Theorem 30. 

 ### Space and the nesting of calls 

### `exists_structEnd_sub_le`

 **The number of cells** of a structure at fr is at most a constant times every bound tp ≥ 1
that, from the threshold on, dominates the cost (8) of Theorem 30. 

### `exists_structEnd_le`

 The same for a structure at the address 0. 

### `exists_lim31_depth_le`

 **The nesting of calls** that the limits allow is at most a constant times every bound tp ≥ 1
that, from the threshold on, dominates the cost (8) of Theorem 30. 

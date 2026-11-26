---
{
  "module": "proof/rates/CountedRecursion/TotalCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/TotalCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/TotalCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The count, by induction on the depth

The cost of the tower at the depth j, if a query to the tables of the instance costs t ≥ 1, is at
most t times the bound of the theorem for the depth j (at the bounds for λ and B). The base is
`CountBase`. For the step, the recursion for the cost of the tower is written out
(`Tower.CostShape`);
a call costs at most (cost of an entry + 2) times the bound of the depth below, by the induction
hypothesis, and 2 more; `CountStep` bounds the sum, and `ExponentFits` the exponent of Ξ, with C₀ =
2(c + C₄ + 1). The paper has C₀ = 2(c + C₄ + 1) + C₅. Here C₅ is not needed for the count: a term of
brute force costs K₀ + 1 steps and K₀ queries, so `CountBase` holds for every C₀ ≥ 1; the C₅ of
`SolverBase` bounds the sizes of the states, and goes into the constant of `RecursionMeets`. 

### `totalCountFrom`

 `TotalCountFrom`: the cost bound of Theorem A(b) for the tower, by induction on the depth, from
the base (`CountBase`), the step (`CountStep`), the bound on the exponent of Ξ (`ExponentFits`) and
the shape of the cost recursion (`Tower.CostShape`), with C₀ = 2(c + C₄ + 1). 

### `totalCount`

 `TotalCount`: `totalCountFrom` applied to `countBase`, `countStep`, `exponentFits` and
`Tower.costShape`. 

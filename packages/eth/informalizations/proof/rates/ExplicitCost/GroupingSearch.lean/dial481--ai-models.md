---
{
  "module": "proof/rates/ExplicitCost/GroupingSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingSearch.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «find the first such grouping among all K^g»

* `goodData_iff`: on the input that belongs to ζ = a/b, K and a network N, the test of the procedure
  says yes to the number y exactly if the grouping number y has at most 2g/K nodes in every group
  and Y_{γ,γ'} ≤ L for all γ ≠ γ'.
* `searchFinds`: in case (i) or (ii) some grouping is such (`AppRunningTime.someGrouping`), every
  grouping has a number below K^g, so there is a first number that the test accepts.
* `Sizes.search_sizes`: the arithmetic of the sizes of the states.
* `searchCost`: the loop halts at the first number x that the test accepts, after 2·(x + 1) ≤ 2·K^g
  steps (`Exits.stFirstUntil`; a test is one step). The constant is 10. 

### `goodData_iff`

 The test of the procedure says yes to y exactly if the grouping number y has the two properties. 

### `searchFinds`

 In case (i) or (ii) the search finds a grouping: there is a first x < K^g that the test accepts,
and its grouping has the two properties. 

### `size_pow_le`

 K^g has at most g² + 1 binary digits, for K ≤ g. 

### `size_groupingInput`

 The size of the input of the procedure. 

### `search_sizes`

 With X = g(P+B), s the length of ζ and 1 ≤ K ≤ g: four copies of the input, four of K^g and 40
more units are at most (X + s)², hence at most (X + s)^10. 

### `searchCost`

 The search takes at most 10·K^g steps, on states of size at most (g(P+B) + the length of
ζ)^{10}. 

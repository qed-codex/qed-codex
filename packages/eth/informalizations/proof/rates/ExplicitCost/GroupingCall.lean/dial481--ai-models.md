---
{
  "module": "proof/rates/ExplicitCost/GroupingCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingCall.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 8 (the grouping lemma of Appendix A) up to the call

The procedure `groupingCall` of Lemma 8 runs the search and then asks one query, the call, whose
answer is its result. With the call answered by the value of the clique of the groups, that result
is the value of the network (in the proof of Lemma 8: «whose value is that of the network»,
`Value.StValueEqualsZ`).

* `abs_value_le`, `size_value_le`: the value of a network on [g] with parameters P, B is at most
  2^{gP + gB + g²B} in absolute value. The last state of the procedure holds the value, so its size
  has to be bounded.
* `Sizes.add_three_le`, `value_sizes`: arithmetic of the sizes.
* `groupingWithCallFrom`: how the steps give the lemma up to the call; with the constant C of the
  search the constant is C + 12.
* `groupingWithCall`: the lemma up to the call. 

### `abs_value_le`

 The value of a network: at most (2^P)^g terms, each a product of g values of the W_a and at most
g² values of the Ψ_{a,b}. 

### `size_value_le`

 The value of a network has at most gP + gB + g²B + 1 binary digits. 

### `add_three_le`

 u + v + w ≤ Z^{n+2} if u, v, w ≤ Z^n and Z ≥ 2. 

### `value_sizes`

 gP + gB + g²B + 2 ≤ (g(P+B) + s)^{10}. 

### `groupingWithCallFrom`

 How the search, its cost, the size bounds and the equality of the values (the clique of the
groups has the value of the network) give Lemma 8 up to the call. 

### `groupingWithCall`

 **Lemma 8 up to the call.** 

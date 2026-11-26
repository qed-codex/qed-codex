---
{
  "module": "proof/sparsification/SparsificationLemma/Cal/Facts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Facts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Facts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Facts (i) and (iii) on the tree for Calabro's thresholds

This file proves `FactI` and `FactIIIy` of proof/sparsification/SparsificationLemma/Cal/Defs.lean.
Calabro's thresholds satisfy the conditions `ThrC` with τ = α (`stThrCal`), so the general theorem
`stGen` applies with
D = (β₁ + … + β_{k−1})·n. Its first clause is fact (i).
For fact (iii), `stGen` bounds the number of leaves by Σ_{j ≤ (k−1)n/α} C(D, j). By fact (iv), D ≤
L·n with L = 4·(32α)^(k−2). The estimate `sum_choose_le_two_rpow` of
proof/sparsification/SparsifyWidthK/Thresholds.lean bounds the sum by
2^(yn) as soon as ((k−1)/α)·log₂(e·α·L) ≤ y, and e·α·L ≤ (32α)^(k−1) because 4e ≤ 32; so y =
(k−1)²·log₂(32α)/α will do. 

### `gen`

 The general theorem for Calabro's thresholds, with τ = α and D = (β₁ + … + β_{k−1})·n. 

### `factI`

 Fact (i), with β₁ + … + β_{k−1}: no path of the tree has more than (β₁ + … + β_{k−1})·n steps. 

### `log_le_yC`

 ((k−1)/α)·log₂(e·α·L) ≤ y for L = 4·(32α)^(k−2), α ≥ 1 and k ≥ 2. 

### `factIIIy`

 Fact (iii), first part: the tree has at most 2^(yn) leaves. 

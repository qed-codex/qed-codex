---
{
  "module": "Ov/Core/Spec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Spec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Spec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Spectral points: the basic calculus

Paper: the subsection "Tensors". A spectral point F is multiplicative and
monotone for restriction, F(s) ≤ F(t_1) + … + F(t_m) if s = t_1 + … + t_m, and 1 ≤ F(t) ≤ rank of t for
a tensor t that is not 0. A spectral point can be pulled back along a map g of sets of parties (the
paper's t ↦ φ(gt)).


### `rankLE_iff`

 Rank, in coordinates: a tensor has rank at most r if and only if it is a sum of r products of
vectors. 

### `RankLE.sumRestr`

 A tensor of rank at most r is a sum of r restrictions of 1. 

### `rankLE_card`

 Every tensor has a rank bound: the number of its entries. 

### `mono`

 F is monotone for restriction. 

### `congr`

 Equivalent tensors have the same price. 

### `prod_fin`

 F of the product of a family indexed by 0, …, n-1. 

### `prod`

 F of the product of a family. 

### `kpow`

 F of a power. 

### `zero`

 F is 0 at a tensor whose array is 0. 

### `one_le`

 F is at least 1 at a tensor with an entry that is not 0. 

### `le_rank`

 F is at most the rank. 

### `le_card`

 F is at most the number of entries. 

### `le_sum_val`

 F is subadditive for sums of arrays. 

### `le_mul`

 A restriction of a product costs at most the product of the prices. 

### `le_prod`

 A restriction of the product of a family costs at most the product of the prices. 

### `pull`

 The pull-back of a spectral point along a map π of parties: a tensor over J costs what it costs
if the leg j is held by π j. 

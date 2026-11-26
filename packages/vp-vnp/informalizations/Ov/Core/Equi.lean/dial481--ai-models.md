---
{
  "module": "Ov/Core/Equi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Equi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Equi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Equivalence of tensors

The paper identifies tensors that are restrictions of one another (in the subsection "Tensors"). Here they are called equivalent, `Equi`, and this file has the laws of products,
powers, products of families and `push` (giving legs to parties) up to equivalence.


### `Equi.refl`

 Every tensor is equivalent to itself. 

### `Equi.symm`

 Equivalence is symmetric. 

### `Equi.trans`

 Equivalence is transitive. 

### `Equi.mul`

 Products of equivalent tensors are equivalent. 

### `Equi.push`

 Giving the legs of equivalent tensors to parties. 

### `Equi.of_equiv`

 Tensors whose index sets correspond to one another, leg by leg, with equal entries are
equivalent. 

 ### Products 

### `Equi.mul_comm`

 The product is commutative. 

### `Equi.mul_assoc`

 The product is associative. 

### `Equi.one_mul`

 1 is neutral. 

### `Equi.mul_one`

 1 is neutral. 

### `Equi.prod_reindex`

 Renaming the factors of a product. 

### `Equi.prod_empty`

 The product of the empty family. 

### `Equi.prod_unique`

 The product of a family with one member. 

### `Equi.prod_sum`

 The product over a disjoint union. 

### `Equi.prod_fin_succ`

 The product of a family indexed by 0, …, n is its first member times the product of the others. 

### `Equi.prod_fin_two`

 The product of a family of two tensors. 

 ### Powers 

### `Equi.kpow_zero`

 The power with exponent 0. 

### `Equi.kpow_succ`

 The power with exponent k + 1. 

 ### Giving legs to parties 

### `Equi.push_id`

 Giving each leg to the party of its own name changes nothing, up to equivalence. 

### `Equi.push_push`

 Giving legs away twice. 

### `Equi.push_mul`

 Giving legs away, for a product. 

### `Equi.push_one`

 Giving legs away, for 1. 

### `Equi.push_prod`

 Giving legs away, for the product of a family. 

### `Equi.push_kpow`

 Giving legs away, for a power. 

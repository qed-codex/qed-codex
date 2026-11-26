---
{
  "module": "Ov/Core/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Restrictions and sums of restrictions: the basic calculus

Paper: the subsection "Tensors". `Restr s t` says that s is a restriction of t, and `SumRestr s b` that s
is covered by the b k. Restriction is reflexive and
transitive and compatible with products, powers, products of families and `push` (giving legs to
parties); sums of restrictions can be substituted in one another and multiplied, and are compatible
with the same operations.


 ### Values of the constructions 

### `kpow_eq_prod`

 The k-th power is the product of k equal tensors. 

### `withVal`

 The same legs with another array. 

 ### Local maps applied to arrays 

### `appG`

 Local maps L applied to an array f; this is `app` for plain index sets in the place of the legs of
tensors. 

### `appG_comp`

 Local maps compose. 

### `appG_sum`

 Local maps applied to a sum. 

### `appG_mul`

 Local maps applied to a product of two arrays. 

### `appG_prod`

 Local maps applied to a product of a family of arrays. 

### `pushEquiv`

 The index tuples of the legs sorted by their parties correspond to the index tuples of all
legs. 

### `appG_push`

 Local maps applied to an array whose legs are sorted by parties. 

### `appG_map`

 Local maps whose matrices have at most one entry that is not 0 in each row: the row a of the
matrix of p has the entry w p a in the column g p a. 

 ### Restrictions 

### `Restr.refl`

 A tensor is a restriction of itself. 

### `Restr.trans`

 A restriction of a restriction is a restriction. 

### `Restr.mul`

 Products of restrictions. 

### `Restr.prod`

 Products of a family of restrictions. 

### `Restr.push`

 Restrictions stay restrictions if the legs are given to other parties. 

### `Restr.of_map`

 If the entry of s at x is a product of local factors times the entry of t at g(x), where g acts
leg by leg, then s is a restriction of t. 

### `Restr.of_map'`

 If the entry of s at x is the entry of t at g(x), where g acts leg by leg, then s is a
restriction of t. 

### `Restr.one_le`

 1 is a restriction of every tensor with an entry that is not 0, if there is a party. 

 ### Sums of restrictions 

### `sumRestr_iff`

 s is a sum of restrictions of the b k if and only if its array is a sum of arrays, the k-th
of which is a restriction of b k. 

### `SumRestr.of_withVal`

 If the array of s is the sum of the arrays v k, then s is a sum of restrictions of the tensors
with these arrays. 

### `Restr.sumRestr`

 A restriction is a sum of restrictions with one term. 

### `SumRestr.of_zero`

 A tensor whose array is 0 is a sum of restrictions of the empty family. 

### `SumRestr.bind`

 A sum of restrictions of tensors that are themselves sums of restrictions is a sum of restrictions
(covers are transitive). 

### `Restr.trans_sum`

 A restriction of a sum of restrictions is a sum of restrictions of the same tensors. 

### `SumRestr.mono`

 In a sum of restrictions every term may be replaced by a tensor of which it is a restriction. 

### `SumRestr.reindex`

 The terms of a sum of restrictions may be renamed. 

### `SumRestr.mul`

 The product of two sums of restrictions is a sum of restrictions of the products of two terms. 

### `SumRestr.push`

 A sum of restrictions stays one if the legs are given to other parties. 

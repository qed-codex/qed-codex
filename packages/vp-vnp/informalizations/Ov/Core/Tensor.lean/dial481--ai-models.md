---
{
  "module": "Ov/Core/Tensor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Tensor.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Core/Tensor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Tensors over a finite set of parties

Paper: the subsection "Tensors". A tensor over a set I of parties is an array
with one index for each party. This file defines local maps, restrictions, sums of restrictions,
products, powers, push-forwards (`push`), and spectral points. The field is any field (where more is
needed, it is a hypothesis).


### `Ten`

 A tensor over the parties I with entries in K: for each party p a finite index set ι p, and an
array. The zero array is allowed. 

### `Loc`

 Linear maps on the legs, as matrices: from the legs of t to the legs of s. 

### `app`

 The array obtained from t by the local maps L. 

### `Restr`

 s is a restriction of t: s arises from t by local maps. 

### `SumRestr`

 s is covered by the tensors b k: it is a sum of restrictions of them. There is one
restriction of each b k; it may be 0. 

### `Equi`

 s and t are restrictions of one another. (The paper identifies such tensors.) 

### `one`

 The tensor 1: all legs one-dimensional, the entry 1. 

### `mul`

 The product (Kronecker product, party by party). 

### `kpow`

 The k-th power: indices are k-tuples. 

### `prod`

 The product of a finite family. 

### `push`

 The push-forward πt: the index j of a tensor on J is given to the party π j. A party may get several
indices, or none (then its index set has one element). 

### `unit`

 The unit tensor ⟨r⟩_J of size r on J. 

### `wire`

 The wire ⟨n⟩_pq of dimension n between p and q. If p = q and n > 0 it is equivalent to 1. 

### `RankLE`

 A tensor has rank at most r if it is a restriction of the unit tensor of size r. (If there is a
party, this is the same as being a sum of r products of vectors: `rankLE_iff`.) 

### `Spec`

 A spectral point over the parties I: a real function F ≥ 0 on the tensors over I that is
multiplicative, with F(1) = 1 and F(s) ≤ ∑ F(b k) whenever s is a sum of restrictions of the b k. This
is the paper's definition, a multiplicative gauge; with the empty family it gives F(0) = 0. 

### `e`

 The paper's d_φ(p,q), the exponent of a wire: log₂ of the value at the wire of dimension 2 between p and q. 

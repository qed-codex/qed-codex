---
{
  "module": "proof/networks/Groundwork/Net/Net.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Net/Net.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Net/Net.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Theorems on the definitions of Groundwork.Net.Defs: an instance
padded to a larger alphabet has the value of the instance's network, the half-edge form of Z,
merging keeps the value and
multiplies the size by the class size, and the instance made from a network has the network's value;
also bounds on the sizes and
values of a merged network and of the instance made from a network. 

### `prod_erase_eq_pairs`

 A product over ordered pairs of distinct nodes, regrouped by unordered pairs. 

### `prod_le_prod_of_nonneg`

 Products of nonnegative factors are monotone. 

### `abs_prod_le_two_pow`

 A product of at most k integers of absolute value at most 2^B has absolute value at most
2^(B·k). 

### `card_class_pairs_le`

 If every class has at most m members, there are at most m² ordered pairs from one class to
another. 

### `pr_of_lt`

 Both orders of a pair a < b have the name (a, b). 

### `lab_comm`

 The label set of a pair does not depend on the order of the two nodes. 

### `Ψ_comm`

 The interaction of a pair, read from the other side. 

### `Z_toInst`

 The instance made from a network has the network's value, for every way (D, dec) of naming its
labels by elements of A. 

 ### Half-edges and padding 

### `Inst.net`

 An instance as a network: a state of v is a vector of half-edges with source v; the edge {v,w}
asks that the two
half-edges agree. The capacities are set to 0: no statement on sizes is made of this network. 

### `Inst.toInst_net`

 An instance, made into a network and back into an instance over a larger alphabet, is the padded
instance. 

### `Inst.Z_pad_eq_value`

 The padded instance has the value of the network of the instance. 

### `Inst.Z_eq_value`

 An instance has the value of its network. 

### `Inst.Z_eq_halfEdges`

 Half-edges: every edge is cut into two half-edges that must agree.
Z(R) = Σ_ℓ ∏_w R_w(ℓ(w,·)) ∏_{w<w'} [ℓ(w,w') = ℓ(w',w)], with ℓ(w,w) = d. 

 ### Merging 

### `merge_Ψ_lt`

 The interaction of two classes G < G' is the product of the interactions of their members. 

### `merge_Ψ`

 The interaction of two classes is the product of the interactions of their members. 

### `prod_orient`

 A product of a symmetric function over unordered pairs in different classes, oriented by class
or by node. 

### `merge_summand`

 One summand of the value of a network, regrouped by classes. 

### `value_merge`

 Merging keeps the value. 

### `card_merge_S`

 The number of states of a class. 

### `merge_shaped`

 If every class has at most m members, the merged network has the shape of a network of size P·m. 

### `merge_sized`

 If every class has at most m members, the merged network has size P·m and values bounded by
2^{B·(m+m²)}:
a merged weight is a product of at most m weights and at most m² interactions, a merged factor or
interaction is a
product of at most m² factors or interactions. 

### `abs_toInst_le`

 A value of the instance is a sum of at most 2^P terms, each a product of one weight and card J −
1 factors. 

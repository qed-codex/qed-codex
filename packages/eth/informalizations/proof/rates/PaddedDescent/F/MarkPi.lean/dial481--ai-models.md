---
{
  "module": "proof/rates/PaddedDescent/F/MarkPi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkPi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkPi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers: the sum over the sets of violated clauses

Fix an assignment σ. A set P of clauses that σ violates, with at most w clauses in every layer, gets
the sign (−1)^(number of its clauses outside the first layer). The sum of
these signs is the product over the layers of the cut-off sums: Σ_{j ≤ w} C(v, j) for the first
layer and Σ_{j ≤ w} (−1)^j·C(v, j) for the others, where v is the number of
violated clauses of the layer (`stPiSum`). The reason: P is chosen layer by layer, and a layer has
C(v, j) sets of j violated clauses.
The first part is about any finite set V with a map `lay` into the layers 0, …, R − 1; the second
part applies it to the list of all clauses of
`proof/rates/PaddedDescent/F/MarkNet.lean`. 

 ### Any finite set divided into layers 

### `sum_powerset_union`

 The sum of F (X ∩ A) · G (X ∩ B) over the subsets X of a disjoint union A ∪ B is the sum of F
over the subsets of A times the sum of G over the subsets of B. 

### `sum_powerset_layers`

 Let a subset X of V have the weight Π_{i < R} φ i (the part of X in layer i). The sum of the
weights is the product over the layers of the sum of φ i over the subsets
of layer i. 

### `sum_powerset_cap`

 The sum of s^|P| over the subsets P of S with at most w elements is Σ_{j ≤ w} s^j·C(|S|, j). 

### `prod_sign`

 With the factor 1 for each element of layer 0 and −1 for each other element, the product over
the layers is (−1)^(number of elements outside layer 0). 

### `sum_capped`

 The sum of (−1)^(number of elements outside layer 0) over the subsets X of V with at most w
elements in every layer is the product over the layers of the cut-off sums. 

 ### The list of all clauses 

### `card_filter_range_getD`

 The number of places of a list whose entry has the property p is the count of p in the list. 

### `sum_range_ite`

 A sum over the places below n in which only the place i counts, with c, is c if i < n and 0
otherwise. 

### `prod_map_eq_prod_range`

 The product of f over a list is the product over its places. 

### `layer_lt`

 The layer of a clause of the list of all clauses is below the number of layers. 

### `countP_cls`

 Among all clauses, those of layer i with the property p are as many as the clauses with p in the
list of layer i. 

 ### The interface statement 

### `card_layP_vset`

 The violated clauses of layer i are as many as `nvio` counts in the list of layer i. 

### `sum_vset`

 The sum, over the sets P of violated clauses with at most w clauses in every layer, of the sign
of P is the product of the cut-off sums of the layers: unsigned for the
first layer, signed for the others. 

### `stPiSum`

 `sum_vset`, as the interface states it. 

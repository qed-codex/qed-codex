---
{
  "module": "Paper/Tensors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Tensors.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Tensors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Tensors, prices and duality": tensors

The subsection "Tensors". One theorem for every numbered statement, in the order of the paper and named by its label, and
one for every step of the running text that is used later. Tensors are arrays over a field K with one finite index set for
each party (Ov.Ten); tensors that are restrictions of one another (Ov.Ten.Equi) are not identified, instead a spectral point
has the same value on them (def_spectral_congr). The other subsections are in Paper/Gauges.lean, Paper/Extension.lean and
Paper/Prices.lean.


 ## Tensors 

### `tensor_mul_laws`

 "Tensors that are restrictions of each other are identified, so that the product is commutative, with unit the tensor
1"; it is also associative. 

### `tensor_one_restr`

 "Every nonzero t has 1 as a restriction". 

### `tensor_covered_by_ones`

 "Every t is covered by finitely many copies of 1." 

### `tensor_push_mul`

 "Push-forward commutes with products". 

### `tensor_push_comp`

 "Push-forward commutes with … compositions". 

### `tensor_push_id`

 The push-forward along the identity does nothing. 

### `tensor_push_one`

 "Push-forward … sends 1 to 1". 

### `tensor_push_cover`

 "Push-forward … sends … covers to covers"; in particular restrictions to restrictions. 

### `def_spectral`

 **Paper: Definition def:spectral.** "A spectral point on I is a function φ ≥ 0 on tensors with φ(1) = 1,
φ(st) = φ(s)φ(t), and φ(s) ≤ ∑ φ(t_j) whenever s is covered by t_1, …, t_r." 

### `def_spectral_values`

 The text after the definition: "So φ(t) ≥ 1 if t ≠ 0, and φ(0) = 0 (the empty sum)." 

### `def_spectral_congr`

 Tensors that are restrictions of each other are identified: a spectral point is monotone under restriction, so it has
the same value on them. 

### `trivialPoint`

 The first example after Definition def:spectral: "An example is φ(t) = 1 for all t ≠ 0". 

### `powerPoint`

 The last example after Definition def:spectral: "φ^s is again a spectral point for 0 < s ≤ 1." 

### `lem_exponents_power`

 Proof of Lemma lem:exponents: "The function q ↦ φ(⟨q⟩_P) is at least 1, multiplicative and monotone, hence a power of q."
The unit tensor has a leg at π a for every a; the exponent is Nc.Price.hexp. 

### `lem_exponents_wire`

 The case of a wire: φ(⟨q⟩_uv) = q ^ d_φ(u,v). 

### `lem_exponents_unit_interval`

 Proof of Lemma lem:exponents: "A wire of dimension q is covered by q copies of 1, so d_φ ≤ 1." (The cover and its
consequence φ(⟨q⟩_uv) ≤ q are Ov.Spec.unit_le.) Also d_φ ≥ 0, as for every exponent. 

### `lem_exponents_self`

 "We put ⟨q⟩_uu = 1": a wire from u to u is a restriction of 1, so d_φ(u,u) = 0. 

### `lem_exponents_symm`

 A wire has no direction. 

### `lem_exponents_contract`

 Proof of Lemma lem:exponents: "Contracting the two indices at v shows that ⟨q⟩_uw is a restriction of ⟨q⟩_uv ⟨q⟩_vw". 

### `lem_exponents_triangle`

 Proof of Lemma lem:exponents: "… this is the triangle inequality." 

### `lem_exponents_tree`

 Proof of Lemma lem:exponents: "Identifying the indices at every vertex in the same way shows that ⟨q⟩_P is a restriction of
the product of the wires on the edges of the tree." The unit tensor has a leg at π p for every vertex p ∈ A; the edge e joins
a e and b e; of the graph only connectedness is used, in the form that a function to Fin q that is constant along edges is
constant. 

### `lem_exponents_tree_le`

 The consequence of lem_exponents_tree in exponents: g_φ(P) ≤ ∑ d_φ(e) over the edges. 

### `lem_exponents`

 **Paper: Lemma lem:exponents.** "Let φ be a spectral point on I. For every nonempty P ⊆ I there is g_φ(P) ≥ 0 with
φ(⟨q⟩_P) = q ^ g_φ(P) for all q ≥ 1. The function d_φ(u,v) = g_φ({u,v}), d_φ(u,u) = 0, is a pseudometric with values in
[0,1], and g_φ(P) ≤ ∑ d_φ(e) over the edges of any tree on P." The function d_φ is Ov.Spec.e. 

---
{
  "module": "Paper/Flat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Flat.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Flat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "The flat case"


 ### The polynomial of the complete network 

### `fkl_eq`

 The polynomial f_{k,ℓ}: the sum over the strings σ on the pairs of the product of the variables x_{a,σ_a}; and as a
tensor on the ends it is the product of the wires on the pairs. 

### `pairOf`

 The other end of a pair. 

### `Val`

 A value of σ_a: a table with no string for a itself. 

### `fklLits`

 The literals of the clause σ_a = ρ. 

### `fklWt`

 The weight x_{a,ρ} of the clause σ_a = ρ. 

### `lem_fkl_perm_clauseSum`

 "It is the clause sum over the bits of σ in which, for every a and every value ρ of σ_a, the clause saying σ_a = ρ
has the weight x_{a,ρ}." 

### `fkl_complete`

 The form of Lemma lem:fkl-perm for every family that is complete for grid sums: if M ≥ κk³ℓ2^(kℓ), then f_{k,ℓ} is a
projection of G_M with affine entries. 

### `lem_fkl_perm`

 **Paper: Lemma lem:fkl-perm.** "If PERM_M has a circuit over k with s gates and M ≥ 3k³ℓ2^(kℓ), then f_{k,ℓ} has
one with 5s gates." (2 ≠ 0 is a standing hypothesis of the section.) 

### `fklExact`

 f_{k,ℓ} with exactly the variables that occur, k blocks of 2^((k-1)ℓ) variables, as printed. 

### `fklExact_computes`

 The unused variables of f_{k,ℓ} are harmless: the polynomial with exactly the occurring variables has the same
circuit sizes. 

### `lem_fkl_perm_printed`

 **Paper: Lemma lem:fkl-perm**, for f_{k,ℓ} with exactly the printed variables. 

 ### Balanced products 

### `linearIn`

 A polynomial that is linear in each block of S and contains no other variables, by its coefficients. 

### `linearPart`

 The part of a polynomial that is linear in each block. 

### `linearIn_mul`

 A product gh, g linear in each block of S and h in each other block, by its coefficients. 

### `lem_balanced`

 **Paper: Lemma lem:balanced.** "If a polynomial has a circuit with L gates, its part f that is linear in each of
k ≥ 2 blocks of variables of equal size is a sum of products gh: for every set S with k ≤ 3|S| ≤ 2k at most L products
in which g is linear in each block of S, h in each other block, and neither contains other variables." The blocks are
{a} × T, and R is any commutative semiring, so it holds for approximating circuits too. 

### `lem_balanced_cf`

 Lemma lem:balanced for the coefficients: the coefficient of ∏ x_{a,y_a} is a sum of products. 

 ### The tensor of f_{k,ℓ} 

### `strEquiv`

 The numbers below 2^ℓ are the strings of ℓ bits. 

### `fklTen`

 The tensor of f_{k,ℓ} on the ends: the product of the wires of dimension 2^ℓ on the pairs. 

### `tables`

 The strings at the tables for an entry of the tensor. 

### `fklTen_val`

 "As a tensor on the ends it is the product of the wires on the pairs." 

### `hubOf`

 The hub of an end for the set S. 

### `hubTen`

 The product of the wires from the ends to their hubs for S and a wire of dimension L between the hubs. 

### `hubCost`

 What the set S costs: ℓ times the wires from the ends to their hubs, and the wire between the hubs. 

### `prop_flat_lower_sum`

 "By Lemma lem:balanced the tensor of f_{k,ℓ} is a sum of at most 2^k tensors, one for each S, each of which Lemma
lem:hubs leads through ±o_S with a wire of dimension L between them." (At most 2^k: card_bal_le.) The tensor here is that of the part linear in
each block of any polynomial with L gates. 

 ### The lower bound 

### `prop_flat_lower_lengths`

 The estimate of the proof of Proposition prop:flat-lower: with the ends at ½u_{ab}, the hubs ±o of length 1/(6√k)
can be chosen so that "the lengths add up to at most N − k/12". 

### `lowerPos`

 The end (a, b) or (b, a) of a pair. 

### `prop_flat_lower`

 **Paper: Proposition prop:flat-lower.** "In the flat case, for every k ≥ 2 there is ℓ₀ such that for ℓ ≥ ℓ₀ every
circuit over k for f_{k,ℓ} has at least 2^(ℓk^(3/2)/6) gates." 

### `prop_flat_lower_printed`

 **Paper: Proposition prop:flat-lower**, for f_{k,ℓ} with exactly the printed variables. 

### `thm_flat_simple`

 **Paper: Theorem thm:flat-simple.** "In the flat case, for every C there is m₀ such that PERM_m has no circuit
over k with m^C gates for m ≥ m₀." 

---
{
  "module": "proof/variables/VariableBound/Field/Quot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Quot.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Quot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The residues modulo X^s + g

Facts on residues for the proof of Lemma 13 (Family of checks), which takes 𝔽 = GF(2^s), finds an
irreducible polynomial of degree s by search, and writes the elements of 𝔽 as strings of s bits.
Here g is a word of s bits,
`modP g` = X^s + g, and `FW g` is the ring of residues modulo it.

* `monic_modP`, `natDegree_modP`: X^s + g is monic of degree s; `two_eq_zero_FW`: 2 = 0 in the ring;
  `root_pow`: X^s ≡ g.
* `bitsW g`: the coordinates of a residue in the basis 1, X, …, X^(s−1), a linear bijection onto the
  strings of s bits. `bitsW_decW`: the coordinates of the residue that a word of s bits stands for
  are its
  bits; so the words of s bits and the residues correspond one to one (`decW_inj`, `decW_surj`).
* `exists_irreducible_modP`: for every s ≥ 1 some X^s + g is irreducible; with `irrW_iff` this makes
  the search succeed (`modW_spec`, proof/variables/VariableBound/Field/Search.lean).
  `irreducible_of_inv`: if every residue other than 0 has an inverse, X^s + g is irreducible. 

### `map_bitR`

 A homomorphism of rings maps a bit to the same bit. 

### `bitR_decide`

 In ZMod 2, c is the bit «c = 1». 

### `bitR_inj`

 Different bits are different elements of ZMod 2. 

### `getD_ofFn`

 The i-th entry of the word of the bits x_0, …, x_(n−1) is x_i. 

### `coeff_polyW`

 The coefficient of X^i in the polynomial of the word w is the i-th bit of w, and 0 beyond the
end of w. 

### `map_decR`

 A homomorphism φ of rings maps b_0 + b_1·r + … to b_0 + b_1·φ(r) + …. 

### `degree_polyW_lt`

 The polynomial of a word of n bits has degree less than n. 

### `monic_modP`

 X^s + g is monic. 

### `natDegree_modP`

 X^s + g has degree s, the length of g. 

### `two_eq_zero_FW`

 2 = 0 in the ring of residues. 

### `mk_polyW`

 The residue of the polynomial of the word w is the residue that w stands for. 

### `root_pow`

 X^s ≡ g modulo X^s + g. 

### `bitsW`

 The elements of the ring of residues written as strings of s bits: the coordinates in the basis
1, X, …, X^(s−1). 

### `Quot.bitsW_mk`

 The i-th coordinate of the residue of a polynomial p is the coefficient of X^i in the remainder
of p modulo X^s + g. 

### `bitsW_decW`

 The coordinates of the residue that a word w of s bits stands for are the bits of w. 

### `decW_surj`

 Every residue is the one that some word of s bits stands for. 

### `decW_inj`

 Two words of s bits that stand for the same residue are equal. 

### `Quot.exists_irreducible`

 Over the field with two elements there is a monic irreducible polynomial of every degree s ≥ 1:
the minimal polynomial of a generator of the field with 2^s elements. 

### `Quot.eq_modP`

 A monic polynomial of degree s over the field with two elements is X^s + g for the word g of its
s lower coefficients. 

### `exists_irreducible_modP`

 For every s ≥ 1 there is a word g of s bits such that X^s + g is irreducible. 

### `irreducible_of_inv`

 For g of length s ≥ 1: if every residue other than 0 modulo X^s + g has an inverse, then X^s + g
is irreducible. 

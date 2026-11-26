---
{
  "module": "proof/variables/VariableBound/Family/SmallBias.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Family/SmallBias.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Family/SmallBias.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 13 (Family of checks): the small-bias parity

The sentences of the proof of Lemma 13 from «For every nonempty set V′ of clauses» to «the
probability is 1/2», and the half of «A clause lies in Γ_u with probability at most 1/v» that speaks
of (u₃, u₄).

Setting: 𝔽 is a finite field that is an algebra over ZMod 2, and `bits` is a linear bijection from 𝔽
to the strings of s bits, so 𝔽 has 2^s elements (`card_eq`). The clauses are the numbers E < m, and
ι(E) = E.
Probabilities are counts with the fractions cleared: «with probability at least 15/32» over (u₃, u₄)
∈ 𝔽² is 15·|𝔽|² ≤ 32·(number of pairs).

In the order of the text:
* `sum_ip`, `odd_iff_ip`: the sum of the ⟨u₃^ι(E), u₄⟩ over E ∈ V′ is ⟨w, u₄⟩ modulo 2 with w = Σ_{E
  ∈ V′} u₃^ι(E);
* `poly_ne_zero`, `poly_natDegree_le`, `roots`: w is a nonzero polynomial of degree at most m − 1 in
  u₃, so w = 0 for at most m − 1 values of u₃;
* `ip_half`: for w ≠ 0 the probability is 1/2 (and `ip_zero`: for w = 0 it is 0);
* `small_bias_count`: the probability is at least (1/2)·(1 − (m−1)/2^s); `small_bias`: this is at
  least 15/32 if 16m ≤ 2^s;
* `half`: for one clause E, ⟨u₃^ι(E), u₄⟩ = 1 with probability at most 1/2. 

 ## The inner product of strings of bits 

### `ip_add_right`

 ⟨x, y + z⟩ = ⟨x, y⟩ + ⟨x, z⟩. 

### `ip_sum_left`

 ⟨Σ_e f e, y⟩ = Σ_e ⟨f e, y⟩. 

### `ip_zero_left`

 ⟨0, y⟩ = 0. 

### `ip_single`

 ⟨x, e_i⟩ = x_i for the string e_i with the single bit 1 at place i. 

### `half_strings`

 For a string x ≠ 0, exactly half of the strings y of s bits have ⟨x, y⟩ = 1: if x_i = 1, then y
↦ y + e_i exchanges the y with ⟨x, y⟩ = 1 and the others. 

### `odd_iff`

 For f with values in ZMod 2, the number of e ∈ T with f e = 1 is odd if and only if the sum of
the f e over e ∈ T is 1. 

### `card_pairs`

 The number of pairs with a property is the sum, over the first entry, of the number of second
entries. 

 ## The sum is ⟨w, u₄⟩ 

### `sum_ip`

 Proof of Lemma 13 (Family of checks), «the sum is ⟨w, u₄⟩ modulo 2 with w = Σ_{E ∈ V′} u₃^ι(E)»:
for every set V′ of clauses and all u₃, u₄ ∈ 𝔽. 

### `odd_iff_ip`

 For every set V′ of clauses and all u₃, u₄ ∈ 𝔽, the number of E ∈ V′ with ⟨u₃^ι(E), u₄⟩ = 1 is
odd if and only if ⟨w, u₄⟩ = 1, with w = Σ_{E ∈ V′} u₃^ι(E). 

 ## The polynomial w 

### `poly`

 w as a polynomial in u₃: Σ_{E ∈ V′} X^ι(E). 

### `eval_poly`

 The value of the polynomial at u₃ is w = Σ_{E ∈ V′} u₃^ι(E); at u₃ = 0 the power with exponent 0
is 1. 

### `poly_ne_zero`

 Proof of Lemma 13 (Family of checks), «a nonzero polynomial»: for V′ nonempty; the coefficient
of X^ι(E) is 1 for E ∈ V′, because ι is injective. 

### `poly_natDegree_le`

 Proof of Lemma 13 (Family of checks), «of degree at most m − 1»: for every set V′ of clauses. 

### `roots`

 Proof of Lemma 13 (Family of checks), «so w = 0 for at most m − 1 values of u₃»: for V′
nonempty. 

 ## For w ≠ 0 the probability is 1/2 

### `card_eq`

 A field whose elements are written, by `bits`, as the strings of s bits has 2^s elements. 

### `ip_half`

 Proof of Lemma 13 (Family of checks), «for w ≠ 0 the probability is 1/2»: for w ∈ 𝔽, w ≠ 0,
exactly half of the u₄ ∈ 𝔽 have ⟨w, u₄⟩ = 1. 

### `ip_zero`

 For w = 0 no u₄ ∈ 𝔽 has ⟨w, u₄⟩ = 1. 

### `ip_le_half`

 For every w ∈ 𝔽, at most half of the u₄ ∈ 𝔽 have ⟨w, u₄⟩ = 1. 

 ## The two counts over (u₃, u₄) 

### `small_bias_count`

 Proof of Lemma 13 (Family of checks), «for every nonempty set V′ of clauses, Σ_{E ∈ V′}
⟨u₃^ι(E), u₄⟩ is odd with probability at least (1/2)·(1 − (m−1)/2^s)» over (u₃, u₄) ∈ 𝔽²: multiplied
by 2·|𝔽|², where |𝔽| = 2^s,
this is |𝔽|² ≤ 2·(number of pairs) + (m−1)·|𝔽|. As V′ is nonempty, m ≥ 1. 

### `small_bias`

 Proof of Lemma 13 (Family of checks), the small-bias parity: if 16m ≤ 2^s, then for every
nonempty set V′ of clauses, Σ_{E ∈ V′} ⟨u₃^ι(E), u₄⟩ is odd with probability at least 15/32 over
(u₃, u₄) ∈ 𝔽². 

### `half`

 Proof of Lemma 13 (Family of checks), the half of «a clause lies in Γ_u with probability at most
1/v» on (u₃, u₄): for every clause E, ⟨u₃^ι(E), u₄⟩ = 1 with probability at most 1/2 over (u₃, u₄) ∈
𝔽². 

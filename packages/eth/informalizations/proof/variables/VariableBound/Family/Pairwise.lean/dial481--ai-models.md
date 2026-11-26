---
{
  "module": "proof/variables/VariableBound/Family/Pairwise.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Family/Pairwise.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Family/Pairwise.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 13 (Family of checks): the events H_E

The part of the printed proof that speaks of (u₁, u₂), one theorem for each of its steps, with
fractions cleared: a probability is a number of pairs (u₁, u₂) ∈ 𝔽², out of |𝔽|².
Throughout, 𝔽 is a finite field, `bits` writes its elements as strings of s bits (linearly over the
field with two elements), ϑ gives the m clauses distinct elements of 𝔽, and v = 2^a.

* `pair_uniform`: for ϑ ≠ ϑ' the pair (u₁ϑ + u₂, u₁ϑ' + u₂) is uniformly distributed in 𝔽².
* `card_H`: the event H_E has probability 2/v.
* `card_H_and`: the events H_E are pairwise independent.
* `sum_Y`, `sum_Y_sq`: the mean y of Y, and E(Y²) ≤ y² + y.
* `second_moment`: Pr(Y > 0) > 2/3 for a set V of more than v clauses. 

### `H`

 The event H_E for the pair p = (u₁, u₂): the first a − 1 = log v − 1 bits of u₁·ϑ_E + u₂ are 0. 

### `instance (bits : F ≃ₗ[ZMod 2] (Fin s → ZMod 2)) (ϑ : Fin m ↪ F) (a : ℕ) (p : F × F) (E : Fin m) : Decidable (H bits ϑ a p E)`

 Whether H_E holds can be decided. 

### `Z`

 The elements of 𝔽 whose first a − 1 bits are 0. 

### `Y`

 Y: the number of the clauses E ∈ V for which H_E holds. 

### `card_F`

 𝔽 has 2^s elements, since its elements are written as strings of s bits. 

### `card_Z`

 If a − 1 ≤ s, one element of 𝔽 in 2^(a−1) has its first a − 1 bits equal to 0. 

### `pair_uniform`

 Proof of Lemma 13 (Family of checks): for distinct ϑ, ϑ' ∈ 𝔽 the pair (u₁ϑ + u₂, u₁ϑ' + u₂) is
uniformly distributed in 𝔽² when (u₁, u₂) is: the map is a bijection of 𝔽². 

### `card_pair_mem`

 The number of pairs (u₁, u₂) whose image (u₁ϑ + u₂, u₁ϑ' + u₂), ϑ ≠ ϑ', lies in a set S ⊆ 𝔽² is |S|. 

### `card_H`

 Proof of Lemma 13 (Family of checks): the event H_E has probability 1/2^(a−1), which is 2/v for
v = 2^a and a ≥ 1, if a − 1 ≤ s: 2^(a−1) times the number of pairs (u₁, u₂) with H_E is |𝔽|². 

### `card_H_and`

 Proof of Lemma 13 (Family of checks): the events H_E are pairwise independent, if a − 1 ≤ s: for
E ≠ E', 4^(a−1) times the number of pairs (u₁, u₂) with H_E and H_E' is |𝔽|². 

### `sum_Y`

 Proof of Lemma 13 (Family of checks): the mean of Y is |V|/2^(a−1), which is y = 2|V|/v for v =
2^a and a ≥ 1, if a − 1 ≤ s: 2^(a−1) times the sum of Y over all pairs (u₁, u₂) is |V|·|𝔽|². 

### `sum_Y_sq`

 Proof of Lemma 13 (Family of checks): E(Y²) ≤ y² + y (the variance of Y is at most its mean y =
2|V|/v), if a − 1 ≤ s: 4^(a−1) times the sum of Y² over all pairs (u₁, u₂) is at most (|V|² +
2^(a−1)·|V|)·|𝔽|². 

### `cauchy_schwarz`

 Proof of Lemma 13 (Family of checks): the Cauchy–Schwarz inequality in the form Pr(Y > 0) ≥
(EY)²/E(Y²): the square of the sum of Y is at most the number of pairs (u₁, u₂) with Y > 0 times the
sum of Y². 

### `second_moment`

 Proof of Lemma 13 (Family of checks): Pr(Y > 0) > 2/3 for a set V of more than v = 2^a clauses,
if 1 ≤ a and a − 1 ≤ s: three times the number of pairs (u₁, u₂) for which H_E holds for some E ∈ V
is more than 2·|𝔽|². 

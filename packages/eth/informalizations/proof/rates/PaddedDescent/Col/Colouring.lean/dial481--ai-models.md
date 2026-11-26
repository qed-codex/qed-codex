---
{
  "module": "proof/rates/PaddedDescent/Col/Colouring.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Col/Colouring.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Col/Colouring.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A colouring lemma for few points

g points carry c a b ≤ M bits between a and b. The proof of Lemma 1 of the paper colours them with K
colours so that any two classes share about
U/K² bits (U = the sum of all c a b); it uses second moments, knows only the row sums of c, and
needs g ≥ 3K⁸. Here the single entries are bounded by M,
and g of the order K·log K is enough: if 4·D²·m·K ≤ g and (g+2)·K < 2^m, some colouring has classes
of fewer than 2g/K points and at most
U/K² + 3g²M/(D·K²) bits from any class to any class.

The proof counts colourings. Only three kinds of sums that are linear in the colouring are
controlled: the size of a class, the bits from one point into a
class, and the sum of the row sums over a class. For weights 0 ≤ x b ≤ 1, the sum over all
colourings χ of exp(θ·Σ_{χ b = γ} x b) is a product over the
points (`sum_exp_le`); this bounds the number of colourings that put at least the mean plus δ·g/K
into the class γ (`card_tail_le`); there are (g+2)·K such events
(`exists_all_good`). Main results: `exists_colouring_cap`, `exists_colouring_cap_nat`. 

### `Wt`

 The weight that the colouring χ puts into the class γ. 

### `exp_le_quad`

 exp y ≤ 1 + y + y² for 0 ≤ y ≤ 1. 

### `sum_exp_le`

 The exponential moment, as a sum over all colourings: at most K^g·exp((θ+θ²)·mean), for 0 ≤ θ ≤ 1. 

### `card_tail_le`

 The tail, as a count: at most K^g·exp(−δ²s/4) colourings put at least mean + δ·s into the class
γ, where s is any upper bound for the mean. 

### `mean_le`

 If x ≤ 1 pointwise, the mean is at most g/K. 

### `exists_all_good`

 Finitely many families of weights at once: if the number of (weight, colour) pairs times
exp(−δ²s/4) is below 1, one colouring is good for all. 

### `Wt_eq`

 The weight of a class as a sum over the class. 

### `exists_colouring_cap`

 **The colouring lemma with a bound M on the bits between two points.** g points, K ≥ 1 colours,
c a b ≤ M, δ = 1/D. If (g+2)·K·exp(−δ²·(g/K)/4) < 1, some
colouring has classes of fewer than 2g/K points, and from any class to any class at most U/K² +
3g²M/(DK²) bits, where U = Σ_{a,b} c a b. 

### `two_pow_le_exp`

 2^m ≤ exp m. 

### `exists_colouring_cap_nat`

 The same lemma for `Fin g`, `Fin K`, with a hypothesis in natural numbers: 4·D²·m·K ≤ g and
(g+2)·K < 2^m for some m. 

---
{
  "module": "proof/rates/ClauseBound/Boson/Half.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Half.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Half.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces made from partitions: the two factors of a term of Q_s, and their sizes

The strings of λ bits are encoded by partitions of h. The piece number s, |s| ≤ 2h, is A_s(x,y,u,v) =
(h!/z_{μ(v)})·Q_s(a^{μ(x)}, t^{μ(v)}) at the entry (μ(u), μ(y)), where z_μ is the number of Appendix
B.

* Q_s is a sum over i ≤ 2h of products of two matrices; written out, a product of matrices is a sum
  over the monomials τ of one weight (`Qk_eq`). `topK` and `botK` are the two factors of such a
  term.
* A function that is a sum over i ≤ 2h and over the monomials τ of weight t(i) of products of two
  factors below 2^{eL h} and 2^{eR h} factors through the logarithm of the number of the pairs (i,
  τ),
  with functions below 2^{big h} (`factors`).
* For 2h + 1 different weights up to 4h, the number of these pairs is at most the number of
  monomials of all weights up to 4h (`sum_pz_le`).

The auxiliary statements are in the namespace `ClauseBound.Boson.Half`. 

### `topK`

 The factor of a term of Q_s that carries a^μ: (−1)^i·Σ_{(c,L) ∈ a^μ} c·C(|L| + h, i)·L[r]. 

### `botK`

 The other factor, with h!/z_ν in front: (h!/z_ν)·ν[r]. 

 ### Q_s as a double sum of products 

### `fL`

 The factor that carries the combination A: (−1)^i·Σ_{(c,L) ∈ A} c·C(|L| + h, i)·g(L). 

### `list_sum_mul_sum`

 A sum over a list of sums of products with a common second factor. 

### `Qk_eq`

 Q_s, with the products of matrices written out. 

 ### Sizes 

### `eL`

 The exponent of the bound for the factor with a^μ. 

### `eR`

 The exponent of the bound for the factor with h!/z. 

 ### The number of pairs (i, τ) 

### `sum_pz_le`

 2h + 1 different weights between 0 and 4h: at most as many monomials as there are of all the
weights up to 4h. 

### `big`

 The exponent of the bound in `factors`: 40(h + 1)^2, which exceeds eL h + eR h, plus the
logarithm, rounded up, of the number of monomials of weight at most 4h. 

### `factors`

 A function that is a sum over i ≤ 2h and over the monomials τ of weight t(i) of products of two
bounded factors factors through the number of the pairs (i, τ). 

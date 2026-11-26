---
{
  "module": "proof/rates/ClauseBound/Boson/KF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/KF.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/KF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The matrices of the parts of a^μ of a given weight

The combination a^μ = ∏_i (−1)^{μ_i−1}·y_{μ_i} has up to ∏_i μ_i monomials, too many to go through
one by one. `KF μ w r` is the matrix of (the part of weight w of a^μ)[r], that is, the sum of
c·L[r] over the monomials L of weight w of a^μ, with their coefficients c. This file proves

* the recursion on the parts of μ (`KF_nil`, `KF_cons`): one more factor (−1)^{n−1}·y_n =
  (−1)^{n−1}·Σ_{j=1}^{n} C(n,j)·t_j takes the tables of the weights w − j to the table of the weight
  w;
* that a sum over the monomials of a^μ with factors that depend on the weight only is a sum over the
  weights 0, …, |μ| (`sum_aFam_eq`);
* a bound on the entries (`abs_KF_le`). 

### `KF`

 The matrix of (the part of weight w of a^μ)[r]. 

 ### Sums over lists 

 ### The normally ordered product is linear in the family 

 ### The monomials of a^μ 

### `aFam_shape`

 A monomial of a^μ has as many parts as μ, its weight is at most that of μ, and its parts are at
most as large as the largest part of μ. 

 ### The statements 

### `KF_eq`

 The table of a weight, with the coefficients in front. 

### `KF_cons`

 One more factor (−1)^{n−1}·y_n. 

### `sum_aFam_eq`

 A sum over the monomials of a^μ with factors that depend only on the weight of the monomial is a
sum over the weights 0, …, |μ|. 

### `abs_KF_le`

 Sizes: as for a single monomial, times the sum of the absolute values of the coefficients. 

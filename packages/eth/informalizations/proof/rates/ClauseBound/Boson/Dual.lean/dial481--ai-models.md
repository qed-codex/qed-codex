---
{
  "module": "proof/rates/ClauseBound/Boson/Dual.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Dual.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Dual.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemmas on the dual families of Lemma 10

For a partition μ let a^μ = ∏_i (−1)^{μ_i−1}·y_{μ_i} with y_n = Σ_{j=1}^{n} C(n,j)·t_j, as in Lemma 10.
This file shows that the monomials of a^μ have positive parts and weight at most |μ| (`aFam_ok`)
and that the absolute values of the coefficients of a^μ add up to at most 2^{|μ|}
(`sum_abs_aFam_le`). It also shows that z_ν divides h! for a partition ν of h (`zz_dvd_factorial`),
so that h!/z_ν, the factor of b^ν in Lemma 10, is an integer. The remaining lemmas are on sums over
lists and on factorials, and these proofs use them. 

 ### Sums over lists 

### `sum_range_eq_list`

 A sum over 0, …, n − 1 as the sum of a list. 

### `sum_map_flatMap`

 The sum over a concatenation of lists is the sum of the sums. 

### `aFam_ok`

 The monomials of a^μ have positive parts and weight at most |μ|. 

### `sum_abs_aFam_le`

 The absolute values of the coefficients of a^μ add up to at most 2^{|μ|}. 

 ### z_ν 

### `pow_mul_factorial_dvd`

 k^m·m! divides (m·k)!. 

### `zz_dvd_factorial`

 z_ν divides h!. 

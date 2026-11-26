---
{
  "module": "proof/rates/GeneralPieces/Ring/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The ring of Appendix B: binomial coefficients, partitions, the spaces V_E and the operators ∇_k

Statements of the paragraph "The ring and its operators" before display (47): Pascal's rule and
Vandermonde's identity for all integers (`GeneralPieces.binomRules`); the partitions of E and
p(E) ≤ p(E+1) (`GeneralPieces.ptnFacts`); V_E consists of the polynomials all of whose monomials t^μ
have |μ| = E (`GeneralPieces.Ring.mem_VE_iff`), V₀ = ℚ (`GeneralPieces.Ring.mem_VE_zero`) and V_E =
0 for E < 0 (`GeneralPieces.Ring.VE_neg`); ∇_k maps V_E to V_{E−k} (`GeneralPieces.Ring.nabla_mem`). 

 ### Binomial coefficients 

 ### Partitions 

### `map_toPNat'_toN`

 Back from natural numbers to positive integers. 

### `toN_map_toPNat'`

 The parts of a partition, made positive integers and natural numbers again. 

 ### Weights 

### `wgt`

 The weight of the variables: t_k has weight k. 

### `weight_toFinsupp`

 The weight of the monomial t^μ is |μ|. 

### `ext_coef`

 Two polynomials with the same coefficients are equal. 

### `mem_VE_iff`

 f has weight E if and only if every monomial of f has weight E. 

### `eq_sum_tpow`

 A polynomial is the sum of its monomials. 

 ### The operators ∇_k 

### `binomRules`

 "Pascal's rule and Vandermonde's identity hold for all integers k, k'." 

### `ptnFacts`

 The partitions of E are the multisets of positive integers with sum E, there are p(E) of them,
and "adding a part 1 shows p(E) ≤ p(E+1)" (`ClauseBound.Part.p_mono`). 

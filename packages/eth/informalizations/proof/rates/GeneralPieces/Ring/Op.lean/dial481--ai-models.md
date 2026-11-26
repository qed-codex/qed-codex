---
{
  "module": "proof/rates/GeneralPieces/Ring/Op.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Op.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Op.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The properties (O1) and (O3) of the operators a[r] of Appendix B

The appendix says "Clearly"; the arguments here start from display (47). (O1): a term of (47) maps
V_E to V_{E+r}, because ∇_k maps V_E to V_{E−k} (`term_mem`, `op_mem`), and it maps integer
polynomials to
integer polynomials (`isInt_term`). (O3): "if some k_i is negative, the positive ones add up to more
than h". Besides: t_n·t^μ as a monomial, coefficients of sums, the partitions of m, and a ↦ a[r]·f
as a linear map. 

 ### (O1): weights 

### `term_mem`

 A term of (47) with Σ k_i = −r maps V_E to V_{E+r}. 

 ### (O1): integer polynomials 

 ### (O1): 1[r] = [r = 0]·Id 

 ### Monomials t_n·t^μ 

 ### Coefficients of sums, partitions of m, and a ↦ a[r]·f as a linear map 

### `Pz_eq`

 The index set `ClauseBound.Boson.Pz m`, the multisets of natural numbers without 0 with sum m,
is the image of the partitions of m. 

### `opLeft`

 a ↦ a[r]·f as a linear map. 

### `o1`

 (O1). 

### `o3`

 (O3). 

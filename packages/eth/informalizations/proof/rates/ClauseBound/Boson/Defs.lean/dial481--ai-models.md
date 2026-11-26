---
{
  "module": "proof/rates/ClauseBound/Boson/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Operators on ℤ[t₁, t₂, …] as matrices: definitions

A monomial is a multiset of positive integers. An operator is given by its matrix K: `K π σ` is the
coefficient of t^π in the image of t^σ. All sums below are finite, so no formal
series are needed. ∇₋ₗ is the multiplication by t_l and ∇ₖ = k·∂/∂t_k (k, l ≥ 1). For a list a of
positive integers (the parts of a monomial), `op a r` is the matrix of the operator a[r] of
Appendix B of the paper, defined by the recursion that the paper calls (O2). Definitions only. 

### `Ker`

 The matrix of an operator. 

### `bet`

 The coefficient of ∇₋ᵣ in the series that belongs to t_n: C(r − 1, n − 1) for r ≠ 0, and 0 for r = 0. 

### `cre`

 ∇₋ₗ ∘ K. 

### `ann`

 K ∘ ∇ₖ. 

### `nop`

 The normally ordered product of the series of t_n with a family of operators F: Σ_{l ≥ 1} C(l−1,
n−1)·∇₋ₗ∘F(r − l) + Σ_{k ≥ 1} C(−k−1, n−1)·F(r + k)∘∇ₖ. At (π, σ) only the l in π and the k in σ
count. 

### `one`

 The identity. 

### `op`

 a[r], for the monomial whose parts are listed in a. 

### `P`

 The monomials of weight m: the multisets of positive integers with sum m. 

### `Pz`

 The same for an integer m; empty for m < 0. 

### `mul2`

 The matrix of a[r] ∘ b[r']. 

### `Gam`

 Γ_{j,n} = n·C(−n−1, j−1) = (−1)^{j−1}·(j+n−1)!/((j−1)!·(n−1)!). 

### `Pos`

 All parts are positive. 

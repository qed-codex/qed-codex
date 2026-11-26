---
{
  "module": "proof/rates/GeneralPieces/Ring/Bridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Bridge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Bridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The integer matrices `ClauseBound.Boson.op` are those of the operators a[r] of Appendix B

`GeneralPieces.stBridge`: the coefficient of t^π in a[r]·t^σ, with a[r] the sum of display (47) over
ℚ[t₁, t₂, …], is the entry (π, σ) of the integer matrix `ClauseBound.Boson.op`, which is defined by
the recursion (O2).
The steps: the rules for ∇_k on monomials; the differentiations commute, so that one more positive
k_i may be applied first (`nordQ_cons_pos`); term by term, the coefficients are those of the same
term
over ℤ[t₀, t₁, …] (`coef_nordQ`); "on f ∈ V_E a term vanishes if its positive k_i add up to more
than E" (`pos_eq_zero`), so that, the sum of the k_i being −r, all k_i of a nonzero term lie
between −M and M for M = E + |r| (`term_eq_zero`, `opMon_eq_sum`); and the finite sum is the entry
of the matrix by `ClauseBound.Boson.op_eq_sum`. 

 ### The operators ∇_k 

### `pn_coe`

 The positive integer |k| as a natural number. 

### `pderiv_comm`

 ∂/∂t_i and ∂/∂t_j commute. 

### `nabla_comm_pos`

 Two differentiations ∇_k, ∇_k' commute. 

### `coef_X_mul`

 The coefficients of t_l·f. 

### `nabla_pos_tpow`

 ∇_k on a monomial, k ≥ 1. 

### `nabla_foldr_pos`

 One more differentiation may be applied first. 

 ### One term of display (47) 

### `nordQ`

 ∏_{k_i < 0} ∇_{k_i} · ∏_{k_i > 0} ∇_{k_i}, applied to f. 

### `wtQ`

 ∏_i C(−k_i−1, μ_i−1). 

### `nordQ_cons_neg`

 A negative index: one more multiplication, applied last. 

### `nordQ_cons_pos`

 A positive index: one more differentiation, which may be applied first. 

 ### Partitions as multisets of natural numbers 

### `wt_erase`

 Without a part l, the weight is smaller by l. 

 ### Term by term, the coefficients are those over ℤ[t₀, t₁, …] 

### `wtQ_eq`

 The products of binomial coefficients are the same. 

 ### Only finitely many terms are nonzero 

### `pos_eq_zero`

 "A term vanishes if its positive k_i add up to more than E", on a monomial of weight E. 

### `filter_sums`

 The negative and the positive entries of a list of integers: their sums add up to the sum of the
list, and every entry lies between them. 

### `term_eq_zero`

 On a monomial of weight E, a term of (47) vanishes unless all k_i lie between −(E + |r|) and E + |r|. 

### `opMon_eq_sum`

 Display (47) on a monomial of weight E as a finite sum: over the lists of nonzero integers
between −M and M with sum −r, for any M ≥ E + |r|. 

### `stBridge`

 The coefficient of t^π in a[r]·t^σ is the entry (π, σ) of the matrix `ClauseBound.Boson.op`. 

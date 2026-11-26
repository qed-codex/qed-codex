---
{
  "module": "proof/rates/GeneralPieces/Ring/Dual.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Dual.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Dual.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 10 of Appendix B, along its proof

a^μ[−h]·b^ν = h!·[μ = ν] for partitions μ, ν of h, on the ring ℚ[t₁, t₂, …] with the operators a[r]
of display (47). The six sentences of the proof are named theorems, in the order of the text:
the numbers ϑ_n(k); the display for (∏ y_{μ_i})[−h]·b; Vandermonde's identity and the two values of
ϑ; a nonzero term has k_i = μ_i; a^μ[−h]·b = ∏ ∇_{μ_i} b; the value at b = t^ν.
The facts about display (47) and (O3) that the proof uses, and Vandermonde's identity, are taken
from the files on the ring (`opFacts`, `o3`, `binomRules`).
A partition is handled as a list of its parts. The sum over the tuples (k_i) of positive integers
with sum h is a sum over the finite set `posTuples` of the lists of the right length with entries in
{1, …, h} and sum h. The fact that z_μ divides h! is taken from
`ClauseBound.Boson.zz_dvd_factorial`. 

 ## The numbers ϑ_n(k) 

### `theta`

 «Let ϑ_n(k) = Σ_{j=1}^{n} C(n, n−j)·C(−k−1, j−1).» 

### `theta_eq`

 «By Vandermonde's identity ϑ_n(k) = C(n−k−1, n−1)». 

### `choose_neg_one`

 C(−1, m) = (−1)^m. 

### `theta_of_lt`

 «… which is 0 for 1 ≤ k < n». 

### `theta_self`

 «… and (−1)^{n−1} for k = n.» 

 ## Lists with one entry from each of given finite sets 

### `tuples`

 The lists with one entry from each of the given finite sets, in their order. 

### `sum_tuples_cons`

 A sum over such lists, sorted by the first entry. 

### `mem_tuples`

 Membership. 

### `prod_map_sum`

 Multiplying out a product of sums. 

 ## The display 

### `nablas`

 ∏_i ∇_{k_i}, applied to f. 

### `posTuples`

 The tuples (k_i) of r positive integers with sum h: a finite set. 

### `mem_posTuples`

 These are the lists of r integers k_i ≥ 1 with sum h. 

### `term_pos`

 A term of display (47) with all k_i positive: there are only differentiations. 

### `opMon_eq_sum`

 «… using (47) and (O3) for each monomial»: on b ∈ V_h, the operator a[−h] of a monomial a is the
sum of the terms of (47) with all k_i positive. 

### `tpow_cons`

 t^μ for a list with a first part. 

### `prod_y`

 «Multiplying out ∏ y_{μ_i}»: the sum over all choices of j_i ∈ {1, …, μ_i} of ∏ C(μ_i, j_i)
times the monomial ∏ t_{j_i}. 

### `op_sum`

 a[r] is linear in a, for finite sums. 

### `binom_symm`

 C(n, n−j) is the binomial coefficient of natural numbers C(n, j), for j ≤ n. 

### `sum_coeff`

 The sum over the j_i of the coefficients is ∏ ϑ_{μ_i}(k_i). 

### `display`

 The display in the proof: for b ∈ V_h, (∏_i y_{μ_i})[−h]·b = Σ over the tuples (k_i) with Σ k_i =
h and k_i ≥ 1 of ∏_i ϑ_{μ_i}(k_i)·∏_i ∇_{k_i} b. 

 ## Only one term is not zero 

### `le_of_prod_ne_zero`

 «So a nonzero term has k_i ≥ μ_i for all i». 

### `eq_of_forall₂_le`

 «… hence k_i = μ_i, because both add up to h.» 

### `sum_cast`

 |μ| as a sum of integers. 

### `sgn`

 The product of the signs (−1)^{μ_i−1}. 

### `prod_theta_self`

 At k_i = μ_i the coefficient is the product of the signs. 

### `display_single`

 The display has one term: (∏_i y_{μ_i})[−h]·b = ∏_i (−1)^{μ_i−1}·∏_i ∇_{μ_i} b, for a partition
μ of h and b ∈ V_h. 

### `aFam_eq`

 a^μ is the product of the signs times ∏ y_{μ_i}. 

### `aFam_op`

 «Therefore a^μ[−h]·b = ∏_i ∇_{μ_i} b.» 

 ## The value at b = t^ν 

### `nabla_tpow`

 ∇_n t^ν = n·m_n(ν)·t^{ν−n}, where ν − n is ν without one part n. 

### `nabla_smul`

 ∇_k is linear. 

### `nablas_snoc_tpow`

 The differentiation that is listed last is applied first. 

### `nablas_tpow_eq_zero`

 «For b = t^ν this is 0 if m_k(μ) > m_k(ν) for some k». 

### `eq_of_count_le`

 «… otherwise μ = ν, because |μ| = |ν|». 

### `zz_erase`

 z_ν = n·m_n(ν)·z_{ν−n}. 

### `nablas_tpow_self`

 «… and it is z_μ.» 

### `nablas_tpow`

 The last sentence of the proof: for partitions μ, ν of the same number, ∏_i ∇_{μ_i} t^ν = z_μ·[μ =
ν]. 

 ## The lemma 

### `weight_toFinsupp`

 The weight of the monomial t^ν is |ν|. 

### `tpow_mem`

 t^ν ∈ V_{|ν|}. 

### `lemmaDual`

 Lemma 10: a^μ[−h]·b^ν = h!·[μ = ν] for all partitions μ, ν of h. 

### `zz_eq`

 z_μ equals `ClauseBound.Boson.zz`, the number of that name where the parts are natural numbers. 

### `zDvd`

 «Here h!/z_μ is an integer»: z_μ divides |μ|!. The paper cites this; the proof here is
`ClauseBound.Boson.zz_dvd_factorial`. 

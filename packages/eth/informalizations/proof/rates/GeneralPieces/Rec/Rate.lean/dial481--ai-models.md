---
{
  "module": "proof/rates/GeneralPieces/Rec/Rate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Rate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Rate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem A, part (b) (Appendix A): the arithmetic, for every x₀ ≥ 18 with 2^x₀ ≥ c + 5

This file follows the proof of part (b) of Theorem A in Appendix A, in its order, for pieces whose
numbers of bits are at most 2λ (`P.m = 1`). The sentences from "so again P = g³λ" to the display for
K²L, and that case (ii) of Lemma 8
applies at every level, are in `proof/rates/GeneralPieces/Rec/Chain.lean`; the display for K²L is
used here. Part (a) enters as e_ℓ ≥ 0, e_ℓ ≤ 1 and e_ℓ·K_ℓ ≥ 1
(`proof/rates/GeneralPieces/Num/PartAUse.lean`).
Notation of the paper: K = K_ℓ, g = g_ℓ, N = g⁴λ, Ξ = g²(λ + B), P = g³λ, B₁ = gB + g²(2λ)^c. L and
B' are the program's numbers `lamNextG` and `bNextG`: L is the lemma's L computed from the program's
upper
bound for U (see Chain.lean), and B' = P·q + (gB + g²·bits)·(q + q²)·K with q = ⌊2g/K⌋, which is not
the lemma's ⌈2gP/K⌉ + g²B₁ but obeys the same crude bound B' ≤ N + g²B₁ (`B'_le`), the only one
used.

What differs. The paper counts operations; here the algorithm is a program that runs in time
polynomial in the length of a pad, and `needG` is the exponent of a pad that is long enough.
So a product of costs in the paper is a sum of exponents here where the program really multiplies
(the number of instances, the recursion) and a maximum where it only needs room
(the groupings K^g, the states 2^{2N/K}, the time 2^{cλ} of the pieces). All instances of a level
are expanded before the next level starts, so their number `cnt` and the bit length `z` of
the sum so far are carried along: by induction on ℓ, for all λ ≥ 1 and all B, cnt, z,
  needG ≤ size cnt + size (z + size cnt) + e_ℓ·K_ℓ²·λ + (6c + 14)·K_ℓ²·log(K_ℓ(λ + B)).
The constant is C₀ = 6c + 17 in place of 2(c + C₄ + 1) + C₅. 

 ### Level 0 

### `brute_le`

 "For ℓ = 0, brute force sums 2^{λK₀(K₀−1)/2} ≤ 2^{e₀K₀²λ} terms". 

### `first_le`

 The first budget (room for the instances of the level) is within the bound. The inequality
e_ℓ·K_ℓ ≥ 1 is taken from part (a). 

### `base_le`

 The induction starts: the first budget, and brute force. 

 ### The number of terms of the sum over ι 

### `nPat_le_quarter`

 "The |I|^{|R|} ≤ Ξ^{cg⁴/4} functions ι". 

### `size_nPat_le`

 In exponents: the bit length of the number of terms is at most c·g⁴·log Ξ + 1. 

### `size_cnt_le`

 The bit length of the number of instances one level down. 

 ### The label length L one level down 

### `capSum_le_four`

 "We have c^row ≤ 2λ as before": the two numbers of bits of a piece add up to at most 4λ. 

### `K2L_le'`

 The display "K²L ≤ U + 2ζN + K² ≤ (ρ + 3ζ)N + (c/4)g⁴·log(2λ) + K²"
(`GeneralPieces.Chain.K_sq_L_le`), with log Ξ in place of log(2λ). 

 ### The crude bounds 

### `L_aux`

 L ≤ N + 1 in plain variables. 

### `L_le`

 "Crude bounds give L ≤ N + 1". 

### `B_aux`

 B' ≤ N + g²B₁ in plain variables; q = 2g/K. 

### `B'_le`

 "Crude bounds give B' ≤ N + g²B₁", with B₁ = gB + g²(2λ)^c. 

### `crude_aux`

 The crude bounds g(P + B₁) ≤ Ξ^{c+4} and K(L + B') ≤ Ξ^{c+5} in plain variables. 

### `KLB_le`

 "Crude bounds give K(L + B') ≤ Ξ^{c+5}". 

### `log_child`

 log(K(L + B')) ≤ (c + 5)·log Ξ. 

 ### The cost 𝒯 one level down 

### `T_aux`

 The display for 𝒯 in real variables: k2 = K², G4 = g⁴, L = log Ξ, lg = log(K(L + B')). 

 ### The budgets of size N/K 

### `c_le_K`

 c ≤ K_ℓ. 

### `c_lam_le`

 "cλ ≤ N/K". 

### `three_le`

 3 ≤ e_{ℓ+1}·K_ℓ: the term 3/K_ℓ of e_{ℓ+1} pays for 2^{2N/K + cλ} in the paper; here each of the
budgets of size N/K fits under e_{ℓ+1}·N by itself. 

### `st_le`

 The budget of the states of a merged part, times K: at most 3N. 

### `le_of_K_mul`

 If k·v ≤ 3N and 3 ≤ e'·k then v ≤ e'·N. 

### `tab_aux`

 The budget (K − 1)·L of a table one level down. 

 ### The exponent of Ξ 

### `half_const`

 "(c + 5)K² ≤ 2^{x₀}K² ≤ g⁴/2". 

### `exponent_le`

 "The exponent of Ξ is at most (c + C₄ + 1)g⁴ + ½C₀g⁴ ≤ C₀g⁴ by the choice of C₀", together with
e(ρ + 3ζ) ≤ e_{ℓ+1}: the number of instances, the bit length of the sum so far and the
exponent one level down. Here k2 = K², G4 = g⁴, L = log Ξ, lg = log(K(L + B')). 

### `step_real`

 All budgets of a step but the first, in real variables. 

 ### The induction 

### `step_le`

 "For the step from ℓ to ℓ + 1". 

### `main_le`

 "By induction on ℓ": the bound at every level, for all λ ≥ 1 and all B, cnt and z. 

### `stRate2`

 Theorem A, part (b), for the exponent of the pad, for every x₀ ≥ 18 with 2^x₀ ≥ c + 5, with C₀ =
6c + 17. 

---
{
  "module": "proof/networks/Eight/SecCrossing_PiecesAC.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_PiecesAC.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_PiecesAC.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces A_0, …, A_t: Lemma 2 (a) and (c)

The pieces are the coefficients in ∏_s (R(x_s,y_s,u_s,v_s) + T·C(x_s,y_s,u_s,v_s)) = Σ_i A_i T^i
(`Eight.prodRC`, `Eight.A`; the blocks are numbered s = 0, …, t − 1). This file proves:
* the product has degree at most t (`natDegree_prodRC_le`);
* «A_i is the sum, over the sets Q ⊆ [t] with |Q| = i, of the product that takes C at the blocks s ∈
  Q and R at the others» (`A_eq_sum_subsets`);
* Lemma 2(a): «Set T = 1 and use R + C = 2[x = v][y = u]; the appended zeros agree» (`a_sum`), and
  «|A_i| ≤ C(t,i) ≤ 2^t» (`abs_A_le_choose`, `a_abs`);
* Lemma 2(c): `c_row`, `c_col`, `crow_add_ccol_le` (≤ 11t), `three_mul_tOf_le` (t ≤ (λ+2)/3),
  `c_sum`.
`a_sum`, `a_abs`, `c_row`, `c_col`, `c_sum` have the types of the fields of `Eight.LemPieces`. The
sign rule `Eight.Signs` is a hypothesis of `a_sum` only; it is proved in
`SecCrossing_Identity.lean`. 

 ## A product of factors r_s + T·c_s 

### `natDegree_prod_linear_le`

 A product of factors r_s + T·c_s over s ∈ S has degree at most |S|. 

### `prod_linear_eq_sum`

 Multiplying out: ∏_{s ∈ S} (r_s + T·c_s) is the sum, over all Q ⊆ S, of T^|Q| times the product
that takes c_s for s ∈ Q and r_s for the other s. 

### `coeff_prod_linear`

 The coefficient of T^i in ∏_{s ∈ S} (r_s + T·c_s): the sum over the Q ⊆ S with |Q| = i. 

 ## The definition of the pieces 

### `natDegree_prodRC_le`

 «The t factors are polynomials in T of degree at most 1», so the product has degree at most t. 

### `A_eq_sum_subsets`

 A sentence of the proof of Lemma 2(b): «A_i is the sum, over the sets Q ⊆ [t] with |Q| = i, of
the product that takes C at the blocks s ∈ Q and R at the others.» The statement is this sentence of
the paper. 

 ## The appended zeros agree 

### `three_mul_tOf_le`

 t ≤ (λ+2)/3, written without a division: 3t ≤ λ + 2. 

### `bitAt_of_lt`

 A bit of the string itself. 

### `forall_blockAt_eq_iff`

 «The appended zeros agree»: two strings are equal exactly when their t blocks are equal. 

### `prod_cross_blocks`

 ∏_s [x_s = v_s][y_s = u_s] = [x = v][y = u]. 

 ## Lemma 2 (a) 

### `sum_A_eq_prod`

 «Set T = 1»: A_0 + … + A_t is the value of the product at T = 1, which is ∏_s (R + C). 

### `a_sum`

 **Lemma 2(a), first half**: A_0 + … + A_t = 2^t·[x = v][y = u]. «Set T = 1 and use R + C = 2[x =
v][y = u]; the appended zeros agree.» The proof is that of the paper. The hypothesis λ ≥ 1 is not
used. 

### `abs_A_le_choose`

 «|A_i| ≤ C(t,i)»: each of the C(t,i) products in `A_eq_sum_subsets` is −1, 0 or 1. 

### `a_abs`

 **Lemma 2(a), second half**: |A_i| ≤ 2^t, from «|A_i| ≤ C(t,i) ≤ 2^t». The proof is that of the
paper. The hypotheses λ ≥ 1 and i ≤ t are not used. 

 ## Lemma 2 (c) 

### `c_row`

 **Lemma 2(c)**: c_i^row ≤ 2λ. «The first two bounds hold by definition.» 

### `c_col`

 **Lemma 2(c)**: c_i^col ≤ 2λ. «The first two bounds hold by definition.» 

### `crow_add_ccol_le`

 «c_i^row + c_i^col ≤ (4t + 3i) + (7t − 3i) = 11t», for i ≤ t. 

### `eleven_tOf_le`

 «t ≤ (λ+2)/3, so 11t ≤ 11λ/3 + 8 = 4ρλ + 8.» 

### `c_sum`

 **Lemma 2(c)**: c_i^row + c_i^col ≤ 4ρλ + 8, where ρ = 11/12. The proof is that of the paper.
The hypothesis λ ≥ 1 is not used. 

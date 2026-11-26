---
{
  "module": "Zeta23/XiPrime/Transfer/Abstract.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer/Abstract.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer/Abstract.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/Transfer/Abstract.lean — ξ′ trace transfer [XF′ Lemma 5.1 + Lemma 6.1]: the
matrix-algebra and elementary-sum lemmas, with NO reference to ξ′, φ̂ or the prime side.

Contents (all over `Matrix n n ℂ`, `n` a Fintype, with RHLinalg.rtrace / frobSq):
  A. entrywise bounds ⇒ |tr| and ‖·‖_F² bounds; the Hadamard scaling ‖Δ∘Q‖_F ≤ (max|Δ|)‖Q‖_F.
  B. "Minkowski for a series of matrices": if the partial sums Σ_{r<R} S_r converge entrywise to D
     and Σ_r ‖S_r‖_F ≤ B then ‖D‖_F² ≤ B²  ([XF′ Lemma 6.1]: ‖M − Mᵀ‖_F ≤ Σ_r 0.38^r ‖Q^{(r)}‖_F).
  C. Abel summation with monotone bounded weights ([XF′ Lemma 6.1], trace part: the weights
     δ_k^r = (½ log(τ_k/T))^r are monotone in k).
  D. the lattice sum Σ_{l<d} min(1, ((k−l)h)⁻²)² ≤ 64(1 + 1/h)  ([XF′ Lemma 5.1]: "for fixed k,
     Σ_l min(1, |(l−k)h|⁻³) ≪ 1/h = L/2π").
  E. the three-matrix bookkeeping G = Mᵀ + D + E ⇒ the two inequalities of XiTraceTransfer with
     explicit losses.
-/
```

 ### A. Entrywise bounds 

### `frobSq_hadamard_le`

 the Hadamard (entrywise) product with a real matrix of entries bounded by θ scales ‖·‖_F² by
at most θ². 

 ### B. Minkowski for a series of matrices, via partial sums 

### `frobSq_le_of_tendsto_partialSums`

 If ‖S_r‖_F ≤ s_r with Σ_{r<R} s_r ≤ B for every R, and the partial sums Σ_{r<R} S_r converge to D
entrywise, then ‖D‖_F² ≤ B². 

 ### C. Abel summation with monotone bounded weights 

### `abs_sum_mul_le_of_monotone`

 If 0 ≤ w_k ≤ W is monotone and every partial sum |Σ_{k<K} q_k| (K ≤ d) is at most B, then
|Σ_{k<d} w_k q_k| ≤ 2WB. 

 ### D. The lattice sum  Σ_l min(1, ((k−l)h)⁻²)² ≪ 1/h 

### `sum_inv_affine_sq_le`

 telescoping: Σ_{m<R} 1/((m+1)h+1)² ≤ 1/h. 

### `sum_inv_affine_sq_le'`

 Σ_{m<R} 1/(m h+1)² ≤ 1 + 1/h. 

### `inv_max_one_sq_le`

 pointwise: 1/max(1, x²) ≤ 4/(|x|+1)². 

### `lattice_sum_le`

 **the lattice sum**: for h > 0 and any k < d,
Σ_{l<d} (1/max(1, ((k−l)h)²))² ≤ 8(1 + 1/h). 

 ### E. Three-matrix bookkeeping 

### `rtrace_sub_of_decomp`

 G = M + D + E ⇒ tr G − tr M = tr D + tr E. 

### `frobSq_le_of_decomp`

 G = M + D + E, ‖D‖_F² ≤ ε_D² N, ‖E‖_F² ≤ ε_E² N ⇒ with η := ε_D + ε_E,
‖G‖_F² ≤ (1 + η)‖M‖_F² + (η + η²) N   (from ‖G‖_F ≤ ‖M‖_F + η√N and 2‖M‖_F√N ≤ ‖M‖_F² + N). 

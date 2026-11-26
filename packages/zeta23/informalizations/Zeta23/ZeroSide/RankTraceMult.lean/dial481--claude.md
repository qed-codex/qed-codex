---
{
  "module": "Zeta23/ZeroSide/RankTraceMult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide/RankTraceMult.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide/RankTraceMult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ZeroSide/RankTraceMult.lean — the multiplicity-aware rank–trace inequality ("Lemma R").
For P = Σ_j m_j v_j v_j* (m_j ≥ 0, v_j ∈ 𝕜ⁿ, x_j := ‖v_j‖²), Q Hermitian with n₊(Q) ≤ b, and c > 0:
   ‖P+Q‖_F² ≥ c·tr P + Σ_j g_c(m_j x_j) + 2c·tr Q − c²·b,     g_c(x) := x² − cx − ((x−c)₊)²
(g_c convex, C¹, g_c(0) = 0, g_c ≥ −c²/4; so with at most r nonzero terms this contains lem:ranktrace).
Proof: the paper's skeleton (Q = Q₊ − Q₋, drop tr(PQ₊) ≥ 0, von Neumann, ‖Q₊‖² ≥ 2c trQ₊ − c²b — reused verbatim from the
imported rank_trace_ineq) with the termwise scalar step (p−n)² ≥ cp + g_c(p) − 2cn, followed by tr g_c(P) ≥ Σ_j g_c(m_jx_j):
(Schur) for PSD M, Σ_j g_c(M_jj) ≤ Σ_i g_c(μ_i(M)) by Jensen along the doubly stochastic |U_ji|², and (transfer) the nonzero spectra
of WWᴴ and WᴴW agree — implemented as Σ_i g(λ_i(WWᴴ)) = Σ_j g(μ_j(WᴴW)) for g(0)=0 via traces of powers + Lagrange interpolation.
-/
```

 ### (A) the scalar function g_c 

### `gc`

 g_c(x) = x² − cx − ((x−c)₊)²:  = x² − cx for x ≤ c,  = cx − c² for x ≥ c. 

### `affine_le_gc`

 the affine minorants: for t ∈ [0,c] and x ≥ 0, (2t − c)x − t² ≤ g_c(x). 

### `affine_eq_gc`

 … with equality at t = min(x, c). 

### `gc_sum_le`

 **Jensen for g_c** via the affine representation: weights w ≥ 0 with Σw = 1, points μ ≥ 0. 

### `sq_sub_ge_gc`

 the termwise step replacing the rank count:  (p − n)² ≥ c·p + g_c(p) − 2c·n  for p, n ≥ 0. 

 ### (B) the Schur step: the diagonal of a PSD matrix vs its spectrum, along the convex g_c 

### `re_diag_eq_sum_normSq_eigenvalues`

 diagonal entries through the spectral decomposition: re M_jj = Σ_i ‖U_ji‖²·μ_i. 

### `sum_gc_diag_le_sum_gc_eigenvalues`

 **Schur–Jensen for g_c**: Σ_j g_c(re M_jj) ≤ Σ_i g_c(μ_i(M)) for PSD M and c ≥ 0. 

 ### (C) transfer of the nonzero spectrum: Σ_i g(λ_i(W Wᴴ)) = Σ_j g(μ_j(Wᴴ W)) whenever g(0) = 0 

### `specMap_pow_succ`

 A^k = specMap (·^k) for k ≥ 1, hence rtrace (A^k) = Σ λ_i^k. 

### `trace_pow_succ_comm`

 tr((W Wᴴ)^{k+1}) = tr((Wᴴ W)^{k+1}). 

### `sum_eval_eigenvalues_comm`

 for any real polynomial q with q(0) = 0:  Σ_i q(λ_i(WWᴴ)) = Σ_j q(μ_j(WᴴW)). 

### `sum_eigenvalues_comm`

 **Transfer**: for any g : ℝ → ℝ with g 0 = 0,  Σ_i g(λ_i(WWᴴ)) = Σ_j g(μ_j(WᴴW))  (interpolate g on the joint spectrum ∪ {0}). 

 ### (D) Lemma R 

### `Wmat`

 the d×s matrix with columns √m_j · v_j. 

### `Pmat`

 P := W Wᴴ = Σ_j m_j v_j v_j*. 

### `xsq`

 x_j := ‖v_j‖² = Σ_a ‖v_j a‖². 

### `re_gram_diag`

 the Gram matrix M := Wᴴ W has diagonal m_j x_j. 

### `rtrace_Pmat`

 tr P = Σ_j m_j x_j. 

### `sum_gc_eigenvalues_ge`

 **tr g_c(P) ≥ Σ_j g_c(m_j x_j)** — Schur + transfer (this is where "per-zero integrality survives interaction"). 

### `rank_trace_mult`

 **Lemma R (multiplicity-aware rank–trace inequality).**  For P = Σ_j m_j v_jv_j* (m_j ≥ 0), Q Hermitian with n₊(Q) ≤ b,
and c > 0:   c·tr P + Σ_j g_c(m_j‖v_j‖²) + 2c·tr Q − c²·b ≤ ‖P + Q‖_F². 

 ### the k_c form (leak-free target) and the integer specializations 

### `kc`

 k_c(p) := c² − ((c−p)₊)²  (= 2cp − p² for p ≤ c, = c² for p ≥ c): nondecreasing, concave, k_c(0) = 0. 

### `rank_trace_mult_k`

 **Lemma R, k-form**:  2c·tr(P+Q) − ‖P+Q‖_F² ≤ Σ_j k_c(m_j‖v_j‖²) + c²·b. 

### `rank_trace_mult_k_le`

 … and the **leak-free** form: with ‖v_j‖² ≤ 1 the right side only increases when x_j ↦ 1. 

### `kc_two_one`

 integer values: k₂(0)=0, k₂(1)=3, k₂(m)=4 for m ≥ 2;  k₃(0)=0, k₃(1)=5, k₃(2)=8, k₃(m)=9 for m ≥ 3. 

 ### integer bookkeeping for the assembly (c = 2: simple zeros; c = 3: distinct zeros) 

### `sum_kc_two_nat`

 Σ_j k₂(m_j) = 3·#{m_j = 1} + 4·#{m_j ≥ 2} for positive integer multiplicities. 

### `sum_kc_three_nat`

 Σ_j k₃(m_j) = 5·#{m_j = 1} + 8·#{m_j = 2} + 9·#{m_j ≥ 3}. 

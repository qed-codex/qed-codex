---
{
  "module": "Zeta23/XiPrime/Coeff/DiagLaw.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/DiagLaw.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/DiagLaw.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/DiagLaw.lean — (H3), the diagonal law  [XF′ Lemma 7.1].

  ∀ ε > 0 ∃ T₀ ∀ T ≥ T₀ ∀ y ∈ [0, l(T)]:  | Σ_{N≤e^y} ‖C(N;Λ⋆(T))‖²/N − l(T)²·∫₀^{y/l} D₁ | ≤ ε·l(T)²
for any T-indexed parameter with Re Λ⋆(T) = l(T)/2 and |Im Λ⋆(T)| ≤ 1 (covers L_T = l/2 + iπ/4 and the real l/2).
Assembly (K-truncation): S = Σ_{k≤K} S_sf,k + R with
  S_sf,k  from Coeff/MainTerm (squarefree evaluation + k-fold Mertens induction),
  0 ≤ R ≤ non-squarefree part (Coeff/NonSquarefree, O_K(l)) + k-tail (Coeff/Upper + Coeff/Tail, ≤ ε·l²),
  ∫ D₁ = ∫ D1trunc K + tail (Certificate/D1).
-/
```

 ### the partition of the diagonal sum 

### `sfPart`

 the ω = k squarefree layer:  Σ_{N ≤ e^y, N squarefree, ω(N) = k} ‖C(N;Λ⋆)‖²/N. 

### `bPart`

 the remainder layer:  N not squarefree, or ω(N) > K. 

### `diag_split`

 S(y) = Σ_{k ≤ K} sfPart k + bPart K. 

### `sfPart_zero`

 the k = 0 layer is empty of mass: N squarefree with ω N = 0 means N = 1, and C(1) = 0. 

 ### the remainder layer is small:  bPart ≤ C_K·(1+l) + (tail)·l² 

### `not_squarefree_of_bLayer`

 N in the remainder layer with Λ^{∗m}(N) ≠ 0 for some m ≤ K is not squarefree. 

### `not_squarefree_of_bLayer_lam`

 N in the remainder layer (K ≥ 1) with Λ(N) ≠ 0 is not squarefree. 

### `bPart_le`

 **the remainder bound.**  For K ≥ 1 there are constants C_i such that for x := ‖Λ⋆‖⁻¹ with x·y ≤ 4, 32eK·x ≤ 1,
  we have the bound used downstream:
  bPart ≤ 2Cdef + 2y²·(TAIL_K(x,y,X) + Σ_{i<K} 2^{i+1}x^{2(i+1)}y^{i+1}·C_i(1+y)^i). 

 ### the squarefree layers ω = k ≥ 2:  sfPart k = l²·d_k·(y/l)^{2k+2} + O_k(1+l) 

### `dcoef`

 d_k := 4^k (k−1)!/((k+1)(2k)!)  — the coefficient of s^{2k+2} in ∫₀ˢ D_{1,k}  (k ≥ 1; d₁ = 1). 

### `pow_scaling_identity`

 the scaling identity  (4/l²)^n · y^{2n+2} = l² · 4^n · (y/l)^{2n+2}. 

### `squarefree_and_omega_one_iff`

 squarefree N with ω N = 1 is prime, and conversely. 

### `lamLogPow_offlayer_le`

 the non-(sf ∧ ω = k) part of Σ (Λlog)^{∗k}(N) log²N/N is ≤ y^{k+2}·Nsf k y. 

### `sfPart_asymp`

 **the layer ω = k ≥ 2.**  With a := (‖Λ⋆‖²)⁻¹ (so a ≤ 4/l² and |a^k − (4/l²)^k| ≤ k(4/l²)^{k+1} by Coeff/Param):
  |sfPart Λ⋆ k y − l²·d_k·(y/l)^{2k+2}| ≤ C_k·(1+l)  for 0 ≤ y ≤ l, l ≥ 2. 

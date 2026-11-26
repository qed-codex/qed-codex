---
{
  "module": "Zeta23/XiPrime/Coeff/LSeries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/LSeries.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/LSeries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/LSeries.lean — the L-series of the j-part of the ξ′ coefficients
(consumed by XiEF / [XF′ Thm 4.2]).

  C_J(N;Λ⋆) := Σ_{j<Ω N} Λ⋆^{-(j+1)} [(Λ·log) ∗ Λ^{∗j}](N)   (Basic.xiCoeffJ;  C = −Λ + C_J).
EXACT CONVOLUTION IDENTITY (finite telescoping in j, no analysis):   Λ⋆·C_J − Λ ∗ C_J = Λ·log.
Hence on any half plane of absolute convergence  L(C_J, s)·(Λ⋆ − A(s)) = B(s),  A = L(Λ), B = L(Λ·log), i.e.
  L(C_J, s) = B(s)/(Λ⋆ − A(s))      — the object E′/E ≈ B/(Λ⋆ − A) of the explicit formula.
Absolute bound on any line σ₀ > 1:  Σ_N ‖C_J(N)‖ N^{-σ₀} ≤ (4/(σ₀−1))·A(σ′)/‖Λ⋆‖  for ‖Λ⋆‖ ≥ R₀(σ₀) := 2A(σ′)+1,
σ′ := (σ₀+1)/2, A(σ) := Σ Λ(n) n^{-σ}  (log N ≤ N^ε/ε, F-majorant, the multiplicative weight N^{-σ′}); the line 5/4 (ξ′)
and the lines c ∈ [9/8, 5/4] (Z′) are instances.
-/
```

### `lamC`

 Λ as a complex sequence. 

### `lamLogC`

 Λ·log as a complex sequence. 

 ### the convolution identity  Λ⋆·C_J − Λ ∗ C_J = Λ·log 

### `lamLogConv_zero_apply`

 lamLogConv 0 = Λ·log. 

### `lam_mul_lamLogConv`

 Λ ∗ lamLogConv j = lamLogConv (j+1)  (commutativity of Dirichlet convolution). 

### `lamC_conv_xiCoeffJ`

 the Dirichlet convolution (Λ ∗ C_J)(N), written through the fixed j-range Ω N. 

### `xiCoeffJ_identity`

 **the convolution identity**, pointwise:  Λ⋆·C_J(N) − (Λ ∗ C_J)(N) = Λ(N) log N  (Λ⋆ ≠ 0). 

### `lamLogC_eq`

 the identity as an equality of sequences:  Λ·log = Λ⋆•C_J − Λ ∗ C_J. 

 ### helpers 

### `norm_xiCoeffJ_rpow_nonneg`

 the sequence  N ↦ ‖C_J(N)‖ N^{-5/4}  is nonnegative and vanishes at 0. 

### `norm_term_xiCoeffJ`

 ‖term f s n‖ for our sequences: ‖C_J(N)‖ N^{-Re s}. 

 ### lines Re s ≥ σ₀ > 1:  ε := (σ₀−1)/2,  log N ≤ N^ε/ε,  weight N^{−σ′}, σ′ = σ₀ − ε > 1 

### `Asig`

 A(σ) := Σ' Λ(n) n^{−σ}. 

### `sigAux`

 the auxiliary exponent σ′ := (σ₀+1)/2 ∈ (1, σ₀) and ε := (σ₀−1)/2. 

### `R0sig`

 the threshold radius R₀(σ₀) := 2·A(σ′) + 1. 

### `sum_norm_xiCoeffJ_rpow_le_gen`

 partial sums on the line σ₀:  Σ_{N≤X} ‖C_J(N)‖ N^{−σ₀} ≤ (4/(σ₀−1))·A(σ′)/‖Λ⋆‖. 

### `summable_norm_xiCoeffJ_gen`

 summability on the line σ₀. 

### `norm_xiCoeffJ_tsum_le_of_gt_one`

 **(C2) on any line σ₀ > 1.** 

### `summable_norm_xiCoeffJ_rpow_gen`

 summability of ‖C_J‖·N^{−σ} for σ ≥ σ₀. 

### `norm_LSeries_lamC_le_gen`

 ‖A(s)‖ ≤ A(σ′) for Re s ≥ σ₀. 

### `LSeries_xiCoeffJ_of_gt_one`

 **(C1) the closed form on any line σ₀ > 1**:  L(C_J, s) = B(s)/(Λ⋆ − A(s))  for σ₀ ≤ Re s, ‖Λ⋆‖ ≥ R₀(σ₀). 

 ### the line Re s = 5/4 (the ξ′ explicit formula's contour): instances of the general statements 

### `norm_xiCoeffJ_tsum_le`

 **(C2) absolute bound** at 5/4:  Σ' ‖C_J(N;Λ⋆)‖ N^{-5/4} ≤ C/‖Λ⋆‖ for ‖Λ⋆‖ ≥ R₀ (with summability). 

### `LSeries_xiCoeffJ`

 **(C1) the closed form** at 5/4:  L(C_J, s) = B(s)/(Λ⋆ − A(s))  for 5/4 ≤ Re s and ‖Λ⋆‖ ≥ R₀. 

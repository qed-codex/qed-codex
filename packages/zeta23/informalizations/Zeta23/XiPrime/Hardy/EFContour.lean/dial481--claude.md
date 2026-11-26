---
{
  "module": "Zeta23/XiPrime/Hardy/EFContour.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFContour.lean — the two full-line contour identities of the W explicit formula
([XF′ Prop 9.1, Thm 9.2(a), (Z4)]).

  lminus_line_identity : (1/2π) ∫ [H(c+it) + H(1−c−it)]·(Lfn − L₂)(c+it) dt = ½ (H(0) + H(1)),
  w_full_line_identity : (1/2π) ∫ [H(c+it) + H(1−c−it)]·(L₂ + W′/W)(c+it) dt
                           = Σ'_{ρ ∈ wZeros} m_ρ H(ρ) + Σ_{ρ ∈ lowZerosW c t₀} ord_ρ(W) H(ρ) − (3/2)(H(0) + H(1)),
for 1 < c ≤ 5/4, H = WeilEF.Hfn k (k ∈ C²_c).  Pipeline: EFContour/Rectangle.lean (the identities at a fixed height:
pole-free argument principle for (Γℝ)⁻¹, (Γℝ)⁻¹∘(1−·), s(s−1), s(s−1)², Wreg) → EFContour/Limit.lean (the
integrand-generic R → ∞ passage) with: heights/horizontal bounds from Hardy/GoodHeightsW.lean (W) or from
the explicit Γℝ′/Γℝ log bounds (L₋); the fold symmetries L₋(1−s) = −L₋(s), F_𝒵(1−s) = −F_𝒵(s); summability of the zero
sum from hR.local_count via WeilEF.EF_zero_sum_summable_gen; and FullLine.zero_sum_limit_of for the windows.
The low zeros (|Im ρ| < t₀, 1−c < Re ρ < c, ρ ∉ {0,1}; REAL zeros of W included) form a fixed finite set.
-/
```

 ## §1. L₋ := Lfn − L₂ through G = (Γℝ)⁻¹; symmetry; analyticity; bounds 

### `logDeriv_invGammaℝ_comp_one_sub`

 logDeriv (G∘(1−·)) s = −(G′/G)(1−s). 

### `L2_eq_G`

 L₂ = −½[(G′/G)(s) + (G′/G)(1−s)] wherever Γℝ(s), Γℝ(1−s) ≠ 0. 

### `Lminus_eq_G`

 L₋ = −½(G′/G)(s) + ½(G′/G)(1−s) + 1/s + 1/(s−1). 

### `Lminus_one_sub`

 **L₋ is odd under s ↦ 1−s** (on the strip off the poles). 

### `norm_logDeriv_Gammaℝ_le_strip`

 ‖Γℝ′/Γℝ(u)‖ ≤ log(|Im u|+3) + 6 on −1/4 ≤ Re u ≤ 2, |Im u| ≥ 2 (shift once when Re u ≤ 0). 

### `norm_Lminus_le`

 horizontal bound for L₋: ‖(Lfn − L₂)(s)‖ ≤ log(|Im s|+3) + 7 on 1−c ≤ Re s ≤ c, |Im s| ≥ 2. 

 ## §2. The L₋ line identity 

### `lminus_line_identity`

 **(1/2π) ∫ [H(c+it) + H(1−c−it)] · (Lfn − L₂)(c+it) dt = ½(H(0) + H(1))**, 1 < c ≤ 5/4. 

 ## §3. The low zeros of W and the W full-line identity 

### `lowZerosSet`

 the set of low zeros of W inside the contour strip: W(ρ) = 0, ρ ∉ {0,1}, |Im ρ| < t₀, 1−c < Re ρ < c
(REAL zeros included). 

### `lowZerosW`

 the low zeros of W as a Finset (∅ if infinite — it is finite in every use, see finite_lowZerosSet). 

### `finite_lowZerosSet`

 the low-zero set is finite for every 1 < c ≤ 5/4 and every t₀: it lies in the zero set of the analytic Wreg on the
closed rectangle [1−c, c] × [−T, T] (T = max t₀ 1), and Wreg 0 = ¼ ≠ 0. 

### `exists_heightsW`

 re-indexing good heights into a sequence R_j ∈ [j+j₁, j+j₁+1], j₁ ≥ 1, R_j > t₀. 

### `w_full_line_identity`

 **The W full-line identity** [XF′ Prop 9.1 / (Z4)]. 

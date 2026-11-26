---
{
  "module": "Zeta23/XiPrime/Hardy/EFExpansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFExpansion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFExpansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFExpansion.lean — L₂ on the line Re s = c (9/8 ≤ c ≤ 5/4), the freeze, and the uniform line bounds
for the W explicit formula (template: Zeta23/XiPrime/ExplicitFormula/Expansion.lean §§3–7 with L ↦ L₂,
L⋆ ↦ L₂⋆ := ½log(τ/2π) (real: no phase), 5/4 ↦ c).

 X1 norm_L2_sub_L2star_self_le : ‖L₂(c+it) − L₂⋆(t)‖ ≤ C/t (t ≥ 2)  — one-point Stirling: L₂ = ½[Γℝ′/Γℝ(s) +
    Γℝ′/Γℝ(1−s)], the second shifted to 3−s (Hardy.logDeriv_Gammaℝ_shift); ψ(w) = log w − 1/(2w) + O(Im w)⁻² at
    w₁ = s/2 and w₂ = (3−s)/2, whose logarithms have phases → +π/2, −π/2 that cancel, leaving ½log(t/2) − ½log π.
 X2 norm_deriv_L2_le;  X3 norm_L2_sub_L2star_le, norm_L2_ge;  X4 norm_Afn_le_line, norm_Bfn_le_line;
 X5 freeze_on_line_W;  X6 frozen_uniform_W;  X7 derivE2_div_E2_uniform (+ continuity, conj);  X8 the F_𝒵 / E₂ line bounds.
-/
```

 ## A. the line Re s = c 

 ## X4. Uniform bounds for A and B on the line 

 ## X1. One-point Stirling for L₂ on the line 

### `norm_log_sub_le_gen`

 the complex logarithm near the positive imaginary axis, general abscissa 0 < a ≤ 1:
‖log(a + i t/2) − (log(t/2) + iπ/2)‖ ≤ 6/t for t ≥ 2. 

### `norm_log_sub_le_gen_neg`

 the twin near the NEGATIVE imaginary axis: ‖log(a − i t/2) − (log(t/2) − iπ/2)‖ ≤ 6/t. 

### `L2_eq_digamma_shift`

 the explicit form of L₂ on Re s ∈ (1, 3/2), off the real axis:
L₂(s) = −log π/2 + ¼ψ(s/2) + ¼ψ((3−s)/2) − 1/(2(1−s)). 

### `norm_L2_sub_L2star_self_le'`

 **X1. one-point Stirling for L₂**: ‖L₂(c+it) − L₂⋆(t)‖ ≤ 12/t for t ≥ 2  (L₂⋆(t) = ½log(t/2π), real). 

### `norm_L2_sub_L2star_self_le`

 X1 in ∃-form: ‖L₂(c+it) − L₂⋆(t)‖ ≤ C/t for t ≥ 2. 

 ## X2. L₂′ on the line 

### `L2D`

 the explicit digamma form of L₂ (right side of L2_eq_digamma_shift), for differentiation. 

### `norm_deriv_L2_le'`

 **X2. L₂′ on the line**: ‖L₂′(c+it)‖ ≤ 4/|t| for |t| ≥ 2. 

 ## X3. L₂ against a frozen L₂⋆(τ), and the lower bound for ‖L₂‖ 

### `norm_L2star_sub_L2star_le`

 ‖L₂⋆(t) − L₂⋆(τ)‖ = ½|log t − log τ| ≤ |t−τ|/(2 min t τ). 

### `norm_L2_sub_L2star_le'`

 **X3a. L₂ against a frozen L₂⋆(τ)**: ‖L₂(c+it) − L₂⋆(τ)‖ ≤ (|t−τ| + 24)/(2 min t τ) for t, τ ≥ 2. 

### `norm_L2star_ge`

 ‖L₂⋆(τ)‖ ≥ ½log τ − 1 for τ > 0. 

### `norm_L2_ge_pos`

 ‖L₂(c+it)‖ ≥ ½log t − 7 for t ≥ 2. 

### `norm_L2_ge'`

 **X3b.** ‖L₂(c+it)‖ ≥ ½log|t| − 7 for |t| ≥ 2 (t < 0 by conjugation). 

 ## The archimedean line data for W: (c, L₂, L₂⋆) — instance of ExplicitFormula/Expansion §G 

### `norm_L2_line`

 ‖L₂(c+it)‖ ≤ M·log(2+|t|) for all real t. 

### `archLineData_L2`

 **ArchLineData for W** on 9/8 ≤ c ≤ 5/4: Λ = L₂, Λ⋆(τ) = (L2star τ : ℂ); fields from X1–X4 above. 

 ## X5–X6. The freeze on the line 

### `derivE2_div_E2_eq_line`

 E₂′/E₂ in the (L₂′+B)/(L₂−A) form on the line. 

### `freeze_on_line_W`

 **X5. the freezing estimate on the line Re s = c** [XF′ Lemma 2.4 for W]. 

### `frozen_uniform_W`

 **X6.** the frozen object is uniformly small on the line: ‖B/(L₂⋆(τ) − A(c+it))‖ ≤ 4B₀/log T. 

 ## X7. The uniform bound for E₂′/E₂ on the line (given W ≠ 0 there), continuity, conjugation 

### `continuous_derivE2_div_E2_line`

 continuity of t ↦ E₂′/E₂(c+it), given W ≠ 0 on the line. 

### `derivE2_div_E2_conj`

 conjugation: E₂′/E₂(s̄) = conj(E₂′/E₂(s)) for s on the line with Im s ≠ 0 and W(s) ≠ 0. 

### `derivE2_div_E2_uniform`

 **X7. uniform bound**: given W ≠ 0 on Re s = c, ‖E₂′/E₂(c+it)‖ ≤ C_E for every real t. 

### `derivE2_div_E2_conj_symm`

 The conjugation symmetry in the `dE2` spelling: conj (E₂′/E₂(c − it)) = E₂′/E₂(c + it). 

 ## X8. The line bounds and continuity for E₂ and F_𝒵 = L₂ + W′/W 

### `norm_E2fn_line`

 **X8a.** ‖E₂(c+it)‖ ≤ M log(2+|t|) and t ↦ E₂(c+it) is continuous. 

### `norm_FZ_line`

 **X8b. the line bound for F_𝒵 = L₂ + W′/W** (given W ≠ 0 on the line). 

 ## Packaged in the field order of `E2LineFacts` / `FreezeFactsW` 

---
{
  "module": "Zeta23/XiPrime/Certificate/D1.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Certificate/D1.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Certificate/D1.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Certificate/D1.lean — analytic facts about the diagonal density D₁.

D₁(s) = s − 4s² + Σ_{k≥0} D1coeff k · s^{2k+3}
(Zeta23/XiPrime/Defs.lean §4), D1coeff k = 2·4^{k+1}·k!/(2k+2)!  (= the paper's a_{k+1}, Lemma 7.1).
This file proves:
  * D1coeff_succ      — the ratio  D1coeff (k+1) / D1coeff k = 2(k+1)/((k+2)(2k+3))  (↓ in k, ≤ 1/3);
  * summable_D1coeff_mul_pow — the series converges for every real s (so Defs.D1 is an honest sum);
  * continuous_D1     — D₁ is continuous on ℝ;
  * D1_eq_trunc_add_tail, D1trunc_le_D1 (s ≥ 0), D1_nonneg (s ≥ 0);
  * eps9 := 1024/2990212875 = D1coeff 9 · 231/211 and the CERTIFIED TAIL
      D1 s ≤ D1trunc 9 s + eps9   for s ∈ [0,1]
    (paper Thm 8.2 "Certified constants": ε₉ ≤ 3.43·10⁻⁷; here eps9 < 3.425·10⁻⁷), geometric
    comparison with ratio 20/231 = D1coeff 10 / D1coeff 9.  This is the bound that keeps the Lean
    constant on the CORRECT side: truncating D₁ without the tail would make 1/c smaller and the stated
    proportion larger than the paper proves.
-/
```

 ### the coefficients 

### `D1coeff_succ`

 the ratio recursion: D1coeff (k+1) = D1coeff k · 2(k+1)/((k+2)(2k+3)). 

### `D1coeff_succ_le_third`

 the ratio is at most 1/3 (its value at k = 0). 

### `D1coeff_succ_le`

 for k ≥ 9 the ratio is at most 20/231 (its value at k = 9; the ratio decreases in k). 

### `D1coeff_tail_le`

 geometric domination of the tail coefficients. 

### `D1coeff_le`

 the factorial comparison D1coeff k ≤ 2·4^{k+1}/(k+1)!  (from k!·(k+2)! ∣ (2k+2)!). 

 ### summability and continuity of the series 

### `D1term`

 the general term of the D₁ series. 

### `summable_D1coeff_mul_pow`

 the majorant Σ_k D1coeff k · R^{2k+3} converges (comparison with 2R·Σ (4R²)^{k+1}/(k+1)!). 

### `continuousOn_D1_Icc`

 D₁ is continuous on every [−R, R], hence on ℝ. 

 ### truncation and tail 

### `D1_eq_trunc_add_tail`

 D₁ = (its K-truncation) + (the tail from K on). 

### `D1trunc_le_D1`

 truncations UNDER-estimate D₁ on [0, ∞). 

### `D1trunc_one`

 D1trunc 1 s = s(1 − 2s)². 

### `D1_nonneg`

 D₁ ≥ 0 on [0, ∞)  (D₁ = s(1−2s)² + a series of nonnegative terms). 

### `eps9`

 the certified tail constant ε₉ := D1coeff 9 · Σ_j (20/231)^j = (1024/3273645375)·(231/211). 

### `eps9_lt`

 ε₉ < 3.425·10⁻⁷ (the paper quotes ε₉ ≤ 3.43·10⁻⁷). 

### `D1tail9_le`

 on [0,1] the tail from k = 9 on is at most ε₉. 

### `D1_le_D1trunc9_add`

 **the certified two-sided control of D₁ on [0,1]:**  D1trunc 9 ≤ D₁ ≤ D1trunc 9 + ε₉. 

### `continuous_D1trunc`

 D1trunc K is a polynomial, hence continuous. 

 ### exports for the diagonal law (Coeff.lean H3) 

### `tendsto_D1coeff_tail`

 the coefficient tail Σ_{k ≥ K} D1coeff k → 0. 

### `D1tail_le_coeff_tail`

 on [0,1] the function tail is dominated by the coefficient tail, uniformly in s. 

### `abs_D1_sub_D1trunc_le`

 |D₁ − D1trunc K| ≤ Σ_{k≥K} D1coeff k on [0,1] (uniform truncation error, → 0 as K → ∞). 

### `integral_D1term`

 ∫₀ˢ D1term k = D1coeff k · s^{2k+4}/(2k+4). 

### `integral_D1trunc`

 termwise integration of the truncation (finite sum; no convergence issues). 

### `abs_integral_D1_sub_le`

 **uniform diagonal-law main term:** for s ∈ [0,1],
|∫₀ˢ D₁ − ∫₀ˢ D1trunc K| ≤ Σ_{k≥K} D1coeff k  (→ 0), with ∫₀ˢ D1trunc K explicit above. 

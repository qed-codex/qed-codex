---
{
  "module": "Zeta23/XiPrime/Coeff/MainTerm/Asymp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/MainTerm/Asymp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/MainTerm/Asymp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/MainTerm/Asymp.lean — the k-fold Mertens induction.

  Tk k u := Σ_{N ≤ e^u} (Λ·log)^{∗k}(N)/N,      Wk k u := Σ_{N ≤ e^u} (Λ·log)^{∗k}(N)·log²N/N.
Results:
  Tk_zero, Tk_succ (the recursion from PowerSums.Sdiv_mul),
  Tk_asymp : |Tk k u − u^{2k}/(2k)!| ≤ C_k (1+u)^{2k−1}            (u ≥ 0),
  Wk_asymp : |Wk k u − k/((k+1)(2k)!)·u^{2k+2}| ≤ C_k (1+u)^{2k+1}  (u ≥ 0, k ≥ 1).
The only analytic input is Coeff/Abel.mertens_step (Mertens' first theorem + Abel summation); Wk is
obtained from Tk by one more Abel summation in N with weight log²N.  All constants are free except the
leading rational k/((k+1)(2k)!) of Wk_asymp, which is exact ([XF′ Lemma 7.1(i)]: it produces D_{1,k}).
-/
```

 ### definitions and the recursion 

### `Tk`

 Tk k u := Σ_{N ≤ e^u} (Λ·log)^{∗k}(N)/N. 

### `Wk`

 Wk k u := Σ_{N ≤ e^u} (Λ·log)^{∗k}(N)·(log N)²/N. 

### `sum_lam_log_div_le`

 Σ_{d ≤ e^u} Λ(d) log d / d ≤ u·(u + K). 

### `sum_vonMangoldt_div_mul_log_pow`

 **the one-variable Mertens sums**  Σ_{n ≤ e^u} Λ(n)/n·(log n)^j = u^{j+1}/(j+1) + O((1+u)^j)
(mertens_step with f(v) = v^j; j = 1 is Tk 1, and j = 1, 2, 3 are the three sums of the k = 1 (prime) term). 

 ### the Mertens induction for Tk 

### `integral_mul_sub_pow`

 the polynomial integral ∫₀ᵘ v (u − v)^N dv = u^{N+2}/((N+1)(N+2)). 

### `Tk_step`

 **The induction step.**  From |Tk k v − v^N/N!| ≤ C(1+v)^n (v ≥ 0, N = n+1) deduce
|Tk (k+1) u − u^{N+2}/(N+2)!| ≤ (K(N+1) + C(1+K))·(1+u)^{N+1}  (u ≥ 0). 

### `Tk_one_asymp`

 base case: |Tk 1 u − u²/2| ≤ 2K(1+u). 

### `Tk_asymp_succ`

 the induction, in the subtraction-free form k = j+1. 

### `Tk_asymp`

 **B2.**  |Tk k u − u^{2k}/(2k)!| ≤ C_k (1+u)^{2k−1} for u ≥ 0. 

### `Tk_asymp'`

 Tk_asymp with a nonnegative constant. 

 ### Wk from Tk by Abel summation with weight log² 

### `Tk_log_eq_sum_Icc`

 Tk k (log t) as the partial sum that Abel summation produces. 

### `Wk_asymp`

 **B3.**  |Wk k u − k/((k+1)(2k)!)·u^{2k+2}| ≤ C_k (1+u)^{2k+1} for u ≥ 0 (k ≥ 1). 

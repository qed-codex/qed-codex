---
{
  "module": "Zeta23/XiPrime/Coeff/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/Basic.lean — pointwise algebra of the ξ′ coefficients C(N; Λ⋆).

The definitions  lamLogConv j := (Λ·log) ∗ Λ^{∗j}  and
  xiCoeff Λ⋆ N := −Λ(N) + Σ_{j < Ω N} Λ⋆^{-(j+1)} · lamLogConv j N
live in Zeta23/XiPrime/Defs.lean.  Here: nonnegativity / support / size of the Dirichlet
powers Λ^{∗m} (the ring power in ArithmeticFunction ℝ IS the Dirichlet power), the vanishing of the j-sum
beyond Ω(N), C(0) = C(1) = 0, conjugation symmetry, and the basic majorant
  ‖C(N;Λ⋆)‖ ≤ Λ(N) + log N · Σ_{1 ≤ m ≤ Ω N} ‖Λ⋆‖^{-m} Λ^{∗m}(N)        (lamLogConv j N ≤ log N · Λ^{∗(j+1)} N).
No analysis in this file.
-/
```

 ## §0. Summing a Dirichlet convolution over N ≤ X

  Σ_{N ≤ X} (f ∗ g)(N) · h(N)  =  Σ_{d ≤ X} f(d) · Σ_{e ≤ X/d} g(e) · h(d·e),  and for nonnegative f, g and a nonnegative
  sub-multiplicative weight w:  Σ_{N≤X}(f∗g)(N)w(N) ≤ (Σ f w)(Σ g w),  Σ_{N≤X} f^{∗(m+1)}(N)w(N) ≤ (Σ f w)^{m+1}. 

### `sum_Ioc_mul_apply`

 Σ_{N≤X} (f∗g)(N)·h(N) = Σ_{d≤X} f(d) Σ_{e≤X/d} g(e) h(de). 

### `sum_Ioc_mul_apply'`

 Same with the factors swapped: Σ_{N≤X} (f∗g)(N) h(N) = Σ_{e≤X} g(e) Σ_{d≤X/e} f(d) h(de). 

### `SubmultWeight`

 A nonnegative weight with w(de) ≤ w(d)·w(e) (e.g. N ↦ N^{-σ}, or N ↦ g(N)/N with g submultiplicative). 

### `sum_Ioc_mul_apply_le`

 product bound: Σ_{N≤X} (f∗g)(N) w(N) ≤ (Σ_{d≤X} f(d)w(d))·(Σ_{e≤X} g(e)w(e)) for f, g, w ≥ 0, w submult. 

### `mul_apply_nonneg`

 f ≥ 0 and g ≥ 0 pointwise ⇒ f ∗ g ≥ 0 pointwise. 

### `pow_apply_nonneg`

 f ≥ 0 pointwise ⇒ every Dirichlet power f^{∗m} ≥ 0 pointwise. 

### `sum_Ioc_pow_apply_le`

 power bound: Σ_{N≤X} f^{∗(m+1)}(N) w(N) ≤ (Σ_{n≤X} f(n)w(n))^{m+1}. 

 ### Λ, Λ·log and the Dirichlet powers Λ^{∗m} 

### `lamLog`

 (Λ·log)(n) = Λ(n)·log n  (the first factor of lamLogConv). 

### `one_le_cardFactors_of_vonMangoldt_ne_zero`

 Λ(b) ≠ 0 forces b > 1, hence Ω b ≥ 1. 

### `cardFactors_of_mem_divisorsAntidiagonal`

 in a divisor pair (a,b) of n, Ω n = Ω a + Ω b. 

### `lamPow_eq_zero_of_cardFactors_lt`

 Λ^{∗m}(n) = 0 unless Ω(n) ≥ m  (each Λ-factor uses up one prime factor counted with multiplicity). 

### `lamLogConv_eq_zero_of_le`

 lamLogConv j n = 0 unless Ω(n) ≥ j+1. 

### `lamPow_le_log_pow`

 Λ^{∗m}(n) ≤ (log n)^m : induct, using Σ_{d | n} Λ(d) = log n and log a ≤ log n for a | n. 

### `lamLogConv_le`

 lamLogConv j n ≤ log n · Λ^{∗(j+1)}(n)  (bound log a ≤ log n on the (Λ·log)-factor). 

### `lamLogPow_le`

 (Λ·log)^{∗k}(n) ≤ (log n)^k · Λ^{∗k}(n)  (each log q_i ≤ log n). 

 ### C(N; Λ⋆): trivial values, range-independence, conjugation, basic majorant 

### `xiCoeff_eq_sum_range_of_le`

 the j-sum may be taken over any range ⊇ range (Ω N): the extra terms vanish. 

### `xiCoeff_conj`

 C(N; conj Λ⋆) = conj C(N; Λ⋆)  (C is a real polynomial in Λ⋆⁻¹). 

### `xiCoeffJ`

 the "j-part" of C:  C_J(N;Λ⋆) := Σ_{j<Ω N} Λ⋆^{-(j+1)}·lamLogConv j N, so that C = −Λ + C_J.
This is the coefficient sequence met by the explicit formula: its L-series is B/(Λ⋆ − A). 

### `norm_xiCoeffJ_le_aux`

 ‖C_J(N;Λ⋆)‖ ≤ log N · F_{‖Λ⋆‖⁻¹}(N)  (proved below, after Fmaj). 

### `Fmaj`

 the majorant  F_x(N) := Σ_{m=1}^{Ω N} x^m Λ^{∗m}(N)  (x = ‖Λ⋆‖⁻¹); indexing m = i+1, i < Ω N. 

### `Fmaj_eq_sum_range_of_le`

 like xiCoeff, Fmaj may be summed over any range ⊇ range (Ω N). 

### `norm_xiCoeffJ_le`

 ‖C_J(N;Λ⋆)‖ ≤ log N · F_{‖Λ⋆‖⁻¹}(N). 

### `norm_xiCoeff_le`

 ‖C(N;Λ⋆)‖ ≤ Λ(N) + log N · F_{‖Λ⋆‖⁻¹}(N). 

### `norm_xiCoeff_sq_le`

 squared form used by the diagonal sums: ‖C‖² ≤ 2Λ(N)² + 2 log²N · F_x(N)². 

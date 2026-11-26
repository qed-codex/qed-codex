---
{
  "module": "Zeta23/XiPrime/Coeff/NonSquarefree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/NonSquarefree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/NonSquarefree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/NonSquarefree.lean — "each repeated prime costs a factor 1/l"  [XF′ Lemma 7.1 (ii)].

For each fixed m:  Σ_{N ≤ e^u, N not squarefree} Λ^{∗m}(N)/N ≤ C_m·(u + mK + 1)^{m−1}   — one power of u less than
the full sum Σ_{N≤e^u}Λ^{∗m}(N)/N ≍ u^m/m! (Coeff/PowerSums).  Route: a PREDICATED version of the swap recursion,
  Σ_{N≤X, P N}(g∗f)(N)/N ≤ Σ_{d≤X, Q d} g(d)/d·Sdiv f(·) + Σ_{d≤X} g(d)/d·Σ_{e, R d e} f(e)/e    whenever P(de) ⇒ Q d ∨ R d e,
applied with P = ¬Squarefree:  de not squarefree ⇒ d not prime ∨ e not squarefree ∨ (d prime ∧ d ∣ e), and with
P = (p ∣ ·).  The only arithmetic input beyond Mertens is the tree's proper-prime-power defect bound
Cheb.defect_bounded_explicit:  Σ_{n≤x} Λ(n)(log n − Λ(n))/n ≤ 1537, which dominates Σ_{n not prime}Λ(n)/n,
Σ_{n not sqfree}Λ(n)²/n, Σ_{n not sqfree}Λ(n)log n/n and Σ_p log²p/p².
-/
```

 ### predicated sums and the predicated recursion 

### `SdivP`

 Σ_{N ≤ e^u, P N} f(N)/N. 

### `SdivP_eq_sum_ite`

 SdivP as an unrestricted sum with an indicator. 

### `SdivP_mul_le`

 **the predicated recursion.**  If P(de) (with g d ≠ 0 ≠ f e) forces Q d ∨ R d e, then
  Σ_{N≤e^u, P N}(g∗f)(N)/N ≤ Σ_{d ≤ e^u, Q d} g(d)/d · Sdiv f (u − log d) + Σ_{d ≤ e^u} g(d)/d · SdivP f (R d) (u − log d). 

 ### the arithmetic inputs: proper prime powers are sparse 

### `Cdef`

 the defect constant. 

### `exists_prime_pow_of_vonMangoldt_ne_zero`

 structure of n with Λ n ≠ 0: n = p^k, p prime, k ≥ 1, Λ n = log p, log n = k log p. 

### `vonMangoldt_le_log_sub_of_not_prime`

 if Λ n ≠ 0 and n is not prime, then log n − Λ n ≥ Λ n ≥ log 2  (n = p^k with k ≥ 2). 

### `not_prime_of_not_squarefree`

 a non-squarefree n with Λ n ≠ 0 is not prime. 

### `sum_not_prime_vonMangoldt_div_le`

 Σ_{n ≤ x, n not prime} Λ(n)/n ≤ Cdef / log 2. 

### `sum_not_squarefree_vonMangoldt_sq_div_le`

 Σ_{n ≤ x, n not squarefree} Λ(n)²/n ≤ Cdef. 

### `sum_not_squarefree_lamLog_div_le`

 Σ_{n ≤ x, n not squarefree} Λ(n) log n/n ≤ 2·Cdef. 

### `sum_prime_log_sq_div_sq_le`

 Σ_{p ≤ X prime} log²p/p² ≤ Cdef  (the a = 2 slice of the defect sum at X²). 

### `sum_dvd_vonMangoldt_div_le`

 Σ_{d ≤ X, p ∣ d} Λ(d)/d ≤ 2 log p / p  for p prime (d ranges over the powers of p). 

 ### sums over multiples of a prime:  D m p u := Σ_{N ≤ e^u, p ∣ N} Λ^{∗m}(N)/N 

### `Dsum`

 Σ_{N≤e^u, p∣N} Λ^{∗m}(N)/N. 

### `Gb`

 the bracket G := u + (m+1)K + 1 used in all the inductions (≥ 1, ≥ u + K, monotone in m and u). 

### `Dsum_le`

 **D_{m+1}(p,u) ≤ (m+1)·(2 log p/p)·Gb m u ^ m.** 

 ### the non-squarefree sums:  Nsf m u := Σ_{N ≤ e^u, N not squarefree} Λ^{∗m}(N)/N 

### `Nsf`

 Σ_{N≤e^u, ¬Squarefree N} Λ^{∗m}(N)/N. 

### `split_not_squarefree`

 the splitting: d·e not squarefree, Λ d ≠ 0 ⇒ d not prime ∨ e not squarefree ∨ (d prime ∧ d ∣ e). 

### `Nsf_le`

 **Nsf (m+1) u ≤ C_m · Gb m u ^ m**, with an (inexplicit) constant depending on m only. 

### `Nsf_le_poly`

 polynomial form: for each m ≥ 1 there is C with  Nsf m u ≤ C·(1+u)^{m−1}  (u ≥ 0). 

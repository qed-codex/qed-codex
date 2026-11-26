---
{
  "module": "Zeta23/XiPrime/Coeff/Upper.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Upper.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Upper.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/Upper.lean — the uniform upper bound for the ξ′ diagonal sum and (H1), (H2).

[XF′ Lemma 7.1 (iii)] in the crude form the prime side consumes ([XF′ Remark 7.2]):
  S(u) := Σ_{N ≤ e^u} ‖C(N;Λ⋆)‖²/N ≤ C·(1+u)²      for 0 ≤ u with ‖Λ⋆‖⁻¹·u ≤ 4 and ‖Λ⋆‖ ≥ 32eK   (K = log 4 + 4),
whence for a T-indexed parameter Λ⋆(T) with ‖Λ⋆(T)‖ ≥ l(T)/2:
  (H2) Σ_{N≤x} ‖C(N;Λ⋆(T))‖² ≤ C·x·l(T)²,   (H1) Σ_{N≤x} ‖C(N;Λ⋆(T))‖/√N ≤ C·√x·l(T)     (2 ≤ x ≤ e^{l(T)}, T ≥ T₀).
Route (no asymptotics): ‖C‖² ≤ 2Λ² + 2log²N·F²  (Basic), F(N)² ≤ Σ_m 2^m x^{2m} Λ^{∗m}(N)² (dyadic Cauchy–Schwarz),
Λ^{∗m}(N)² ≤ u^m Λ^{∗m}(N) (Basic.lamPow_le_log_pow), Σ_{N≤e^u} Λ^{∗m}(N)/N ≤ (u+mK)^m/m! (PowerSums), and
Σ_m [(4x²u²)^m/m! + (4eK·x²u)^m] ≤ e^{64} + 2.
-/
```

 ### small combinatorial facts 

### `cardFactors_le_self`

 Ω n ≤ n. 

### `sq_sum_range_le_sum_two_pow_mul_sq`

 dyadic Cauchy–Schwarz: (Σ_{i<n} a_i)² ≤ Σ_{i<n} 2^{i+1} a_i². 

 ### the F-majorant: Σ_{N≤e^u} F_x(N)²/N is bounded 

### `CF`

 the absolute constant bounding Σ F²/N. 

### `term_bound`

 per-m bound:  2^m x^{2m} u^m (u+mK)^m/m! ≤ (4x²u²)^m/m! + (4eK x²u)^m. 

### `Fmaj_term_le`

 the m-th dyadic term is summable-small:  2^m x^{2m} u^m Σ_{N≤e^u}Λ^{∗m}(N)/N ≤ 64^m/m! + 2^{-m}
(m = i+1), provided x·u ≤ 4 and 32eK·x ≤ 1. 

### `sum_Fmaj_sq_div_le`

 **Σ_{N ≤ e^u} F_x(N)²/N ≤ CF**, provided x·u ≤ 4 and 32eK·x ≤ 1 (x ≥ 0, u ≥ 0). 

 ### the diagonal sum: S(u) ≤ C(1+u)² 

### `sum_vonMangoldt_sq_div_le`

 Σ_{N ≤ e^u} Λ(N)²/N ≤ u(u + K). 

### `CS`

 the absolute constant in S(u) ≤ CS·(1+u)². 

### `diagSum_le`

 **uniform upper bound for the diagonal sum.**  For ‖Λ⋆‖ ≥ 32eK and u·‖Λ⋆‖⁻¹ ≤ 4 (u ≥ 0):
  Σ_{N ≤ e^u} ‖C(N;Λ⋆)‖²/N ≤ CS·(1+u)². 

 ### (H2) and (H1) for a T-indexed parameter with ‖Λ⋆(T)‖ ≥ l(T)/2 

### `T0coeff`

 the height threshold: l(T) ≥ 64eK (so ‖Λ⋆‖ ≥ l/2 ≥ 32eK) and l(T) ≥ 1. 

### `coeff_H2`

 **(H2)**: Σ_{N≤x} ‖C(N;Λ⋆(T))‖² ≤ 4CS·x·l(T)² for 2 ≤ x ≤ e^{l(T)}, T ≥ T0coeff, whenever ‖Λ⋆(T)‖ ≥ l(T)/2. 

### `coeff_H1`

 **(H1)**: Σ_{N≤x} ‖C(N;Λ⋆(T))‖/√N ≤ 2√CS·√x·l(T), same range, by Cauchy–Schwarz from the diagonal bound. 

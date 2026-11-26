---
{
  "module": "Zeta23/XiPrime/Coeff/MainTerm/Squarefree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/MainTerm/Squarefree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/MainTerm/Squarefree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/MainTerm/Squarefree.lean — exact evaluation of the Dirichlet powers at squarefree N.

For N squarefree, every prime-power divisor of N is a prime, so the k-fold Dirichlet power of any
arithmetic function supported on prime powers is explicit:
  (f^{∗k})(N) = k! · ∏_{p | N} f(p)  if ω(N) = k,  and 0 otherwise.
Consequences ([XF′] Def 2.3, "For squarefree N = p_1⋯p_k …"):
  Λ^{∗k}(N), (Λ·log)^{∗k}(N), [(Λ·log) ∗ Λ^{∗j}](N) = j!·log N·∏ log p  (ω N = j+1),
  C(N;Λ⋆) = (k−1)!·Λ⋆^{−k}·log N·∏_{p|N} log p   (k = ω N ≥ 2),   C(p;Λ⋆) = −log p + Λ⋆^{−1} log²p,
  ‖C(N;Λ⋆)‖² = ‖Λ⋆‖^{−2k}·((k−1)!²/k!)·(Λ·log)^{∗k}(N)·log²N.
No analysis in this file.
-/
```

 ### squarefree bookkeeping 

### `cardDistinctFactors_eq_card_primeFactors`

 A0: ω N = #(prime factors of N). 

### `prime_of_isPrimePow_dvd_squarefree`

 a prime-power divisor of a squarefree number is a prime. 

### `primeFactors_div_of_mem`

 for p a prime factor of squarefree N: the prime factors of N/p. 

### `vonMangoldt_eq_zero_of_cardDistinctFactors_ne_one`

 ω N ≠ 1 means N is not a prime power, so Λ N = 0. 

### `cardFactors_eq_cardDistinctFactors_of_squarefree`

 for squarefree N, Ω N = ω N. 

 ### the generic evaluation 

### `pow_apply_squarefree`

 **Dirichlet powers at squarefree N.**  If f is supported on prime powers then, for N squarefree,
(f^{∗k})(N) = k!·∏_{p|N} f(p) when ω N = k, and 0 otherwise. 

### `lamPow_apply_squarefree`

 A1. 

### `lamLogPow_apply_squarefree`

 A2. 

### `sum_primeFactors_log_of_squarefree`

 Σ_{p | N} log p = log N for squarefree N. 

### `lamLogConv_apply_squarefree`

 A3: [(Λ·log) ∗ Λ^{∗j}](N) = j!·log N·∏_{p|N} log p if ω N = j+1, else 0  (N squarefree). 

 ### C(N; Λ⋆) at squarefree N 

### `xiCoeff_squarefree`

 A4: for squarefree N with k = ω N ≥ 2:  C(N;Λ⋆) = (k−1)!·Λ⋆^{−k}·log N·∏_{p|N} log p. 

### `xiCoeff_prime`

 C(p;Λ⋆) = −log p + Λ⋆^{−1} log²p. 

### `norm_sq_xiCoeff_squarefree`

 ‖C(N;Λ⋆)‖² for squarefree N with ω N ≥ 2, in terms of (Λ·log)^{∗ω N}(N). 

---
{
  "module": "Zeta23/XiPrime/Coeff/PrimeSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/PrimeSums.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/PrimeSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/PrimeSums.lean — Mertens-level monomial sums and the prime sums Σ_{p≤e^u} log^b p / p.
Used for the k = 1 (N prime) part of the diagonal law [XF′ Lemma 7.1 (i), D_{1,1}].

  |Σ_{n ≤ e^u} (Λ(n)/n)(log n)^a − u^{a+1}/(a+1)| ≤ 2K(1+u)^a                    (mertens_step with f = v^a),
  |Σ_{p ≤ e^u, p prime} (log p)^{b}/p − u^{b}/b| ≤ C_b (1+u)^{b−1}   (b ≥ 2)      (non-primes: defect bound).
-/
```

### `mertens_monomial`

 Σ_{n ≤ e^u} (Λ n/n)·(log n)^a = u^{a+1}/(a+1) + O((1+u)^a). 

### `sum_not_prime_lam_logpow_div_le`

 Σ_{n ≤ X, n not prime} Λ(n)(log n)^a/n ≤ 2·Cdef·(log X)^{a−1}... we only need the crude form with u:
for n ≤ e^u:  Σ_{n not prime} Λ n (log n)^{b-1}/n ≤ u^{b-2}·2Cdef  (b ≥ 2). 

### `sum_prime_logpow_eq`

 the prime sum as "all n" minus "non-primes":  Σ_p log^b p/p = Σ_n Λ n log^{b−1} n/n − Σ_{n not prime} Λ n log^{b−1} n/n. 

### `prime_logpow_sum`

 **Σ_{p ≤ e^u} (log p)^b/p = u^b/b + O((1+u)^{b−1})**  for b ≥ 2. 

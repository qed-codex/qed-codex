---
{
  "module": "proof/rates/ClauseBound/Part/Lower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Lower.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Part/Lower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A lower bound for the number of partitions

`exists_le_p`: there are constants H > 0 and B with p(E) ≥ H·exp(c·√E)/E^B for all E ≥ 1, where c =
π·√(2/3). Appendix B of the paper quotes the asymptotic formula of Hardy and
Ramanujan, which gives B = 1; here B = 3890, which is enough where the bound is used.

The proof is Erdős's induction on n through the recurrence n·p(n) = Σ_{k,v ≥ 1, kv ≤ n} v·p(n − kv).
Write f(m) = exp(c·√m)/m^B and s = √n. For small n the bound holds because
H is small. For large n:

* f(n − x)/f(n) ≥ exp(−α·x)·(1 − γ·x²) for 0 ≤ x < n, with α = c/(2s) − B/n and γ = c/(2s³)
  (`ratio_ge`), and the right-hand side is not positive for x ≥ n;
* so for every k the sum of v·f(n − kv)/f(n) over the v with kv < n is at least the whole series Σ_v
  v·e^{−αkv}·(1 − γk²v²), which is at least
  1/(αk)² − 1/4 − 486·γ·k²/(αk)⁴ as long as αk ≤ 2 (`sum_v_ge`, from the closed form of Σ v·r^v,
  1/sinh² z ≥ 1/z² − 1, and Σ v³·r^v ≤ 6/(1 − r)⁴);
* the sum of this over k ≤ K = ⌈1/α⌉ is at least (ζ(2) − 1/K)/α² − K/4 − 486·γ·ζ(2)/α⁴ (`sum_k_ge`),
  with ζ(2) = π²/6 = c²/4;
* ζ(2)/α² ≥ n + 4B·s/c, and the three losses are together at most 15557·s/c + 1/4 (`step_arith`).

The auxiliary statements are in the namespace `ClauseBound.Part.Lower`. 

 ### Real-variable lemmas 

### `sqrt_sub_ge`

 √(1 − y) ≥ 1 − y/2 − y²/2 on [0, 1], scaled: √(N − x) ≥ √N − x/(2√N) − x²/(2N√N) for 0 ≤ x ≤ N. 

### `ratio_ge`

 The comparison function exp(c√m)/m^B at m = s² − x against its value at s²: the quotient is at
least exp(−(c/(2s) − B/s²)·x)·(1 − c·x²/(2s³)). 

### `sinh_le_mul_cosh`

 sinh z ≤ z·cosh z for z ≥ 0. 

### `inv_sq_sub_one_le`

 1/z² − 1 ≤ 1/sinh² z for z > 0. 

### `T1_ge`

 Σ_v v·e^{−yv} in closed form is at least 1/y² − 1/4. 

### `cube_le`

 v³ ≤ 6·C(v+3, 3). 

### `T3_le`

 Σ_v v³·r^v ≤ 6/(1 − r)⁴ for 0 ≤ r < 1. 

### `one_sub_exp_neg_ge`

 1 − e^{−y} ≥ y/3 for 0 ≤ y ≤ 2. 

 ### The sum over v for one k 

### `sum_v_ge`

 Σ_{1 ≤ v ≤ n} v·e^{−yv}·(1 − η·v²) ≥ 1/y² − 1/4 − 486·η/y⁴ if 0 < y ≤ 2 and the terms with v > n
are not positive. 

 ### The sum over k 

### `sum_inv_sq_le`

 Σ_{k ≤ K} 1/k² ≤ π²/6. 

### `le_sum_inv_sq`

 Σ_{k ≤ K} 1/k² ≥ π²/6 − 1/K. 

### `sum_k_ge`

 The sum over 1 ≤ k ≤ K of the lower bounds for the sums over v. 

 ### The arithmetic of the induction step 

### `step_arith`

 With s = √n, α = c/(2s) − B/s², γ = c/(2s³), c² = 4Z and 1/α ≤ K ≤ 1/α + 1, the lower bound for
the double sum is at least n, if B ≥ 3890 and s ≥ 4B/c + c. 

 ### The induction step 

### `cHR_sq`

 c² = 4·ζ(2), with c = π·√(2/3) and ζ(2) = π²/6. 

### `step`

 If the bound holds below n, and √n ≥ 4B/c + c with B ≥ 3890, it holds at n. 

### `exists_le_p`

 p(E) ≥ H·exp(π·√(2E/3))/E^B for E ≥ 1, with constants H > 0 and B. 

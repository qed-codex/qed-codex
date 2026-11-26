---
{
  "module": "proof/machines/Wrap/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A power of the time of the wrapped machine is below c·2^{δn}

A machine that is put around another one needs q·(t + X + 1)^q steps, where t bounds the steps of
the inner machine, X is the length of the outer input and q is a constant. Here t is
2^{C₁·min{m'/√(lg m'), n'·lg lg n'/√(lg n')}}, rounded down, plus C₂·L^{C₂}, with 4 ≤ n' ≤ n + 4,
and L and X are at most a·(n+2)^d. The main lemma of this file, `Wrap.wrapped_time_le`, says: for
every δ > 0 there is a c
such that the whole expression is at most ⌊c·2^{δn}⌋, for all n, m', n', L, X within these bounds.

The steps, with ε = δ/(q+1):
1. `rate_below`: 2^{B·n·lg lg n/√(lg n)} ≤ c·2^{εn} for n ≥ 4, because lg lg n/√(lg n) tends to 0.
2. `poly_below`: (n+2)^D ≤ c·2^{εn}.
3. `poly_part_le`: C·L^C + X + 1 ≤ (C·a^C + a + 1)·(n+2)^{dC+d}.
4. So t + X + 1 ≤ K·2^{εn} for a constant K, and the q-th power of the right side is at most
   K^q·2^{δn}.

Only the bound in n' of the minimum is used. Only numbers; no machine and no formula occurs in this
file. Throughout, lg is the logarithm to base 2. 

 ### The rate n·lg lg n/√(lg n) is below ε·n, up to a constant 

### `half_lt_log_two`

 The natural logarithm of 2 is above 1/2. 

### `lg_le_fourth_root`

 lg y ≤ 8·y^(1/4) for y > 0; the fourth root is written as a square root of a square root. 

### `lg_div_sqrt_le`

 lg y/√y ≤ 8/y^(1/4) for y > 0. 

### `rate_le_const_add`

 For B ≥ 0, ε > 0 and any natural number n₀ ≥ 2^((8B/ε)^4): B·n·lg lg n/√(lg n) ≤ 8·B·n₀ + ε·n
for all n ≥ 4.
For n ≤ n₀ the first summand is enough, because lg lg n/√(lg n) ≤ 8; for n ≥ n₀ the second is
enough, because then B·lg lg n/√(lg n) ≤ ε. 

### `rate_below`

 For every B ≥ 0 and ε > 0 there is a c with 2^{B·n·lg lg n/√(lg n)} ≤ c·2^{εn} for all n ≥ 4:
take a natural number n₀ ≥ 2^((8B/ε)^4) and then c ≥ 2^(8·B·n₀). 

### `timeMin3_le`

 The time with the minimum of the two exponents is at most the power of 2 with the exponent in n
alone: ⌊2^{C·min{m/√(lg m), n·lg lg n/√(lg n)}}⌋ ≤ 2^{C·n·lg lg n/√(lg n)}. No hypothesis on C, m,
n. 

 ### A polynomial is below c·2^{εn} 

### `le_two_mul_two_rpow`

 s ≤ 2·2^s for every real s ≥ 0. 

### `poly_below`

 For every D and ε > 0 there is a c with (n+2)^D ≤ c·2^{εn} for all n. With K = D + 1: n + 2 ≤
(2K/ε + 2)·2^{εn/K}, and the K-th power of the right side is (2K/ε + 2)^K·2^{εn}. 

### `poly_part_le`

 If L and X are at most a·(n+2)^d, then C·L^C + X + 1 ≤ (C·a^C + a + 1)·(n+2)^{dC+d}. 

 ### The main lemma 

### `wrapped_time_le`

 For all q, C₁, C₂, a, d and every δ > 0 there is a c such that q·(⌊2^{C₁·min{m'/√(lg m'), n'·lg
lg n'/√(lg n')}}⌋ + C₂·L^{C₂} + X + 1)^q ≤ ⌊c·2^{δn}⌋ whenever m' ≥ 2, 4 ≤ n' ≤ n + 4 and L, X ≤
a·(n+2)^d.
The constant C₁ in the exponent and the constant C₂ in the polynomial need not be equal. The proof
does not use m' ≥ 2. 

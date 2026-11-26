---
{
  "module": "proof/machines/Wrap/ArithRate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/ArithRate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/ArithRate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A polynomial in a time bound of the Main Theorem's form stays below c·2^{c·9·n·lg lg(n+4)/√(lg(n+4))}
An expression of this kind bounds the time of a machine that decides 3-SAT on the plain input code
by a polynomial-time front end and a simulation of a machine that counts within the bound of the
Main Theorem.
The expression is that of Arith.lean: q·(t + X + 1)^q, where t is 2^{C₁·min{m'/√(lg m'), n'·lg lg
n'/√(lg n')}}, rounded down, plus C₂·L^{C₂}, with 4 ≤ n' ≤ n + 4, and L and X are at most a·(n+2)^d.
The main lemma of this file, `Wrap.wrapped_time_le_rate`, says: there is a c such that the whole
expression is at most ⌊c·2^{c·9·n·r(n)}⌋ with r(n) = lg lg(n+4)/√(lg(n+4)), for all n, m', n', L, X
within these bounds.

The steps, with E = n·r(n):
1. `div_sqrt_lg_mono`: x/√(lg x) grows with x ≥ 2. So n'·lg lg n'/√(lg n') ≤ (n+4)·r(n)
   (`exponent_le`), and this is at most E + 32, because r(n) ≤ 8 (`rate_le_eight`).
2. `lg_le_rate`: lg(n+4) ≤ 64·E + 256. So (n+2)^D ≤ 2^{D·(64·E + 256)} (`pow_le_rate`).
3. So t + X + 1 ≤ K·2^{κE} with constants K and κ = C₁ + 64·(d·C₂ + d), and the q-th power of the
   right side is K^q·2^{qκE}.

Only the bound in n' of the minimum is used. Only numbers; no machine and no formula occurs in this
file. Throughout, lg is the logarithm to base 2. 

 ### The rate 

### `rate_eq`

 The rate with exponents 1 and 1/2, written with lg and a square root: lg lg(n+4)/√(lg(n+4)). 

### `lg_add_four_facts`

 lg(n+4) ≥ 2 and lg lg(n+4) ≥ 1, for every n ≥ 0. 

### `rate_nonneg`

 The rate is not negative. 

### `rate_le_eight`

 The rate is at most 8. 

 ### x/√(lg x) grows 

### `lg_le_two_mul_sub`

 lg t ≤ 2·(t − 1) for t ≥ 1. 

### `one_le_lg_real`

 lg x ≥ 1 for real x ≥ 2. 

### `sq_mul_lg_le`

 x²·lg y ≤ y²·lg x for 2 ≤ x ≤ y. With t = y/x: lg y = lg x + lg t ≤ lg x + 2(t−1) ≤ t²·lg x,
because lg x ≥ 1. 

### `div_sqrt_lg_mono`

 x/√(lg x) ≤ y/√(lg y) for 2 ≤ x ≤ y. 

### `exponent_le`

 n'·lg lg n'/√(lg n') ≤ (n+4)·lg lg(n+4)/√(lg(n+4)) for 4 ≤ n' ≤ n + 4. 

 ### A polynomial is below a power of 2 with the rate in the exponent 

### `lg_le_rate`

 lg(n+4) ≤ 64·n·r(n) + 256 with r(n) = lg lg(n+4)/√(lg(n+4)). With Λ = lg(n+4): Λ·√Λ ≤ Λ² ≤
64·√(n+4) ≤ 64·(n+4); divide by √Λ ≥ 1 and use lg Λ ≥ 1. 

### `pow_le_rate`

 (n+2)^D ≤ 2^{D·(64·n·r(n) + 256)} with r(n) = lg lg(n+4)/√(lg(n+4)), because n + 2 ≤ n + 4 =
2^{lg(n+4)}. 

 ### The main lemma 

### `wrapped_time_le_rate`

 For all q, C₁, C₂, a, d there is a c such that q·(⌊2^{C₁·min{m'/√(lg m'), n'·lg lg n'/√(lg
n')}}⌋ + C₂·L^{C₂} + X + 1)^q ≤ ⌊c·2^{c·9·n·lg lg(n+4)/√(lg(n+4))}⌋ whenever m' ≥ 2, 4 ≤ n' ≤ n + 4
and L, X ≤ a·(n+2)^d.
The proof does not use m' ≥ 2. 

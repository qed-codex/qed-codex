---
{
  "module": "proof/rates/PaddedDescent/RateLemmas.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/RateLemmas.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/RateLemmas.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From an integer time bound to the rate statement, and what «2^{o(n)} with one machine» implies

1. `inRateTM_of_mulForm`: a machine with finite alphabets that decides 3-SAT within A·2^(e n) steps,
   where e n·2^(sOf n) ≤ C₁·(n + 2^(sOf n))
   (that is, A·2^(C₁·n / 2^(sOf n) + C₁) steps, in natural numbers without division; the arithmetic
   step is also proved in real numbers, `le_rateBound_of_real`)
   witnesses `Sat3.InRateTM (3/19)`, that is time C·2^{C·n/(log₂(n+2))^{3/19}}, for all n. The rate
   theorem uses
   `inRateTM_of_mulForm`, which `inRateTM_of_padded_mul` (proof/rates/PaddedDescent/PadRate.lean)
   applies.
2. Checks on `ThreeSatRateStatement.lean`: `rateBound` decreases when c grows, so the claim for c
   implies the claim for every c' ≤ c;
   and «2^{o(n)} with one machine» (`SubexpTM`) implies `InTimeTM δ` for every δ > 0, which refutes
   `ETH_TM`.

Only `ThreeSatStatement.lean`, `ThreeSatRateStatement.lean`, the definition of `sOf` and the file
`proof/machines/ToTuring/EndLemmas.lean` (monotonicity of
`DecidesTM`, and ¬ETH_TM ↔ ∀ δ > 0, InTimeTM δ) are used. 

 ### The logarithm 

### `one_le_logb`

 log₂(n+2) ≥ 1. 

### `logb_rpow_pos`

 (log₂(n+2))^c > 0 for every real c. 

### `add_two_le_two_pow`

 m + 2 ≤ 2^(⌊log₂ m⌋ + 2), for every m (with `Nat.log2 0 = 0`). 

### `logb_le_two_pow`

 log₂(n+2) ≤ 2^(⌊log₂⌊log₂ n⌋⌋ + 2), for every n. 

### `logb_rpow_le_two_pow`

 If p·(⌊log₂⌊log₂ n⌋⌋ + 2) ≤ q·(s+b) then (log₂(n+2))^{p/q} ≤ 2^{s+b}: so 2^{-s} ≤ 2^b /
(log₂(n+2))^{p/q}. 

 ### From natural numbers to `rateBound` 

### `le_rateBound_of_real`

 The arithmetic core, for one n. Let s be tied to n by p·(⌊log₂⌊log₂ n⌋⌋ + 2) ≤ q·(s+b). Then a
number t of steps that is at most
A·2^{C₁·n/2^s + C₁} (real exponent) is at most C·2^{C·n/(log₂(n+2))^{p/q}} with C = A·2^{C₁} +
C₁·2^b. 

### `le_rateBound_of_mul_le`

 The same in natural numbers and without division: the exponent e satisfies e·2^s ≤ C₁·(n + 2^s),
that is e ≤ C₁·n/2^s + C₁. 

### `log2_log2_le_sOf`

 3·(⌊log₂⌊log₂ n⌋⌋ + 2) ≤ 19·(sOf n + 146) for every n, also where `sOf n = 0`. (Recall `sOf n` =
3·(⌊log₂⌊log₂ n⌋⌋ − 911)/19, rounded down.) 

### `inRateTM_of_mulForm`

 A machine with finite alphabets that decides 3-SAT within t n ≤ A·2^(e n) steps, for any
exponents with e n · 2^(sOf n) ≤ C₁·(n + 2^(sOf n)), witnesses the rate statement with c = 3/19. 

 ### Checks on the statement 

### `rateBound_anti`

 `rateBound` decreases when c grows. 

### `InRateTM.mono`

 The claim for an exponent c implies the claim for every smaller exponent c'. 

### `SubexpTM.inTimeTM`

 «2^{o(n)} with one machine» implies `InTimeTM δ` for every δ > 0. 

### `SubexpTM.not_ETH_TM`

 «2^{o(n)} with one machine» refutes the Exponential Time Hypothesis. 

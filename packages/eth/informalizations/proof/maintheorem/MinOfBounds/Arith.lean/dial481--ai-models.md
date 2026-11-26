---
{
  "module": "proof/maintheorem/MinOfBounds/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MinOfBounds/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MinOfBounds/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 11 from Theorem A (c) and Theorem D (b): the arithmetic

This file proves the sentence of the proof of Corollary 11 that reads: «This multiplies the number
of operations of the faster one by a constant; as km/√(log m) and n·log log n/√(log n) are at least
2, this constant goes into C.» No machine and no formula occurs in it.

Write A for 2^{C₁·km/√(log m)} and B for 2^{C₂·k²·n·log log n/√(log n)}, both rounded down, T for
the smaller of A and B, and P for C₁·L₁^C₁ + L + 1. The number to be bounded is q·(min(A + C₁·L₁^C₁,
B) + L + 1)^q.
1. It is at most q·(T + P)^q, and (T + P)^q ≤ 2^q·T^q + 2^q·P^q (`add_pow_le`).
2. `exponential_part_le`: T is at most 2^{D·X}, where D is the larger of C₁ and C₂ and X the smaller
   of the two exponents (`min_time_le`). As X ≥ 2, the factor q·2^q is at most 2^{q·X}. So q·2^q·T^q
   is at most 2^{(q·D + q)·X}.
3. `polynomial_part_le`: as L₁ ≤ a·L^a and L ≥ 1, q·2^q·P^q is at most a constant times a power of
   L.
4. `overheadGoesIntoC`: C is the sum of the three constants that come up.

`bound_le_timeM` is the arithmetic of `MinOfBounds.BoundInMSuffices`: C·2^{C·km/√(log₂(m+2))} ≤
2^{3C·km/√(log m)} for k ≥ 1 and m ≥ 2. 

### `add_pow_le`

 (T + P)^q ≤ 2^q·T^q + 2^q·P^q for all natural numbers: the sum is at most twice the larger of
the two. 

### `min_time_le`

 The smaller of the times 2^{C₁·km/√(log m)} and 2^{C₂·k²·n·log log n/√(log n)} is at most
2^{D·X}, where D is the larger of C₁ and C₂ and X is the smaller of the two exponents km/√(log m)
and k²·n·log log n/√(log n); for k ≥ 1, m ≥ 2 and n ≥ 4. 

### `factor_goes_into_exponent`

 On real numbers: if T ≤ 2^{D·X} and X ≥ 2, then q·(2^q·T^q) ≤ 2^{(q·D + q)·X}. Here X ≥ 2 is
used: q·2^q ≤ 2^{2q} ≤ 2^{q·X}. 

### `exponential_part_le`

 The exponential part: q·2^q·T^q, where T is the smaller of the two times with the constants C₁
and C₂, is at most the time of Corollary 11 with the constant q·max(C₁, C₂) + q; for k ≥ 1, m ≥ 2
and n ≥ 4. 

### `polynomial_part_le`

 The polynomial part: for L ≥ 1 and L₁ ≤ a·L^a, q·2^q·(C₁·L₁^C₁ + L + 1)^q is at most
q·2^q·(C₁·a^C₁ + 2)^q times L^((a·C₁ + 1)·q). 

### `timeCor_mono`

 The time of Corollary 11 grows with the constant; for k ≥ 1, m ≥ 2 and n ≥ 4. 

### `overheadGoesIntoC`

 «… as km/√(log m) and n·log log n/√(log n) are at least 2, this constant goes into C.» The
constant is C = (q·max(C₁, C₂) + q) + q·2^q·(C₁·a^C₁ + 2)^q + (a·C₁ + 1)·q. 

### `bound_le_timeM`

 The bound of `AppRunningTime.BoundInM` with the constant C, C·2^{C·km/√(log₂(m+2))} rounded
down, is at most 2^{3C·km/√(log m)} rounded down; for k ≥ 1 and m ≥ 2. The factor C in front goes
into the exponent because km/√(log m) is at least 2. 

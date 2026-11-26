---
{
  "module": "ThreeSumApsp/Util/PrimeCounting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/PrimeCounting.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/PrimeCounting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Counting the primes up to m, in natural numbers

Three elementary bounds on the number `π(m)` of primes up to `m`, the cardinality of
`Nat.primesLE m`.

* `π(m) ≤ m` (`Nat.card_primesLE_le`).
* `m ≤ (⌊log₂ m⌋ + 1)(π(m) + 1)` (`Nat.le_log_mul_card_primesLE`), from the bound
  `2^m ≤ (m + 1) lcm(1, …, m)` of Mathlib: each prime power in the least common multiple is at most
  `m`.
* So there are at least `w` primes up to `(w + 1)(2⌊log₂(w + 1)⌋ + 4)`
  (`Nat.le_card_primesLE_mul_log`).


### `card_primesLE_le`

 There are at most `m` primes up to `m`. 

### `le_log_mul_card_primesLE`

 A lower bound of Chebyshev's type in natural numbers: `m ≤ (⌊log₂ m⌋ + 1)(π(m) + 1)`. 

### `le_card_primesLE_mul_log`

 There are at least `w` primes up to `(w + 1)(2⌊log₂(w + 1)⌋ + 4)`. 

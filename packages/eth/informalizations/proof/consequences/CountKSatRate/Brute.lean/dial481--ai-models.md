---
{
  "module": "proof/consequences/CountKSatRate/Brute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Brute.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Brute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Exhaustive counting is correct

`bruteN k (x, pad)` of proof/consequences/CountKSatRate/Defs.lean reads the formula written in x,
the code of an instance of k-SAT, and counts, among the assignments number 0, …, 2^n − 1
that the pad reaches, those that satisfy it. Assignment number y gives the variable i the i-th
binary digit of y, so these numbers stand for the 2^n assignments, each exactly once.
With a pad of at least 2^n units nothing is cut off, and the result is the count (`stBruteC`, which
proves the interface statement `StBruteC` of
proof/consequences/CountKSatRate/Interfaces.lean).
The file is the counting version of `bruteA_enc_of_le` in proof/rates/PaddedDescent/BrutePad.lean. 

### `satAt_toN`

 Assignment number y satisfies the formula, with variables written as natural numbers, exactly
when its binary digits make a literal of every clause true. 

### `length_filter_satAt`

 Among the numbers below 2^n, as many satisfy the formula as there are satisfying assignments. 

### `outW_eq_binary`

 `outW` writes N as n + 1 bits, lowest bit first, exactly as `binary n N`. 

### `stBruteC`

 With a pad of at least 2^n units, exhaustive counting returns the number of satisfying
assignments. 

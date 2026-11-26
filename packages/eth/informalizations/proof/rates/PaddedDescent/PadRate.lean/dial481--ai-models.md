---
{
  "module": "proof/rates/PaddedDescent/PadRate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/PadRate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/PadRate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 From a polynomial-time function of the padded input to the rate statement. `inRateTM_of_padded`:
let A be a polynomial-time
function (`PolyT`) of a bit string and a pad, and e a polynomial-time function that says how long
the pad is to be, namely 2^(e x). If on
the code of every instance of 3-SAT on n variables e is at most C₀·(n / 2^(sOf n) + 1), and A with
the pad of that length returns the bit
«satisfiable», then `Sat3.InRateTM (3/19)` holds: one Turing machine decides 3-SAT within
C·2^{C·n/(log₂(n+2))^{3/19}} steps, for some constant C.
The work here is to absorb the polynomial in the length of the input, (n+2)^{4q}, into the bound:
⌊log₂(n+2)⌋·2^s ≤ 8·(n + 2^s) whenever
2^s ≤ ⌊log₂(n+2)⌋, which holds for s = sOf n. 

### `sq_le_four_mul_two_pow`

 L² ≤ 4·2^L. 

### `log2_mul_two_pow_le`

 If 2^s ≤ ⌊log₂(n+2)⌋ then ⌊log₂(n+2)⌋·2^s ≤ 8·(n + 2^s). 

### `two_pow_sOf_le`

 2^(sOf n) ≤ ⌊log₂(n+2)⌋, for every n. 

### `padded_time_le`

 The arithmetic, for one n. Let 2^s ≤ ⌊log₂(n+2)⌋ and E·2^s ≤ C₀·(n + 2^s). Then the time
q·(25(n+2)^4 + 2^E)^q of the padded machine
is at most q·2^e' for e' = q·(E + 4·⌊log₂(n+2)⌋ + 10), and e'·2^s ≤ q·(C₀ + 42)·(n + 2^s). 

### `inRateTM_of_padded_mul`

 Without division. Let `e` and `A` be polynomial-time, and let E be a function of the number n of
variables with
E n · 2^(sOf n) ≤ C₀ · (n + 2^(sOf n)), that is E n ≤ C₀·n/2^(sOf n) + C₀. If on the code x of every
instance of 3-SAT e x ≤ E n, and
A (x, the list of 2^(e x) units) is the bit «satisfiable», then the rate statement holds with c =
3/19. 

### `inRateTM_of_padded`

 Let `e` (from bit strings to numbers) and `A` (from a bit string and a list of units to a bit)
be polynomial-time. If on the code x
of every instance of 3-SAT on n variables e x ≤ C₀ · (n / 2^(sOf n) + 1) (division rounded down),
and A (x, the list of 2^(e x) units) is
the bit «satisfiable», then one Turing machine decides 3-SAT within C·2^{C·n/(log₂(n+2))^{3/19}}
steps, for some constant C. 

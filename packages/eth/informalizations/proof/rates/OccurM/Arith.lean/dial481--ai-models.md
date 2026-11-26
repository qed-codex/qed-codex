---
{
  "module": "proof/rates/OccurM/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From the bound C·2^{C·km/(log₂(m+2))^α} of `SatM.bound` to the printed bound 2^{C·km/(log m)^α} + C·(length)^C

The bound `SatM.bound (SatM.rPow α) C` is C·2^{C·k·m/(log₂(m+2))^α}, the printed one 2^{C·km/(log
m)^α} plus a polynomial in the length of the formula. Throughout 0 ≤ α ≤ 1, k ≥ 1 and m ≥ 2, and X
is the printed exponent km/(log m)^α.

1. `ClausesOccur.expHalf`: at α = ½ the printed exponent is that of the Main Theorem.
2. `one_le_expClauses`: X ≥ 1. `shift_le`, `expClauses_le`: k·m/(log₂(m+2))^α ≤ X ≤
   2·k·m/(log₂(m+2))^α.
3. `pow_le_timeClauses`, `timeClauses_mono`: powers of two below the printed bound; the printed
   bound grows with the constant.
4. `bound_le_pow`: the bound `SatM.bound` with the constant C is at most 2^E for a natural number E
   ≤ (2C+1)·X.
5. `steps_le`: q·(a + 2^E + 1)^q, with E ≤ G·X, X ≥ 1 and a ≥ 1, is at most the printed bound plus
   the polynomial in a, both with the constant `stepsC q G`.

Only numbers; no machine and no formula occurs in this file. 

### `expHalf`

 At α = ½ the exponent is that of the Main Theorem. 

 ### The printed exponent 

### `one_le_lg_rpow`

 (log m)^α ≥ 1. 

### `lg_rpow_le`

 (log m)^α ≤ log m. 

### `one_le_expClauses`

 The printed exponent is at least 1. 

### `shift_le`

 k·m/(log₂(m+2))^α ≤ k·m/(log m)^α. 

### `lg_add_two_le`

 log₂(m+2) ≤ 2·log m, since m + 2 ≤ m². 

### `lg_add_two_rpow_le`

 (log₂(m+2))^α ≤ 2·(log m)^α. 

### `expClauses_le`

 k·m/(log m)^α ≤ 2·k·m/(log₂(m+2))^α. 

 ### The printed bound 

### `pow_le_timeClauses`

 2^e is at most the printed bound with the constant C if e ≤ C·X. 

### `timeClauses_mono`

 The printed bound grows with the constant. 

### `bound_le_pow`

 The bound `SatM.bound` with the constant C is at most 2^E for a natural number E ≤ (2C+1)·X: the
factor in front goes into the exponent. 

 ### The steps of a machine that runs on a pad of 2^E units, or around a machine with 2^E steps 

### `stepsC`

 The constant of `steps_le`. 

### `steps_le`

 q·(a + 2^E + 1)^q, with E ≤ G·X, X ≥ 1 and a ≥ 1, is at most 2^{C·X} + C·a^C with C =
`stepsC q G`. 

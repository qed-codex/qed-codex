---
{
  "module": "proof/variables/VariableBound/Paper/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From log₂(m+2), log₂(n+4) and a factor in front to the printed bounds

`UniformInKStatement.lean` has the bounds C·2^{C·k²·n·log₂ log₂(n+4)/√(log₂(n+4))} and
C·2^{C·min(that exponent, k·m/√(log₂(m+2)))}. `MainTheoremFormsStatement.lean` has 2^{C·k²·n·log log
n/√(log n)} for n ≥ 4 and
2^{C·min{km/√(log m), k²·n·log log n/√(log n)}} for m ≥ 2 and n ≥ 4. Here:

1. `two_le_expM`, `two_le_base`: km/√(log m) (k ≥ 1, m ≥ 2) and n·log log n/√(log n) (n ≥ 4) are at
   least 2 (proof of Corollary 11).
2. `boundNK_le`, `boundBothK_le`: the bounds with the constant C are at most the printed bounds with
   the constant 3C.
3. `timeCor_eq`: the minimum of the two powers is the power of the minimum («This is the Main
   Theorem»).
4. `timeMin_three_le`: at k = 3 the printed bound with C is at most the bound without k with 9C.

Only real numbers; no machine and no formula occurs in this file. 

 ### The logarithm 

### `lg_mono`

 log x ≤ log y for 0 < x ≤ y. 

### `lg_two`

 log 2 = 1. 

### `lg_two_mul`

 log(2x) = 1 + log x for x > 0. 

### `one_le_lg`

 log m ≥ 1 for m ≥ 2. 

### `lg_le_sub_one`

 log m ≤ m − 1 for m ≥ 1. 

### `two_sqrt_lg_le`

 2·√(log m) ≤ m for m ≥ 1. 

### `lg_add_four`

 For n ≥ 4: 2 ≤ log n ≤ log(n+4), 1 ≤ log log n, and 0 ≤ log log(n+4) ≤ 2·log log n. 

 ### Both exponents are at least 2 

### `two_le_expM`

 k·m/√(log m) ≥ 2 for k ≥ 1 and m ≥ 2. 

### `two_le_base`

 n·log log n/√(log n) ≥ 2 for n ≥ 4. 

### `expN_eq`

 The exponent in n is k² times n·log log n/√(log n). 

### `expM_eq`

 The exponent in m is k times m/√(log m). 

### `two_le_expN`

 k²·n·log log n/√(log n) ≥ 2 for k ≥ 1 and n ≥ 4. 

 ### The exponents with shifts against the printed exponents 

### `shiftM_le`

 k·m/√(log₂(m+2)) ≤ k·m/√(log m) for m ≥ 2. 

### `shiftN_le`

 k²·n·log₂ log₂(n+4)/√(log₂(n+4)) ≤ 2·k²·n·log log n/√(log n) for n ≥ 4. 

 ### The factor in front goes into the exponent 

### `natCast_le_two_rpow`

 C ≤ 2^{C·X} for X ≥ 1. 

### `absorb`

 If E ≤ 2·X and X ≥ 1, then C·2^{C·E} ≤ 2^{3C·X}. 

### `boundNK_le`

 For k ≥ 1 and n ≥ 4 the bound in n of `UniformInKStatement.lean` with the constant C is at most
the printed bound of Theorem D (b) with the constant 3C. 

### `boundBothK_le`

 For k ≥ 1, m ≥ 2 and n ≥ 4 the bound with the minimum of `UniformInKStatement.lean` with the
constant C is at most the printed bound of Theorem 1 with the constant 3C. 

 ### The printed bounds among themselves 

### `timeMin_mono`

 The printed bound of Theorem 1 grows with the constant, for k ≥ 1, m ≥ 2 and n ≥ 4. 

### `timeCor_eq`

 min{2^{C·a}, 2^{C·b}} = 2^{C·min{a, b}}: the time of Corollary 11 is the time of Theorem 1. No
hypothesis on C, k, m, n. 

### `timeMin_three_le`

 At k = 3 the printed bound of Theorem 1 with the constant C is at most 2^{9C·min{m/√(log m),
n·log log n/√(log n)}}, for m ≥ 2 and n ≥ 4. 

---
{
  "module": "proof/variables/PairsToBound/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (b) from Theorem D (a): the arithmetic

Sentences (5), (6) and (8) of Step 6 of Appendix D, in the numbering of
proof/variables/PairsToBound/Defs.lean, and the numbers for the main statement.

* `mainRegimeBound`: sentence (5). It is the «In particular» of Theorem D (a)
  (`MainTheoremForms.ThmVariablesAInParticular`) at α′ = 1/2, where (log n)^(1/2) = √(log n).
* `theBoundIncreasesWithTheWidth`: «the bound increases with k».
* `fallBackIsWithinTheBound`: sentence (8). The one inequality that needs work is log n ≤ n/√(log
  n), that is (log n)³ ≤ n² (`lg_cube_le`): with y = (2/3)·ln n, log n ≤ (50/23)·y ≤ 1 + y + y²/2 ≤
  e^y, and (e^y)³ = n².
* `choice_le`: if t and len + 1 are at most 2^{c₁·X} and X ≥ 1, then q·(t + len + 1)^q ≤
  2^{q(c₁+2)·X}. `main_case_le` and `fall_back_case_le` apply it with X = k²·n·log log n/√(log n) to
  the two branches of the algorithm of Step 6; `le_of_wide` and `le_of_small` give n ≤ D·X in the
  two cases in which the algorithm tries all
  assignments. 

 ### Sentence (5): the main regime 

### `mainRegimeBound`

 «So for n ≥ K₀^17 and 3 ≤ k ≤ (log n)^(1/4) the algorithm of Theorem D (a) takes time
2^{O(k²·n·log log n/√(log n))}» (Step 6 of Appendix D), for every machine with the conclusion of
Theorem D (a). 

 ### «The bound increases with k» 

### `expN_mono`

 For n ≥ 4 and k ≤ k′: k²·n·log log n/√(log n) is at most the same number at k′. 

### `expVariablesA_mono`

 For 3 ≤ k ≤ k′ and 0 < e ≤ 1: k²·e·n·log(k/e) is at most the same number at k′. 

### `theBoundIncreasesWithTheWidth`

 «the bound increases with k» (Step 5 of Appendix D), for the bound of Theorem D (b) and for that
of Theorem D (a). 

 ### Sentence (8): trying all assignments is within the bound 

### `lg_cube_le`

 (log n)³ ≤ n² for n ≥ 1. 

### `lg_le_div_sqrt`

 «log n ≤ n/√(log n)», for n ≥ 2. 

### `div_sqrt_le_base`

 «n/√(log n) ≤ n·log log n/√(log n)», for n ≥ 4. 

### `mul_lg_le_expN`

 «so k·log n ≤ k²·n·log log n/√(log n)», for k ≥ 1 and n ≥ 4. 

### `mul_lglg_le_expN`

 «if k > (log n)^(1/4), then k²·n·log log n/√(log n) ≥ n·log log n», for n ≥ 4. 

### `div_sqrt_level_le_base`

 «and if n < K₀^17, then n·log log n/√(log n) ≥ n/√(17·log K₀)», for n ≥ 4. 

### `fallBackIsWithinTheBound`

 «It is within the bound: …» (Step 6 of Appendix D): the printed inequalities. 

 ### The numbers for the main statement 

### `expN_le_nine`

 «which multiplies k² by at most 9»: if k′² ≤ 9k², the exponent at k′ is at most 9 times that at
k, for n ≥ 4. 

### `le_of_wide`

 If the width k′ used by the algorithm exceeds (log n)^(1/4) and k′² ≤ 9k², then n ≤ 9·k²·n·log
log n/√(log n). 

### `le_of_small`

 If n < K₀^17 and √(17·log K₀) ≤ D, then n ≤ D·k²·n·log log n/√(log n), for k ≥ 1, K₀ ≥ 2 and n ≥ 4. 

### `natCast_pow_eq`

 n^j = 2^{j·log n} for n ≥ 1. 

### `two_rpow_mono`

 2^{a·X} ≤ 2^{b·X} for natural numbers a ≤ b and X ≥ 0. 

### `choice_le`

 The polynomial factor q·(t + len + 1)^q goes into the constant: if t ≤ 2^{c₁·X}, len + 1 ≤
2^{c₁·X} and X ≥ 1, then q·(t + len + 1)^q ≤ 2^{q(c₁+2)·X}, rounded down. 

### `length_le_rpow`

 A code of length len with len + 1 ≤ (n+2)^(5k) has len + 1 ≤ 2^{10·X}, X = k²·n·log log n/√(log
n), for k ≥ 1 and n ≥ 4. 

### `main_case_le`

 The branch of the main regime, as numbers: for k ≥ 1, n ≥ 4, k′² ≤ 9k², len + 1 ≤ (n+2)^(5k) and
c₁ at least 9C₁ and at least 10, q·(2^{C₁·k′²·n·log log n/√(log n)} + len + 1)^q ≤
2^{q(c₁+2)·k²·n·log log n/√(log n)}, both powers of 2 rounded down. 

### `fall_back_case_le`

 The branch that tries all assignments, as numbers: for k ≥ 1, n ≥ 4, n ≤ D·k²·n·log log n/√(log
n), len + 1 ≤ (n+2)^(5k) and c₁ at least c(D+1) and at least 10, q·(2^{c·n}·n^{c·k} + len + 1)^q ≤
2^{q(c₁+2)·k²·n·log log n/√(log n)}, rounded down. 

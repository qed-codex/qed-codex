---
{
  "module": "proof/variables/PairsToBound/Exhaust.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Exhaust.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Exhaust.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The machine that tries all assignments

**The sentence answered** (Step 6 of Appendix D). «In the other cases … the algorithm tries all
assignments; as there are fewer than (2n+1)^k ≤ n^(2k) clauses, this takes time 2^n·n^{O(k)},
reading the input included.»

**What is proved.**
* `everyExhaustiveMachineTriesAll : EveryExhaustiveMachineTriesAll`: EVERY machine that computes the
  named function `exhaust` (exhaustive counting) with a padding string of 2ⁿ units, within q·(|x| +
  2ⁿ + 1)^q steps, counts the satisfying assignments of every k-CNF on n ≥ 2 variables, k ≥ 1,
  within 2^{c·n}·n^{c·k} steps, for c = 8q.
* `exhaustiveMachineExists : ExhaustiveMachineExists`: there is such a machine, with finite
  alphabets.

**How.**
* The value (`exhaust_enc`). On the code of (k, φ) the reader returns n and φ
  (`ClauseBound.Alg.Decode.stDecM`); with 2ⁿ units nothing is cut off, so the count is the number of
  satisfying assignments (`CountKSatRate.stBruteC`); it is written in n + 1 bits.
* The length of the input (`length_enc_succ_le`), by the printed reason. The code of (k, φ) has k +
  n + 2 + m·k·(⌊log₂ 2n⌋ + 1) symbols. There are m ≤ (2n+1)^k clauses
  (`VariableBound.Paper.clauseCount`), and (2n+1)^k ≤ n^(2k) for n ≥ 3 (`clauseCountPowStmt`), while
  5^k ≤ 2^(3k) for n = 2. With k ≤ n^k and ⌊log₂ 2n⌋ + 1 ≤ n², the length plus one is at most
  n^(8k).
* The time (`steps_le`). |x| + 2ⁿ + 1 ≤ n^(8k) + 2ⁿ ≤ n^(8k)·2ⁿ, and q ≤ 2^q.
* The machine. `exhaust` and x ↦ n are polynomial-time, so the padding machine of this development
  (`CountKSatRate.stPaddedW`) computes `exhaust` in the sense of `Computes`. 

 ### The value 

### `toWord_eq_map`

 The word of ℓ bits of y, lowest bit first, lists the binary digits number 0, …, ℓ − 1 of y. 

### `outW_replicate`

 The last step writes the number v in n + 1 bits, as the statements of the theorems ask. 

### `exhaust_enc`

 On the code of (k, φ), for k ≥ 1 and a k-CNF φ on n variables, with a padding string of 2ⁿ
units, exhaustive counting returns the number of satisfying assignments of φ in n + 1 bits. 

 ### The length of the input 

### `clauseCountPow_of_two_le`

 (2n+1)^k ≤ n^(3k) for n ≥ 2: for n ≥ 3 by the printed (2n+1)^k ≤ n^(2k), for n = 2 because 5 ≤
2³. 

### `length_enc_succ_le`

 «… as there are fewer than (2n+1)^k ≤ n^(2k) clauses …, reading the input included»: the code of
(k, φ), for k ≥ 1 and a k-CNF φ on n ≥ 2 variables, has fewer than n^(8k) symbols. 

 ### The time 

### `steps_le`

 If L + 1 ≤ n^(8k) and n ≥ 2, k ≥ 1, then q·(L + 2ⁿ + 1)^q ≤ 2^(8q·n)·n^(8q·k). 

### `triesAllWithin_of_computes`

 «… the algorithm tries all assignments; … this takes time 2^n·n^{O(k)}, reading the input
included.» Every machine that computes exhaustive counting with a padding string of 2ⁿ units, with
the constant q, tries all assignments within 2^{c·n}·n^{c·k} steps for c = 8q. 

### `everyExhaustiveMachineTriesAll`

 Every machine that computes exhaustive counting with a padding string of 2ⁿ units tries all
assignments within 2^{c·n}·n^{c·k} steps, for some c. 

 ### The machine 

### `exhaust_polyT`

 Exhaustive counting is polynomial-time in the input and the padding string. 

### `exhaustiveMachineExists`

 There is a machine with finite alphabets that computes exhaustive counting with a padding string
of 2ⁿ units on every bit string, and so tries all assignments within 2^{c·n}·n^{c·k} steps. 

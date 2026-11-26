---
{
  "module": "proof/rates/ClauseBound/Alg/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemmas on codes, logarithms and time, for bounds in m

This file holds lemmas for bounding, in the number m of clauses, the number of steps of the padding
machine on the code x of (k, φ).
That machine runs for q·(|x| + 2^(e x) + 1)^q steps on the input x. For the code x of (k, φ), with m
clauses, all variables occurring, |x| + 1 ≤ 8·(k·m)² (`length_enc_succ_le`).
The exponent e x is at most n ≤ k·m and at most the exponent of the clique algorithm at the level
picked for m (`eM_enc_le`). If r(m) ≥ 1/(c₁·(log₂(m+2))^c₁), then log₂(k·m) = O(k·m·r(m))
(`mul_le_two_rpow`),
and `time_le` turns such bounds into a bound C·2^(C·X) on q·(|x| + 2^E + 1)^q. 

 ### What the readers return on a code 

### `kOf_enc`

 The leading 1s of the code of (k, φ) are k in number. 

### `restOf_enc`

 After 1ᵏ 0 comes the code of φ as an instance of k-SAT. 

### `fmlOf_enc`

 The reader returns n in unary and the formula. 

 ### The exponent function 

### `needTopC_getD_le`

 The exponent computed under the bound b, or else b, is at most b and at most the exponent of the
clique algorithm. 

### `eM_enc_le`

 On the code of (k, φ) the exponent is at most n and at most the exponent of the clique algorithm
at the level picked for m. 

 ### The length of a code 

### `length_enc`

 The code of (k, φ) has k + n + 2 + m·k·(⌊log₂ 2n⌋ + 1) symbols. 

### `n_le`

 If every variable occurs in a k-CNF with m clauses then n ≤ k·m. 

### `length_enc_succ_le`

 The length of the code, plus one, is at most 8·(k·m)². 

 ### Logarithms 

### `one_le_log`

 log₂(m+2) ≥ 1. 

### `log_le_self`

 log₂(m+2) ≤ m + 2. 

### `log_pow_le`

 (log₂(m+2))^j ≤ 3·j!·2^j·m for m ≥ 1. 

### `one_le_mul_of_div_le`

 If r ≥ 1/(c·y^c) with c ≥ 1 and y ≥ 1 then c·y^c·r ≥ 1. 

### `mul_le_two_rpow`

 k·m ≤ 2^(2·c·D·k·m·r), where D = 3·(c+1)!·2^(c+1), if r ≥ 1/(c·(log₂(m+2))^c). 

 ### The time 

### `time_le`

 If L + 1 ≤ 8T², T ≤ 2^(H·X) and E ≤ G·X then q·(L + 2^E + 1)^q ≤ C·2^(C·X) with C = q·9^q +
q·(2H + G). 

---
{
  "module": "proof/variables/VariableBound/Paper/Decide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Decide.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Decide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What the end of the proof of Theorem 1 uses of an algorithm, and the bit «satisfiable»

Theorem 1 counts the satisfying assignments; the count is positive exactly if the formula is
satisfiable, so the bit «satisfiable» is a polynomial-time function of the count. This file has

* `VariableBound.Decide.Alg rn rm A e`: what the end of the proof of Theorem 1 uses of an algorithm,
  given as a function A of (input, pad) with an exponent function e for the pad: both are
  polynomial-time, A is right on the code of every
  (k, φ) when the pad has at least 2^(e x) units, and the number of steps q·(|x| + 2^(e x) + 1)^q of
  the padding machine is within the bound in n and within the bound in m;
* `bitOf`, «some bit of the word is 1», and `polyT_bitOf`: it is polynomial-time.

Nothing here depends on which algorithm is used. 

### `Alg`

 What the end of the proof of Theorem 1 uses of an algorithm: a function A of (input, pad) and an
exponent function e for the pad. 

### `Alg.polyA`

 A is polynomial-time 

### `Alg.polyE`

 e is polynomial-time 

### `Alg.correct`

 on the code of (k, φ), k ≥ 1, φ a k-CNF, with a pad of at least 2^(e x) units, A is the number
  of satisfying assignments in n + 1 bits 

### `Alg.timeN`

 for n ≥ 1 the number of steps of the padding machine is within the bound in n, for every q,
  with a constant that does not depend on k 

### `Alg.timeM`

 if all variables occur and m ≥ 1, it is within the bound in m, for every q, with a constant
  that does not depend on k 

### `bitOf`

 The one bit «some bit of the word w is 1». 

 ### The bit 

### `polyT_bitOf`

 «Some bit is 1» is polynomial-time. 

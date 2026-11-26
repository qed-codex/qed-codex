---
{
  "module": "proof/consequences/ThmCount/Rates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/Rates.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/Rates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem C from Theorem D(b): the comparison of the rates

No sentence of the paper stands behind this file. Write r(n) = log log(n+4)/√(log(n+4))
(`SatK.rN 1 (1/2) n`), with log = log₂.
* `time_le`: for all constants C, q, a, d there is K such that q·(2^{C·9·(n+4)·r(n)} + a·(n+2)^d + 1)^q
  ≤ 2^{K·R} for every n and every real R ≥ 1 with n·r(n) ≤ 8·R. It uses r(n) ≤ 8 and (n+2)^d ≤
  2^{d·(64·n·r(n) + 256)} from proof/machines/Wrap/ArithRate.lean.
* `rate_le`: for n ≥ 2 and e ≤ 1/4, R = n/(log n)^e is such a number. It uses log y/√y ≤ 8/y^{1/4}
  (`Wrap.Arith.lg_div_sqrt_le`).
* `stRates` (= `ThmCount.StRates`): e = 1/20. `remark_rate`: for n ≥ 4, R = n·(log log n)^{2/3}/(log
  n)^{1/6} is such a number too, because (log log n)^{2/3} ≥ 1. 

### `sqrt_sqrt_eq`

 The fourth root, written with two square roots. 

### `one_le_logb`

 log₂ n ≥ 1 for n ≥ 2. 

### `rate_le`

 For n ≥ 2 and e ≤ 1/4: n·r(n) ≤ 8·n/(log n)^e, and n/(log n)^e ≥ 1. 

### `natCast_le_two_rpow`

 A natural number q is at most 2^q. 

### `time_le`

 For all constants C, q, a, d there is K such that, for every n and every real R ≥ 1 with n·r(n)
≤ 8·R: q·(2^{C·9·(n+4)·log log(n+4)/√(log(n+4))} + a·(n+2)^d + 1)^q ≤ 2^{K·R}. 

### `stRates`

 The comparison of the rates: for all constants C, q, a, d there is C' such that for every n ≥ 2,
q·(2^{C·9·(n+4)·log log(n+4)/√(log(n+4))} + a·(n+2)^d + 1)^q ≤ 2^{C'·n/(log n)^{1/20}}. This is the
statement `ThmCount.StRates`. 

### `remark_rate`

 For n ≥ 4, R = n·(log log n)^{2/3}/(log n)^{1/6} has n·r(n) ≤ 8·R and R ≥ 1. 

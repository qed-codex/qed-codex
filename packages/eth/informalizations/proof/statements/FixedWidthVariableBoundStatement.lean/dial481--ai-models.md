---
{
  "module": "proof/statements/FixedWidthVariableBoundStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/FixedWidthVariableBoundStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/FixedWidthVariableBoundStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Counting the satisfying assignments of a k-CNF on n variables within 2^{O(n·r(n))}, for a fixed width k: the definitions

Definitions only. `SatK.CountsTM k M t` (in `CountKSatStatement.lean`): the machine M outputs the
count of every instance of k-SAT on n variables, in n + 1 bits, within t n steps; here all 2ⁿ
assignments are counted, and variables need not occur. The machine and the constant C may depend on
k.

## How to read it

* In `CountInRateN k r` the width k is fixed first; then come the machine M and the constant C; then
  n and the formula. The width is not part of the input.
* A smaller rate r is the stronger statement.
* The shift n + 4 in `rN` makes log₂ log₂ (n + 4) ≥ 1, so that `rN j α n` is positive for every n.

## What `CountInRateN` does not say

* Nothing uniform in k: M and C depend on k, and nothing is said about how.
* C is not explicit, and the bounds are asymptotic: they are below exhaustive counting (2ⁿ) only
  where C·r(n) < 1.
* Nothing about inputs that are not codes of instances of k-SAT (at most k literals per clause, no
  clause written twice): a promise on the input.
* The machine model is Mathlib's multi-stack machine `Turing.FinTM2`, as explained in
  `ThreeSatStatement.lean`. 

### `boundN`

 The time bound C·2^{C·n·r(n)}, rounded down. 

### `CountInRateN`

 «#k-SAT on n variables is in time 2^{O(n·r(n))}»: one machine, finite alphabets, one constant C. 

### `rN`

 r(n) = (log₂ log₂ (n+4))^j / (log₂ (n+4))^α. 

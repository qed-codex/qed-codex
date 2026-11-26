---
{
  "module": "proof/variables/FixedWidthSteps/Choice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Choice.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Choice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The main statement, from its four premises

Fix k, and let w ≤ max(k, 3) be the width that the algorithm takes. If the test is true, the «In
particular» of Theorem D (a) bounds the time of M on the rewritten code by 2^{C₁·w²·E(n)}, E(n) =
n·log log n/(log n)^α. If the test is false, n is one of finitely many
(`ConditionsHoldEventually` at max(k, 3)), and the time 2^{cn}·n^{ck} of trying all assignments is
within the bound by `SmallCasesAreWithinTheBound`. In both cases the overhead q·(t + |x| + 1)^q of
the machine that chooses is absorbed (`absorb`), because the code has
length below (n + 2)^{5k}. The step from w to max(k, 3) is made in the constant: C₁·w² ≤ C₁·max(k, 3)²,
and `two_rpow_mono` raises the constant in the exponent. 

### `timeVariablesAAlpha_le`

 The time of the «In particular» of Theorem D (a) at the width w is at most 2^{C·w²·E(n)}. 

### `everyChoiceCountsFrom`

 The main statement, from the «In particular» of Theorem D (a), the conditions for all but
finitely many n, the finitely many other n, and the facts on the width that the algorithm takes. 

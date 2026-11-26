---
{
  "module": "proof/variables/FixedWidthSteps/Absorb.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Absorb.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Absorb.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What the bound absorbs

`lg_le_exp`: for every α ≥ 0 there is a c₁ with log n ≤ c₁·n·log log n/(log n)^α for all n ≥ 4. For
large n this is the fact «k log n ≤ en for large n» of Step 5 of Appendix D
(`MainTheoremForms.stepSparsifyLarge`) at k = 1 and e = (log n)^{−⌈α⌉}; for the finitely many other
n
it follows from `SmallCasesAreWithinTheBound`. `absorb`: so q·(t + X + 1)^q is within the bound if t
is, with the constant D, and X + 1 ≤ (n + 2)^D; the constant becomes q·(2D + 2)·c₁. 

### `pow_eq_two_rpow`

 x^m = 2^{m·log x}. 

### `two_rpow_mono`

 2^{a·E} ≤ 2^{b·E} for a ≤ b and E ≥ 0. 

### `lg_le_exp`

 log n ≤ c₁·n·log log n/(log n)^α for all n ≥ 4. 

### `absorb`

 If t ≤ 2^{D·E(n)} and X + 1 ≤ (n + 2)^D, then q·(t + X + 1)^q ≤ 2^{C·E(n)} with C = q·(2D + 2)·c₁,
where E(n) = n·log log n/(log n)^α. 

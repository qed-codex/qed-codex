---
{
  "module": "proof/rates/ClauseBound/TopN/ArithR.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/ArithR.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/ArithR.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The master inequality W ≤ A₁·K·e, between real numbers

This file proves the master inequality `master`, with its constants `cK`, `qE`, `a0`, `A1` and the
bound `D_le`, and defines the slope `ckN` and proves the estimate `le_of_small`. 

 ### The master inequality: W ≤ A₁·K·e 

### `cK`

 2^(k+1) + 1, the slope of β in 4s + 17. 

### `qE`

 The power of log₂ K that bounds W/e. 

### `a0`

 The constant in D ≤ a₀·(log₂ K)^(4·c·C·C₀). 

### `A1`

 The constant of the master inequality. 

### `D_le`

 D = 2^β is at most a constant times a power of log₂ K. 

### `master`

 W ≤ A₁·K·e. 

 ### The exponent 

### `ckN`

 The slope of b = β + 3 in s + 1. 

 ### An estimate 

### `le_of_small`

 If s is below a bound t and 2^(−s) ≤ e, then n ≤ 2^t·(n·e). 

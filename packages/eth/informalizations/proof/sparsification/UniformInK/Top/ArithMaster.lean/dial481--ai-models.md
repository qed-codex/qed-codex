---
{
  "module": "proof/sparsification/UniformInK/Top/ArithMaster.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/ArithMaster.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/ArithMaster.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # W ≤ A₁·K·e with a constant that depends on C₀ only

Notation as in proof/sparsification/UniformInK/Top/ArithDefs.lean: D = 2^β, b = β + 3, Y the number
of binary digits of K, W = b²·D·Y; y = log₂ K.
* `stMasterU`: if D⁶ ≤ K then W ≤ D³·2y ≤ e·2·D³·y^(C₀+1) ≤ e·(D⁶ + y^(2C₀+2)) ≤ A₁·K·e. The
  relative for a fixed width is `master` of proof/rates/ClauseBound/TopN/ArithR.lean, whose constant
  grows with k.
* `stSixU`: a number D ≤ (⌊log₂ n⌋ + 1)^c has D⁶ ≤ K if 2·(102·C₀·c)² ≤ ⌊log₂ n⌋ and n < K^(17·C₀). 

### `stMasterU`

 W ≤ A₁·K·e if D⁶ ≤ K. 

### `stDLogU`

 2^(betaU k s) ≤ (⌊log₂ n⌋ + 1)^(a·k) for a = `aU C C₀`, if 2 ≤ K ≤ n, 1/(log₂ K)^C₀ ≤ e and 2^s
≤ (2/e)^C. 

### `stSixU`

 A number D ≤ (⌊log₂ n⌋ + 1)^c has D⁶ ≤ K, if 2·(102·C₀·c)² ≤ ⌊log₂ n⌋ and n < K^(17·C₀). 

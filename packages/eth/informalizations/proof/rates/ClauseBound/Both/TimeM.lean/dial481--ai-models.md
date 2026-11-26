---
{
  "module": "proof/rates/ClauseBound/Both/TimeM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Both/TimeM.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Both/TimeM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The running time of the padding machine against the bound in m

`stTimeM : StTimeM`, from `StTopArith`: for the exponent `eM` of the algorithm for the bound in m
and every q there is a D with q·(|x| + 2^(eM x) + 1)^q ≤ D·2^(D·k·m·r(m)) on the code x of (k, φ).
This inequality
is proved here with the lemmas of proof/rates/ClauseBound/Alg/End.lean: |x| + 1 ≤ 8·(k·m)²; the
exponent is at most n ≤ k·m, which is used if m is below a
constant, and at most A·k·m·e_l otherwise; and log₂(k·m) = O(k·m·r(m)) because r(m) ≥
1/(c₁·(log₂(m+2))^c₁). 

### `stTimeM`

 For the exponent of the algorithm for m, the running time of the padding machine is within the
bound in m. 

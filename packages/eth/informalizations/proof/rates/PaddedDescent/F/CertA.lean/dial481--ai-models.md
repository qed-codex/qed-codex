---
{
  "module": "proof/rates/PaddedDescent/F/CertA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The function `A` of proof/rates/PaddedDescent/F/Prog.lean is polynomial-time (`certA`), given
the certificates of the rebalancing, of the descent through the levels, of
the brute force at the bottom and of the network of marks as hypotheses. 

### `A_polyT_aux`

 The function `A` at any width k of the clauses, with the pad, the threshold τ, the schedule S,
the parameters q of the evaluations, the number R of layers (in unary) and the formula φ as
arbitrary functions of a context. 

### `certA`

 The function `A` is polynomial-time, given the certificates of the rebalancing, the descent, the
brute force at the bottom and the network of marks. 
